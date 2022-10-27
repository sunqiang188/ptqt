import sys
import utils.login
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from utils import data
from utils.login_utils import DetectorMainWindow, platformWindow


class LoginMainWindow(utils.login_utils.LoginWindow, QMainWindow):
    def __init__(self):
        super(LoginMainWindow, self).__init__()
        self.pushButton_login.clicked.connect(self.login_button)

    def login_button(self):
        if self.lineEdit_password.text() == "":
            QMessageBox.warning(self, '警告', '密码不能为空，请重新输入！')
            return None

        if (self.lineEdit_password.text() == data.password) and self.lineEdit_user.text() == data.username:
            platform.show()
            self.close()

        else:
            QMessageBox.warning(self, '错误', '账号或者密码错误，请重新输入！')
            self.lineEdit_password.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginMainWindow()
    platform = platformWindow()
    detector = DetectorMainWindow()
    platform.pushButton_server.clicked.connect(detector.show)
    window.show()
    sys.exit(app.exec_())
