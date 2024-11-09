#FONKSİYONLAR VE PARAMETRE(*args,**kwargs,ders="25!")

def topla(*sayilar): #Eğer bir fonksiyona girilecek parametre sayısı belli değilse, parametre adının başına * koyarız.
    toplam=0
    for i in sayilar:
        toplam+=i
    return toplam
print(topla(25,30,40,78,12))

def topla1(*sayilar):
    return sum(sayilar) #'sum' fonksiyonu Python içinde gömülü bir toplama fonksiyonudur.
print(topla1(25,30,40,78,12))

def yazdir(*degerler):
    for i in degerler:
        print(i,end=" ")
yazdir("Ahmer","Selim","Kısa",25,"Gülhan KISA\n")

def kuvvetAl(sayi,kuvvet=2): #Yani fonksiyon kullanılırken 2. parametre girilmezse fonksiyon bunu varsayılan olarak 2 alacaktır.
    return sayi**kuvvet
print(kuvvetAl(3,4))
print(kuvvetAl(3))

def degerleri_goster(**degerler): # ** kulladığımıza da dictionary değerler göstereceğimiz anlamındadır. Yaani yappıları anahtar ve değer şeklinde tutuyor.
    for anahtar,deger in degerler.items():
        print(anahtar,deger)
degerleri_goster(mert="Mekatronik",ahmet="Selim",renk="Yeşil")

liste = [2,45,1,23,8,6,4,9]
liste.sort() #Küçükten büyüğe sıralama
print(liste)
liste.sort(reverse=False) #Küçükten büyüğe sıralama
print(liste)
liste.sort(reverse=True) #Büyükten küçüğe sıralama
print(liste)


