//
//  ContentView.swift
//  PeePassNFCScanner
//
//  Created by Jon Caceres on 11/15/23.
//

import SwiftUI
import AVFoundation
import Combine
import MapKit

struct ContentView: View {
    @State private var isWelcomeScreen = true
    @State private var isScannerScreen = false
    @State private var scannedURL: String = ""
    @State private var fourDigitCode: String = ""
    
    let timer = Timer.publish(every: 5, on: .main, in: .common).autoconnect()
    
    var body: some View {
        if isWelcomeScreen {
            WelcomeScreen(isWelcomeScreen: $isWelcomeScreen)
        } else if isScannerScreen {
            ScannerScreen(scannedURL: $scannedURL, fourDigitCode: $fourDigitCode, isWelcomeScreen: $isWelcomeScreen, isScannerScreen: $isScannerScreen, timer: timer)
        } else {
            RestroomMapView(isScannerScreen: $isScannerScreen)
        }
    }
}

struct WelcomeScreen: View {
    @Binding var isWelcomeScreen: Bool
    
    var body: some View {
        VStack {
            Spacer()
            Image("PeePass-logo")
                .resizable()
                .scaledToFit()
                .frame(width: 300, height: 400)
            Spacer()
            Button(action: {
                self.isWelcomeScreen = false
            }) {
                Text("Find Nearby Restrooms")
                    .font(.headline)
                    .foregroundColor(.white)
                    .padding()
                    .frame(height: 50)
                    .frame(maxWidth: .infinity)
                    .background(Color.black)
                    .cornerRadius(25)
            }
            .buttonStyle(PlainButtonStyle())
            .padding(.horizontal)
            Spacer()
        }
        .background(Color.white.edgesIgnoringSafeArea(.all))
    }
}

struct Restroom: Identifiable {
    let id = UUID()
    let name: String
    let coordinate: CLLocationCoordinate2D
    let details: String
}

struct RestroomMapView: View {
    @Binding var isScannerScreen: Bool
    @State private var region = MKCoordinateRegion(
        center: CLLocationCoordinate2D(latitude: 40.7558, longitude: -73.9560),
        span: MKCoordinateSpan(latitudeDelta: 0.01, longitudeDelta: 0.01)
    )
    @State private var showingRestroomDetails = false
    
    var body: some View {
        ZStack {
            Map(coordinateRegion: $region, annotationItems: [cornellTechLocation]) { restroom in
                MapAnnotation(coordinate: restroom.coordinate) {
                    Button(action: {
                        showingRestroomDetails = true
                    }) {
                        ZStack {
                            Rectangle() // Add a black square under the image
                                .fill(Color.black)
                                .frame(width: 35, height: 35) // Make the square the same size as the image
                                .cornerRadius(10)
                            Image(systemName: "toilet.fill")
                                .resizable()
                                .aspectRatio(contentMode: .fit)
                                .frame(width: 25, height: 25)
                                .foregroundColor(.white)
                                .overlay(
                                    RoundedRectangle(cornerRadius: 10)
                                        .stroke(Color.black, lineWidth: 2)
                                )
                        }
                    }
                }
            }
            .edgesIgnoringSafeArea(.all)
            
            if showingRestroomDetails {
                // Transparent background to detect taps outside the modal
                Color.black.opacity(0.1).edgesIgnoringSafeArea(.all)
                    .onTapGesture {
                        showingRestroomDetails = false
                    }
                RestroomDetailsView(restroom: cornellTechLocation, isScannerScreen: $isScannerScreen)
            }
        }
    }
}

struct RestroomDetailsView: View {
    let restroom: Restroom
    @Binding var isScannerScreen: Bool
    
