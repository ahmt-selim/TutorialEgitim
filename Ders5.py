#Veri Dönüşümleri

k=5.16
print(type(k))
l="500"
print(int(l)+200)
"""m="7082m"
#print(int(m)) string ifadedeki harfler integer olarak dönüştürülemez."""

sayi=3215468446798
print(len(str(sayi)))

a=int(input("sayi1 "))
b=int(input("sayi2 "))

secenek=int(input("1-topla\n2-çıkar\n3-çarp\n4-böl"))

if secenek==1:
    print(a+b)
elif secenek==2:
    print(a-b)
elif secenek==3:
    print(a*b)
else:
    print(a/b)