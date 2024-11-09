#if&else blokları

"""sayi=int(input("Bir sayi gir: "))
if sayi%2==0:
    print("Bu sayi Çifttir.")
else:
    print("Bu sayi tektir.")"""

"""elif (else-if) : elif bloğu if bloğu için else’den önce gelen bir yoldur. 
Eğer if’teki koşul tutmazsa program elif’e bakar, elif’teki koşulda tutmazsa else’e geçer"""

#SİZ KODLAYIN! - if&elif&else
print("****YIL SONU HARF NOTU HESAPLAMA****","\n")
ad=input("Öğrencinin Adı: ")
soyad=input("Öğrencinin Soyadı: ")
no=input("Öğrenci Numarası: ")

print("--Notlar--","\n")
vize=int(input("Vize Notunu Giriniz: "))
final=int(input("Final Notunu Giriniz: "))
ort=float((vize*0.4)+(final*0.6))
print(ad,soyad,"'ın Yıl sonu ortalaması: {} ".format(ort))
if 85<=ort<=100:
    print("Harf Notu: AA")
elif 70<=ort<80:
    print("Harf Notu: BA")
elif 60<=ort<70:
    print("Harf Notu: BB")
elif 50<=ort<60:
    print("Harf Notu: CB")
elif 40<=ort<50:
    print("Harf Notu: CC")
elif 0<=ort<40:
    print("Harf Notu: FF")
else:
    print("Hatalı Not Girdiniz!!")

#Bunu bir dosyaya kaydetme(ayrıntı)

with open("Notlar.txt","w") as dosya:
    dosya.writelines("asdasdasdasd")