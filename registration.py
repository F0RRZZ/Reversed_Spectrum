import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget


def is_user_in_database(nickname: str) -> bool:
    with sqlite3.connect('database.sqlite') as connection:
        cur = connection.cursor()
        for i in cur.execute("""SELECT nickname FROM data""").fetchall():
            if i[0] == nickname:
                return True
        return False


class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('uis/registration.ui', self)
        self.myclose = False
        self.initUI()

    def initUI(self):
        pixmap = QPixmap()
        pixmap.load('images/logo.png')
        self.logo.setPixmap(pixmap)

        self.signup.clicked.connect(self.sign_up)

    def sign_up(self):
        if (not self.nickname_le.text()) or (not self.password_le.text()):
            self.error_lbl.setText('Fill in all the fields!')
            return
        nickname, password = self.nickname_le.text(), self.password_le.text()
        with sqlite3.connect('database.sqlite') as connection:
            cur = connection.cursor()
            if not is_user_in_database(nickname):
                cur.execute("""INSERT INTO data(nickname, password) VALUES(?, ?)""", (nickname, password))
                with open(file="account_data.txt", mode='w', encoding="utf-8") as file:
                    file.write(nickname + "\n0\n0\n0")
            else:
                for i in cur.execute("""SELECT * FROM data WHERE nickname = ?""", (nickname, )).fetchall():
                    if i[2] == password:
                        with open(file="account_data.txt", mode='w', encoding="utf-8") as file:
                            file.write(f"{nickname}\n{i[3]}\n{i[4]}\n{i[5]}")
                        self.close()
                    else:
                        self.error_lbl.setText('Incorrect password!')
                        return


def start():
    app = QApplication(sys.argv)
    registration_window = RegistrationWindow()
    registration_window.show()
    app.exec_()
