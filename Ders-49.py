#GENERATOR

"""Generatörler büyük ve fazla yer kaplayacak verilerde tüm veriyi bir anda çekmek yerine
o veriyi teker teker almakla eşdeğer bir olaydır.
Generatör objesi fonksiyonlarda 'return' anahtar kelimesi yerine
'' anahtar kelimesi kullanıldığında bu fonksiyın bir 'Generatör' objesi olur otomatikman"""

def sayiArttir():
    a=1
    return a
print(sayiArttir())

def sayiArttir1():
    a=1
    yield a
    a+=1
    yield a
    a+=1
    yield a

for i in sayiArttir1(): #Bu bir Generatör obje olduğu için for döngüsüyle bu generatör objesindeki next adlı fonksiyon tetikleniyor ve her seferindeki a yı yazdırıyor.
    print(i)

sayiArttir1()
print("********")
f=sayiArttir1()
print(next(f))
print(next(f))
print(next(f))
#print(next(f)) # fonksiyonda 4. bir değer olamdığı için hata veriyor.

def sayiArttir2(max):
    for i in range(max):
        yield i
f2=sayiArttir2(1000)
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))






