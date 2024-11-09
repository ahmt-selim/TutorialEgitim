#VERİ TABANI | SQLITE

import sqlite3 #İlk olarak modülümüzü koda dahil edelim.
#Şimdi bir veri tabanına bağlanalım.
baglanti=sqlite3.connect("veritabanı.db") #Eğer bulunduğumuz dizinde veritabanı.db isimli bir dosya yoksa yeni oluşturulacak varsa direkt ona bağlanılacaktır.
imlec=baglanti.cursor() #Şimdi ise veri tabanında işlem yapabilmek için cursor sınıfından bir obje yani bir imleç oluşturalım.

#       ***TABLO OLUŞTURMA***
#Veri tabanımızın içinde veri saklayabileceğimiz bir tablo oluşturmak için imlec objemizin execute metodunu kullanacağız.
imlec.execute("CREATE TABLE IF NOT EXISTS ekip(isim TEXT,yas INT,cinsiyet TEXT)") #Tablo yoksa oluştur ve ekip ismindeki tablonun stunlarını ve cinslerini giriyoruz.

#       ***TABLOYA VERİ YAZMA***
#Oluşturduğumuz tabloya veri eklemek için "INSERT INTO tabloadi VALUES(....,....,....)"komutunu kullanacağız.
"""imlec.execute("INSERT INTO ekip VALUES('Ahmet Selim',25,'Erkek')")
baglanti.commit() #baglantı objemizin commit metodu ile değişliklikleri kaydettik, eğer kaydetmesek eklediğimiz verileri göremezdik
imlec.execute("INSERT INTO ekip VALUES('Gülhan',22,'Kız')")
imlec.execute("INSERT INTO ekip VALUES('Beyza',19,'Kız')")
imlec.execute("INSERT INTO ekip VALUES('Sevgi',46,'Kız')")
imlec.execute("INSERT INTO ekip VALUES('Haydar',49,'Erkek')")
baglanti.commit()
#baglanti.close() #Bu işlemin biz kullanmazken bilgisayarımızdan RAM yememesi için fonksiyonu kapatmamız gerekir.
#Ama bunu kısa yolu da vardır. "with ... as" kullanarak yapmak"""
"""
with sqlite3.connect("veritabani.db") as baglanti
    imlec=baglanti.cursor()  
    imlec.execute("CREATE TABLE IF NOT EXISTS ekip(isim TEXT,yas INT,cinsiyet TEXT)")
    imlec.execute("INSERT INTO ekip VALUES('Gülhan',22,'Kız')")
    imlec.execute("INSERT INTO ekip VALUES('Beyza',19,'Kız')")
    imlec.execute("INSERT INTO ekip VALUES('Sevgi',46,'Kız')")
    imlec.execute("INSERT INTO ekip VALUES('Haydar',49,'Erkek')")
    baglanti.commit()
"""

#           ***TABLODAN VERİ OKUMA***
#Tablomuzdan veri okurken SELECT komutunu kullanacağız.

imlec.execute("SELECT *FROM ekip")
veriler = imlec.fetchall() # fetchall metodu tablodaki tüm verileri okur ve liste döndürür
print(veriler)

for veri in veriler:
    print(veri)

imlec.execute("SELECT yas from ekip") #Sadece yaşları almak için
imlec.execute("SELECT isim,yas from ekip ") #İsim ve Yaşları almak için
imlec.execute("SELECT *from ekip WHERE yas<25") #Yaşı 25 den küçük olan verileri çeker.
imlec.execute("SELECT *from ekip WHERE yas==22") #Yaşı 22 ye eşit olanları çeker.
imlec.execute("SELECT *from ekip WHERE yas==22 AND cinsiyet=='Erkek' ")
baglanti.commit()
baglanti.close()


#           ***TABLODAN VERİ GÜNCELLEME***
with sqlite3.connect("veritabanı.db") as baglanti:
    imlec=baglanti.cursor()
    imlec.execute("UPDATE ekip SET yas=25 WHERE isim='Beyza'") #İsmi Beyza olan satırdaki yas karakterini ddeğiştirir.

    baglanti.commit()

#           ***TABLODAN VERİ SİLME***

imlec.execute("DELETE FROM ekip WHERE isim='Gülhan'") #Gülhan adlı değer ve satırı siler.

