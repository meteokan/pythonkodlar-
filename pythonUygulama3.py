#  siteden bilgi alma uygulaması
import requests
from bs4 import BeautifulSoup
import pythonMailYollama
import time
url= "https://www.hepsiburada.com/hp-laser-mfp-135w-yazici-baski-fotokopi-tarama-dakikada-20-sayfaya-kadar-siyah-beyaz-4zb83a-pm-HB00000L218G"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}

def fiyat_kontrol():
    sayfa= requests.get(url,headers=headers)
    parcala = BeautifulSoup(sayfa.content,"html.parser")
    baslik=parcala.find(id="product-name").get_text().strip()
    print(baslik)
    etiket=parcala.find(id="offering-price").get_text().strip()
    etiket=etiket[0:5].strip().replace(".","")
    fiyat=float(etiket)
    print(fiyat)
    if fiyat<7000:
        pythonMailYollama.mail_yolla()
        print("fiyat düştü")
    else:
        print("Fiyat aynı")

while(1):
    fiyat_kontrol()
    time.sleep(60*60)

