# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/template/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.Workpace = QtWidgets.QWidget(MainWindow)
        self.Workpace.setObjectName("Workpace")
        self.Label = QtWidgets.QLabel(self.Workpace)
        self.Label.setGeometry(QtCore.QRect(10, 10, 640, 360))
        self.Label.setText("")
        self.Label.setObjectName("Label")
        self.Show = QtWidgets.QPushButton(self.Workpace)
        self.Show.setGeometry(QtCore.QRect(10, 380, 113, 32))
        self.Show.setObjectName("Show")
        MainWindow.setCentralWidget(self.Workpace)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Show.setText(_translate("MainWindow", "Show"))

