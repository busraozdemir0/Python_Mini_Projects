liste=["1","2","5a","10b","abc","10","50"]

#1- Liste elemanları içerisindeki sayısal değerleri bulunuz.

# for x in liste:
#     try:
#         result=int(x)
#         print(result)
#     except ValueError: #hata görsede listenin sonuna kadar devam etmesi için
#         continue

#2- Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayısal değer olduğundan emin olun. Aksi halde hata mesajı yazın.

# while True:
#     sayi=input("Sayı: ")
#     if sayi=="q":
#         break

#     try:
#         result=int(sayi)
#         print("Girdiğiniz sayı: ",result)
#         break
#     except ValueError:
#         print("Geçersiz sayı")


#3- Girilen parola içinde türkçe karakter hatası veriniz.

# def checkPassword(parola):
#     turkce_karakterler="şçğüöıİ"
#     for i in parola:
#         if i in turkce_karakterler: #eğer parola karakterleri turkce_karakterler içerisinde varsa hata fırlatacak
#             raise TypeError("Parola türkçe karakter içeremez.")
#         else:
#             pass
#     print("Geçerli parola")

# parola=input("Parola: ")

# try:
#     checkPassword(parola)
# except TypeError as err:
#     print(err)



#4- Faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.

def faktoriyel(x):
    x=int(x)

    if(x<0):
        raise ValueError("Negatif değer")
    
    result=1

    for i in range(1,x+1):
        result*=i
    
    return result


for x in [5,10,20,-3,"10a"]:
    try:
        y=faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)