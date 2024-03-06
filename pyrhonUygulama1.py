# soru sorma uygulaması(oop)
class sorular:
    def __init__(self, soru,secenekler,cevap):
        self.soru=soru
        self.secenekler=secenekler
        self.cevap =cevap
    def cevap_kontrol(self,cevap):
        return self.cevap== cevap
class denetim:
    def __init__(self,denetim_sorulari):
        self.denetim_sorulari=denetim_sorulari
        self.skor=0
        self.soru_index=0
    def soruvar(self):
        return self.denetim_sorulari[self.soru_index]
    def sorulariYazdir(self):
        sorusu=self.soruvar()
        print(f"Soru {self.soru_index+1}: {sorusu.soru}")
        for q in sorusu.secenekler:
            print("-"+q)
        kul_cevap=input("cevap:  ")
        self.tahmin(kul_cevap)
        self.soru_yuklemesi()
    def tahmin(self,kul_cevap):
        soru= self.soruvar()

        if soru.cevap_kontrol(kul_cevap):
            self.skor +=1
        self.soru_index +=1

    def soru_yuklemesi(self):
        if len(self.denetim_sorulari)== self.soru_index:
            self.skoru_goster()
        else:
            self.ilerleme()
            self.sorulariYazdir()
    def skoru_goster(self):
        print("Toplam doğru cevap=", self.skor)

    def ilerleme(self):
        toplamSoru=len(self.denetim_sorulari)
        soruNumarasi= self.soru_index+1
        if soruNumarasi>toplamSoru:
            print("Denetim Bitii")
        else:
            print(f"Soru {soruNumarasi} toplam soru {toplamSoru}")

s1=sorular("Kask taktınız mı?",["Evet","Hayır"],"Evet")
s2=sorular("Eldiven taktınız mı?",["Evet","Hayır"],"Evet")
s3=sorular("Koruma gözlüğü taktınız mı?",["Evet","Hayır"],"Evet")

denetim_sorulari=[s1,s2,s3]

denetle=denetim(denetim_sorulari)
denetle.soru_yuklemesi()
