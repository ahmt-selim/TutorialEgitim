#Planlama Programı, Dosya İşlemleri 2 (Yazma)

dosya=open("planlar.txt","w",encoding="utf-8")
"""#Bu işlem ile programa dosya yazma işlemi yapacağımızı söylemiş olduk.
#Bu işlem ile eğer böyle bir dosya yoksa oluşturacak, varsa üzerine yazma yapacak.
#Bu yüzden bu komutu kullanırken çok dikkatli olmalıyız. Çünkü daha önce böyle bir dosya varsa üzerine yazma yapacağından önceki veriler kaybolabilir."""
dosya.write("7:30 Kahvaltı") #Bu şekilde yazarsak programı tekrar çalıştırdığımızda silinip üzerine yazar.
#Yazacaklarımızı ya tek seferde 'writelines' ile liste halinde yazmalıyız ya da 'w' yi 'a' yaparak ekleyerek yazmalıyız.
dosya.writelines(["7:30 Kahvaltı\n","9:00 Koşu\n","11:00 Kitap okuma\n"])


dosya.close() #Bunun yerine tek satırlık with komutu ile de açılıp kapatılabilir.:
with open("planlar.txt","a",encoding="utf-8") as dosya: # Dosyayı açıp işlemi yaptıktan sonra tekrar kapatan komut.
    dosya.write("12:00 Öğle yemeği")

"""Kipler ve Görevleri
r   Dosyayı sadece okumak için açar.
r+  Dosyayı hem okumak hem de yazmak için açar.
w   Dosyayı sadece yazmak için açar.(Dosya varsa üzerine yazar yoksa yeni oluşturur.)
w+  Dosyayı okumak ve yazmak için açar. (Dosya varsa üzerine yazar yoksa yeni oluşturur.)
a   Eğer dosya varsa sonuna ekleme yapmak için açar dosya yoksa yeni oluşturur.
a+  Eğer dosya varsa okumak ve sonuna ekleme yapmak için açar dosya yoksa yeni oluşturur.
"""





