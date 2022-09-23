# def hello(name):
#     print("Merhaba "+ name)

# hello("Yusuf") # Merhaba Yusuf





# def toplama(a,b):
#     return a+b

# sonuc = toplama(10,20)
# print(sonuc) # 30



# def superToplama(*args):
#     return sum(args)
# print(superToplama(100,200,300))  # 600





def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)      # Kendisine gönderilen bir sayının tam bölenlerini bulan basit bir uygulama

    return tamBolenler 

print(tamBolenleriBul(12))









# def kimlik(ad,soyad):
#     return f"Ad: {ad}, Soyad: {soyad}"
# print(kimlik("Yusuf","Çeker"))










def kontrolFonksiyonu(string):
    return "e" in string

print(kontrolFonksiyonu("emir")) # true









def bolmeIslemi(numara):
    return numara / 2


benimListem = [1,2,3,4,5,6,7,8,9,10]


yeniListe = []
for eleman in benimListem:
    yeniListe.append(bolmeIslemi(eleman))
print(yeniListe)



#  they are the same 




print(list(map(bolmeIslemi,benimListem))) # with map function..






stringList = ["yusuf","ahmet","mehmet","ali","veli"]

print(list(map(kontrolFonksiyonu,stringList)))


print(list(filter(kontrolFonksiyonu,stringList))) # içinde e olan isimleri söylüyor.





# ages = [5, 12, 17, 18, 24, 32]

# def myFunction(age):
#   if age < 18:
#     return False
#   else:
#     return True

# adults = filter(myFunction, ages)

# for age in adults:
#   print(age)







# x = lambda a, b : a * b
# print(x(5, 6))  # 30


# y = lambda a, b, c : a + b + c
# print(y(5, 6, 2))  # 13



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) # 22
print(mytripler(11)) # 33