# Github Api ile Repo oluşturma, görüntüleme, kullanıcı bulma uygulaması

import requests

class Github:
    def __init__(self):
        self.api_url="https://api.github.com"
        self.token="<token_bilgisi>"  #github üzerinde kendi hesabımıza ulaşabilmek için token oluşturduk
    
    def getUser(self, username):  #girilen kullanıcı adına göre bilgileri döndürecek olan fonksiyon
        response=requests.get(self.api_url+"/users/"+username)
        return response.json() #bilgileri json formatında geri döndürüyoruz
    
    def getRepositories(self,username): #girilen kullanıcı adına göre repo isimlerini döndürecek olan fonksiyon
        response=requests.get(self.api_url+ "/users/"+username+"/repos")
        return response.json()
    
    def createRepository(self,name):
        #giriş yapılan hesap için repo oluşturacağımızdan dolayı post işlemi yapıyoruz.
        response=requests.post(self.api_url+"/user/repos?access_token="+self.token, json=
            {"name": name,
            "description": "This is your first repository",
            "homepage":"https://github.com",
            "private":True,
            "has_issues":True,
            "has_projects":True,
            "has_wiki":True}
            ) 
        return response.json()

github=Github()

while True:
    secim=input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ")

    if secim=="4":
        break

    else:
        if secim=="1":
            username=input("Username:" )
            result=github.getUser(username)
            print(f"Name: {result['name']} public repos: {result['public_repos']}  followers: {result['followers']} ")

        elif secim=="2":
            username=input("Username:" )
            result=github.getRepositories(username)
            for repo in result:
                print(repo["name"])

        elif secim=="3":
            name=input("Repository Name: " )
            result=github.createRepository(name)
            print(result)

        else:
            print("Yanlış seçim.")