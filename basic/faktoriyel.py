#Faktöriyel Hesabı

while True:
    sayi=input("Faktöriyelini almak istediğiniz sayiyi girin Çıkmak için q: ")
    if(sayi=="q"):
        break
    sayi=int(sayi)
    sonuc=1
    for i in range(2,sayi+1):
        sonuc=sonuc*i
    print("Sonuç: ",sonuc)


