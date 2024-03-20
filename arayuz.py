import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QRadioButton, QCalendarWidget
from PyQt5.QtCore import Qt
import mysql.connector

class KayitArayuzu(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Müşteri Kayıt Arayüzü')

        self.tckimlik_label = QLabel('TC Kimlik:')
        self.tckimlik_input = QLineEdit()

        self.ad_label = QLabel('Ad:')
        self.ad_input = QLineEdit()

        self.soyad_label = QLabel('Soyad:')
        self.soyad_input = QLineEdit()

        self.dogum_label = QLabel('Doğum Tarihi:')
        self.dogum_calendar = QCalendarWidget()

        self.cinsiyet_label = QLabel('Cinsiyet:')
        self.erkek_radio = QRadioButton('Erkek')
        self.kadin_radio = QRadioButton('Kadın')

        self.kaydet_button = QPushButton('Kaydet')
        self.kaydet_button.clicked.connect(self.kaydet)

        v_box = QVBoxLayout()
        v_box.addWidget(self.tckimlik_label)
        v_box.addWidget(self.tckimlik_input)
        v_box.addWidget(self.ad_label)
        v_box.addWidget(self.ad_input)
        v_box.addWidget(self.soyad_label)
        v_box.addWidget(self.soyad_input)
        v_box.addWidget(self.dogum_label)
        v_box.addWidget(self.dogum_calendar)
        v_box.addWidget(self.cinsiyet_label)
        v_box.addWidget(self.erkek_radio)
        v_box.addWidget(self.kadin_radio)
        v_box.addWidget(self.kaydet_button)

        self.setLayout(v_box)
        self.show()

    def kaydet(self):
        tckimlik = self.tckimlik_input.text()
        ad = self.ad_input.text()
        soyad = self.soyad_input.text()
        dogumtarihi = self.dogum_calendar.selectedDate().toString(Qt.ISODate)

        if self.erkek_radio.isChecked():
            cinsiyet = 'E'
        elif self.kadin_radio.isChecked():
            cinsiyet = 'K'
        else:
            cinsiyet = ''

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root123",
                database="pymete"
            )
            imlec = mydb.cursor()

            sql = "INSERT INTO musteri(tckimlik,ad,soyad,dogumtarihi,cinsiyet) VALUES(%s, %s, %s, %s, %s)"
            veriler = (tckimlik, ad, soyad, dogumtarihi, cinsiyet)

            imlec.execute(sql, veriler)
            mydb.commit()

            self.temizle()  # Alanları temizle
            print("Kayıt başarıyla eklendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)
        finally:
            mydb.close()

    def temizle(self):
        self.tckimlik_input.clear()
        self.ad_input.clear()
        self.soyad_input.clear()
        self.erkek_radio.setChecked(False)
        self.kadin_radio.setChecked(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KayitArayuzu()
    sys.exit(app.exec_())
