# myDict = {"car":300,"plane":500,"rocket":600,"helicopter":700}

# for (key,value) in myDict.items():
#     print(value) #it's show the values

# for (key,value) in myDict.items():
#     print(key)  #it's show the keys






# isim = input('isminiz: ')
# yas = int(input('yaşınız: '))
# egitim = input('eğitim: ')

# if (yas>=18):
#     if (egitim=='lise' or egitim=='üniversite'):
#         print(f'{isim} ehliyet alabilirsin.')
#     else:
#         print(f'{isim} ehliyet alamazsın eğitim durumun yetersiz.')
# else:
#     print(f'{isim} ehliyet alamazsın yaşın tutmuyor.')




# yazili1 = float(input('1.yazılı: '))
# yazili2 = float(input('2.yazılı: '))
# sozlu = float(input('sözlü: '))

# ortalama = (yazili1 + yazili2 + sozlu)/3

# if (ortalama>=0) and (ortalama<25):
#      print(f'ortalamanız: {ortalama} notunuz: 0')
# elif (ortalama >= 25 ) and (ortalama<45):
#      print(f'ortalamanız: {ortalama} notunuz: 1')
# elif (ortalama >= 45 ) and (ortalama<55):
#     print(f'ortalamanız: {ortalama} notunuz: 2')
# elif (ortalama >= 55 ) and (ortalama<70):
#     print(f'ortalamanız: {ortalama} notunuz: 3')
# elif (ortalama >= 70 ) and (ortalama<85):
#     print(f'ortalamanız: {ortalama} notunuz: 4')
# elif (ortalama >= 85 ) and (ortalama<=100):
#     print(f'ortalamanız: {ortalama} notunuz: 5')
# else:
#     print('yanlış bilgi girdiniz.')





email = 'email@yusufceker.com'
password = '1234'

girilenEmail = input('email: ')
girilenPassword = input('password: ')

if girilenEmail == email and girilenPassword == password:
    print("Giriş Başarılı")
elif girilenEmail != email and girilenPassword == password:
    print("Email bilginiz yanlış")
elif girilenPassword != password and girilenEmail == email:
    print("Şifreniz yanlış")
else:
    print("Şifre ve Email bilgileriniz yanlış, lütfen tekrar deneyin.1")








# myList  = [1,2,3,4,5,6,7,8,9]

# if 1 in myList:
#     print("evet")
# else:
#     print("hayır")