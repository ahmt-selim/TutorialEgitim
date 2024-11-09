#Dictionary Veri Tipleri
sozluk=dict()
print(type(sozluk))

yaslar={"Ahmet":25,"Gülhan":22,"Beyza":19,"Haydar":48,"Sevgi":46} #suzluk={anahtar objesi : değer objesi}
print(yaslar["Sevgi"])

klub={"uyeler":["Ali","Osman","Hayriye"],
      "moderator":["Veli","Ayşe","Kadir"],
      "yonetici":["Tahsin","Arda","Mecnun"]}
print(klub)
print(klub["uyeler"])
klub["kurucular"]=["Hakan","Erdal"] #Kütüphaneye yeni bir anahtar ve değer ikilisi ekleme
print(klub)
klub["uyeler"].append("Yavuz") #Değer objesine veri ekleme
print(klub["uyeler"])
klub["yonetici"].pop(1) # Drğer objesinden veri silme
print(klub["yonetici"])
klub1=klub.copy() #Kopyalamak
print(klub1)
klub1.pop("moderator") #Kütüphaneden bir sözlük objesi siliyoruz
print(klub1)
tum_kullanicilar=klub.values() #Sadece değer objelerini seçiyoruz
print(tum_kullanicilar)
siniflar=klub.keys() #Sadece anahtar objelerini seçiyoruz
print(siniflar)
tum_kullanicilar1=klub.items() #Dictionary objesini bir list objesi şeklinde getiriyor(Tuple'ler ile karışık olarak.)
print(tum_kullanicilar1)
for i,j in tum_kullanicilar1:
      print(i,j)

"""Sözlüklerin Kullanımı:
Yöntemler 	Açıklamları
clear() 	Sözlükteki tüm öğeleri kaldırır.
copy() 	    Sözlüğün bir kopyasını döndürür.
fromkeys() 	Belirtilen tuşları ve değeri içeren bir sözlük döndürür.
get() 	    Belirtilen anahtarın değerini döndürür.
items() 	Her bir anahtar değer çifti için bir demet içeren bir liste döndürür.
keys() 	    Sözlüğün anahtarlarını içeren bir liste döndürür.
pop() 	    Belirtilen tuşla öğeyi kaldırır.
popitem() 	Son eklenen anahtar-değer çiftini kaldırır
setdefault() Belirtilen anahtarın değerini döndürür. Anahtar yoksa: anahtarı belirtilen değerle yerleştirin.
update() 	Sözlüğü belirtilen anahtar-değer çiftleriyle günceller.
values() 	Sözlükteki tüm değerlerin bir listesini döndürür."""


