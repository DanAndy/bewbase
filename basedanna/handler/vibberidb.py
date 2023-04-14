import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QWidget, QApplication
import viborbd
import servicee
import sys
import sqlite3
import regis2 as regis2

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from service import Ui_Form
import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi


# db = sqlite3.connect("handler\\blagodat.db")
# sql = db.cursor()



# class Registration(QtWidgets, Ui_Form):
#     def __init__(self):
#         super(Registration,self).__init__()
#         loadUi("handler\\regis2.ui",self)

        
#         self.password.setEchoMode(QtWidgets.QLineEdit.leLogin_2)
#         self.loginbutton.clicked.connect(self.loginfunction)
#         # self.createaccbutton.clicked.connect(self.gotocreate)
        

#     def loginfunction(self):

#         login=self.leLogin.text()
#         password=self.leLogin_2.text()
        
#         if login == "0000" and password == "0000":
#             print("Вы зашли как админ")
#             # loginbutton=admin()
#             MainWindow.addWidget(loginbutton)
#             MainWindow.setCurrentIndex(MainWindow.currentIndex()+1)
#         sql.execute(f"SELECT * FROM admin WHERE login = '{login}' AND pass = '{password}';")
#         db.commit() 
        

#         if sql.fetchone() == None:
#             sql.execute(f"SELECT * FROM admin WHERE login = '{login}' AND pass = '{password}';")
#             if sql.fetchone() == None:
#                 print("Такого пользователя нет")
#             else:
#                 print('Welcome')
#                 loginbutton=MainWindow(login,password)
#                 MainWindow.addWidget(loginbutton)
#                 MainWindow.setCurrentIndex(MainWindow.currentIndex()+1)
#         else:
#             print('Welcome')
#             loginbutton=MainWindow(login,password)
#             MainWindow.addWidget(loginbutton)
#             MainWindow.setCurrentIndex(MainWindow.currentIndex()+1)
    



    # def gotocreate(self):
    #     createaccbutton=CreateAcc()
    #     widget.addWidget(createaccbutton)
    #     widget.setCurrentIndex(widget.currentIndex()+1)

class MyWidget1(QWidget, Ui_Form):
    def __init__(self):
        super(MyWidget1, self).__init__()
        loadUi("handler\\service.ui", self)
        # self.setupUi(self)
        #self.cbPost.addItems(STAFF_POSTS)
        self.pushButton.clicked.connect(self.open)
        self.pushButton_2.clicked.connect(self.insert)

    def open(self):
        #try:
        self.conn = sqlite3.connect('handler\\blagodat.db')
        cur = self.conn.cursor()
        data = cur.execute("select * from 'services'")
        col_name = [i[0] for i in data.description]
        data_rows = data.fetchall()
        #except Exception as e:
            # print("Ошибка с подключением к базе данных")
            # return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount()+1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()

    def update_twStaffs(self, query="select * from services"):
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() +1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
            self.twStaffs.resizeColumnsToContents()

    def insert(self):
        row = [self.leID.text(), self.lename.text(), self.lecode.text(), self.lecount.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into workers (ID, name, code, count)
            values('{row[0]}', '{row[1]}', '{row[2]}','{row[3]}')""")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print("Не смогли добавить запись.")
            return e
        self.update_twStaffs()

class MyWidget2(QWidget, Ui_Form):
    def __init__(self):
        super(MyWidget2, self).__init__()
        loadUi("handler\\xexexex.ui", self)
        # self.setupUi(self)
        #self.cbPost.addItems(STAFF_POSTS)
        self.pushButton.clicked.connect(self.open)
        self.pushButton_2.clicked.connect(self.insert)

    def open(self):
        #try:
        self.conn = sqlite3.connect('handler\\blagodat.db')
        cur = self.conn.cursor()
        data = cur.execute("select * from workers")
        col_name = [i[0] for i in data.description]
        data_rows = data.fetchall()
        #except Exception as e:
            # print("Ошибка с подключением к базе данных")
            # return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount()+1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()

    def update_twStaffs(self, query="select * from workers"):
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() +1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
            self.twStaffs.resizeColumnsToContents()

    def insert(self):
        row = [self.leID.text(), self.lepost.text(), self.lename.text(), self.leINN.text(), self.leSNILS.text(), self.lePhone.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into workers (ID, post, name, INN, SNILS, Phone)
            values('{row[0]}', '{row[1]}', '{row[2]}','{row[3]}','{row[4]}','{row[5]}')""")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print("Не смогли добавить запись.")
            return e
        self.update_twStaffs()

