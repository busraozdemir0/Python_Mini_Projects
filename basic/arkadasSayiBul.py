#Kullanıcı bir sayi girer, girdiği sayının arkadaş sayısı var mı bulunuz.
"""Örnek: 220 ve 284 sayıları Arkadaş sayılardır.

220 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284

284 = 1 + 2 + 4 + 71 + 142 = 220"""
# toplam1=0
# toplam2=0
# sayi=int(input("Sayı giriniz: "))

# for i in range(1,sayi):
#     if(sayi%i==0):
#         toplam1+=i
       
# for j in range(1,toplam1):
#     if(toplam1%j==0):
#         toplam2+=j

# if(sayi==toplam2):
#     print(f"{sayi} sayısının arkadaş sayısı: {toplam1}")
# else:
#     print(f"{sayi} sayısının arkadaş sayısı yok.")


# Kullanıcının girdiği iki sayı arasındaki arkadaş sayıları bulunuz.

sayi1=int(input("1. Sayıyı giriniz: "))
sayi2=int(input("2. Sayıyı giriniz: "))

for i in range(sayi1,sayi2+1):
    toplam1,toplam2=0,0
    for j in range(1,i):
        if(i%j==0):
            toplam1+=j

    for k in range(1,toplam1):
        if(toplam1%k==0):
            toplam2+=k
    if(i==toplam2):
        print(f"{i}, {toplam1} sayısı arkadaş sayıdır.") 

