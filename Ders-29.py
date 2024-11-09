#CLASS(SINIF) Yapısı Nedir?

class Araba(): #Araba adında bir sınıf tanılayıp o sınıftan ''Renault'' adında bir nesne türettik. Artık Renault nesnemizin çeşitli özellikleri var. Onları şu şekilde kullanabiliriz.
    marka="Renault"
    model="Clio"
    fiyat=50_000
    renk="Beyaz"

    def bilgileriYazdir(self): #Objenin ismi ne olursa olsun referansa 'self' atansın.
        print(self.marka,self.model,self.fiyat,self.renk)

araba=Araba()
print(araba.marka)
print(araba.fiyat)
otomobil=Araba() #Yani farklı isimle atadığımız sınıfın verilerini self sayesinde kullanabiliyoruz.
araba.bilgileriYazdir()
otomobil.bilgileriYazdir()

print(araba)
print(otomobil) #İkiside bir Araba objesi fakat farklı adreslerde kaytlı.

class Araba1():
    def __init__(self,marka,model,fiyat,renk): #__init__ fonksiyonu sınıftan bir nesne türettiğimizde çalışan fonksiyondur.
        print("Araba objesi oluştu.")
        self.gelenMarka=marka
        self.gelenModel=model
        self.gelenFiyat=fiyat
        self.gelenRenk=renk

    def bilgileri_yazdir(self):
        print(self.gelenMarka,self.gelenModel,self.gelenFiyat,self.gelenRenk)

    def renk_degistir(self,renk):
        self.gelenRenk=renk


araba1=Araba1("Renault","Toros",7_000,"Beyaz")
araba2=Araba1("Ford","Mustang",200_000,"Siyah")
araba1.bilgileri_yazdir()
araba2.bilgileri_yazdir()
araba1.renk_degistir("Yeşil")
araba1.bilgileri_yazdir()

sayilar=[1,2,3,4,5,6]
sayilar.append(20) #Yani sayilar listesinde değişiklik için append fonksiyonunu kullandık. Yukarda ise renk değiştirmek için araba sınıfımızda tanımladığımız rank_degistir fonksiyonunu kullanarak değişiklik yaptık.
print(sayilar)

print(araba1)
class Araba2():
    def __init__(self,marka,model,fiyat,renk): #__init__ fonksiyonu sınıftan bir nesne türettiğimizde çalışan fonksiyondur.
        print("Araba objesi oluştu.")
        self.gelenMarka=marka
        self.gelenModel=model
        self.gelenFiyat=fiyat
        self.gelenRenk=renk

    def __str__(self):
        return self.bilgileri_yazdir()
    def bilgileri_yazdir(self):
        return self.gelenMarka+" "+self.gelenModel+" "+str(self.gelenFiyat)+" "+self.gelenRenk

    def renk_degistir(self,renk):
        self.gelenRenk=renk

araba3=Araba2("Nissan","Almera",21_500,"Mavi")
print(araba3)




