#KALITIM
"""Kalıtım konusu en kısa deyimi ile bir sınıfın özelliklerini başka bir sınıfta kullanabilmemizi sağlar.
Böylece büyük bir kod tekrarından kurtulmuş oluruz."""

class Personel():
    def __init__(self,ad,soyad,yas,cinsiyet,maas):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.cinsiyet=cinsiyet
        self.maas=maas

    def bilgileriYazdir(self):
        print("""
        {} {} Bilgileri Şunlardır:
        Yaş: {}
        Cinsiyet: {}
        Maaş: {}""".format(self.ad,self.soyad,self.yas,self.cinsiyet,self.maas))

    def __str__(self):
        return """
        {} {} Bilgileri Şunlardır:
        Yaş: {}
        Cinsiyet: {}
        Maaş: {}""".format(self.ad,self.soyad,self.yas,self.cinsiyet,self.maas)

personel=Personel("Ahmet Selim","Kısa","25","Erkek",5000)
personel.bilgileriYazdir()
print(personel) #Burda print fonksiyonuna 'perspnel' adlı objeyi gönderdik ve 'srt' adlı fonksiyonun üzerine ezerek bu yapıyı oluşturmuş olduk.

"""Her yönetici de aslında bir çalışan olduğundan çalışanlarla aynı özelliklere sahiptir. 
Bu yüzden Yönetici isimli bir sınıf tanımlarken aynı özellikleri tekrar tanımlamak yerine Çalışan sınıfından miras alabiliriz."""
class Yonetici(Personel): #Burda kalıtımı kullandık.
    pass

yonetici=Yonetici("Gülhan","Kısa","22","Kız",7700)
print(yonetici)
"""Yönetici sınıfının içinde hiçbir işlem yapmasak bile Çalışan sınıfında tanımladığımız her şey burada da geçerli oldu.
Yönetici sınıfında Çalışan sınıfından aldığımız fonksiyonlar haricinde başka fonksiyonlarda tanımlayabiliriz."""

class Yonetici1(Personel):
    def __init__(self,ad,soyad,yas,cinsiyet,maas):
        super().__init__(ad,soyad, yas, cinsiyet, maas)
        print("Yönetici Sınıfının init fonksiyonu.")
"""super().__init__(ad,soyad, yas, cinsiyet, maas) satırı ile yaptığımız olay aslında Yönetici sınıfını init fonksiyonunun ad,soyad,yaş,cinsiyet ve maaş parametrelerinden aldığımız değeri Çalışan sınıfın init fonksiyonuna parametre olarak göndermek. 
Bu şekilde hem Yönetici init fonksiyonunda başka işlemler yaparken hem de miras aldığımız init fonksiyonundaki işlemleri yaptık.

Bunu sadece init'te değil override ettiğimiz tüm fonksiyonlarda yapabiliriz."""

def bilgileriYazdir(self):
        print(f"*********\nİsim: {self.ad} \nSoyisim: {self.soyad}\nYaş: {self.yas}\nCinsiyet: {self.cinsiyet}\nMaaş: {self.maas}\n********")

Beyza=Yonetici1("Beyza","Kısa","19","Kız",6500)
Beyza.bilgileriYazdir()
"""Yönetici sınıfından bilgileri_göster fonksiyonunu çağırdığımızda Çalışan sınıfındakinden farklı bir sonuç aldık. 
Çünkü o fonksiyonu Yönetici sınıfında tekrar tanımlayarak değiştirdik.

Bu işlem nesne tabanlı programlamada override olarak adlandırılır. 
Şimdide init fonksiyonunu override etmeyi deneyelim."""

#Kalıtım konusunu İyice anlamak için bir örnek daha yapalım.

class Insan():
    def __init__(self, isim, kilo, boy, yas):
        self.isim = isim
        self.kilo = kilo
        self.boy = boy
        self.yas = yas

    def bilgileri_goster(self):
        print(f"isim: {self.isim} _ kilo: {self.kilo} _ boy: {self.boy} _ yaş: {self.yas}")
# İnsan isimli bir sınıf oluşturduk, şimdi bu sınıftan miras alan çaşitli sınıflar oluşturalım.
class Ogretmen(Insan):

    def __init__(self, isim, kilo, boy, yas, brans, ders_sayisi):
        super().__init__(isim, kilo, boy, yas)

        self.brans = brans
        self.ders_sayisi = ders_sayisi

    def bilgileri_goster(self):

        super().bilgileri_goster()
        print(f"branş: {self.brans} _ ders sayısı: {self.ders_sayisi}\n")

class Doktor(Insan):

    def __init__(self, isim, kilo, boy, yas, brans, vaka_sayisi):
        super().__init__(isim, kilo, boy, yas)

        self.brans = brans
        self.vaka_sayisi = vaka_sayisi

    def bilgileri_goster(self):

        super().bilgileri_goster()
        print(f"branş: {self.brans} _ vaka sayısı: {self.vaka_sayisi}\n")

class Bilgisayar_Muhendisi(Insan):

    def __init__(self, isim, kilo, boy, yas, brans, proje_sayisi):
        super().__init__(isim, kilo, boy, yas)

        self.brans = brans
        self.proje_sayisi = proje_sayisi

    def bilgileri_goster(self):

        super().bilgileri_goster()
        print(f"branş: {self.brans} _ proje sayısı: {self.proje_sayisi}\n")

class Asker(Insan):

    def __init__(self, isim, kilo, boy, yas, rutbe, catisma_sayisi):
        super().__init__(isim, kilo, boy, yas)

        self.rutbe = rutbe
        self.catisma_sayisi = catisma_sayisi

    def bilgileri_goster(self):

        super().bilgileri_goster()
        print(f"rütbe: {self.rutbe} _ catisma sayısı: {self.catisma_sayisi}\n ")

Nalan=Ogretmen("Nalan Korkmaz",69,117,35,"Matematik",15)
Nalan.bilgileri_goster()
Yakup=Doktor("Yakup",75,175,42,"Genel Cerrahi",102)
Yakup.bilgileri_goster()
Fidan=Bilgisayar_Muhendisi("Fidan",64,170,28,"Yapay Zeka",102)
Fidan.bilgileri_goster()
Mustafa=Asker("Mustafa",80,179,67,"Albay",89)
Mustafa.bilgileri_goster()



