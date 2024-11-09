#-Yıldızlı Parametreler-
print("Galatasaray")
print(*"Galatasaray")
#1 den 1000 e kadar olan sayıların toplamını yapan bir fonksiyon oluşturalım.
def sayilariTopla(*degerler):
    toplam=0
    for deger in degerler:
        toplam+=deger
    return toplam
sayilar=[x for x in range(1,1001)]

print(sayilariTopla(*sayilar))

""" Yani sonuç olarak 'Yıldız Parametrelerin' 2 tane kullanım şekli var.
Bunlardan birincisi Ampek işlemi(Elemanları yada indeksteki bulunan yapıları teker teker parametre olarak almayı sağlıyor. 
İkincisi ise birden fazla argüman alma işlemidir."""