    var body: some View {
        VStack(alignment: .center, spacing: 10) {
            Text("Restroom Details")
                .font(.title2)
                .fontWeight(.bold)
                .padding(.top)
                .foregroundColor(.black)
            
            Text(restroom.name)
                .font(.title3)
                .fontWeight(.semibold)
                .foregroundColor(.black)
            
            Text(restroom.details)
                .font(.body)
                .foregroundColor(.black)
            
            Text("0.1 miles away") // Placeholder for actual distance calculation
                .font(.caption)
                .foregroundColor(.gray)
            
            Button(action: {
                isScannerScreen = true
            }) {
                Text("Scan QR Code")
                    .font(.headline)
                    .foregroundColor(.white)
                    .padding()
                    .frame(height: 50)
                    .frame(maxWidth: .infinity)
                    .background(Color.black)
                    .cornerRadius(25)
            }
            .buttonStyle(PlainButtonStyle())
            .padding(.bottom)
        }
        .padding()
        .background(Color.white)
        .cornerRadius(10)
        .shadow(radius: 5)
        .frame(width: UIScreen.main.bounds.width * 0.9)
        .overlay(
            RoundedRectangle(cornerRadius: 10)
                .stroke(Color.black, lineWidth: 2)
        )
    }
}

// Cornell Tech location for the map pin
let cornellTechLocation = Restroom(
    name: "Cornell Tech",
    coordinate: CLLocationCoordinate2D(latitude: 40.7558, longitude: -73.9560),
    details: "2 W Loop Rd, New York, NY 10044"
)

struct ScannerScreen: View {
    @Binding var scannedURL: String
    @Binding var fourDigitCode: String
    @Binding var isWelcomeScreen: Bool
    @Binding var isScannerScreen: Bool
    let timer: Publishers.Autoconnect<Timer.TimerPublisher>
    
    @State private var showingSpinner = false // State to control the spinner visibility
    @State private var showingScanSuccess = false // State to show the scan success overlay
    
    @State private var gearRotationAngle = 0.0
    
    @State private var isScannerActive = true
    
    var body: some View {
        ZStack {
            VStack {
                Spacer()
                    .frame(width: 0, height: 80)
                HStack {
                    Button(action: {
                        self.isScannerScreen = false
                        self.isWelcomeScreen = true
                    }) {
                        Image(systemName: "arrow.left.circle")
                            .resizable()
                            .scaledToFit()
                            .frame(width: 40, height: 40)
                    }
                    .buttonStyle(PlainButtonStyle())
                    .padding()
                    Spacer()
                }
                
                Text("PeePass")
                    .font(.largeTitle)
                    .fontWeight(.bold)
                
                Text("QR Code Scanner")
                    .font(.title)
                    .fontWeight(.bold)
                    .padding(.bottom, 0)
                
                    QRCodeScannerView(isActive: $isScannerActive) { result in
                        switch result {
                        case .success(let code):
                            self.isScannerActive = false
                            self.showingSpinner = true // Show the scan success overlay
                            DispatchQueue.main.asyncAfter(deadline: .now() + 3) { // 1-second delay
//                                self.isScannerActive = true
                                self.showingSpinner = false
                                self.showingScanSuccess = true
                                DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
                                    self.showingScanSuccess = false
                                    self.isScannerActive = true
                                }
                                makeGetRequest(to: code)
                            }
                        case .failure(let error):
                            print("Scanning failed: \(error)")
                        }
                    }
                    .opacity(isScannerActive ? 1 : 0)
                    .frame(width: 300, height: 300)
                    .padding()
                Text("Unable to scan QR Code?")
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                Text("Please enter in the following 4 digit code")
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                    .padding(.bottom, 20)
                Text(fourDigitCode)
                    .font(.title)
                    .fontWeight(.bold)
                if !scannedURL.isEmpty {
                    Text("Scanned URL: \(scannedURL)")
                        .padding()
                }
                Spacer()
            }
            VStack {
                if showingSpinner {
                    ZStack {
                        Rectangle()
                            .foregroundColor(.black.opacity(0.75)) // Translucent black rectangle
                            .edgesIgnoringSafeArea(.all) // To cover the entire screen

                        Image(systemName: "gearshape.fill")
                            .resizable()
                            .aspectRatio(contentMode: .fit)
                            .frame(width: 75, height: 75) // Adjust size as needed
                            .foregroundColor(.white) // Gear color
                            .rotationEffect(Angle(degrees: gearRotationAngle))
                            .onAppear {
                                withAnimation(Animation.linear(duration: 1).repeatForever(autoreverses: false)) {
                                    gearRotationAngle = 360
                                }
                            }
                    }
                }
            }
            VStack {
                if showingScanSuccess {
                    ZStack {
                        Rectangle()
                            .foregroundColor(.black.opacity(0.75)) // Translucent black rectangle
                            .edgesIgnoringSafeArea(.all) // To cover the entire screen
                        VStack {
                            Image(systemName: "lock.open.fill")
                                .resizable()
                                .aspectRatio(contentMode: .fit)
                                .frame(width: 75, height: 75) // Adjust size as needed
                                .foregroundColor(.white) // Gear color
                            Text("Unlocked!")
                                .foregroundColor(.white) // Gear color
                                .font(.largeTitle)
                                .fontWeight(.bold)
                        }
                    }
                }
            }

        }
        .onAppear {
            fetchFourDigitCode()
        }
        .onReceive(timer) { _ in
            fetchFourDigitCode()
        }
        .border(Color.black)
        .edgesIgnoringSafeArea(.all)
    }
    
    func fetchFourDigitCode() {
        let urlString = "https://copwatch-api-test-9c567e874ba4.herokuapp.com/get_code"
        guard let url = URL(string: urlString) else {
            print("Invalid URL")
            return
        }
        
        let task = URLSession.shared.dataTask(with: url) { data, response, error in
            if let error = error {
                print("Error with fetching data: \(error)")
                return
            }
            
            guard let httpResponse = response as? HTTPURLResponse,
                  (200...299).contains(httpResponse.statusCode),
                  let data = data else {
                print("Error with the response, unexpected status code: \(String(describing: response))")
                fourDigitCode = "Unable to display code"
                return
            }
            if let dataString = String(data: data, encoding: .utf8) {
                print("Received data: \(dataString)")
            }
            
            do {
                let decodedResponse = try JSONDecoder().decode(FourDigitCodeResponse.self, from: data)
                DispatchQueue.main.async {
                    self.fourDigitCode = decodedResponse.fourDigitCode
                }
            } catch {
                print("Decoding error: \(error)")
            }
        }
        
        task.resume()
    }
}

