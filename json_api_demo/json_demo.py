# Json modülü ile eklenen kullanıcıları json dosyasına kaydetme, giriş yapma ve çıkış yap işlemleri yapan basit bir uygulama

import json
import os

class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

class UserRepository:

    def __init__(self):
        self.users=[]
        self.isLoggedIn=False
        self.currentUser={}

        #load users from .json file

        self.loadUsers()
    
    def loadUsers(self):
        if os.path.exists("users.json"): #users.json dosyası var mı
            with open("users.json","r",encoding="utf-8") as file: #r modu => ile dosyaadki bilgileri okuma işlemi yapıyoruz
                users=json.load(file)
                for user in users:
                    user=json.loads(user) #json string bilgiden python objesine dönüştürme işlemi
                    newUser=User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append(newUser)
            print(self.users)

    def register(self,user:User):  #gönderilecek olan user'in user:User sayesinde User tipinde olmasını istiyoruz.
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu.")

    def login(self,username,password):
        for user in self.users:
                if user.username==username and user.password==password:
                    self.isLoggedIn=True
                    self.currentUser=user
                    print("Login işlemi yapıldı")
                    break
          
    def logout(self):
        self.isLoggedIn=False
        self.currentUser={}
        print("Çıkış yapıldı")

    def identity(self):
        if self.isLoggedIn:
            print(f"Username: {self.currentUser.username}\nPassword: {self.currentUser.password}")
        else:
            print("Giriş yapılmadı")

    def savetoFile(self):
        list=[]

        for user in self.users:
            list.append(json.dumps(user.__dict__)) #burada user class yapısını dictionary yapısına çevirdik


        with open("users.json","w") as file: #w modu => içerisinde bilgi varsa silip tekrar oluşturacak
            json.dump(list,file) #list objesini file ile kayıt ediyoruz, dump -- json tipine dönüştürür
                                       #fakat burada user kullansaydık sınıf tipinde olduğu için dump metodundan dolayı hata verecektir. Bu yüzden sınıf yapısını sözlük yapısına çevirerek işlemleri gerçekleştirdik

repository=UserRepository()

while True:
    print("Menü".center(50,"*"))
    secim=input("1-Register\n2-Login\n3- Logout\n4- İdentity\n5- Exit\nSeçiminiz: ")
    if secim=="5":
        break
    else:
        if secim=="1":
            username=input("Username: ")
            password=input("Password: ")
            email=input("E-mail: ")

            user=User(username=username, password=password, email=email)
            repository.register(user)

            print(repository.users) #kullanıcıları ekrana yazdırıyoruz

        elif secim=="2": #başarılı bir şekilde giriş yapılırsa Login işlemi yapıldı mesajı gelecek
            if repository.isLoggedIn:
                print("Zaten login oldunuz")
            else:
                username=input("Username: ")
                password=input("Password: ")

                repository.login(username,password)

        elif secim=="3":
           repository.logout()

        elif secim=="4":
            repository.identity()

        else:
            print("Yanlış seçim yaptınız.")

