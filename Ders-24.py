#FONKSİYONLAR VE RETURN

def goster():
    print("Mert Mekatronik")
print(goster())
print(type(goster()))

def goster1():
    return "Mert Mekatronik"

print(goster1())
print(type(goster1()))

#Fonksiyonlar 'return' anahtar kelimesini gördükten sonra returnun karşısındaki değeri döndürür ve işlemi durdurur.

def tek_mi(sayi):
    if sayi%2==0:
        return False
    else:
        return True
def cift_mi(sayi):
    if sayi%2==0:
        return True
    else:
        return False
a=int(input("Bir sayi giriniz: "))
print(tek_mi(a))
print(cift_mi(a))

#Örnek: Sayi tek ise ekrana yazdır çift ise o sayiya kadar olan sayiları topla ve yazdir.
def tekmi_ciftmi(sayi):
    if sayi%2==1:
        return sayi
    toplam=0
    for i in range(1,sayi+1):
        toplam=toplam+i
    return toplam
b=int(input("Bir sayi giriniz: "))
print(tekmi_ciftmi(b))



