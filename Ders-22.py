#😎 SİZ KODLAYIN

#Örnek 1 - Faktöriyel hesaplama:
sayi=int(input("Bir sayi giriniz: "))
faktoriyel=1
for x in range(1,sayi+1):
    faktoriyel=faktoriyel*x
print("{}!".format(sayi),"= ",faktoriyel)

#Örnek 2 - ATM Simülasyonu
anapara=2000
kart_sahibi="Ahmet Selim KISA"
secim=input("Kartı sokmak için 's', Ayrılmak için 'a' yazın: ")
if secim=="a":
    print("ATM den Ayrıldınız!")
elif secim=="s":
    print("****ATM'ye HOŞGELDİNİZ****")
    while True:
        islem = int(input("\n1. Para çekme\n2. Para Yatırma\n3. Kart Bilgileri\n4. Kart İade\n-------\nYapmak istediğiniz işlemi seçin: "))
        if islem==4:
            print("Kartı iade aldınız. ATM den ayrıldınız!")
            break
        elif islem==1:
            cekilen=int(input("Çekmek istediğiniz tutarı girin: "))
            if cekilen>anapara:
                print("Bakiyeniz yetersizdir!")
            else:
                anapara-=cekilen # Bu ifade aynı zamanda: anapara=anapara-cekilen demektir.
                print("Para verildi.")
        elif islem==2:
            yatirilan=int(input("Yatırmak istediğiniz tutarı girin: "))
            anapara+=yatirilan
            print("Para yatırıldı.")
        elif islem==3:
            print("\nKart Bilgileri:\nKart Sahibi: {}\nHesap Bakiyesi: {}".format(kart_sahibi,anapara))
        else:
            print("Hatalı tuşlama yaptınız!")
else:
    print("Yanlış Tuşlama Yaptınız!")




