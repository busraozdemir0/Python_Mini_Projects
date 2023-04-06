# themoviedb.org => film ve dizi arşivi
# themoviedb'nin sunduğu apiyi bu uygulamamızda kullanacağız
# *Anahtar kelimeye göre arama işlemi
# **En popüler film listesini getirme işlemi

import requests

class theMovieDb:
    def __init__(self):
        self.api_url="https://api.themoviedb.org/3"
        self.api_key="<api_key>"  #themovie.org sitesinden aldığımız api key--üye olup kendi api keyinizi girin

    def getPopulars(self):
        response=requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1") #page=1 ifadesi sonuçların sadece ilk sayfası gelmesi için
        return response.json()
    
    def getSearchResults(self,keyword): #girilen keyword'e göre film listeleme işlemi yapan fonksiyon
        response=requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json
    
movieApi=theMovieDb()

while True:
    secim=input("1- Popular Movies\n2- Search Movies\n3- Exit\nSeçim: ")

    if secim=="3":
        break

    else:
        if secim=="1":
            movies=movieApi.getPopulars()
            for movie in movies["results"]:
                print(movie["title"])  # popüler olan film listesinin sadece isimleri gelecek
        
        elif secim=="2":
            keyword=input("Arayacağınız kelimeyi girin: ")
            movies=movieApi.getSearchResults(keyword)
            for movie in movies["results"]:
                print(movie["name"])  # girilen kelimeye göre bu kelimenin geçtği filmlerin isimleri gelecek
        
        else:
            print("Yanlış seçim.")

       