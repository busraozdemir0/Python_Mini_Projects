# Kullanıcının girdigi sayı armstrong sayısı mıdır?

"""Basamaklarının küpleri toplamı kendisine eşit olan sayılara Armstrong sayı denir .

Örnek; 1,407,153,370,371,407

407 için = (4*4*4)+(7*7*7)=407 Bu yüzden 407 armstrong bir sayıdır."""

sayi=(input("Sayi giriniz: "))
basamak=len(sayi)
# sayi=int(sayi)
toplam=0

while(basamak!=0):
    toplam+=(int(sayi[basamak-1])**3)
    basamak-=1

if(toplam==int(sayi)):
    print(f"{sayi} sayısı armstrong bir sayıdır")
else:
    print(f"{sayi} sayısı armstrong bir sayı değildir")
