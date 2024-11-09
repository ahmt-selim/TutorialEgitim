#WHILE döngüsü

#While döngüsü, verdiğimiz koşul doğru olduğu sürece içindeki kod bloğunu çalıştırır.
a=10
while(a>=0):
    print(a)
    print("Burası döngünün içi")
    a-=2
print("Burası döngünün dışı")

liste=[1,2,"Ahmet","Selim",9,5,True] #Örnek
liste_uzunluk=len(liste)
sayac=0
while sayac<liste_uzunluk:
    print(liste[sayac])
    sayac+=1

#Örnek Yazı-Tura
import random
yazi_gelen=0
tura_gelen=0
para_yuzeyi=["Yazi","Tura"]
atilacak_para=int(input("Parayı kaç kere atmak istiyorsunuz: "))
while atilacak_para>0:
    gelen_yuzey=random.choice(para_yuzeyi) #.cohice : içine girilen list objesi elemanlarından rastgele seçim yapar.
    if gelen_yuzey=="Tura":
        tura_gelen+=1
        print("Tura")
    else:
        print("Yazi")
        yazi_gelen+=1
    atilacak_para-=1
print("Gelen Tura sayisi: {}\nGelen Yazi sayisi: {}".format(tura_gelen,yazi_gelen))


