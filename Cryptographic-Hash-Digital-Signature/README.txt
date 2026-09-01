CRYPT0GUARD - ASSIGNMENT 5

This is a desktop GUI application for:
Evaluation of Cryptographic Hash Algorithms and Digital Signature Schemes.

FEATURES
- SHA-256 hashing
- SHA-512 hashing
- RSA-2048 digital signature generation
- Original signature verification
- Modified-message verification
- Visual demonstration of integrity/authentication

REQUIREMENTS
- Python 3.10 or newer
- Windows recommended
- cryptography package

RUN FROM COMMAND PROMPT
1. Extract this ZIP.
2. Open the extracted folder.
3. Type cmd in the File Explorer address bar and press Enter.
4. Run:

python -m pip install cryptography

5. Run:

python crypto_app.py

Alternatively, double-click run_app.bat.

DEMO
Original message:
Transfer amount: 5000

Modified message:
Transfer amount: 9000

Expected:
Original signature = VALID
Modified signature = INVALID

NOTE
The RSA key pair is generated when the application starts. This project is intended as an educational demonstration.