struct FourDigitCodeResponse: Codable {
    let fourDigitCode: String
    
    enum CodingKeys: String, CodingKey {
        case fourDigitCode
    }
    
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        
        if let intValue = try? container.decode(Int.self, forKey: .fourDigitCode) {
            // If it's an integer, convert it to a string
            fourDigitCode = String(intValue)
        } else {
            // Otherwise, decode it as a string
            fourDigitCode = try container.decode(String.self, forKey: .fourDigitCode)
        }
    }
}



class Coordinator: NSObject, AVCaptureMetadataOutputObjectsDelegate {
    var parent: QRCodeScannerView
    
    init(parent: QRCodeScannerView) {
        self.parent = parent
    }
    
    func metadataOutput(_ output: AVCaptureMetadataOutput, didOutput metadataObjects: [AVMetadataObject], from connection: AVCaptureConnection) {
        if let metadataObject = metadataObjects.first {
            guard let readableObject = metadataObject as? AVMetadataMachineReadableCodeObject else { return }
            guard let stringValue = readableObject.stringValue else { return }
            AudioServicesPlaySystemSound(SystemSoundID(kSystemSoundID_Vibrate))
            parent.completion(.success(stringValue))
        }
    }
}

func makeGetRequest(to urlString: String) {
    guard let url = URL(string: urlString) else {
        print("Invalid URL")
        return
    }
    
    let task = URLSession.shared.dataTask(with: url) { data, response, error in
        if let error = error {
            print("Error with fetching data: \(error)")
            return
        }
        
        guard let httpResponse = response as? HTTPURLResponse,
              (200...299).contains(httpResponse.statusCode) else {
            print("Error with the response, unexpected status code: \(String(describing: response))")
            return
        }
        
        if let data = data,
           let stringData = String(data: data, encoding: .utf8) {
            DispatchQueue.main.async {
                // Process the data or update the UI as needed
                print("Response Data: \(stringData)")
            }
        }
    }
    
    task.resume()
}

#Preview {
    ContentView()
}
