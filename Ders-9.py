#Tuple Veri Tipleri
a=()
b=tuple()
print(type(a),type(b))
c=(1,2,3,4,5,6)
#c[2]=20 #Var olan bir değer Tuple'ın içerisinde değiştirilemez
yazi="Mert Mekatronik"
yeniyazi=tuple(yazi) #String İfadeyi Tuple Yapmak:
print(yeniyazi)
yeni=(1,2,3,"Ahmet","Selim",56,"Turkiye","Mert","Mert","Selim","Selim")
print(yeni.index("Selim")) #Demet Objesinden Değerin Kaçıncı İndekste Olduğunu Bulmak:
print(yeni.count("Selim")) #Demet Objesinde Kaç tane Aynı Objede Olduğunu Bulmak:





