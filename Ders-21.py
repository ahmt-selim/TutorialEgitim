#LIST COMPREHENSION (LİSTE ANLAMASI)
#list comprehension, for döngüsü ile iki üç satırda tanımlayabileceğimiz listeleri tek satırda tanımlama imkanı sunar.

sayilar=[]
for i in range(1,100001): # 1 den yüz bine kadar olan sayılardan hem 2 ye hem de 3 e tam bölünenleri yazdırdık.
    if i%2==0 and i%3==0:
        sayilar.append(i)
#print(sayilar)

#LIST COMPREHENSION ile bu işlemi tek satırda yapabiliriz:
sayilar1=[x for x in range(1,100_001) if x%2==0 and x%3==0]
print(sayilar1)

#Örnek
kisiler=["Mert","Murat","Ali","Merve","Ahmet","Zeynep","Mustafa","Kemal","Mahmut","Elif"]
m_ile_baslayan=[kisi for kisi in kisiler if "m" in kisi[0] or "M" in kisi[0]]
print(m_ile_baslayan)

sayilar2=[y for y in range(1,101)] # Burda da 1 den 100 e kadar olan sayıları bir liste olarak sakladık.
print(sayilar2)
s1 = [x for x in range(1 ,11)]
s2 = list(range(1 ,11))
s3 = [range(1 ,11)]
print(s1,"\n",s2,"\n",s3)