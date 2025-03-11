import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow  # Sửa tên lớp từ Ui MainWindow thành Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):  # Sửa _init_ thành __init__
        super().__init__()
        self.ui = Ui_MainWindow()  # Sửa self.ui Ui MainWindow() thành self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.plain_TextEdit.toPlainText(),  # Sửa từ txt_plain_text thành plain_TextEdit
            "key": self.ui.plain_TextEdit_2.toPlainText()  # Sửa từ txt_key thành plain_TextEdit_2
        }
        try:
            response = requests.post(url, json=payload)  # Sửa lỗi cú pháp
            if response.status_code == 200:  # Sửa = thành ==
                data = response.json()  # Sửa lỗi cú pháp
                self.ui.plain_TextEdit_3.setPlainText(data["encrypted_message"])  # Sửa từ txt_cipher_text thành plain_TextEdit_3
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.plain_TextEdit_3.toPlainText(),  # Sửa từ txt_cipher_text thành plain_TextEdit_3
            "key": self.ui.plain_TextEdit_2.toPlainText()  # Sửa từ txt_key thành plain_TextEdit_2
        }
        try:
            response = requests.post(url, json=payload)  # Sửa lỗi cú pháp
            if response.status_code == 200:  # Sửa = thành ==
                data = response.json()  # Sửa lỗi cú pháp
                self.ui.plain_TextEdit.setPlainText(data["decrypted_message"])  # Sửa từ txt_plain_text thành plain_TextEdit
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

if __name__ == "__main__":  # Sửa _main_ thành __main__
    app = QApplication(sys.argv)
    window = MyApp()  # Sửa window MyApp() thành window = MyApp()
    window.show()
    sys.exit(app.exec_())