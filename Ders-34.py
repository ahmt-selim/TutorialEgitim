#Hata Bulma | Try Except

#Kütle Endeks Programı yapımı:
boy=float(input("Boyunuzu metre cindinden giriniz: "))
kilo=float(input("Kilonuzu kg cinsinden giriniz: "))

print(kilo/boy**2)

#Eğer try blokunun içindeki kodda except anahtar kelimesinden sonra belirttiğimiz hata meydana gelirse program hata vermek yerine except bloğundaki işlemi yapar ve işlemeye devam eder.
while True:
    try: #Hatayı dene demek. Yani eğer girilen değerde hata bulursa 'except' altındaki işlemi yapar. Eğer hata bulmazsa excepte girmeden devam eder.
        boy1=float(input("Boyunuzu metre cindinden giriniz: "))
        break
    except ValueError: #Sadece değer hatalarnı yakalamak istiyorsak veya başka bir gömülü hatayı yakalamak istiyorsak buraya yazarız.
        print("Lütfen Değeri doğru giriniz! ")

while True:
    try:
        kilo1=float(input("Kilonuzu kg cinsinden giriniz: "))
        break
    except: #Eğer her türlü hatayı yakalamak istiyorsak boş bırakırız.
        print("Lütfen değeri doğru giriniz!")

print(kilo1/boy1**2)


