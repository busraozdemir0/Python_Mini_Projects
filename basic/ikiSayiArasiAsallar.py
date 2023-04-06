#Kullanıcının Girdiği İki Sayı Arasındaki Asallar?

# sayi1=int(input("Birinci sayıyı giriniz: "))
# sayi2=int(input("İkinci sayıyı giriniz: "))

# for i in range(sayi1,sayi2+1):
#     for j in range(2, i):
#         if(i%j==0):
#             break
#     else:
#         print(i, " sayısı asaldır")

### diğer yöntem
sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))

for i in range(sayi1,sayi2+1):
    sayac=0
    for j in range(1, i+1):
        if(i%j==0):
            sayac+=1
    if sayac==2: #Eğer sayi asal ise 1'e ve kendisine tam bölüneceğinden 2 böleni vardır Bu yüzden sayac 2'ye eşitse asal sayıdır kontrolü yaptık.
        print(i, " sayısı asaldır")
