urunler={"Masa":2000,"Sandalye":3000,"Tabak":1000,"Kitap":100}
aranan_urun=input("Aradığınız ürün: ").capitalize()
if aranan_urun in urunler:
    print("Bu ürün mevcuttur.")
else:
    print("Ürün yok")
oran=1.25
# for i,j in urunler.items():
#     print(i,j)
toplam_deger=0
z_toplam_deger=0
for i in urunler:
    print(i,urunler[i],round(urunler[i]*oran))
    toplam_deger+=urunler[i]
    z_toplam_deger+=urunler[i]*oran
print("Zam öncesi: ",toplam_deger)
print("Zam sonrası: ",z_toplam_deger)
# iki listeyi sözlüğe çevirme
elemanlar=["mete","okan","elif"]
maas=[20000,30000,40000]
katsayi=1.50
for j in range(len(elemanlar)):
    print(elemanlar[j],maas[j]*katsayi)
    maas[j]=maas[j]*katsayi
sozluk=dict(zip(elemanlar,maas))
print(sozluk)
for k,v in sozluk.items():
    print(f"isim : {k} maaş: {v}TL")
