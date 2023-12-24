from bs4 import BeautifulSoup
import requests
import pandas as ps

product_Name = []
price = []
info = []
rating = []
reviews = []

for i in range(2,10):
    url = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_7_4.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_OUJ0NDXWZCCJ_wp2&fm=neo%2Fmerchandising&iid=M_8a65da8f-3e06-4b5e-9296-b207eefd8ec9_4.OUJ0NDXWZCCJ&ssid=kkt1ieiu3k0000001677144198397"+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    box = soup.find('div', class_="_1AtVbE col-12-12")
#print(soup)

name = soup.find_all('div', class_="_4rR01T")
for i in name:
        name = i.text
        product_Name.append(name)
#print(product_Name)

Price = soup.find_all('div',class_="_30jeq3 _1_WHN1")
for i in Price:
        name = i.text
        price.append(name)
#print(price)

Info = soup.find_all('ul', class_="_1xgFaf")
for i in Info:
        name = i.text
        info.append(name)
#print(info)

rate = soup.find_all('div', class_="_3LWZlK")
for i in rate:
        name = i.text
        rating.append(name)
#print(rating)

review = soup.find_all('span', class_="_2_R_DZ")
for i in review:
        name = i.text
        reviews.append(name)
#print(reviews)

a = {'product_Name': product_Name,'Price': price, 'info': info, 'rate': rating, 'Review': reviews}
df = ps.DataFrame.from_dict(a, orient='index')
df = df.transpose()
print(df)

