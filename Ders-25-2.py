#LAMBDA FONKSİYONLAR VE GLOBAL

#Global değişkenler, koddaki her yerden ulaşabileceğimiz değişkenlerdir.
a=10
def carp(b,c):
    print(a) # a değişkeni bir global değişken olduğu için fonksiyonun içinden ulaşabildik.
    return a*b*c
print(carp(4,5))

def bol(a,b):
    print(a/b)
    c=10
bol(12,3)
#print(c) Burada bu hatayı almamızı sebebi c değişkeninin lokal(yerel) değişken olması.

c=10
def carp1(a,b):
    global c #c nin başına global anahtar kelimesini eklediğimizde programa yukarıda tanımladığımız c değişkenini kullanacağımızı söyledik. Böylece yaptığımız değişiklikler fonksiyonun dışında da geçerli oldu.
    c = 5
    print("fonksiyonun içinde c : ",c)
    print(a*b)
carp1(2,9)
print("fonksiyonun dışında c : ",c)

#'lambda' ifadesi küçük fonksiyonları tek satırda tanımlamamızı sağlar. Yani tek satırlık fonksiyonları tanımlamamızı sağlar.
tek_mi=lambda sayi: sayi%2==1 #Yani bu fonksiyon sayının 2 ye bölümünden kalan 1 ise True değerini değilse False değerini döndürecek.
print(tek_mi(21))

carp2=lambda a,b: a*b
print(carp2(20,4))

toplam=lambda *sayilar: sum(sayilar)
print(toplam(45,86,74,12,33))

