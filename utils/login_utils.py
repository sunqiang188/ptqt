from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QMenu, QGraphicsOpacityEffect, QDesktopWidget, qApp
from PyQt5.QtCore import Qt
import utils.detector_server
import utils.platform, utils.login


class LoginWindow(utils.login.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        # 登录界面居中显示
        self.center()
        # 登录界面无边框
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.pushButton_quit.clicked.connect(self.closeWindow)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2), int((screen.height() - size.height())/2))

    def closeWindow(self):
        result = QMessageBox.question(self, '退出', '确定退出吗？', QMessageBox.Yes|QMessageBox.No)
        if result == QMessageBox.Yes:
            qApp.quit()


class DetectorMainWindow(utils.detector_server.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(DetectorMainWindow, self).__init__()
        self.setupUi(self)
        self.center()
        self.pushButton_video.clicked.connect(self.openVideo)
        self.pushButton_model.clicked.connect(self.openModel)
        self.pushButton_save.clicked.connect(self.saveResult)

    # 打开视频
    def openVideo(self):
        video_name, ok = QFileDialog.getOpenFileName(self, '打开视频', '', '*.mp4')
        if ok:
            QMessageBox.information(self, '成功', '视频加载成功')
        else:
            QMessageBox.warning(self, '错误', '视频加载失败，请重新加载')

    # 打开模型
    def openModel(self):
        model_name, ok = QFileDialog.getOpenFileName(self, '打开模型', '', 'All File(*)')
        if ok:
            QMessageBox.information(self, '成功', '模型加载成功')
        else:
            QMessageBox.warning(self, '错误', '模型加载失败，请重新加载')

    def saveResult(self):
        result_name, ok = QFileDialog.getOpenFileName(self, '保存结果', '', 'All File(*)')
        if ok:
            QMessageBox.information(self, '成功', '结果保存成功')
        else:
            QMessageBox.warning(self, '错误', '结果保存失败')

    # 退出警告
    def closeEvent(self, event):
        result = QMessageBox.question(self, '退出', '你确定要退出吗?', QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 右键快捷菜单
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        openMenu = cmenu.addMenu('打开')
        videoAct = openMenu.addAction('打开视频')
        modelAct = openMenu.addAction('打开模型')
        videoAct.triggered.connect(self.openVideo)
        modelAct.triggered.connect(self.openModel)
        cmenu.exec_(self.mapToGlobal(event.pos()))

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2), int((screen.height() - size.height())/2))


class platformWindow(utils.platform.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(platformWindow, self).__init__()
        self.setupUi(self)
        self.center()
        self.initUI()

    def initUI(self):
        op1 = QGraphicsOpacityEffect()
        op1.setOpacity(0.8)
        self.pushButton_video.setGraphicsEffect(op1)

        op2 = QGraphicsOpacityEffect()
        op2.setOpacity(0.8)
        self.pushButton_server.setGraphicsEffect(op2)

    def closeEvent(self, event):
        result = QMessageBox.question(self, '退出', '你确定要退出吗？', QMessageBox.Yes|QMessageBox.No)
        if result == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2), int((screen.height() - size.height())/2))
