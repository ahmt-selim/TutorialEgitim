#😎SİZ KODLAYIN!

import random
oyun_durumu=True
while oyun_durumu:
    print("***Sayi tahmin oyununa hoşgeldiniz***\n1-100 arası bir sayıyı bulmak için en fazla 7 deneme hakkınız var.")
    sayi = random.randint(1, 100)
    deneme = 7
    while True:
        if deneme>0:
            tahmin = int(input("{}. Deneme: ".format(8-deneme)))
        else:
            print("Sayıyı tahmin edemediniz. Sayı: {}".format(sayi))
            break
        if tahmin!=sayi:
            deneme-=1
            if tahmin<sayi:
                print("Yukarı")
            else:
                print("Aşağı")
        else:
            print("Tebrikler Sayıyı Bildiniz. Sayı: {}".format(tahmin))
            break

    devam=input("Oyuna devam etmek istiyor musunu? \nEvet ise 'E' Hayır ise 'H' ye basın: ")
    if devam=="e":
        oyun_durumu=True

    else:
        oyun_durumu=False



