# Bankamatik Uygulaması

# Dictionary yapısı kullanarak referans type kullanmış olacağız
# *Bu şekilde fonksiyon içerisinde yapılan değiştirme veya güncellemeler global'de tanımlanan değişkenlere de yansıyacaktır

busra={
    "ad": "Büşra Özdemir",
    "hesapNo": "123456789",
    "bakiye": 8500,
    "ekHesap":1000
}

samet={
    "ad": "Samet Sarıkaya",
    "hesapNo": "987654321",
    "bakiye": 10000,
    "ekHesap":3000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if (hesap["bakiye"]>=miktar):
        hesap["bakiye"] -=miktar
        print("Paranızı alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam=hesap["bakiye"]+hesap["ekHesap"]

        if(toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı? (e/h): ")
            
            if(ekHesapKullanimi=="e"):
                ekhesapKullanilacakMiktar=miktar-hesap["bakiye"]
                hesap["bakiye"]=0
                hesap["ekHesap"] -=ekhesapKullanilacakMiktar 
                print("Paranızı alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        
        else:
            print("Üzgünüz :( Bakiyeniz yetersiz.")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")


cekilecekTutar=int(input("Lütfen çekmek istediğiniz tutarı giriniz: "))

paraCek(busra,cekilecekTutar)