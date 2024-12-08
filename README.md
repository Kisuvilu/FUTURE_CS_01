# FUTURE_CS_01

# Two-Factor Authentication (2FA) in Python (CLI Version)

## Overview
This project demonstrates how to implement Two-Factor Authentication (2FA) using Time-Based One-Time Passwords (TOTP) in Python. It provides a command-line interface (CLI) for generating, verifying, and managing OTPs. Additionally, it allows users to generate QR codes for easy integration with the Google Authenticator app.

## Features 
- Generate secure, random secret keys.
- Generate Time-Based One-Time Passwords (TOTP).
- Verify OTP input for added security.
- Create QR codes for easy setup in Google Authenticator or similar apps.
- Simple CLI for interacting with the 2FA system.

## Prerequisites
Make sure you have Python installed. Install the required libraries by running:
Terminal 
pip install pyotp qrcode pillow

## Usage
1. Clone this repository or download the `2fa.py` file.
2. Run the script using:
      terminal 
   python 2fa.py

3. Follow the CLI instructions to:
   - Generate a secret key.
   - Scan a QR code with Google Authenticator.
   - Test OTP generation and verification.

## How It Works
1. Secret Key : A secure, random base32 string is generated to act as the unique secret key for TOTP generation.
2. TOTP Generation: Based on the secret key and current timestamp, a 6-digit OTP is generated every 30 seconds.
3. OTP Verification: User input is validated against the current OTP.
4. QR Code Generation: A provisioning URI is created and converted to a QR code that can be scanned with an authenticator app.


## Project Structure
- `2fa.py`: Main script for implementing and testing 2FA functionality.
- `totp_qrcode.png`: QR code image generated for use with Google Authenticator.


## Sample Output

Your secret key: JBSWY3DPEHPK3PXP
Scan the QR Code saved as 'totp_qrcode.png' using your Google Authenticator app.

Options:
1. Display Current OTP
2. Verify OTP
3. Exit
Enter your choice:


## References
- [PyOTP Documentation](https://pyauth.github.io/pyotp/)
- [Google Authenticator](https://github.com/google/google-authenticator)

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

## License
This project is open-source and available under the [MIT License](LICENSE).


## Acknowledgments
Thanks to the Python and open-source communities for providing excellent tools and libraries like `pyotp` and `qrcode`.
