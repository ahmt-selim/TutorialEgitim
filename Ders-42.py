#SET(Küme) Sınıfı

#Python'da kümeler de tıpkı listeler, demetler vb. gibi bir veri tipidir.
#Kümelerde, liste ve demetlerden farklı olarak, bir değer en fazla bir kez olabilir.
#Bir küme oluşturmanın iki yolu vardır,

kume={"Ahmet","Selim","Kısa","Ahmet","Kısa","Mert","Mekatronik",40,25,50} # 1. Yolu
print(type(kume))
print(kume) #Tekrar eden elemanlar bir defa gösterilir.

liste = ["Mert", "Mekatronik", "Mert"]
kume1 = set(liste) # 2.yol
print(kume1)
print(len(kume1))

yazi="Mert Mekatronik Udemy Dersleri"
print(set(yazi))
print(dir(yazi)) #Kümelerle kullanılan fonsiyonları sıraladık. Bunlardan en sık kullanılanları şunlar:

kume.add(10) #Kümeye eleman ekleme.
print(kume) #Kümeler sıralı yapılar değildir.
kume.discard("Mekatronik")#Kümeden eleman silme.
print(kume)

A={1,2,3,4,5,6}
B={4,5,6,7,8,9}
C={7,8,9,10,11,12}
print(A.difference(B)) # A'da olup B'de olmayan elemanları döndürür.
print(B.difference(A)) #Bu işlemlerden sonra küme elemanlarında bir değişiklik ollmaz
A.difference_update(B) #A da olan B de olmayan elemanları güncelleyip A ya atıyor.
print(A) #Artık A kümesinin elemanları değişti.
print(B)
print(B.intersection(C)) #A ve B deki ortak elemanları gösteren fonksiyon.(Kesişim kümesi)
print(A.isdisjoint(B)) #Eğer A ile B kümesinin ortak elemanı varsa 'False' değerini döndüren fonksiyon.
print(B.isdisjoint(C))
D={4,5,6}
print(D.issubset(B)) #D kümesinin B kümesinin bir alt kümesi olup olmadığını denetleyen fonksiyondur. Alt kümesiyse 'True' değer döndürür.
print(A.issubset(C))

print(A.union(B)) #A ve B kümelerinin birleşimi olan kümeyi gösterir.

