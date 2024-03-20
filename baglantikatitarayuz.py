import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from kaydet import Ui_setWindowTitle
import mysql.connector

class KayitArayuzu(QtWidgets.QMainWindow):
    def __init__(self):
        super(KayitArayuzu,self).__init__()
        self.ui=Ui_setWindowTitle()
        self.ui.setupUi(self)
        self.ui.kaydet_button.clicked.connect(self.kaydet)
    def kaydet(self):
        tckimlik=self.ui.tckimlik_input.text()
        ad=self.ui.ad_input.text()
        soyad=self.ui.soyad_input.text()
        dogumtarihi=self.ui.dogum_calendar.selectedDate().toString(Qt.ISODate)

        if self.ui.erkek_radio.isChecked():
            cinsiyet='E'
        elif self.ui.kadin_radio.isChecked():
            cinsiyet='K'
        else:
            cinsiyet=''
        try:
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="root123",
                database="pymete"
            )
            imlec=mydb.cursor()

            sql="INSERT INTO musteri(tckimlik,ad,soyad,dogumtarihi,cinsiyet) VALUES(%s, %s, %s, %s, %s)"
            veriler=(tckimlik, ad, soyad, dogumtarihi, cinsiyet)

            imlec.execute(sql, veriler)
            mydb.commit()
            self.temizle()  # Alanları temizle
            print("Kayıt başarıyla eklendi.")
            self.ui.mesaj_label.setText("Kayıt başarıyla eklendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)
        finally:
            mydb.close()

    def temizle(self):
        self.ui.tckimlik_input.clear()
        self.ui.ad_input.clear()
        self.ui.soyad_input.clear()
        self.ui.erkek_radio.setChecked(False)
        self.ui.kadin_radio.setChecked(False)
def app():
    app= QtWidgets.QApplication(sys.argv)
    win=KayitArayuzu()
    win.show()
    sys.exit(app.exec_())

app()