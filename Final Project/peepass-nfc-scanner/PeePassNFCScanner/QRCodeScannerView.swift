//
//  QRCodeScannerView.swift
//  PeePassNFCScanner
//
//  Created by Jon Caceres on 11/26/23.
//

import SwiftUI
import AVFoundation

struct QRCodeScannerView: UIViewRepresentable {
    @Binding var isActive: Bool
    var completion: (Result<String, Error>) -> Void
    private let captureSession = AVCaptureSession()

    func makeUIView(context: Context) -> UIView {
        let view = UIView(frame: UIScreen.main.bounds) // Set view size to full screen

        guard let videoCaptureDevice = AVCaptureDevice.default(for: .video) else {
            completion(.failure(ScanningError.cameraUnavailable))
            return view
        }
        
        let videoInput: AVCaptureDeviceInput

        do {
            videoInput = try AVCaptureDeviceInput(device: videoCaptureDevice)
        } catch {
            completion(.failure(error))
            return view
        }

        if captureSession.canAddInput(videoInput) {
            captureSession.addInput(videoInput)
        } else {
            completion(.failure(ScanningError.badInput))
            return view
        }

        let metadataOutput = AVCaptureMetadataOutput()

        if captureSession.canAddOutput(metadataOutput) {
            captureSession.addOutput(metadataOutput)

            metadataOutput.setMetadataObjectsDelegate(context.coordinator, queue: DispatchQueue.main)
            metadataOutput.metadataObjectTypes = [.qr]
        } else {
            completion(.failure(ScanningError.badOutput))
            return view
        }

        DispatchQueue.main.async {
            let previewLayer = AVCaptureVideoPreviewLayer(session: captureSession)
            previewLayer.frame = view.layer.bounds
            previewLayer.videoGravity = .resizeAspectFill
            view.layer.addSublayer(previewLayer)

            DispatchQueue.global(qos: .userInitiated).async {
                captureSession.startRunning()
            }
        }

        return view
    }
    
    func startScanning() {
        DispatchQueue.main.async {
            if !self.captureSession.isRunning {
                self.captureSession.startRunning()
            }
        }
    }
    
    func stopScanning() {
        DispatchQueue.main.async {
            if self.captureSession.isRunning {
                self.captureSession.stopRunning()
            }
        }
    }

    enum ScanningError: Error {
        case cameraUnavailable, badInput, badOutput
    }

    func updateUIView(_ uiView: UIView, context: Context) {
        if isActive {
            startScanning()
        } else {
            stopScanning()
        }
    }

    func makeCoordinator() -> Coordinator {
        return Coordinator(parent: self)
    }
}
