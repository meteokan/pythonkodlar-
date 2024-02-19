import tkinter as tk
from tkinter import filedialog
import pandas as pd
def excel_to_csv():
    excel_yol=filedialog.askopenfilename(filetype=[("Excel Files","*.xlsx;xls")])
    if excel_yol:
        oku=pd.read_excel(excel_yol)

        csv_yol=excel_yol.replace(".xlsx",".csv")
        oku.to_csv(csv_yol, index=False)
arayuz=tk.Tk()
arayuz.title("Excel to Csv")
button_secim=tk.Button(arayuz,text="Excel dosyası seç", command=excel_to_csv)
button_secim.pack()

label_sonuc=tk.Label(arayuz, text="")
label_sonuc.pack()

arayuz.mainloop()




