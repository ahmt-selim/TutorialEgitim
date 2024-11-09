#FONKSİYONLAR

"""Fonksiyonlar belli bir kod bloğunu bir kez yazıp istediğimiz kadar kullanabilmemizi sağlar.

Bu sayede bizi büyük kod tekrarlarından kurtarır. Ayrıca daha okunaklı ve modüler bir kod yazmamızda önemli bir yere sahiptir."""

def yazdir():
    for i in range(1,15):
        print("Ahmet Selim KISA")
yazdir()

def yazdir1(yazi,adet):
    for x in range(1,adet+1):
        print(yazi)
yazi=input("yazi yaziniz: ")
adet=int(input("Kaç adet yazdırılacak: "))
yazdir1(yazi,adet)

# EBOB Örneği:
def ebob(a,b):
    kucuksayi=min(a,b) #'Min' Python içinde gömülü bir fonksiyondur ve içindeki sayıların en küçüğünü döndürür.
    enbuyuk_bolen=1
    for i in range(1,kucuksayi+1):
        if a%i==0 and b%i==0:
            enbuyuk_bolen=i
    print(f"{a} ve {b} sayılarının EBOB'u : {enbuyuk_bolen} sayısıdır.")

ebob(45,30)




