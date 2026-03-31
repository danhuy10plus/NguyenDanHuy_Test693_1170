import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QTextEdit, QGroupBox, QFormLayout)
from PyQt5.QtCore import Qt
from cipher.transposition import TranspositionCipher 

class TranspositionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cipher = TranspositionCipher()
        self.initUI()

    def initUI(self):
        # Thiết lập cửa sổ chính
        self.setWindowTitle('TRANS CIPHER - Desktop Version')
        self.setFixedWidth(500)
        
        main_layout = QVBoxLayout()

        # Tiêu đề
        title_label = QLabel("TRANS CIPHER")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-weight: bold; font-size: 25px; margin-bottom: 20px;")
        main_layout.addWidget(title_label)

        # --- PHẦN ENCRYPTION ---
        encrypt_group = QGroupBox("ENCRYPTION")
        encrypt_group.setStyleSheet("QGroupBox { font-weight: bold; color: blue; }")
        encrypt_layout = QFormLayout()

        self.input_plain = QLineEdit()
        self.input_plain.setPlaceholderText("Input Plain Text")
        
        self.key_plain = QLineEdit()
        self.key_plain.setPlaceholderText("Input Key (Number)")
        
        self.btn_encrypt = QPushButton("Encrypt")
        self.btn_encrypt.setStyleSheet("background-color: #007bff; color: white; padding: 5px;")
        self.btn_encrypt.clicked.connect(self.handle_encrypt)

        encrypt_layout.addRow("Plain text:", self.input_plain)
        encrypt_layout.addRow("Key:", self.key_plain)
        encrypt_layout.addRow(self.btn_encrypt)
        encrypt_group.setLayout(encrypt_layout)
        main_layout.addWidget(encrypt_group)

        # --- PHẦN DECRYPTION ---
        decrypt_group = QGroupBox("DECRYPTION")
        decrypt_group.setStyleSheet("QGroupBox { font-weight: bold; color: blue; }")
        decrypt_layout = QFormLayout()

        self.input_cipher = QLineEdit()
        self.input_cipher.setPlaceholderText("Input Cipher Text")
        
        self.key_cipher = QLineEdit()
        self.key_cipher.setPlaceholderText("Input Key (Number)")
        
        self.btn_decrypt = QPushButton("Decrypt")
        self.btn_decrypt.setStyleSheet("background-color: #007bff; color: white; padding: 5px;")
        self.btn_decrypt.clicked.connect(self.handle_decrypt)

        decrypt_layout.addRow("Cipher text:", self.input_cipher)
        decrypt_layout.addRow("Key:", self.key_cipher)
        decrypt_layout.addRow(self.btn_decrypt)
        decrypt_group.setLayout(decrypt_layout)
        main_layout.addWidget(decrypt_group)

        # --- PHẦN KẾT QUẢ ---
        result_label = QLabel("RESULT:")
        result_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        main_layout.addWidget(result_label)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setStyleSheet("background-color: #f8f9fa;")
        main_layout.addWidget(self.result_display)

        self.setLayout(main_layout)

    def handle_encrypt(self):
        try:
            text = self.input_plain.text()
            key = int(self.key_plain.text())
            encrypted = self.cipher.encrypt(text, key)
            
            output = f"Original: {text}\nKey: {key}\nEncrypted Text: {encrypted}"
            self.result_display.setText(output)
        except ValueError:
            self.result_display.setText("Error: Key must be a number!")
        except Exception as e:
            self.result_display.setText(f"Error: {str(e)}")

    def handle_decrypt(self):
        try:
            text = self.input_cipher.text()
            key = int(self.key_cipher.text())
            decrypted = self.cipher.decrypt(text, key)
            
            output = f"Cipher: {text}\nKey: {key}\nDecrypted Text: {decrypted}"
            self.result_display.setText(output)
        except ValueError:
            self.result_display.setText("Error: Key must be a number!")
        except Exception as e:
            self.result_display.setText(f"Error: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TranspositionApp()
    ex.show()
    sys.exit(app.exec_())