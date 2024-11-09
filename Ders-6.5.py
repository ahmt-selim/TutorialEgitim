dosya=open("metinbelgesi.txt","w")
print("Merhabalar-",file=dosya)
dosya.close() # close() dosya değişkenini kapatmamızı sağlar.
dosya = open("deneme.txt", "w") # deneme.txt adlı dosya yoksa oluşturup, var ise açıp yazı yazarız.
print("-Merhabalar.", file = dosya, flush = True) # print ile dosya adlı değişkenin deneme.txt adlı dosyada "-Merhabalar" yazarız.