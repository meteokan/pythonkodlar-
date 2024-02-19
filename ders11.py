kullanilabilir_karakterler="0123456789+-*/"
while True:
    girdi = input("yapmak istediğiniz işlemi -*/+ kullanarak yazınız. ")
    if(girdi=="q"):
        print("çıkış yaptınız.")
        break
    for x in girdi:
        if x not in kullanilabilir_karakterler:
            print("Burada matematiksel işlemler yapılır.")
            quit()
    sonuc=eval(girdi)
    print(f"verdiğiniz işlemin sonucu:{sonuc}")
