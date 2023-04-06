import random

# ~~~ Yer Değiştirmeli Sıralama (Kabarcık Sıralaması) ~~~

# liste=list(range(10))
# liste=random.sample(liste,10)
# print(liste)

# for i in range(0,len(liste)-1):
#     for j in range(i+1,len(liste)):
#         if(liste[i]>liste[j]):
#             bos=liste[i]
#             liste[i]=liste[j]
#             liste[j]=bos
# print(liste)

# ~~~ Seçmeli Sıralama (Selection Sort) ~~~

# liste=list(range(10))
# liste=random.sample(liste,10)
# print(liste)

# for i in range(0,len(liste)-1):
#     enKucuk=i
#     for j in range(i+1,len(liste)):
#         if(liste[enKucuk]>liste[j]):
#             enKucuk=j
#     bos=liste[i]
#     liste[i]=liste[enKucuk]
#     liste[enKucuk]=bos
# print(liste)


# ~~~ Doğrusal Arama (Linear Search) ~~~

# liste=list(range(1,10,2)) #1'den 10'a kadar 2'şer 2'şer liste oluşturur
# print(liste)

# aranan=int(input("Aramak istediğiniz sayıyı girin: "))
# sayac=0

# for i in range(len(liste)):
#     sayac+=1
#     if(aranan==liste[i]):
#         print(f"Aradığınız {aranan} sayısı listenin {i+1}. elemanında bulundu")
#         break
# else:
#     print(f"Aradığınız {aranan} sayısı listede yok")


# ~~~ İkili Arama (Binary Serach) ~~~

""" Örnek olarak elimizde   9, 7, 6, 4, 3, 2, 1   sıralı dizisi olsun.   Bu dizi arasında 6 sayısını aralım.

1.  Dizinin ortasına bakılır  .  4 ? 6  –> 4 < 6  . Aranan değer büyük olduğundan dizinin sağ tarafı 
dikkate alınmaz ve sol taraf üzerinden arama işlemine devam edilir. Böylece veri kümemizi yarı yarıya küçültmüş oluruz.

2.  9 , 7 , 6 .. bu sefer elimizde kalan dizinin tam ortasına bakılır. 7 ? 6 –> 7 > 6. Aranan değer küçük olduğundan arama 
işlemine sağ taraftan devam edilir.

3.  6 = 6 .. Aranan değer bulunmuş olur. """

liste=list(range(1,30,2))
liste=random.sample(liste,15)
print("Rastgele liste: ",liste)

#öncelikle rastgele oluşan diziyi sıralayalım
for i in range(0,len(liste)-1):
    for j in range(i+1,len(liste)):
        if(liste[i]>liste[j]):
            bos=liste[i]
            liste[i]=liste[j]
            liste[j]=bos
print("Sıralanmış liste: ",liste)

aranan=int(input("Aramak istediğiniz sayıyı giriniz: "))
ek=-1
eb=len(liste)
orta=0
sayac=0
while(eb-ek)>1:
    orta=(eb+ek)//2
    sayac+=1
    print("ek:{}, eb:{}, orta:{}, sayac:{}".format(ek,eb,orta,sayac))
    if(aranan==liste[orta]):
        break
    elif(aranan<liste[orta]):
        eb=orta
    elif(aranan>liste[orta]):
        ek=orta
if(eb-ek==1):
    print(f"Aradığınız {aranan} sayısı listede bulunamadı")
else:
    print(f"Aradığınız {aranan} sayısı listenin {orta+1}. elemanında bulundu")
