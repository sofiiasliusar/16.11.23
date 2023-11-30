
#! python -m PyQt5.uic.pyuic -x password.ui -o ui.py
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
from uifile import Ui_MainWindow as UMW

# 

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UMW()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.generate)
        
# дизайн
    def generate(self):
        
        password_len, ok = QInputDialog.getInt(self, 'Ваш вибір', 'Вкажіть кількість символів:', 8, 1, 15, 1) 
        # імпортуємо з QtPy5 діалогове вікно з заданими заголовком і текстом, 8 -початкове значення, 1 - найменше, 15-найбільше, 1 - крок
        if not ok:
            return #не генерує
        
        alphabet = 'abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM'
        numbers = '1234567890'
        symbols = "!@#$%^&*()-_=+|\\'\"/.<>,"

        categories = []
        if self.ui.cb_alphabet.isChecked():
            categories.extend(random.choices(alphabet, k=password_len))
        if self.ui.cb_numbers.isChecked():
            categories.extend(random.choices(numbers, k=password_len))
        if self.ui.cb_symbols.isChecked():
            categories.extend(random.choices(symbols, k=password_len))

        if not categories:
            QMessageBox.information(self, 'Помилка', 'Виберіть хоча б одну категорію.', QMessageBox.Ok)
            return
        

        password = ''.join(random.choice(categories) for _ in range(password_len))

        self.ui.resultLineEdit.setText(password)
        print(password)
        
            
                
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
# порожнє вікно





