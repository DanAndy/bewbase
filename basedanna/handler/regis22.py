import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QDialog, QApplication
from PyQt5.uic import loadUi 
import regis2

class Login(QWidget):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("handler\\regis2.ui",self)
        self.loginbutton.clicked.connect(self.loginfuction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def loginfuction(self):
        email=self.email.text()
        password=self.password.text()
        print("Succes", email, "Succes pass", password)

app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(479)
widget.show()
app.exec_()

