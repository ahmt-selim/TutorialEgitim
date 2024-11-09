#Mantıksal Bağçlarlar (and | or )

print(5==5 and "Mert"=="Mert")
print(5%2==3 and "Mert"=="Mert") #5'in 2ye bölümünden kalan
print(7%5==2 or "Ahmet"=="Selim")
print(7%5==5 or "Gülhan"=="Beyza")

#And Örnek
kullanici_bilgileri=["ahmet.selim12","12345m"]
kullanici_adi=input("Kullanıcı Adınızı girin: ")
sifre=input("Şifrenizi girin: ")
a=kullanici_adi==kullanici_bilgileri[0] and sifre==kullanici_bilgileri[1]
print(a)

#Or Örnek
sayiAl=int(input("Bir sayi giriniz: "))
a=sayiAl%2==0 or sayiAl%3==0 or sayiAl%5==0
print(a)


