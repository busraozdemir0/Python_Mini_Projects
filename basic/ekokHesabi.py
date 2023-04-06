# Kullanıcıdan aldiginiz iki sayinin EKOK'u

"""Örnek: 4 ve 6 sayılarının en küçük ortak katını bulmak için 
öncelikle bu sayıların pozitif katları yazılır ve ortak olanlar işaretlenir.

4= 8,12,16,20,24,28…

6= 12,18,24,26,42…

Yukarıdaki işlemde ortak katların en küçüğü olan 12 bu iki sayının 
ekoku’dur ve EKOK (4,6)= 12 şeklinde gösterilir.
"""

sayi1=int(input("Sayı 1: "))
sayi2=int(input("Sayı 2: "))

if(sayi1>sayi2):
    buyukSayi=sayi1
else:
    buyukSayi=sayi2

while buyukSayi <= sayi1 * sayi2:            # EKOK' u hesapla
    if buyukSayi % sayi1 == 0 and buyukSayi % sayi2 == 0:
         ekok = buyukSayi
         break                      # iki sayıyı çarp birbirlerine bölümü tam ise döngüyü kır
    buyukSayi = buyukSayi + 1

print(f"EKOK({sayi1},{sayi2}): {ekok}")