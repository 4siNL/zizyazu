import sys
import UI.main, UI.addEditCoffeeForm
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3


class MyWidget(QMainWindow, UI.main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        db = sqlite3.connect('data/coffee.sqlite')
        cur = db.cursor()
        coffee = cur.execute('''SELECT * FROM coffee''').fetchall()
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Кофе',
                                                    'название сорта',
                                                    'степень обжарки',
                                                    'молотый/в зернах',
                                                    'описание вкуса', 'цена',
                                                    'объем упаковки'])
        self.tableWidget.setRowCount(0)
        for i, j in enumerate(coffee):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(j[0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(j[1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(j[2])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(j[3])))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(j[4])))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(j[5])))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(j[6])))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(str(j[7])))


class MyWidget1(QMainWindow, UI.addEditCoffeeForm.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = sqlite3.connect('data/coffee.sqlite')
        self.pushButton.clicked.connect(self.toCreate)
        self.pushButton_3.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.change)

    def toCreate(self):
        if self.lineEdit_2.text() == '' or self.lineEdit_3.text() == '' or \
                self.lineEdit_4.text() == '' or \
                self.lineEdit_5.text() == '' or \
                self.lineEdit_6.text() == '' or \
                self.lineEdit_7.text() == '' or \
                self.lineEdit_8.text() == '':
            self.label_9.setText('Заполните все поля')
        else:
            a1 = self.lineEdit_2.text()
            a2 = self.lineEdit_3.text()
            a3 = self.lineEdit_4.text()
            a4 = self.lineEdit_5.text()
            a5 = self.lineEdit_6.text()
            a6 = self.lineEdit_7.text()
            a7 = self.lineEdit_8.text()
            cur = self.db.cursor()
            cur.execute('''INSERT INTO coffee(coffee, name, roasting,
            ground_in_grains, description, price, volume) VALUES(?, ?, ?, ?, ?,
            ?, ?)''', (a1, a2, a3, a4, a5, a6, a7))
            self.db.commit()
            self.label_9.setText('Успешно!')

    def search(self):
        if self.lineEdit.text() == '':
            self.label_10.setText('Введите ID')
        else:
            cur = self.db.cursor()
            result = cur.execute('''SELECT * FROM coffee WHERE id = ?''',
                                 (self.lineEdit.text(),)).fetchone()
            if result is None:
                self.label_10.setText('Не найдено')
                return
            self.id = self.lineEdit.text()
            self.tableWidget_2.setColumnCount(7)
            self.tableWidget_2.setHorizontalHeaderLabels(['Кофе',
                                                        'название сорта',
                                                        'степень обжарки',
                                                        'молотый/в зернах',
                                                        'описание вкуса',
                                                        'цена',
                                                        'объем упаковки'])
            self.tableWidget_2.setRowCount(1)
            self.tableWidget_2.setItem(0, 0, QTableWidgetItem(str(result[1])))
            self.tableWidget_2.setItem(0, 1, QTableWidgetItem(str(result[2])))
            self.tableWidget_2.setItem(0, 2, QTableWidgetItem(str(result[3])))
            self.tableWidget_2.setItem(0, 3, QTableWidgetItem(str(result[4])))
            self.tableWidget_2.setItem(0, 4, QTableWidgetItem(str(result[5])))
            self.tableWidget_2.setItem(0, 5, QTableWidgetItem(str(result[6])))
            self.tableWidget_2.setItem(0, 6, QTableWidgetItem(str(result[7])))

    def change(self):
        for i in range(7):
            if self.tableWidget_2.item(0, i).text() == '':
                break
        else:
            a1 = self.tableWidget_2.item(0, 0).text()
            a2 = self.tableWidget_2.item(0, 1).text()
            a3 = self.tableWidget_2.item(0, 2).text()
            a4 = self.tableWidget_2.item(0, 3).text()
            a5 = self.tableWidget_2.item(0, 4).text()
            a6 = self.tableWidget_2.item(0, 5).text()
            a7 = self.tableWidget_2.item(0, 6).text()
            cur = self.db.cursor()
            cur.execute('''UPDATE coffee SET coffee = ?, name = ?,
            roasting = ?, ground_in_grains = ?, description = ?, price = ?,
            volume = ? WHERE id = ?''', (a1, a2, a3, a4, a5, a6, a7, self.id))
            self.db.commit()
            self.label_10.setText('Успешно!')
            return
        self.label_10.setText('Заполните все поля')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex1 = MyWidget1()
    ex1.show()
    sys.exit(app.exec_())