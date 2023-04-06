import requests
from bs4 import BeautifulSoup

# BeautifulSoup =>  web'den sonuç çekmek için bire bir. herhangi bir web sayfasından html ya da xml dökümanları parçalayarak istediğiniz biçimde, istediğiniz bilgilere erişmenizi sağlar.
# Web Scraping(kazıma) => Web kazıma web sitelerinden bilgi çıkartmanın bilgisayar programı tekniğidir.

# imdb.com sitesinde Top 250 Movies kısmından ilk 10 filmi web scraping ile getirdik

url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html=requests.get(url).content #sayfanın html içeriği gelir
soup=BeautifulSoup(html,"html.parser")

list=soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=10) #class'ı lister-list olan tbody'i getirecek (ilk 10 film gelecek)
count=1

for tr in list:
    title=tr.find("td",{"class":"titleColumn"}).find("a").text #tr içinde olan td'lerden classı titleColumn olanın a etiketindeki text'i al
    year=tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()") #yıl bilgisini aldık strip ile yılın kenarlarında olan parantezleri kaldırdık
    rating=tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text #rating bilgisini aldık

    print(f"{count} - film: {title.ljust(50)} yıl: {year} değerlendirme: {rating}") #title.ljust(50) -> ile sola hizalı elli karakterlik yer ayrıldı
    count+=1
