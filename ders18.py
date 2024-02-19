# dosya=open("yeni_dosya.txt","a",encoding="utf-8")
# dosya.write("deneme")
# dosya.close()

with open("deneme1.txt","w",encoding="utf-8") as dosya:
    satir=["1. satır\n","2. satır\n","3. satır\n"]
    dosya.writelines(satir)
with open("deneme1.txt","r",encoding="utf-8") as dosya:
    print(dosya.readline(4))
    print(dosya.readline(),end="")
    print(dosya.readline(),end="")
    print(dosya.readline(),end="")