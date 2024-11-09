#RANGE()

#Range fonksiyonu, istediğimiz aralıktaki ardışık sayıları alabilmemizi sağlar.
"""a=range(1,5) #1'den 5'e kadar 5 dahil değil.
print(a)
print(type(a))
print(*a)

for i in range(101): #Bunun eşdeğeri: while i>=101
    print(i)
for i in range(20,101):
    print(i)
for i in range(50,101,5):
    print(i)"""
#Örnek : Girilen sayiya kadar olan asal sayiları yazdıran program.
girilen_sayi=int(input("Bir sayi giriniz: "))
sayi=2
asal_sayilar=[]
while girilen_sayi>1:
    asal_sayilar.append(girilen_sayi)
    while sayi<girilen_sayi:
        if girilen_sayi%sayi==0:
            asal_sayilar.remove(girilen_sayi)
            break
        sayi+=1
    sayi=2
    girilen_sayi-=1
print(asal_sayilar)
print(len(asal_sayilar))

#Aynı örneğin for ile yapılışı
def asal_mi(g_sayi):
    for i in range(2,g_sayi):
        if g_sayi%i==0:
            return False
    return True
g_sayi=int(input("Bir sayi giriniz: "))
asal_sayilar1=[]
for i in range(2,g_sayi+1):
    if asal_mi(i):
        asal_sayilar1.append(i)
print(asal_sayilar1)
print(len(asal_sayilar1))

