#zip, enumerate, filter, all, any, len - (YGFS)

#zip(iter*) : zip fonksiyonu iki diziyi eşleştirmemizi kolaylaştırır.
ogrenciler=["Mert","Ela","Ahmet","Mehmet","Ali","Ayşe","Osman"]
notlari=[80,95,50,65,70,75,100]
yaslari=[18,15,14,12,17,18,17]

print(list(zip(ogrenciler,notlari,yaslari))) #list objesi veya tuple şeklinde saklanabilir.
print(tuple(zip(ogrenciler,notlari,yaslari)))

#enumerate(iter*,sayi=0) : Bu fonksiyon girdiğimiz parametrenin elemanlarını numaralandırır.
print(list(enumerate(ogrenciler))) #Varsayılan olarak sıfırdan başlar.
print(list(enumerate(ogrenciler,10)))

#Enumerate kullanmadan da şu şekilde yapılabilir:
def enum(x,sayac=0):
    list1=[]
    sayac=sayac
    for i in x:
        list1.append((sayac,i))
        sayac+=1
    return list1
print(enum(ogrenciler,2))

#filter(fonk,iter) : filter fonksiyonu bir dizi içinden belirlediğimiz koşulu tutan elemanların süzebilmemize yarar.
import re # Regular expresions kütüphanesini ekledik.
#Bu kütüphane sayesinde gönderdiğimiz string objenin yapısını kontrol etmiş oluyoruz.
def dogrula(yazi):
    return re.search("^[A-Z].*",yazi) #Yani yazi objesindeki string ifadelerin baş harfinin büyüklüğünü kontrol ediyor.

isimler=["Mert45","46Ali","***İsmail***","---Merve","Ela","tolga","1215"]
print(list(filter(dogrula,isimler)))

#all(iter) : Eğer iterable elemanlarının hepsi True ise all() fonksiyonu True değerini dndürür.
#any(iter) : Eğer iterable elemanlarının hepsi False ise any() fonksiyonu True değerini döndürür.

#!!! Hatırlatma: '0' değeri ""(tırnaklar içinde bir şey olmayan bir string objesi) veya None değeri haricinde Python'da tüm objeler True değerine tekabul eder.
a=[0,"Ahmet","Selim",True,"Ceylan"]
b=[[10,20],"Ali","Kısa",True,"Buse",]
c=[0,"",None,0]
print(all(a))
print(any(b))
print(any(c))

#len(iter): İterable objenin sahip olduğu toplam eleman sayısını döndüren fonksiyondur.
d=[2,55,68,12,-89,23,1,5,9,0,3,4,0,-89,-789,32,65,998,45,13,2,6,4,9,5,584,78]
e=tuple(d)
f="Ahmet Selim KISA (Mengüalp)"

print(len(d),len(e),len(f),"=> Keşke ben de bu kadar şanşlı olabilsem :)")
