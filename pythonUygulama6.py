import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sqlite3

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Veritabanı Kaydı")
        self.setGeometry(200, 200, 300, 200)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label_name = QLabel("Ad:", self)
        self.edit_name = QLineEdit(self)
        layout.addWidget(self.label_name)
        layout.addWidget(self.edit_name)

        self.label_surname = QLabel("Soyad:", self)
        self.edit_surname = QLineEdit(self)
        layout.addWidget(self.label_surname)
        layout.addWidget(self.edit_surname)

        self.label_gender = QLabel("Cinsiyet:", self)
        self.edit_gender = QLineEdit(self)
        layout.addWidget(self.label_gender)
        layout.addWidget(self.edit_gender)

        self.button_save = QPushButton("Kaydet", self)
        self.button_save.clicked.connect(self.saveToDatabase)
        layout.addWidget(self.button_save)

        self.setLayout(layout)

    def saveToDatabase(self):
        name = self.edit_name.text()
        surname = self.edit_surname.text()
        gender = self.edit_gender.text()

        if name and surname and gender:
            try:
                connection = sqlite3.connect("database.db")
                cursor = connection.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, gender TEXT)")
                cursor.execute("INSERT INTO Users (name, surname, gender) VALUES (?, ?, ?)", (name, surname, gender))
                connection.commit()
                connection.close()
                print("Kayıt başarıyla eklendi.")
            except sqlite3.Error as error:
                print("Veritabanı hatası:", error)
        else:
            print("Lütfen tüm alanları doldurun.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
