# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import QRect,QMetaObject,QCoreApplication
from PyQt5.QtWidgets import QMainWindow,QWidget,QScrollArea,QVBoxLayout,QFrame,QPushButton,QLineEdit,QLabel,QMenuBar,QStatusBar,QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QRect(559, 10, 231, 541))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 229, 539))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 231, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(20, 10, 521, 541))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.start = QPushButton(self.frame)
        self.start.setGeometry(QRect(370, 440, 111, 51))
        self.start.setObjectName("start")
        self.stop = QPushButton(self.frame)
        self.stop.setGeometry(QRect(230, 440, 111, 51))
        self.stop.setObjectName("stop")
        self.add_key = QPushButton(self.frame)
        self.add_key.setGeometry(QRect(400, 180, 75, 23))
        self.add_key.setObjectName("add_key")
        self.key_edit = QLineEdit(self.frame)
        self.key_edit.setGeometry(QRect(50, 80, 171, 21))
        self.key_edit.setObjectName("key_edit")
        self.music_choose = QPushButton(self.frame)
        self.music_choose.setGeometry(QRect(260, 80, 211, 23))
        self.music_choose.setObjectName("music_choose")
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(50, 60, 47, 13))
        self.label.setObjectName("label")
        self.frame2 = QFrame(self.centralwidget)
        self.frame2.setGeometry(QRect(0, 0, 0, 0))
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.frame2.setObjectName("frame")
        self.key_edit2 = QLineEdit(self.frame2)
        self.key_edit2.setGeometry(QRect(50, 80, 171, 21))
        self.key_edit2.setObjectName("key_edit2")
        self.music_choose2 = QPushButton(self.frame2)
        self.music_choose2.setGeometry(QRect(260, 80, 211, 23))
        self.music_choose2.setObjectName("music_choose2")
        self.label2 = QLabel(self.frame2)
        self.label2.setGeometry(QRect(50, 60, 47, 13))
        self.label2.setObjectName("label")
        self.update = QPushButton(self.frame2)
        self.update.setGeometry(QRect(400, 140, 75, 23))
        self.update.setObjectName("update")
        self.delete_2 = QPushButton(self.frame2)
        self.delete_2.setGeometry(QRect(400, 170, 75, 23))
        self.delete_2.setObjectName("delete_2")
        self.pushButton = QPushButton(self.frame2)
        self.pushButton.setGeometry(QRect(30, 450, 101, 61))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KeySounder"))
        self.start.setText(_translate("MainWindow", "start keysounder"))
        self.stop.setText(_translate("MainWindow", "stop keysounder"))
        self.add_key.setText(_translate("MainWindow", "add"))
        self.music_choose.setText(_translate("MainWindow", "No music selected"))
        self.label.setText(_translate("MainWindow", "key"))
        self.pushButton.setText(_translate("MainWindow", "go back"))
        self.delete_2.setText(_translate("MainWindow", "delete"))
        self.update.setText(_translate("MainWindow", "update"))
        self.music_choose2.setText(_translate("MainWindow", "No music selected"))
        self.label2.setText(_translate("MainWindow", "key"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
