# IDD Final Project

## Team Members

Shai Aarons (sla88) - "The Bacchanalian" 🕺

Ariana Bhigroog (ab2959) - "The One Who Sees All" ❤️‍🔥

Jon Caceres (jc3569) - "The Apparatus" 🚀

Rachel Minkowitz (rhm256) - "The Weaver" 🍄

Amando  Xu (ax45) - "The Miracle Worker" ✨

## Big Idea

<p align="center">
<img src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/a133dd5d-7eda-4567-9f90-31baba90083b" width="600">
</p>

TLDR; PeePass is a mobile application that connects users to nearby business restrooms offering accessible clean toilets all over cities through an <ins>application interface</ins> and <ins>proprietary lock</ins> on bathroom doors. 

PeePass is a cool mobile app that makes finding a clean restroom a breeze. With a simple interface, it connects users with nearby businesses within cities that offer top-notch toilets. Plus, its seamless integration with a proprietary bathroom security system and locking mechanism adds an extra layer of privacy for an *elite bathroom experience*.

Imagine you're out and about, and suddenly, you need to use the restroom. Public restrooms trigger some sort of trauma, but you dont have to fret! Whip out PeePass, find the closest restroom, scan your QR code and viola an unlocked sparkling clean toilet for you to use. The app's design is easy to navigate ad intuitive, making your bathroom quest a piece of cake.

But here's the real kicker: PeePass isn't just about finding a restroom; it's about making the whole experience better. The bathroom doors are equipped with a QR display which displays a unique QR code once a user redeems tokens when selecting a restroom. There are also accessibility measures in place in case a user does not have access to their camera at the time of restroom access. This proprietary lock is not just a lock; it's like your personal VIP entry to a clean and comfy oasis.

So, whether you're in the middle of your homecity exploring or stranded somewhere unfamiliar, PeePass is your restroom sidekick. It's all about keeping things simple, making sure you find a great restroom without any fuss, and ensuring a private and exclusive experience with our snazzy door lock. Say goodbye to restroom stress and hello to hassle-free pit stops with PeePass!

## Objective

Our objective for this Final IDD Project was to collborate our team's Startup Studio idea (PeePass) with Interactive devices. Specifically, developing the _proprietary locking mechanism_ discussed before. Our idea is to create a 3D miniature bathroom setting which would *simulate* the user journey of someone using PeePass. Our model would include a life size lock on the 'door' that would unlock using the PeePass app and QR code display/Numpad connected to our Raspberry Pi. Most importantly, to spice up our project, we plan to include LED lights that are indicated as "active" inside the bathroom when the door is locked and are then "deactivated" when the door is unlocked.

### Project Plan:

_Note:_ This project plan was created at the start of our project before we pivoted certain methods and features
#### 1. Conceptualization and Design (Week 1)

- **Designing the App Interface:** Basic functionality for NFC scanning and keypad code entry.
- **3D Bathroom Model Design:** Plan the dimensions, placement of the door lock, and interior details like the toilet and bathtub.
- **Laser System Conceptualization:** Determine the placement and type of lasers and how they will be integrated.

#### 2. Development and Procurement (Weeks 2-3)

- **iOS App Development:**
    - Setup a basic user interface.
    - Implement NFC reading functionality.
    - Integrate keypad input with a 4-digit code system.
- **3D Model Printing:**
    - Finalize the design and start 3D printing components.
- **Raspberry Pi Setup:**
    - Program the Pi to respond to NFC scans and keypad inputs.
    - Integrate the electric strike lock.
- **Laser System Setup:**
    - Source the lasers and any necessary wiring (fishing wire or fiber optics).
    - Install and test the laser system within the model.

#### 3. Assembly and Testing (Week 4)

- **Assemble the Bathroom Model:**
    - Install the electric strike lock and connect it to the Raspberry Pi.
    - Place the interior model pieces.
    - Set up the laser system.
- **Integration Testing:**
    - Test the iOS app with the NFC reader and keypad on the Raspberry Pi.
    - Ensure the lock mechanism works correctly.
    - Test the visibility and alignment of the laser system.

#### 4. Final Adjustments and Presentation (Week 5)

- **Troubleshooting and Adjustments:**
    - Address any issues found during testing.
    - Make adjustments to the hardware or software as necessary.
- **Final Review and Demonstration:**
    - Prepare a demonstration setup.
    - Review the project against initial objectives and specifications.

