import sqlite3
import sys 
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication




def login(login, passw, signal):
    con = sqlite3.connect('handler/aaapopbd.db')
    cur = con.cursor()

    # Проверяем есть ли такой пользователь
    statement = f"SELECT login from users WHERE login='{login}' AND pass = '{passw}';"
    cur.execute(statement)
    if not cur.fetchone():
        signal.emit('Такого пользователя нету ')
    else:
        signal.emit("ты принят")
        
        # pushButton_2 = MyWidget(login, passw)
        # MyWidget.addWidget(pushButton_2)
        # MyWidget.setCurrentIndex(MyWidget.currentIndex()+1)
        #class MainWindow(QDialog):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         loadUi("des.py",self)
#         self.pushButton_2.clicked.connect(self.gotoScreen2)


#     cur.close()
#     con.close()


#     class MainWindow(QDialog):
#         def __init__(self):
#             super(MainWindow, self).__init__()
#             loadUi("des.py",self)
#             self.pushButton_2.clicked.connect(self.gotoScreen2)

#         def gotoScreen2(self):
#             widget.setCurrentIndex(widget.currentIndex()+1)



#     class Screen2(QDialog):
#         def __init__(self):
#             super(Screen2,self).__init__()
#             loadUi("xexex.ui",self)




# # main

#     app = QApplication(sys.argv)
#     widget=QtWidgets.QStackedWidget()
#     des =MainWindow()
#     xexex=Screen2()
#     widget.addWidget(des)
#     widget.addWidget(xexex)
#     widget.show()

def register(login, passw, signal):
    con = sqlite3.connect('handler/aaapopbd.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE login="{login}";')
    value = cur.fetchall()

    if value != []:
        signal.emit('Такой ник уже используется!')
    elif value == []:
        cur.execute(f"INSERT INTO users (login, pass) VALUES ('{login}', '{passw}')")
        signal.emit('Вы успешно зарегистрированы!')
        con.commit()

    cur.close()
    con.close()
