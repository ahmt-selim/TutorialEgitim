#😎SİZ KODLAYIN!

#Örnek1: Sayının tam bölenlerini bulma.
def tam_bolenler(a):
    liste=[]
    for i in range(1,a+1):
        if a%i==0:
            liste.append(i)
    return print("{} sayisinin tam bölenleri: ".format(a),liste) #liste # Ya da : print("{} sayisinin tam bölenleri: ".format(a),liste)
sayi=int(input("Bir sayi giriniz: "))
tam_bolenler(sayi)

#Örnek2: EKOK (En küçük ortak kat)
def ekok(a,b):
    c=max(a,b)-1
    d=a*b
    katlar=[]
    for i in range(d,c,-1):
        if i%a==0 and i%b==0:
            katlar.append(i)
    e=min(katlar)
    return print("{} ve {} sayilarının EKOK'u: {}".format(a,b,e))
print("\nEkoku alınacak sayilari giriniz:\n")
a=int(input(" "))
b=int(input(" "))
ekok(a,b)

#Örnek3: Asallık bulma:
def asallik(a):
    for i in range(2,a):
        if a%i==0:
            return print("Sayı asal değildir.")
        else:
            return print("Sayi asaldır.")
a=int(input("Bir sayi giriniz: "))
asallik(a)
