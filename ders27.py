from openpyxl import load_workbook
dosya="dosya_adi.xlsx"
wb=load_workbook(dosya)
yeni_sayfa=wb.active

deger_A1=yeni_sayfa["A1"].value
print(f"A1 hücresinin değeri :{deger_A1}")
for row in yeni_sayfa["E1":"g4"]:
    for cell in row:
        print(cell.value, end="\t")
    print()

for cell in yeni_sayfa["H"]:
    print(cell.value)


