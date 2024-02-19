personel=["mete","okan","erdoğan","elif"]
maas=[22000,18520,24752,35412]
toplam=personel+maas
sor=input("eleman eklemek için e basınız : ")
if(sor=="e"):
    ekle=input("Adı : ")
    ekle1=int(input("Maaşı : "))
    personel.append(ekle)
    maas.append(ekle1)
for x in range(len(personel)):
    print(personel[x],maas[x])
print("-"*25)
for i,j in zip(personel,maas):
    print(f"Adı: {i} Maaşı: {j}")
print("-" * 25)
tmaas=sum(maas)
print(tmaas)
print(personel,maas)
