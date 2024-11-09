#Hayatı kolaylaştıran STR sınıfı fonksiyonları

#upper()-lower(): Orjinal string objesini değiştirmeden upper fonksiyonu bir string objesinin tüm harflerini büyük yaparken lower fonksiyonu tam tersini yapar.
yazi="merHabA BeNim Adım nAmE. nabeR?"
print(yazi.upper())
print(yazi.lower())
print(yazi)

#replace(eski,yeni,adet=0): 'replace' fonksiyonu bir string objesinin içinden istediğimiz bir değeri istediğimiz bir değerle ve istedğimiz adet kadar değiştirir.
a="Antalya Hava Meydan Komutanlığı Asteğmen Ahmet Selim KISA"
print(a)
print(a.replace("Antalya","İzmir"))
print(a.replace("a","e"))

# startswith(değer,başlama,bitiş): startswith fonksiyonu bir stirng objesinin girdiğimiz değerle başlayıp başlamadığını,
# endswith(değer,başlama,bitiş): endswith fonksiyonu ise girdiğimiz değerle bitip bitmediğini kontrol eder.
yazi1="www.mertmekatronik.com sitesinde bir sürü kaliteli makale ve içerik bulabilirsiniz!"
print(yazi1.startswith("www")) #bool değer döndürür
print(yazi1.startswith(("www","http","https"))) #İçine tuple değerde girebiliriz yani içindeki değerlerden herhangi biriyle başlıyorsa da True değeri üretir.
print(yazi1.endswith("!"))
print(yazi1.endswith("."))

#split(): split fonksiyonu string objesini girdiğimiz değerlerden bölerek bir liste haline getirir. Eğer içi boş bırakılırsa "" yani boşluk karakterini baz alarak ayrıştırma yapar.
print(yazi1.split())
print(yazi1.split("ve"))

#strip(): strip fonksiyonu bir string objesinden girdiğimiz değerleri çıkartır.
print(yazi1.strip("w"))

#find(): find fonksiyonu string objemizin içinde girdiğimiz değerin index numarasını verir.
print(yazi1.find("bir"))
print(yazi1.find("t"))
print(yazi1.find("t",8)) #Başlangıç değeri girilebilir.

#count(): count fonksiyonu girdiğimiz değerin string objesinde kaç kez geçtiğini döndürür.
print(yazi1.count("e"))

#join(): join fonksiyonunu bir listenin elemanlarını arasına bu fonksiyonu kullandığımız string objesini koyarak yeni bir string objesi oluşturur.
isimler="Mert,Ahmet,Selim,Ela,Beyza,Osman,Ali,Veli,Ayşe"
print("-".join(isimler.split(",")))

