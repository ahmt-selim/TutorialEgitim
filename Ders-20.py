#BREAK & CONTINUE
#break ifadesi içinde bulunduğu döngüyü kırar. Yani bitirir.

""""while True: #while döngüsüne True koşulunu vererek bir sonsuz döngü oluşturduk.
    sayi=int(input("Bir sayi giriniz(Eğer sayi tek ise döngü sonlanacak): "))
    if sayi%2==1:
        break
    print("Sayı Tek. Döngünün sonu!")
print("Sayı Çift. Döngü bloğunun sonu!!")"""

#continue ifadesinin break'den farkı sadece o tur için döngüyü kırmasıdır.

while True:
    sayi1=int(input("Bir sayi giriniz(Sayi tekse ekranda yazmayacak): " ))
    if sayi1%2==1:
        continue #eğer if döngüsü True üretirse işlem While döngüsünün başına geldi yani döngüyü başa aldı.
    print(sayi1)


