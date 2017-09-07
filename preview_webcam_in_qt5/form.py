# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startButton = QtWidgets.QPushButton(Form)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.ImgWidget = QtWidgets.QWidget(self.groupBox)
        self.ImgWidget.setGeometry(QtCore.QRect(0, 20, 978, 723))
        self.ImgWidget.setStyleSheet("background-color:#E5E5E5")
        self.ImgWidget.setObjectName("ImgWidget")
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.startButton.setText(_translate("Form", "start"))
        self.groupBox.setTitle(_translate("Form", "preview"))

