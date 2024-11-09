#MODÜLLER

"""Fikir: kodu en aza indirmektir.
Modüller oluşturursak, bu kodu sadece bir program için kullanabileceğimiz anlamına gelmez,
bu modülleri diğer programlar için de çağırabiliriz."""

#Modül Oluşturmak: hesapmakinesi. py adında bir dosya oluşturalım ve içine dört fonksiyon tanımlayalım.

import hesap_makinesi #Kullanacağımız modülleri projemize import anahtar kelimesi ile dahil ederiz.
print(hesap_makinesi.topla(10,6))
print(hesap_makinesi.carp(10,6))
print(hesap_makinesi.bol(10,6)) #Modülümüzden fonksiyonları ister bu şekilde tek tek çağıra bilir veya  hepsini ve bazılarını çağırabiliriz.

#from anahtar kelimesi ile modülün içinden sadece istediğimiz fonksiyonu alabiliriz ya da 'import*' yaparak içindeki tüm fonksiyonlara ulaşabiliriz..
from hesap_makinesi import topla,cikar #Bu şekilde ise Modülden sadece belirli fonksiyonları çağırdık ve kullandık.
print(cikar(80,60))
print(topla(80,60))

from hesap_makinesi import* #Modülü bu şekilde çağırdığımızda içindeki bütün fonksiyonları kullanabiliriz.
print(carp(100,20))
print(cikar(100,20))
print(bol(100,20))

import hesap_makinesi as hm # 'as' anahtar kelimesi ile çağıracağımız modülü ve fonksiyonu programa farklı bir isimle dahil edebiliriz.
print(hm.carp(12,3))

#Örnek Python Matematik Modülü ve fonksiyonları

import math #Python'ı geliştirenlerin bize sağladığı matematik modülünü projemize dahil etmiş olduk. Şimdi bununla neler yapabileceğimize bakalım.

for i in dir(math): #dir fonksiyonu içine koyduğumuz modülün tüm özelliklerini bir liste olarak döndürdü, for döngüsüyle sırayla ekrana yazdırdık.
    print(i)

print(math.ceil(2.8))
print(math.ceil(2.3)) # ceil fonksiyonu girdiğimiz ondalıklı sayıyı bir üstündeki tam sayıya yuvarladı.

print(math.fabs(-12))
print(math.fabs(12)) # fabs fonksiyonu giridğimiz sayının mutlak değerini verdi.

print(math.pow(2,3))
print(math.pow(4,2)) # pow fonksiyonu birinci parametrenin ikinci parametrenci kuvvetini verdi.

print(math.sqrt(64))
print(math.sqrt(12)) # sqrt fonksiyonu girdiğimiz sayının karekökünü verdi.

import math
#print(help(math.sqrt(4))) # help fonksiyonu içine girdiğimiz fonksiyonun ya da modülün kısa bir açıklaması verir.

#print(help(math)) # help(math) ile math modülündeki tüm fonksiyonların açıklamasını, help('modules') ile python'daki tüm modülleri görebilirsiniz.
print(help('modules'))