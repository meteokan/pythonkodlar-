liste=["elma", "armut"]
print(liste)
liste[0]="Muz"
liste.remove("armut")
print(liste)
demet=("mete","okan")
demet1=("erdoğan","elif")
yeni_demet=list(demet)+list(demet1)
print(type(yeni_demet))
Ydemet=tuple(yeni_demet)
print(type(Ydemet))
#demet[0]="erdoğan"
#set veri yapısı
personel={"hakan","mine",65,85}
print(personel)
for x in personel:
    print(x)
print(len(personel))
#dictinary veriyapısı
urunler=({"urun_adi":"Çanta","urun_Fiyati":"2500"})
print(type(urunler))
print(urunler["urun_adi"])
print(urunler["urun_Fiyati"])
print(urunler.values())
print(urunler.keys())
print(urunler.items())
print(urunler.get("urun_adi"))
for k in urunler.items():
    print(k)
for k, v in urunler.items():
    print(k, v)







