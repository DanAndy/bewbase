# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 480)
        Dialog.setStyleSheet("background-color: rgb(33, 33, 33)")
        self.loginbutton = QtWidgets.QPushButton(Dialog)
        self.loginbutton.setGeometry(QtCore.QRect(120, 330, 151, 51))
        self.loginbutton.setStyleSheet("color: rgb(20, 255, 236)")
        self.loginbutton.setObjectName("loginbutton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 110, 181, 31))
        self.lineEdit.setStyleSheet("color: rgb(20, 255, 236)")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 180, 181, 31))
        self.lineEdit_2.setStyleSheet("color: rgb(20, 255, 236)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 110, 71, 31))
        self.label.setStyleSheet("color: rgb(20, 255, 236)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 180, 61, 31))
        self.label_2.setStyleSheet("color: rgb(20, 255, 236)")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loginbutton.setText(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "login"))
        self.label_2.setText(_translate("Dialog", "password"))
