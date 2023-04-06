# Kullanıcıdan aldiginiz iki sayının EBOB'u

"""
18= 1,2,3,6,9,18

24= 1,2,3,4,6,8,12,24

Vermiş olduğumuz örnekte, ortak bölenlerin en büyüğü 6 olduğu için bu iki tamsayının ebobu 6’dır."""

sayi1=int(input("Sayı 1: "))
sayi2=int(input("Sayı 2: "))

if(sayi1>sayi2):
    kucukSayi=sayi2
else:
    kucukSayi=sayi1

for i in range(1,kucukSayi+1):
    if(sayi1%i==0 and sayi2%i==0):
        ebob=i
print(f"EBOB({sayi1},{sayi2}): {ebob}")