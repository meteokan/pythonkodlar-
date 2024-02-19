import csv
from tabulate import tabulate
with open("kayitlar.csv", newline='', encoding="utf-8") as csvfile:
    csvoku=csv.reader(csvfile,delimiter=",")
    for row in csvoku:
        print(row)
satirlar=[]
with open("kayitlar.csv", newline='', encoding="utf-8") as dosya:
    okuyucu=csv.reader(dosya)
    for satir in okuyucu:
        satirlar.append(satir)
print(tabulate(satirlar))

