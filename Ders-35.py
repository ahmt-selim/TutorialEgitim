#Dosya İşlemleri (Okuma)

#Şuan Ders-35.py ve planlar.txt dosyalarımız aynı klasörde bulunduğu için direkt dosya adını yazdık, eğer klasörde olmasalardı dosya yolunu belirtmemiz gerekirdi.
dosya=open("planlar.txt","r",encoding="utf-8") #'r' ile okuma işlemi yapaağımızı belirttik. encoding="utf-8": Dosyadaki türkçe harflerin düzgün görünmesini sağlıyor.
#print(type(dosya.read()))
#print(dosya.read(30)) #Eğer içerisine bir parametre girersek(Bu parametre int olmak zorunda) dosyayı o kadar okur.
# Aynı zamanda dosyada her alt satıra geçtiğinde satır sonunda gizli bir '\n' vardır.
#print(dosya.readline(60)) # readline  fonksiyonu her çağrıldığında dosyanın tek bir satırını okur.
#print(dosya.readlines()) #Tüm satırları okuyarak bir liste objesine atıyor ve her satır bir eleman oluyor.
#print(dosya.readlines()[0]) #Listenin sıfırıncı indeksi yani dosyanın birinci satırını yazdırdı.
#print(dosya.tell()) #İmlecin kaçta olduğunu gösterir. Yani '\n' leri de dahil ederek ne kadar okuma yapıldığını.
dosya.seek(5) #Dosya imlecinin yerini  belirlemeyi sağlar. Yani imlecin yerini değiştirip tekrardan okuma işlemi yapar.
print(dosya.read(19))
dosya.write("asdasda") #Bu fonk çalışmaz çünkü biz en başta okuma işlemi için açtık dosyayı.

dosya.close() # Eğer dosyayı kapatmazsak PyCharmı her açtığımızda çalışır ve RAM de yer kaplar.