class MyWidget3(QWidget, Ui_Form):
    def __init__(self):
        super(MyWidget3, self).__init__()
        loadUi("handler\\client.ui", self)
        # self.setupUi(self)
        #self.cbPost.addItems(STAFF_POSTS)
        self.pushButton.clicked.connect(self.open)
        self.pushButton_2.clicked.connect(self.insert)

    def open(self):
        #try:
        self.conn = sqlite3.connect('handler\\blagodat.db')
        cur = self.conn.cursor()
        data = cur.execute("select * from client")
        col_name = [i[0] for i in data.description]
        data_rows = data.fetchall()
        #except Exception as e:
            # print("Ошибка с подключением к базе данных")
            # return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount()+1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()

    def update_twStaffs(self, query="select * from client"):
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() +1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
            self.twStaffs.resizeColumnsToContents()

    def insert(self):
        row = [self.leID.text(),self.leFIO.text(),self.leCodeClient.text(),self.leSeria.text(),
               self.leNomer.text(),self.leHP.text(),self.lePostIndex.text(),self.leCity.text(),
               self.leStreet.text(),self.leHouse.text(),self.leFlat.text(),self.leLogin.text(),self.lePass.text(),]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into workers (ID, FIO, кодклиента, серия, номер, др, post_index, city, street, house, flat, login, pass)
            values('{row[0]}', '{row[1]}', '{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}','{row[11]}','{row[12]}')""")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print("Не смогли добавить запись.")
            return e
        self.update_twStaffs()

class MyWidget4(QWidget, Ui_Form):
    def __init__(self):
        super(MyWidget4, self).__init__()
        loadUi("handler\\zakazi.ui", self)
        # self.setupUi(self)
        #self.cbPost.addItems(STAFF_POSTS)
        self.pushButton.clicked.connect(self.open)
        self.pushButton_2.clicked.connect(self.insert)

    def open(self):
        #try:
        self.conn = sqlite3.connect('handler\\blagodat.db')
        cur = self.conn.cursor()
        data = cur.execute("select * from zakazi")
        col_name = [i[0] for i in data.description]
        data_rows = data.fetchall()
        #except Exception as e:
            # print("Ошибка с подключением к базе данных")
            # return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount()+1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()

    def update_twStaffs(self, query="select * from zakazi"):
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() +1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
            self.twStaffs.resizeColumnsToContents()

    def insert(self):
        row = [self.leID.text(), self.leCode.text(), self.leDate.text(), self.leTime.text(), self.leCodeClient.text(), self.leTimeClose.text(), self.leTimeHour.text(), self.leCodeYslygi.text(), self.leHeigh.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into zakazi (ID, Кодзаказа, Датасоздания, Времязаказа, Кодклиента, Датазакрытия, Времявчасах, кодуслуги, старшийсмены)
            values('{row[0]}', '{row[1]}', '{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}')""")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print("Не смогли добавить запись.")
            return e
        self.update_twStaffs()

class MainWindow1(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow1, self).__init__()
        loadUi("handler\\viborbd.ui", self)
        # loadUi("handler\\zakazi.ui", self)
        # loadUi("handler\\client.ui", self)
        # loadUi("handler\\service.ui", self)
        # loadUi("handler\\xexexex.ui", self)
        # self.pushButton.clicked.connect(self.gotoService)
        # self.pushButton_2.clicked.connect(self.gotoWorkers)
        # self.pushButton_3.clicked.connect(self.gotoClient)
        # self.pushButton_4.clicked.connect(self.gotoZakazi)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('MainWindow')


    def show_window_1(self):
        self.w1 = MainWindow1()
        self.w1.pushButton.clicked.connect(self.gotoService)
        self.w1.pushButton.clicked.connect(self.w1.close)
        # self.w1.show()

    # def show_window_1(self):
        # self.w1 = MainWindow1()
        self.w1.pushButton_2.clicked.connect(self.gotoWorkers)
        self.w1.pushButton_2.clicked.connect(self.w1.close)
        # self.w1.show()

    # def show_window_1(self):
        # self.w1 = MainWindow1()
        self.w1.pushButton_3.clicked.connect(self.gotoClient)
        self.w1.pushButton_3.clicked.connect(self.w1.close)
        # self.w1.show()

    # def show_window_1(self):
        # self.w1 = MainWindow1()
        self.w1.pushButton_4.clicked.connect(self.gotoZakazi)
        self.w1.pushButton_4.clicked.connect(self.w1.close)
        self.w1.show()

    def gotoService(self):
        self.w2 = MyWidget1()
        self.w2.show()
        # loadUi("handler\\service.ui", self)

    def gotoWorkers(self):
        self.w2 = MyWidget2()
        self.w2.show()
        # loadUi("handler\\xexexex.ui", self)

    def gotoClient(self):
        self.w2 = MyWidget3()
        self.w2.show()
        # loadUi("handler\\client.ui", self)
    
    def gotoZakazi(self):
        self.w2 = MyWidget4()
        self.w2.show()
        # loadUi("handler\\zakazi.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.show_window_1()
    # w.gotoService = MyWidget1
    # w.gotoWorkers = MyWidget2
    # w.gotoClient = MyWidget3
    # w.gotoZakazi = MyWidget4
    sys.exit(app.exec_())
