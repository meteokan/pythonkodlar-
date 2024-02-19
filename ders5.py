ogrenciler=["mete", "Okan","Elif",12,255,69]
print(type(ogrenciler))
print(ogrenciler)
print(len(ogrenciler))
print(ogrenciler[0:4])
print(ogrenciler[-3:-1])
for i in ogrenciler:
    print(i)
yeni_eleman=input("Değeri giriniz: ")
ogrenciler.append(yeni_eleman)
for i in ogrenciler:
    print(i)
ogrenciler.insert(3,"Çiğdem")
for i in ogrenciler:
    print(i)
veli=["veli1","veli2"]
ogrenciler.extend(veli)
for i in ogrenciler:
    print(i)
print("-"*20)
ogrenciler.remove("mete")
for i in ogrenciler:
    print(i)
print("-"*20)
ogrenciler.pop(3)
for i in ogrenciler:
    print(i)
print("-"*20)
ogrenciler.clear()
for i in ogrenciler:
    print(i)
print("-"*20)
