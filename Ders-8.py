#Liste Veri Tipleri
a=list()
b=[]
print(type(b))
sınıf=["Ahmet","Selim","Rukiye","Gülhan","Beyza","Fatih","Ali","Sevgi","Haydar"]
print(sınıf)
print(len(sınıf))
print(sınıf[2])
sınıf.remove("Selim") #Listeden veri silme
print(sınıf)
print(len(sınıf)) #Listedeki veri sayısını yazdırma
basariliogrenciler=sınıf[0:3]#0'dan 3'e kadar yazdırma
print(basariliogrenciler)
print(type(basariliogrenciler))
#ya da
basariliogrenciler1=sınıf[:3] #0'dan 3'e kadar yazdırma
print(basariliogrenciler1)
print(sınıf[1:6]) #1'den 6'ya kadar yazdırma
print(sınıf[::2]) #İkişer atlayarak yazdırma
print(sınıf[::-1]) #Verileri tersten yazdırma
print(sınıf)
print(sınıf[5:1:-1]) # 5. indeksten 1'e kadar tersten yazdırma
sınıf[5]="Tolga" #Yani Liste içerisindeki elemanlar Değiştirilebilir, Silinebilir ve Eklenebilir
print(sınıf)

isim="Ahmet Selim"
isim1=list(isim) #String İfadeyi List İfadesine Çevirmek:
print(isim1)
isim1[5]="_"
print(isim1)
print("".join(isim1)) #List e dönüştürdüğümüz ifadeyi tekrar String'e dönüştürdük (AYRINTI)

sınıf1=["Anıl","Muhiddin","İsa","Meryem"]
sınıf=sınıf+sınıf1 #Listeleri Toplamak:
print(sınıf)
liste1=[1,2,3]
print(liste1*3) #Listeleri Çarpmak:
liste1.append("Mert") #Listeye Obje Eklemek:
print(liste1)
cikarilan=liste1.pop() #Listeden Obje Çıkarmak:.pop() Boş bırakırsak sondan 1 tane çıkaracaktır.
# Parantez içine indeks numarası girilerek o indeks de çıkartılablir.
print(liste1)
print(cikarilan)

sayilar=[44,56,12,78,666,23,0,99,4]
print(sayilar)
sayilar.sort() #Listeyi Küçükten Büyüğe Sıralamak:
print(sayilar)
sayilar.sort(reverse=True)
print(sayilar) #Listeyi Büyükten Küçüğe Sıralamak:

isimler=["Mert","Beyza","Gülhan","Zeynep","Hakan","Alparslan","Kemal","Osman"]
print(isimler)
isimler.sort()#Listeyi Alfabetik sıralama
print(isimler)
isimler.sort(reverse=True) #Listeyi ters alfabeden sıralama
print(isimler)

kullanıcılar=["ahmet_selim","byz.ksa","gulhan-ksa99"]
sifreler=["123456","654321","123123"]
users=[kullanıcılar,sifreler] #Liste İçinde Liste Tanımlamak:
print(users[0][0],users[1][0])



