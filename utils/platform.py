# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'platform.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(730, 300)
        MainWindow.setMinimumSize(QtCore.QSize(730, 300))
        MainWindow.setMaximumSize(QtCore.QSize(730, 300))
        MainWindow.setTabletTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("#MainWindow{border-image: url(:/selectplatform/hisense.png);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_server = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_server.setGeometry(QtCore.QRect(20, 70, 290, 140))
        self.pushButton_server.setMinimumSize(QtCore.QSize(290, 140))
        self.pushButton_server.setMaximumSize(QtCore.QSize(290, 140))
        font = QtGui.QFont()
        font.setFamily("方正书宋_GBK")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_server.setFont(font)
        self.pushButton_server.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_server.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/platform/ico/server.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_server.setIcon(icon)
        self.pushButton_server.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_server.setAutoRepeat(False)
        self.pushButton_server.setObjectName("pushButton_server")
        self.pushButton_video = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_video.setGeometry(QtCore.QRect(420, 70, 290, 140))
        self.pushButton_video.setMinimumSize(QtCore.QSize(290, 140))
        self.pushButton_video.setMaximumSize(QtCore.QSize(290, 140))
        font = QtGui.QFont()
        font.setFamily("方正书宋_GBK")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_video.setFont(font)
        self.pushButton_video.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/platform/ico/camera.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_video.setIcon(icon1)
        self.pushButton_video.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_video.setObjectName("pushButton_video")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "平台选择"))
        self.pushButton_server.setText(_translate("MainWindow", "服务器平台"))
        self.pushButton_video.setText(_translate("MainWindow", "声像一体机平台"))
import image.image_rc