#### Parts Needed: 
- PeePass iOS App -> NFC Tokens
- Life size door lock
- numpad
- raspi
- Pi compatible NFC Reader
- Restroom 3D Assets
- LASERS
- mini smoke machine? (++coolness factor)
  
#### Fallback Plan:
We are hopeful that the NFC reader will be compatible with Apple NFC tokens but if that does not work, we will use a QR code to unlock the door through a user's phone camera on the app. Additionally, right now we are planning on 3D printing the entire 3D restroom but if it's too complicated to build a 3D model with the lock dimensions embedded, we will opt for wood or some other material for the structure.

### Functioning Project:

Project view: https://drive.google.com/file/d/1GehffDm9t65VjD8sZKnVWR6-5UkuFXEK/view?usp=sharing <br>
Functioning project in use: https://drive.google.com/file/d/1shWUXQ4ZxUWaTMsXuufOiYjUlLCXqeNt/view?usp=sharing <br>

### Design Process:
We wanted to include thorough documentation of our design process (for documentation purposes and to look back at the fun that we had!)

#### Background and Ideation
Throughout the semester we were very excited for this Final Project. So much so, that whenever we came up with a good idea we tabled it for the final project :) 

A couple of ideas we came up with throughout the semester include:
1. Building on our Bender Security System to be more efficient and robust
2. Smart Wallet - a wallet that indicates which cards it is holding (i.e. insurance card, credit card A) according to colored lights, instead of a user having to take out each card
3. Smart Mirror - A mirror that displays inspirations quotes and motivating sayings if it detects someone is sad
4. Medication motivation - a pill bottle/box which nudges a user to take their meds and reacts with some sort of reward when the user does
5. Start working on Startup Studio by building the PeePass app and lock functionality

We decided to go with option 5 - starting to work on the team's next semester startup studio -- PeePass. While ideating the presentation for our proprietary lock, we initially contemplated showcasing it in a simple manner, perhaps placing a lock on a table etc. However, after thorough consideration we settled on a display that seemed feasible and ✨cute✨ at the same time. While the ultimate goal of PeePass is to serve as a practical solution, acting as a functional lock on a real bathroom door, we encountered the challenge of not having access to a full-scale bathroom door and doorpost for experimentation. In light of this limitation, our strategy shifted towards creating a realistic simulation of the PeePass user experience. To achieve this, would construct a miniature bathroom setting, complete with a life-sized lock. This lock will demonstrate its functionality by responding to the PeePass App NFC Tokens/camera capture of the NFC Reader/QR code display/keypad to authenticate user entrance into a restroom.

#### Storyboard
<br>
<img width= "700" alt="PeePass storyboard" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/59359994-889c-4678-9094-baef1c6e6261">
<br><br>

#### Initial Sketches
We wanted to emulate the genuine PeePass experience as closely as possible, even within the constraints of a scaled-down model. We believe that by meticulously replicating key features, such as the App and the unlocking mechanisms, we can effectively convey the practicality and functionality of PeePass, setting the stage for its real-world application as a reliable and secure lock on bathroom doors for businesses.

<img width="400" height="400" alt="ideation sketch" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/47a7abfa-4285-452d-8b8f-5f7c87addba6">
<br>
<img width="400" height="400" alt="sketch" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/d6d19451-894e-4cb9-8872-d407fcf80216">

<img width="400" height="400" alt="door sketch" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/5cdc86e2-e42b-427d-ad70-8a02752db811">

##### Tech Pieces of the Puzzle:

