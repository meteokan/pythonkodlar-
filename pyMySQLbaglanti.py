import mysql.connector
def kayitislemi():
    mydb = mysql.connector.connect(
        host= "localhost", #192.52.65.87
        user="root",
        password="root123",
        database="pymete"
    )
    # print(mydb)
    imlec=mydb.cursor()
    # imlec.execute("CREATE DATABASE pymete")
    # databse oluşmuş mu kontrol edelim.
    # imlec.execute("SHOW DATABASES")
    # for x in imlec:
    #     print(x)
    # imlec.execute("CREATE TABLE musteriler(isim VARCHAR(255), adres VARCHAR(255)) ")

    # kaydetme işlemi
    sql="INSERT INTO musteri(tckimlik,ad,soyad,dogumtarihi,cinsiyet) VALUES(%s," \
        "%s,%s,%s,%s)"
    veriler=("123","mete","okan","2001-9-9.","E")

    try:
        mydb.commit()
    except mysql.connector.Error as err:
        print("Hata:",err)
    finally:
        mydb.close()
        print("Database bağlantısı kesildi.")
kayitislemi()