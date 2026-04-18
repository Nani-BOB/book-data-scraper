import requests
from bs4 import BeautifulSoup as bs4
import csv
data = []
headers = {
    "User-Agent":"Mozilla/5.0"
    }
for page in range(1, 4):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    
    
    
    response = requests.get(url, headers=headers)

    soup = bs4(response.content, "lxml")

    prod = soup.find_all("article", class_="product_pod")



    for item in prod:
        
        price = item.find("p", class_="price_color").text.strip()
        
        title = item.find("h3").find("a")["title"]
        
        rating_tag = item.find("p", class_="star-rating")
        rating_classes = rating_tag["class"]
        rating = rating_classes[1]
        
        availability = item.find("p", class_="instock availability").text.strip()
        data.append([title, price, rating, availability])
      
        
with open("projectessel.csv","w",newline="",encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Title","Price","Rating","Availability"])
    
    writer.writerows(data)



print("Done Writing")