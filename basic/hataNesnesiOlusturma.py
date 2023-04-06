# Girilen parolanın doğrulanması yanlış girildiği takdirde parolanın tekrar istenmesi işlemi

def check_password(sifre):
    import re
    if len(sifre)<8:
        raise Exception("Parola en az 7 karakter olmalıdır.")
    elif not re.search("[a-z]",sifre):
        raise Exception("Parola küçük harf içermelidir")
    elif not re.search("[A-Z]",sifre):
        raise Exception("Parola büyük harf içermelidir")
    elif not re.search("[0-9]",sifre):
        raise Exception("Parola rakam içermelidir")
    elif not re.search("[_@$.*#]",sifre):
        raise Exception("Parola alfa nümerik karakter içermelidir")
    elif re.search("[\s]",sifre):
        raise Exception("Parola boşluk içermemelidir")
    else:
        print("Geçerli parola")

while True :
    password=input("Parola giriniz: ")

    try:
        check_password(password)
    except Exception as ex:
        print(ex)
    else:
        break
    finally:
        print("Parolama doğrulama işlemi")