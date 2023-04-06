#1-100 arasında üretilen sayıyı 5 hak ile buldurmaya çalışalım.
# *100 üzerinden bir puanlama yapın. Her soru 20 puan.
# **Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.


import random

sayi=random.randint(1,100) #1-100 arasında rastgele sayı üretir
can=int(input("Kaç hak kullanmak istersiniz?: "))
hak=can
sayac=0

while hak>0:
    hak-=1
    sayac+=1
    tahmin=(int(input("Tahmininiz: ")))

    if sayi==tahmin:
        print(f"Tebrikler {sayac}. defada bildiniz... Toplam puanınız: {100-(100/can)*(sayac-1)}")
        break
    elif sayi>tahmin:
        print("Tahmin ettiğiniz sayı tutulan sayıdan daha küçük. Tekrar deneyin")
    else:
        print("Tahmin ettiğiniz sayı tutulan sayıdan daha büyük. Tekrar deneyin")

    if(hak==0):
        print(f"Hakkınız bitti. Tutulan Sayi: {sayi}")