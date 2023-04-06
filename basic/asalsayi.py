#Girilen bir sayının asal olup olmadığını bulan program

sayi=int(input("Sayı giriniz: "))
asalMi=True

if(sayi==1):
    asalMi=False

for i in range(2,sayi):
    if(sayi%i==0):
        asalMi=False
        break

if(asalMi):
    print("Girdiğiniz sayı asaldır.")
else:
    print("Girdiğiniz sayı asal değildir.")