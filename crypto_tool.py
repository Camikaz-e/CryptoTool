import sys
import hashlib
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTextEdit, QComboBox, QLineEdit, QFileDialog
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from Crypto.Cipher import AES, DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

class CryptoTool(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Cryptographic Algorithm Tool')
        self.setGeometry(100, 100, 500, 500)
        
        # Set background color
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(40, 44, 52))
        self.setPalette(palette)
        
        layout = QVBoxLayout()
        
        self.algorithm_label = QLabel('Select Encryption Algorithm:')
        self.algorithm_label.setFont(QFont('Arial', 12))
        self.algorithm_label.setStyleSheet("color: white;")
        layout.addWidget(self.algorithm_label)
        
        self.algorithm_combo = QComboBox()
        self.algorithm_combo.addItems(['AES', '3DES', 'SHA-256', 'SHA-512', 'Encrypt Image', 'Decrypt Image'])
        self.algorithm_combo.setStyleSheet("background-color: white; color: black;")
        layout.addWidget(self.algorithm_combo)
        
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter text to encrypt/decrypt or hash")
        self.input_text.setStyleSheet("background-color: white; color: black;")
        layout.addWidget(self.input_text)
        
        self.key_label = QLabel("Enter Key (for AES/3DES):")
        self.key_label.setFont(QFont('Arial', 12))
        self.key_label.setStyleSheet("color: white;")
        layout.addWidget(self.key_label)
        
        self.key_input = QLineEdit()
        self.key_input.setStyleSheet("background-color: white; color: black;")
        layout.addWidget(self.key_input)
        
        self.generate_key_button = QPushButton('Generate Key')
        self.generate_key_button.setStyleSheet("background-color: #88C0D0; color: black; font-size: 14px; padding: 20px; border-radius: 15px;")
        self.generate_key_button.clicked.connect(self.generate_key)
        layout.addWidget(self.generate_key_button)
        
        self.file_button = QPushButton('Select Image File')
        self.file_button.setStyleSheet("background-color: #D08770; color: white; font-size: 14px; padding: 20px; border-radius: 15px;")
        self.file_button.clicked.connect(self.select_file)
        layout.addWidget(self.file_button)
        
        self.process_button = QPushButton('Process')
        self.process_button.setStyleSheet("background-color: #5E81AC; color: white; font-size: 14px; padding: 20px; border-radius: 15px;")
        self.process_button.clicked.connect(self.process_crypto)
        layout.addWidget(self.process_button)
        
        self.output_text = QTextEdit()
        self.output_text.setPlaceholderText("Output will appear here")
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("background-color: white; color: black;")
        layout.addWidget(self.output_text)
        
        self.setLayout(layout)
    
    def generate_key(self):
        key_length = 32  # Default to AES-256
        key = get_random_bytes(key_length)
        self.key_input.setText(base64.b64encode(key).decode())
    
    def select_file(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if self.file_path:
            self.output_text.setText(f"Selected File: {self.file_path}")
    
    def process_crypto(self):
        algorithm = self.algorithm_combo.currentText()
        key = self.key_input.text().encode()
        
        if algorithm in ['AES', '3DES']:
            text = self.input_text.toPlainText().encode()
            if algorithm == 'AES':
                if len(key) not in [16, 24, 32]:
                    self.output_text.setText("AES key must be 16, 24, or 32 bytes long!")
                    return
                cipher = AES.new(key, AES.MODE_CBC, iv=get_random_bytes(16))
                encrypted = cipher.encrypt(pad(text, AES.block_size))
            elif algorithm == '3DES':
                if len(key) not in [16, 24]:
                    self.output_text.setText("3DES key must be 16 or 24 bytes long!")
                    return
                cipher = DES3.new(key, DES3.MODE_CBC, iv=get_random_bytes(8))
                encrypted = cipher.encrypt(pad(text, DES3.block_size))
            self.output_text.setText(base64.b64encode(encrypted).decode())
        
        elif algorithm == 'SHA-256':
            text = self.input_text.toPlainText().encode()
            hashed = hashlib.sha256(text).hexdigest()
            self.output_text.setText(hashed)
        
        elif algorithm == 'SHA-512':
            text = self.input_text.toPlainText().encode()
            hashed = hashlib.sha512(text).hexdigest()
            self.output_text.setText(hashed)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CryptoTool()
    window.show()
    sys.exit(app.exec_())

