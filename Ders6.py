#print("Fonksiyonu Ve Özellikleri")
a="Mert"
b="Onur"
c="Ali"
print(a,b,c)
print(a+b+c)
print("Ahmet\nSelim") #Alt satıra geçmek.
print("Gülhan\tBeyza") #Tab boşluğu bırakmak.

#'sep = ""' kullanarak Yazıların Arasını Ayarlamak.
print("Merhabalar",4,2,6,"SA",sep="-")
#'end = ""' kullanarak Yazıların Sonunu Ayarlamak.
print("Merhabalar","Ben","Bu","Yerlerden","Biriyim",sep="_",end=" - ")
print("Uzunca","zamandır","bizim","haneden","firariyim",sep="_")
#başına '*' ekleyerek Yazıların Arasını Ayarlamak.
print(*"TBMM")
print(*"TBMM",sep=".")
print("TBMM",sep=".")
#sonuna '.format()' ekleyerek Yazıların Sonradan Ayarlayalım:
print("{} ile {} sayısının toplamı = {} sayısıdır".format(6,5,11))

print("{d} ile {e} sayısının toplamı = {f}'dir".format(d=5,e=6,f=7))
#'% ()' İle Yazıların İçerisine Sonradan Değişken eklemek % ():
print("%s ile %s sayısının çarpımı:%s" %(4,5,20))

