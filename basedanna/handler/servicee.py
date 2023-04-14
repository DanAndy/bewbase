import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from service import Ui_Form

#STAFF_POSTS = ['бухгалтер', 'менеджер', 'программист']

class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setupUi(self)
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())