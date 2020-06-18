import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5 import QtPrintSupport
from PyQt5.QtGui import *
from PyQt5.QtCore import *
errors = ['Делить на 0' + '\n' + 'нельзя !', 'Неправильная' + '\n' + 'запись!']

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui',self)
        #кнопки 0 - 9
        self.push0.clicked.connect(self.print_)
        self.push1.clicked.connect(self.print_)
        self.push2.clicked.connect(self.print_)
        self.push3.clicked.connect(self.print_)
        self.push4.clicked.connect(self.print_)
        self.push5.clicked.connect(self.print_)
        self.push6.clicked.connect(self.print_)
        self.push7.clicked.connect(self.print_)
        self.push8.clicked.connect(self.print_)
        self.push9.clicked.connect(self.print_)
        #кнопки операций и скобок
        self.pushdiv.clicked.connect(self.print_)
        self.pushmul.clicked.connect(self.print_)
        self.pushsum.clicked.connect(self.print_)
        self.pushmin.clicked.connect(self.print_)
        self.pushs1.clicked.connect(self.print_)
        self.pushs2.clicked.connect(self.print_)
        #равно и очистить
        self.pusheval.clicked.connect(self.calc)
        self.pushdel.clicked.connect(self.del_one)
        self.pushdelall.clicked.connect(self.dell_all)

    def print_(self, a):
        if self.label.text() == '0' or self.label.text() == errors[0] or self.label.text() == errors[1]:
            self.label.setText('')
        sender = self.label.text() + self.sender().text()
        self.label.setText(sender)
    
    def calc(self):
        try:
            answer = eval(self.label.text())
            self.label.setText(str(answer))
        except ArithmeticError:
            self.label.setText(str(errors[0]))
        except Exception:
            self.label.setText(errors[1])

    def del_one(self, a):
        text = self.label.text()
        self.label.setText(text[:-1])

    def dell_all(self):
        self.label.setText('')

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Calculator()  # Создаём объект класса Calculator
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
