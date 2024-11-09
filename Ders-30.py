#BASİT ŞİRKET OTOMASYONU - CLASS(OOP) Önemi

class Sirket():
    def __init__(self,ad):
        self.ad=ad
        self.calisma=True
    def program(self):
        secim=self.menuSecim()

        if secim==1:
            self.calisanEkle()
        if secim==2:
            self.calisanCikar()
        if secim==3:
            self.verilecekMaasGoster()
        if secim==4:
            self.maaslariVer()
        if secim==5:
            self.masrafGir()
        if secim==6:
            self.gelirGir()
    def menuSecim(self):
        secim=int(input("****{} Otomasyonuna Hoş Geldiniz**** \n\n1-Çalışan Ekle\n2-Çalışan Çıkar\n3-Verilecek Maaş Göster\n4-Maaşları Ver\n5-Masraf Gir\n6-Gelir Gir\n\nSeçiminizi Girin: ".format(self.ad)))
        while secim<1 or secim>6:
            secim=int(input("Lütfen 1-6 arasında  belirtilenlerden giriniz: "))
        return secim
    def calisanEkle(self):
        pass
    def calisanCikar(self):
        ad=input("Çalışanın adını giriniz: ")
        soyad=input("Çalışanın soyadını giriniz: ")
        yas=input("Çalışanın yaşını giriniz: ")
        cinsiyet=input("Çalışanın cinsiyetini giriniz: ")
        maas=input("Çalışanın maaşını giriniz: ")

        with open("calisanlar.txt","r") as dosya:
            dosya.readlines()
    def verilecekMaasGoster(self,hesap="a"):
        """hesap: a ise aylık, y ise yıllık hesap"""
        pass
    def maaslariVer(self):
        pass
    def masrafGir(self):
        pass
    def gelirGir(self):
        pass

sirket=Sirket("Ahmet Selim")
while sirket.calisma:
    sirket.program()





