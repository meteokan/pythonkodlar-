a="    Merhaba dünya     "
print(a)
print(len(a))
b=a.split()
print(len(a.strip()))
print(len(b))
print(b[:8])
print(a.upper())
isim=input("Adınız : ")
print(isim)
print("İsim karakter sayısı: {} ".format(len(isim)))
print(isim.strip())
temiz_isim=isim.strip()
print("temizlendikten sonra karakter sayısu : {}".format(len(temiz_isim)))
print(temiz_isim.upper())
print(temiz_isim.replace("salak","*****"))
renk=input("Kızın göz rengi : ")
siir="""
Ben maviyi severim,
Buz mavisi,
Gök mavisi,
Deniz mavisi,
Ama en çok senin koyu {},
Gözlerindeki maviyi sevdim,
Ben seni sevdim.
""".format(renk)
print(siir)
cumle=siir.split(",")
print(cumle)
print("şiirdeki cümle saysı : ",len(cumle))
print("merhaba \"mete\" \n nasılsın?")

