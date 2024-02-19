import dortislem
while True:
    adi=input("Adınız: ")
    if (adi=="cık"):
        break
    dogum_yili=int(input("doğum yılınız: "))
    kilo=int(input("kilonuz: "))
    boy=int(input("boyunuz: "))
    def fonksiyonum(i):
        print("merhaba",i)
    fonksiyonum(adi)
    deger=dortislem.carpma(boy,boy)
    deger2=dortislem.oran(kilo,deger)
    print(round(deger2*10000,2))
    sonuc=deger2*10000
    if (sonuc<18):
        print("zayıf")
    elif(sonuc<25):
        print("normal")
    elif(sonuc<30):
        print("kilolu")
    else:
        print("obez")
    simdi=2024
    yas=dortislem.fark(simdi,dogum_yili)
    print(f"yaşınız: {yas}")



