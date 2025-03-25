import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow  # Đảm bảo đường dẫn chính xác
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối nút bấm với chức năng tương ứng
        self.ui.bnt_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.bnt_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.plainTextEdit.toPlainText().strip(),
            "key": self.ui.plainTextEdit_2.toPlainText().strip()
        }
        self.process_request(url, payload, "encrypted_message", self.ui.plainTextEdit_3)
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.plainTextEdit_3.toPlainText().strip(),
            "key": self.ui.plainTextEdit_2.toPlainText().strip()
        }
        self.process_request(url, payload, "decrypted_message", self.ui.plainTextEdit)

    def process_request(self, url, payload, response_key, output_widget):
        """Gửi yêu cầu API và hiển thị kết quả"""
        if not payload["plain_text"] or not payload["key"]:
            self.show_message("Vui lòng nhập đầy đủ dữ liệu")
            return
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                output_widget.setPlainText(data.get(response_key, ""))
                self.show_message("Thành công!")
            else:
                self.show_message(f"Lỗi API: {response.text}")
        except requests.exceptions.RequestException as e:
            self.show_message(f"Lỗi kết nối: {e}")

    def show_message(self, text):
        """Hiển thị thông báo"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())