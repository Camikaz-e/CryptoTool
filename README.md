# CryptoTool - A simple Cryptographic Algorithm Tool

CryptoTool is a Python-based GUI application designed to encrypt, decrypt, and hash data using various cryptographic algorithms. It supports text-based encryption (AES, 3DES), hashing (SHA-256, SHA-512), and also includes a feature to encrypt and decrypt images.

## Features
- **Encryption & Decryption:**
  - AES (Advanced Encryption Standard)
  - 3DES (Triple Data Encryption Standard)
  - Image encryption & decryption
- **Hashing Algorithms:**
  - SHA-256
  - SHA-512
- **Key Management:**
  - Generate secure encryption keys
  - Manually enter encryption keys
- **User-Friendly GUI:**
  - Built with PyQt5 for a sleek and interactive experience
  - Customizable theme and cube-shaped buttons
- **Cross-Platform Support:**
  - Works on Linux, Windows, and macOS

## Installation
### Prerequisites
Ensure you have Python 3 installed. Then, install the required dependencies using:
```bash
sudo apt update
sudo apt install python3-pip python3-pyqt5
pip install pycryptodome
```

### Clone the Repository
```bash
git clone https://github.com/Camikaz-e/CryptoTool.git
cd CryptoTool
```

### Run the Application
```bash
python3 crypto_tool.py
```

## Usage
1. Select an encryption algorithm from the dropdown menu.
2. Enter the text or select an image file.
3. Provide an encryption key (or generate one).
4. Click "Process" to encrypt, decrypt, or hash the input.
5. View the output in the designated text box.

## Contributing
Feel free to contribute by creating pull requests or reporting issues!

## License
This project is licensed under the MIT License.

## Author
**Camikaz-e** - [GitHub Profile](https://github.com/Camikaz-e)

