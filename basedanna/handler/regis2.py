# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regis2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 479)
        Form.setStyleSheet("background-color: rgb(33, 33, 33)")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 70, 71, 31))
        self.label.setStyleSheet("color: rgb(20, 255, 236)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 150, 61, 31))
        self.label_2.setStyleSheet("color: rgb(20, 255, 236)")
        self.label_2.setObjectName("label_2")
        self.email = QtWidgets.QLineEdit(Form)
        self.email.setGeometry(QtCore.QRect(180, 70, 181, 31))
        self.email.setStyleSheet("color: rgb(20, 255, 236)")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(180, 150, 181, 31))
        self.password.setStyleSheet("color: rgb(20, 255, 236)")
        self.password.setObjectName("password")
        self.loginbutton = QtWidgets.QPushButton(Form)
        self.loginbutton.setGeometry(QtCore.QRect(120, 310, 151, 51))
        self.loginbutton.setStyleSheet("color: rgb(20, 255, 236)")
        self.loginbutton.setObjectName("loginbutton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "login"))
        self.label_2.setText(_translate("Form", "password"))
        self.loginbutton.setText(_translate("Form", "Login"))
