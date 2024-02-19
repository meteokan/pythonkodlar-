parola=input("parola : ").strip()
tr_harfler="çöşğüıİ"
for harf in parola:
    if (harf in tr_harfler):
        print("Parolada türkçe karakter olamaz")
if len(parola)<4 or len(parola)>8:
    print("4 küçük 8 den büyük olamaz.")