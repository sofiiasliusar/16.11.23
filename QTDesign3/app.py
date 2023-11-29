
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
        if not self.ui.cb_numbers.isChecked() and not self.ui.cb_alphabet.isChecked() and not self.ui.cb_symbols.isChecked():
            QMessageBox.information(self, 'Помилка', 'Виберіть хоча б одну категорію.', QMessageBox.Ok)
            return
        password_len, ok = QInputDialog.getInt(self, 'Ваш вибір', 'Вкажіть кількість символів:', 8, 1, 15, 1) 
        # імпортуємо з QtPy5 діалогове вікно з заданими заголовком і текстом, 8 -початкове значення, 1 - найменше, 15-найбільше, 1 - крок
        if not ok:
            return #початкова кількість 8
        alphabet = 'abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM'
        numbers = '1234567890'
        symbols = "!@#$%^&*()-_=+|\\'\"/.<>,"
        password = ""


    
        for x in range(password_len):
            categories =[alphabet, numbers, symbols]
            if categories:
        
                choice = random.choice(categories)
                if choice == numbers: 
                    password += random.choice(numbers) 
                elif choice == alphabet: 
                    password += random.choice(alphabet) 
                elif choice == symbols: 
                    password += random.choice(symbols)
        
        self.ui.resultLineEdit.setText(password)
        print(password)
        
            
                
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
# порожнє вікно

