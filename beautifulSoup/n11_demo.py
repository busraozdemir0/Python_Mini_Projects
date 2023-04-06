import requests
from bs4 import BeautifulSoup

#n11 sitesindeki dizüstü bilgisayarlar üzerinden 20 ürünün adı, linkini, eski ve yeni fiyatlarını çektik

url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html=requests.get(url).content
soup=BeautifulSoup(html,"html.parser") #n11 sitesindeki dizüstü bilgisayar sayfasındaki kaynak kodları çekmemizi sağlar

list=soup.find_all("li",{"class":"column"},limit=20) #limit=20 ile sadece 20 ürün listelenmesini sağladık

for li in list:
    name=li.div.a.h3.text.strip() #bu şekilde class belirtmesek de ilk sıradaki div etiketinin ilk a etiketini alır...
    link=li.div.a.get("href")
    oldprice=li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL") #sayfada belirtilen classta birinci a tagında üstü çizili olarak eski fiyat yer alıyor
    newprice=li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip("TL") #ürün detaylarında ikinci a tagında yeni fiyat yazıyor

    print(f"name: {name}, link: {link}, old price: {oldprice}, new price: {newprice}")

