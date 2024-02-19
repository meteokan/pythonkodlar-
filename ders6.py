personel=["hakan","mete","elif","buse","mustafa"]
yeni_liste=[]
eleman=input("Yeni elemanı giriniz: ").lower().strip()
personel.append(eleman)
personel.sort()
j=1
for i in personel:
    print("{}.{}".format(j,i.upper()))
    j+=1
print("Personel sayınız {}'dır.".format(len(personel)))
print("*"*15)
for x in range(len(personel)):
    print("{}.{}".format(x+1,personel[x].upper()))
for y in personel:
    if "a" in y:
        yeni_liste.append(y)
print(yeni_liste)
fiyat=[22,8,5]
print(sum(fiyat))