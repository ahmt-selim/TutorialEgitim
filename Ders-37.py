#map() - Yararlı Gömülü Fonksiyon/Sınıflar(YGFS)

#map fonksiyonu için teorik olarak bir listenin tüm elemanlarını bir fonksiyonda sırayla kullanmak diyebiliriz.
# map(fonk,*iter) şeklinde kullanılır.
def kareAl(x):
    return x**2

print(list(map(kareAl,[1,2,3,4,5,6])))

users={"ahmt.selim12":"123456",
       "glhn.ksa":"987654",
       "byz.ksa59":"byz.6987452",
       "klmn.885":"asddsa5562"}
def control(username,password):
    try:
        if users[username]==password:
            return True
        else:
            return False
    except KeyError:
        return False

result=map(control,["ahmt.selim12","glhn.","byz.ksa59","klmn.885"],["123456","987654","byz.6987452","5562"])
#Yukarıda kullanıcı adlarından 2.si ve şifrelerden sonuncuyu hatalı yazdım ve sırasıyla hangilerinin False olduğunu gösterdi.
print(list(result))








