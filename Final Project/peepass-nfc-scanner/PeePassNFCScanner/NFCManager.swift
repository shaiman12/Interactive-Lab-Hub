//
//  NFCManager.swift
//  PeePassNFCScanner
//
//  Created by Jon Caceres on 11/15/23.
//

import Foundation
import CoreNFC

class NFCManager: NSObject, NFCTagReaderSessionDelegate {
    var session: NFCTagReaderSession?

    func beginSession() {
        session = NFCTagReaderSession(pollingOption: .iso14443, delegate: self)
        session?.begin()
    }

    func tagReaderSessionDidBecomeActive(_ session: NFCTagReaderSession) {
        print("Ready to scan")
        // Session began and is ready to scan tags
    }

    func tagReaderSession(_ session: NFCTagReaderSession, didDetect tags: [NFCTag]) {
        print("Detected")
        // Tags were detected, handle them
    }

    func tagReaderSession(_ session: NFCTagReaderSession, didInvalidateWithError error: Error) {
        // Handle error
    }
}
