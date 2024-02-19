with open("C:/Users/pausem/Desktop/dosyamiz/deneme2.txt","a+", encoding="utf-8") as dosya:
    dosya.write("ok.\n")
    dosya.seek(0)
    text=dosya.read()
    print(text)