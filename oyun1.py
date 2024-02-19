import random
deger=random.randrange(1,100)
print(deger)
i=1
while True:
    tahmin=int(input("Tahmininiz : "))
    if (deger==tahmin):
        print(f"{i}.tahmin de kazandınız.")
        break
    elif(deger<tahmin):
        print(f"{i}.tahmin {tahmin} daha küçük değer giriniz.")
    elif(deger>tahmin):
        print(f"{i}.tahmin {tahmin} daha büyük değer giriniz.")
    i+=1

