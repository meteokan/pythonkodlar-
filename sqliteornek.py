import sqlite3
baglan =sqlite3.connect("chinook.db")
imlec = baglan.cursor()
imlec.execute("select * from customers")
sonuc=imlec.fetchall()
for i in sonuc:
    print(i)
baglan.close()
