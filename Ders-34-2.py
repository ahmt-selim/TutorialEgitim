#Hata Bulma 2

def sayilariTopla(sayilar):
    if type(sayilar) != list:
        raise TypeError ("Parametre liste objesi olmalı!") #'raise' komutu ile kendi hata tiplerimizi açıklamalarıyla birlikte türetebiliyoruz.

    toplam=0
    for i in sayilar:
        toplam+=i
    return toplam

print(sayilariTopla((1,2,3,4,5,6)))