1. **Raspberry Pi runs a Flask Script:** The Raspberry Pi, is running a Python script that utilizes Flask. In this case, the script creates a local web server accessible within our local network. At this point - the QR code was accessible locally, which is not enough when accessing the QR code through anyones phone ([Video: Local is a Go!](https://drive.google.com/file/d/16IOC8wSJXLmvBi9g8AYsVX0Kvxjibdx3/view?usp=share_link)) 

2. **Ngrok for External Access:** Because we needed the URL to be accessed from anywhere we used a tool called Ngrok. Ngrok is a tool that creates a secure tunnel to our local server (raspberry pi), allowing it to be accessible over the internet. By using Ngrok, we expose the Flask server running on our Raspberry Pi to the wider internet, making it reachable from outside the local network.

3. **QR Code Display**: The Raspberry Pi generates and displays a QR code through our coded Express.js backend. This QR code encodes a URL, which is the address of our externally accessible server (via Ngrok). The authentication aspect changes every 10 seconds - making the 4 digit pin dynamic, enhancing security.

4. **iOS App with Camera access:** We also developed a main portion of our Startup's functionaluity - the PeePass app. Our iPhone app was created using Swift and has access to the phone's camera. When the camera scans the QR code displayed by the Raspberry Pi, it reads the encoded URL which then leads to API interaction.
   
App Screens: <br>
<img width="200" alt="door sketch" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/64ed78d3-a14d-4902-a103-9d7869715a6a">
<img width="200" alt="door sketch" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/ff359c04-f320-457c-a243-af72b5d804cd">
<img width="200" alt="door sketch" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/564d32eb-1651-428f-a5e0-7ec27e6f2f0f">
<img width="200" alt="door sketch" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/82b8fd32-ed3d-4789-9152-f5b497273fa7">

6. **API Interaction:** Upon scanning the QR code, the iOS app makes a GET request to the URL encoded in the QR code. This URL points to an API hosted on Heroku, a cloud platform service that enables deployment and running of applications. The Heroku-based API, upon receiving this request, then makes another GET request to the Ngrok-exposed server running on our Raspberry Pi which authenticates the user's code and unlocks the lock.


7. **Unlocking with the Numpad:** We wanted to ensure that users who deny camera access or don't have camera access would still be able to enter our restrooms and therefore have included number pad functionality in our unlocking mechanism as well. The app displays a 4 digit pin (that's recevied from the app backend) which the user can input into the numpad and see their input on the QR code display. This input field has error handling as well, in case a users only enters 3 digits etc.

<img width="452" alt="Screen Shot 2023-12-13 at 11 22 38 AM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/cb7536d2-7fc7-4642-909f-a8e6348eb783">

##### Physical Pieces of the Puzzle

1. **Restroom structure:** We had origianlly thought to 3D print the entire restroom and include only a wooden door but that turned out to be harder than anticipated. Instead we bought wood for all the walls and door. After assembling this structure, we decided acryllic walls would make for a more aethstetic appearance.
   
2. **Installing the lock:** The lock we are using is life size and fully functional, therefore in comparison with the rest of the structure, it's 'strength' is significantly more. Becasue of this needed to include reinforcements for the structure so that it's possible for users to open the door without toppling over the rest of the structure. To install the lock -  we did some fancy woodworking and got the lock flushed with the wooden support beam.
   
3. **Fashioning the Pi:** We created a 'drop floor' to hide the pi in the restroom structure while ensuring the lock relay and battery pack remained connected.
   
4. **3D printed assets:** We 3D printed the indoor decor for our bathroom panorama to make the experience more 'realistic'. We added some modern art into the restroom as well to make for an elevated restroom experience.

5. **Attaching the Numpad and Big Screen:** Because we were dealing with a wooden beam, it was hard to embed the sensor and display into the beam while ensuring the projec looked tidy. Instead we opted to mount the sensor and numpad on the face of the beam - which required some homemade standoff screws.
   
6. **Lights:** Another mechanism for user feedback we included was a strip of LED lights. These lights remain red as long as the restroom is locked and turn to white flickering when a user unlocks the restroom.

#### Running/Testing the App + QR code

Assuming the pi and battery pack are switched on and connected we could activate our app and QR by running through this process:

##### **1st Terminal:**

- navigate to project directory - run `git pull`
- activate virtual environment by running `source .venv/bin/activate`
    - if you haven’t already, run `pip install -r requirements.txt`
- run `python qr-code-lock.py`
    - ensure server is running at `0.0.0.0:8000`

##### **2nd Terminal:**

- open another terminal → renter the course folder and reactivate virtual environment
- run command `ngrok http http://0.0.0.0:8000`
    - note: you may need to install ngrok on your device
- copy the Forwarding URL ending in .app

##### **3rd terminal (cd backend directory) NOT in venv**

- navigate to project directory and then to `backend` directory
- open `index.js`
- replace OLD ngrok URL on line 21 with NEW ngrok URL copied from 2nd Terminal
- checkin this change via git (add , commit, push)
- this will automatically deploy to Heroku (give it about 5 min)

##### **4th Terminal**

- navigate to project directory → renter the course folder → reactivate virtual environment
- run `python qr-code-keypad.py`

<aside>
🎉 Tada - navigate to the TestFlight App and scan QR
</aside>

#### Photo Gallery
||||
|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="528" alt="Screen Shot 2023-12-08 at 3 23 25 PM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/6919169a-5f44-45d0-bcfb-bf7dcd53a48a"> |<img width="528" alt="Screen Shot 2023-12-08 at 3 22 48 PM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/186b15cb-27ba-4819-bf32-e23f6ed97cd3">|<img width="528" alt="Screen Shot 2023-12-08 at 3 29 33 PM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/3e9c4d08-fb84-4cb8-a8d9-6adb29f309c8">|
<img width="528" alt="Screen Shot 2023-12-08 at 3 29 45 PM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/bc281684-0ded-4a7a-b466-293f3e1f251d">|<img width="528" alt="Screen Shot 2023-12-08 at 3 29 58 PM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/e5a09e61-fb87-482f-b908-20188dc5333e">|<img width="528" alt="Screen Shot 2023-12-08 at 3 30 12 PM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/ac385088-acaa-49be-ac68-87b67d427ccd">|
<img width="528" alt="Screen Shot 2023-12-08 at 3 30 20 PM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/fa278dd8-4fb6-424e-b708-8f997e6fb1da"> |
<img width="528" alt="Screen Shot 2023-12-08 at 3 30 28 PM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/7396e38e-7eb8-4761-bef0-90535292a7d6">|<img width="528" alt="Screen Shot 2023-12-13 at 11 54 41 AM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/cb903af0-ead4-4529-9c5e-1756146a0c31">|<img width="528" alt="Screen Shot 2023-12-13 at 11 54 56 AM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/4b10022e-482b-4c70-8993-846b32f69fc6">|
<img width="528" alt="Screen Shot 2023-12-13 at 11 55 07 AM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/e8e4eb5b-7b7f-4a85-a5b7-ce530e7dc6e2">|<img width="528" alt="Screen Shot 2023-12-13 at 11 55 25 AM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/83c8ebd9-3fe0-42cf-9c01-65f522fcbef2">|<img width="528" alt="Screen Shot 2023-12-13 at 11 55 36 AM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/a99391b3-548b-4a05-bd41-c551a00c0b1d">|
<img width="528" alt="Screen Shot 2023-12-13 at 11 55 43 AM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/be940d7f-0407-4c62-9b26-ad0e462909ac">|<img width="528" alt="Screen Shot 2023-12-13 at 11 55 56 AM" src="https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/594b6553-a7f6-47ee-963f-c08b7baa82fc">|


### Video of someone using your project
Tester 1 QR code: https://drive.google.com/file/d/1FzVY35NVeGY-c9ZiwQehVA4Trht1vIbs/view?usp=sharing <br>
Tester 1 Numpad: https://drive.google.com/file/d/1DlFcqzbd0bZPgmUwvwLMCQimQa79D5_u/view?usp=sharing <br>

Tester 2 QR code: https://drive.google.com/file/d/1CyDf-W70vyI3BW5c2ApU3LobhNvm-waA/view?usp=sharing<br>
Tester 2 Numpad: https://drive.google.com/file/d/1bTgm4f_zwwlQ7qwlcOBsBX1oiJ3o3LP0/view?usp=sharing<br>

### Reflections and Pivots
In the course of developing our project, the collaborative process was enjoyable (as per usual with this team), fostering a strong sense of teamwork among the group. The camaraderie we shared during the project and semester overall not only made the journey memorable but also made for creative problem-solving and effective communication environment.

However, as with any project, we encountered challenges, specifically in the implementation of the NFC reader and the physical assembly of our miniature model. In hindsight, we underestimated the complexity of door locking mechanisms, both in terms of the lock itself and the intricate latch system. This oversight led to some ad hoc solutions.

Originally we had planned to use an NFC scanner to validate entrance into the restroom (using iOS NFC tokens). When we started to work on it, we realized this sensor was more complicated than we thought. The NFC scanner that we had was not working as expected and the pi was not complying with our requests. We tried various NFC Scanners (thinking that our scanner came broken at first) but could not get the NFC scanner to interact with our iOS NFC token. Instead we opted for QR code authentication. Now, a user would open their app to scan a QR code (the app accesses the phone camera) which would instigate the unlocking mechanism and the user would be able to access the restroom. 

Furthermore, our oversight extended to the physical materials used in the construction of the door. We failed to fully consider the intricate balance between functionality and aesthetics, which affected the overall design and usability of our project. A key lesson learned was the importance of thorough pre-planning, not only in terms of engineering considerations but also in selecting materials that align with both functionality and aesthetic goals. Moreover, midway through the project we moved from a wooden-box design to a glass see-through design - for aesthetic purposes

Also, understanding the limitations of hardware compatibility materials was something that came up often in our process as well. For one, we encountered some sporadic Qwiic Keypad Issues specifically a recurring "Remote I/O error" that caused the controlling script to stop unexpectedly. We intially thought the issue had something to do with the actual keypad and swapped ours out for a new one, tried a new cable, tried a new shim but after seeing that the problem persisted we figured the issue was not a flaw in the hardware. After searching for potential causes online we found a review on Sparkfun's website where a user experienced a similar issue. We finally were able to identify the problem as related to the keypad’s limited bus speed of 100kbit/second, potentially conflicting with other components sharing the same bus but operating at higher speeds.The approach to our solution was reconfigure two GPIO pins to create an additional bus with a limited speed of 100kbit/sec and then connect the keypad to these newly configured pins. We then investigated the `qwiic_keypad` library and modified a line of code that set the bus number to match our newly configured bus. This successfully resolved the connection issues with the Qwiic Keypad and bus speeds. This was one example of the importance of understanding hardware compatibility, particularly in terms of communication protocols and bus speeds. By methodically troubleshooting and modifying software configurations, we were able to overcome a challenging hardware-software interaction issue.

A smaller more physical issue we faced was that, as a finishing touch on our bathroom design we had added tinsel to the door frame for a little party action. While the bathroom panorama looked great, the relay for the lock was not activating while it was working the whole day. We knew the problem could not be the code, and started looking into various hardware pieces that could be the problem. We then realized that tinsel is conductive and may be interfering with a component, unknowingly causing circuit shorts in the other components. At that point we said goodbye to the tinsle and viola - all the components worked again.

Reflecting on our experience, we recognize the need for a thouroughly fleshed out approach to designing hardware. For future iterations, we would opt for a life-size door handle and a custom-sized laser-cut acrylic or wooden box - confirming the setup and layout of the components earlier on. This adjustment would not only enhance functionality but also contribute to a cleaner and more visually appealing aesthetic.

Moreover, acknowledging the challenges we faced with the NFC reader, we now realize the value of prioritizing efficiency. In a hypothetical redo, we would streamline our efforts by opting for a QR code scanner instead of investing time in resolving issues with the NFC reader. This strategic decision would allow us to allocate time and resources more effectively, focusing on aspects of the project where we could achieve greater success.

In essence, our project journey was marked by both triumphs and challenges. What we gained from this experience will undoubtedly guide us toward more informed decision-making and meticulous planning in future endeavors, ultimately contributing to the continuous improvement of our collaborative efforts.

### Group work distribution

The development of PeePass was a collaborative effort that saw each team member contributing their unique skills and expertise to create a comprehensive and functional system. **Jon**, with his full-stack capabilities, took charge of setting up the app from both frontend and backend perspectives. He implemented a robust API for authentication, integrated a QR code scanner, ensured lock and relay compatibility, and even undertook hands-on tasks like installing lock hardware, woodwork, hardware assembly, lights setup, and panorama arrangement. **Amando** played a pivotal role in hardware implementation, focusing on numpad input, error handling, and acting as the wire master. Amando's troubleshooting skills were instrumental in resolving hardware issues. **Shai**, the CEO of the startup, provided visionary leadership, collaborating with Ariana on the PeePass app frontend, introducing dynamic lights, and infusing the team with positive energy and innovative ideas (while helping with some of the hardware work like the woodwork), while also helping Jon and Amando with their hardware and software components. **Ariana**, the frontend maestro, enhanced the user interface, 3D printed bathroom assets, assisted in installing the physical lock in the model, and played a key role in arranging the panorama setup. **Rachel**, the documentation expert, not only led the documentation process but also contributed creatively through laser-cut decor and engineering problem-solving during panorama assembly. Together, the team's collective efforts resulted in the successful and multifaceted development of the PeePass proprietatry lock.
