# dosya=open("isimler.txt","w",encoding="utf-8")
# dosya.write("yeni değer")
# dosya.write("ikinci değer")
dosya=open("isimler.txt","a",encoding="utf-8")
dosya.write("diğer değerler nerede?\n")
kisiler=["mete","okan","elif","ali"]
adet=[2.5,6,3,45]
birlikte=dict(zip(kisiler,adet))
for x in range(len(kisiler)):
    kisi=f"{kisiler[x]}-->{adet[x]} "
    dosya.write(kisi)

dosya=open("isimler.txt","r",encoding="utf-8")
print(dosya.read())
dosya.close()