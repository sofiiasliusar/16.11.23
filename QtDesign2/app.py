from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow as UMW
from random import choice


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UMW()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.exemple)
        self.ui.btn_generate.clicked.connect(self.generate)
        
    def exemple(self):
        print(1)
# дизайн
    def generate(self, password_len=8):
        alphabet = 'abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM'
        numbers = '1234567890'
        symbols = "!@#$%^&*()-_=+|\\'\"/.<>,"
        password = ""

        for x in range(password_len):
            if self.ui.cb_numbers.is_enabled():
                digit = choice(numbers)
                password += digit
            if self.ui.cb_alphabet.is_enabled():
                letter = choice(alphabet)
                password += letter
            symbol = choice(symbols)
            password += symbol
        
        print(password)          

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
# порожнє вікно
