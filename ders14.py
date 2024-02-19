deger=int(input("Değeri giriniz: "))
sonuc={i:pow(i,3) for i in range(1,deger+1)}
print(sonuc)
def sozluk_cevir(keys,values):
    sozluk={}
    for j in range(len(keys)):
        sozluk[keys[j]]=values[j]
    return sozluk
keys=["isim","yas","cinsiyet"]
values=["mete",12,"E"]
print(sozluk_cevir(keys,values))
