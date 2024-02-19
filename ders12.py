
d1=open("isimler1.txt") #dosyayı açtım
d1_satirlar=d1.readlines() #satırları okudum

d2=open("isimler2.txt")
d2_satirlar=d2.readlines()

for x in d1_satirlar:
    if not x in d2_satirlar:
        print(x)

d1.close()
d2.close()
