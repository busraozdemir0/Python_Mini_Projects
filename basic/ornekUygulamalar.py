#1. Metin içerisinde geçen harf sayısı

# metin="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla metus sapien, ultricies nec tortor at, viverra consequat nulla. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec a nunc vel felis pellentesque mollis sed in dolor. Vivamus faucibus, nibh eget egestas iaculis, quam orci ornare tortor, sed consectetur nisl risus in arcu. Aliquam id enim ante. In hac habitasse platea dictumst. Nunc accumsan mauris velit, non eleifend ipsum semper eget. Morbi ullamcorper magna metus, eget feugiat diam efficitur tempor. Suspendisse potenti. Nam luctus in nulla sed interdum. Sed aliquet feugiat nulla, in dictum velit aliquet at. Integer ac neque vitae arcu malesuada bibendum. Pellentesque sit amet varius nulla, in scelerisque odio. Vestibulum vulputate, metus euismod placerat ullamcorper, orci sapien gravida leo, vel tempus leo velit in dui. Duis leo nunc, euismod ac eros et, consequat fringilla enim.
# Nam non purus ac leo hendrerit tristique in eu risus. Phasellus faucibus velit eget urna mattis ultrices. Nulla vel mi vel sem pretium euismod vel vitae sapien. Sed consectetur mi urna, in sagittis nulla elementum quis. Maecenas viverra ipsum porta condimentum sagittis. Donec nec ligula condimentum, molestie enim in, viverra massa. Nulla quam mi, porttitor ut arcu et, sagittis porta ligula. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Duis purus nunc, posuere sit amet semper a, tincidunt sit amet arcu. Phasellus vitae posuere ante. Nunc ullamcorper accumsan elit sit amet scelerisque. Quisque sed tellus at risus dapibus elementum. Curabitur lectus dolor, luctus at tincidunt non, porta et neque. Maecenas ultrices lorem vitae felis elementum venenatis. Nunc vestibulum ipsum vel malesuada sollicitudin.
# Integer et est pellentesque neque interdum cursus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt ante ipsum, at suscipit velit malesuada eget. Donec eros quam, pharetra a venenatis id, convallis a mi. Aenean fringilla eros non urna ultricies viverra. Donec sodales eu sem vitae volutpat. Vivamus euismod pulvinar metus, sit amet auctor diam viverra maximus. Quisque at ipsum ac est luctus pellentesque.
# Nulla luctus diam vitae lorem facilisis laoreet. Fusce eros sem, sodales non pellentesque sit amet, posuere mollis dui. Suspendisse aliquet maximus elit, ut fringilla nulla elementum a. Vivamus quam nulla, iaculis quis finibus vitae, porttitor non enim. Proin pretium, dui a aliquam elementum, erat ex tristique sapien, porttitor maximus mi erat in urna. Morbi tempus turpis vitae tortor facilisis suscipit. Ut in condimentum ante. Morbi auctor erat quis tincidunt congue. Donec aliquet nibh ac est feugiat, vel gravida ipsum faucibus. Maecenas sagittis, purus in tincidunt feugiat, orci eros mattis lectus, ut luctus libero dolor ut leo. Duis imperdiet tortor nec est laoreet gravida. Etiam dapibus egestas augue non dapibus.
# Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed sapien ligula, gravida a dolor sit amet, consectetur faucibus dolor. Pellentesque sed nunc ipsum. Aenean semper felis quis velit interdum, non facilisis felis blandit. Suspendisse urna felis, venenatis eu hendrerit eget, aliquet vel nulla. Quisque at ligula a libero ultricies pulvinar faucibus id nulla. Cras luctus lacus at nulla commodo porta. Proin facilisis eros in nibh tincidunt ultrices. Aenean non nibh vehicula, ornare urna nec, vestibulum dui. Suspendisse dignissim ac nunc a pulvinar.
# """

# harf=input("Aramak istediğiniz harfi girin: ")
# sayac=0
# for m in metin:
#     if(m==harf):
#         sayac+=1

# print(f"{harf} harfi metinde {sayac} kere geçmektedir.")


#2. Kullanıcı Girişi
# *kullanıcı adı ve şifre doğru girilinceye kadar kullanıcı adı ve şifre soran program

# userName="busra81"
# password="12345"

# while(True):
#     kullaniciAd=input("Kullanıcı adınız: ")
#     şifre=input("Şifreniz: ")
#     if(kullaniciAd==userName and şifre==password):
#         print("Giriş başarılı")
#         break
#     else:
#         print("Kullanıcı adınız veya parolanız hatalı. Lütfen tekrar deneyin.")


# 3. Bankamatik örneği
# *ilk basta bakiye=1000
# 1.bakiye sorma
# 2.para yatırma
# 3.para çekme
# 4.çıkış

# bakiye=1000
# print("""1. Bakiye bilgisi
# 2. Para yatırma
# 3. Para çekme
# 4. Çıkış""")

# secenek=input("Lütfen yapmak istediğiniz işlemi seçeneğini girin: ")

# match secenek:
#     case '1': 
#         print(f"Bakiyenizde {bakiye} TL vardır.") 
#     case '2': 
#         miktar=float(input("Yatırmak istediğiniz para miktarını girin: "))
#         bakiye=bakiye+miktar
#         print(f"Toplam bakiyeniz {bakiye} TL") 
#     case '3':
#         cekilecekMiktar=float(input("Çekmek istediğiniz para miktarını girin: "))
#         bakiye=bakiye-cekilecekMiktar
#         print(f"Toplam bakiyeniz {bakiye} TL") 
#     case '4':
#         exit
#     case _:
#         print("Hatalı değer girdiniz. Lütfen tekrar deneyin.")


#4- Girilen sayı asal mı?

sayi=int(input("Sayi giriniz: "))
for i in range(2,sayi):
    if(sayi%i==0):
        print(f"{sayi} sayısı asal değil {i} sayısı tam bölüyor.")
        break
else:
    print(f"{sayi} sayısı asal sayıdır")

        
