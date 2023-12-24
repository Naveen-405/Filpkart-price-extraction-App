from bs4 import BeautifulSoup
import pandas as pd
import requests
#define list
product_name = []
Prices = []
current_price = []
discount_percentage = []

for i in range(2,10):
    url="https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=dce22d9b-29b7-47a4-b6fa-84d424d1408e&as-backfill=on"+str(i)
    r =requests.get(url)
    #print(r)

    soup = BeautifulSoup(r.text, "html.parser")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
    # print(soup)

    names = box.find_all('div',class_="_4rR01T")

for i in names:
    name = i.text
    product_name.append(name)
#print(product_name)

price=box.find_all('div',class_="_30jeq3 _1_WHN1")

for i in price:
    name = i.text
    Prices.append(name)
#print(Prices)

cprice = box.find_all("div",class_="_3I9_wc _27UcVY")

for i in cprice:
    name = i.text
    current_price.append(name)

#print(current_price)

disct=box.find_all("div",class_="_3Ay6Sb")
for i in disct:
    name = i.text
    discount_percentage.append(name)

#print(discount_percentage)

df=pd.DataFrame({
    "product_Name":product_name,
    "prices":Prices,
    "Current_Price":current_price,
    "Discount_Percentage":discount_percentage
})
print(df)

df.to_csv("C:/Users/Public/flipkart_db.csv")