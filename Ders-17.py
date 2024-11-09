#FOR döngüsü

a="m" in "Mert Mekatronik" #İn yapısı bir değerin, bir değer içinde bulunma durumunu kontrol eder.
b="s" in "Mert Mekatronik"
c=2 in (9,8,7,5,2,3,1)
d=3 in [55,770,600,5]
print(a,b,c,d)

sayilar=[1,2,3,4,5,6]
for x in sayilar:
    print(x)
for x in sayilar:
    print(x**2)
liste1=[(1,8),(2,7),(5,9),(4,8)]
for x in liste1:
    print(x[0],x[1])
for x,y in liste1:
    print(x,y)
playlist={"Saian":"Göğe bakmak için",
          "Ceza":"Panorama harem",
          "Sago":"Pavlovun köpeği",
          "MFÖ":"Yandım",
          "Eypio":"16:34"}
for sarkici in playlist.keys(): #Kütüphanedeki sadece anahtar objelerini yazdırma
    print(sarkici)
for sarki in playlist.values(): #Kütüphanedeki sadece değer objelerini yazdırma
    print(sarki)
for sanatci,sarki in playlist.items(): #Kütüphanedeki anahtar ve değer objelerini yazdırma
    print(sanatci,"-",sarki)


