import pyotp
import qrcode
import time

# Generate a secret key
secret_key = pyotp.random_base32()
print(f"Your secret key: {secret_key}")

# Create a TOTP object
totp = pyotp.TOTP(secret_key)

# Generate a QR Code for provisioning
uri = totp.provisioning_uri(name="test_user", issuer_name="MyApp")
qr = qrcode.make(uri)
qr.save("totp_qrcode.png")
print("Scan the QR Code saved as 'totp_qrcode.png' using your Google Authenticator app.")

# CLI to test OTP generation and verification
while True:
    print("\nOptions:")
    print("1. Display Current OTP")
    print("2. Verify OTP")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current OTP:", totp.now())
    elif choice == "2":
        user_input = input("Enter the OTP: ")
        if totp.verify(user_input):
            print("OTP is valid!")
        else:
            print("Invalid OTP!")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
