const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
const QRCode = require('qrcode');

// Body parser middleware to parse JSON bodies
app.use(express.json());

var fourDigitCode;

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

app.get('/generate_qr', async (req, res) => {
  try {
    const url = 'https://0a0c-128-84-95-212.ngrok-free.app/trigger-relay'; // This could be dynamic based on query params
    const qrCodeImage = await QRCode.toDataURL(url);
    res.send(`<img src="${qrCodeImage}"/>`); // Sends QR code as an image
  } catch (error) {
    console.error('Error generating QR code', error);
    res.status(500).send('Error generating QR code');
  }
});

app.get('/get_code', (req, res) => { // Fixed here
  try {
    res.send({ fourDigitCode }); // Directly send the code in response
  } catch (err) {
    console.error("error : ", err);
    res.sendStatus(400);
  }
});

app.post('/validate_code', (req, res) => {
  try {
    if (!req.body) {
      console.error("No body");
      return res.sendStatus(400); // Return added here
    }
    if (req.body.code == fourDigitCode) {
      return res.sendStatus(200);
    } else {
      return res.sendStatus(401); // Send 401 for unauthorized if the code does not match
    }
  } catch (err) {
    console.error("Error: ", err);
    res.sendStatus(400);
  }
});

function generateFourDigitCode() {
  return Math.floor(1000 + Math.random() * 9000);
}

function runEveryMinute() {
  fourDigitCode = generateFourDigitCode();
  console.log(fourDigitCode);
  setTimeout(runEveryMinute, 60000); 
}

// Start the loop
runEveryMinute();
