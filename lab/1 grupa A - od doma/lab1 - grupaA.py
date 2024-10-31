from datetime import date
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from IPython.display import HTML
from urllib3 import request

#Setting the url
url = "https://clevershop.mk/product-category/mobilni-laptopi-i-tableti/"
#Sending HTTP request to the Website
response = requests.get(url)
#print(response.text)
#Printing the status code gotten from the response

# print(requests.get("https://clevershop.mk/product-category/mobilni-laptopi-i-tableti/page/14/").status_code)
data = []
counter_for_pages = 1
while 1:
    tmp_url = f"{url}page/{counter_for_pages}"
    response = requests.get(tmp_url)

    print(f"Response code for page {counter_for_pages} is {response.status_code}")
    if requests.get(tmp_url).status_code != 200:
        print(f"The last page of the scraping was the {counter_for_pages-1}th page, so this page does not exist! That is why the scraping is finished")
        break
    soup = BeautifulSoup(response.text, "html.parser")
    # With the next line we are getting the titles of the product
    product_titles = soup.select(".product-wrapper .wd-entities-title")
    product_prices_list = soup.select(".product-wrapper .price")

    regular_prices = []
    discounted_prices = []
    # Here i make the checking if there is discounted price and the regular price of a product in the list of products
    for i in range(0, len(product_prices_list)):
        if "Original" in product_prices_list[i].text.split(" "):
            regular_prices.append(product_prices_list[i].text.split(" ")[0])
            discounted_prices.append(product_prices_list[i].text.split(" ")[-1])
        else:
            regular_prices.append(product_prices_list[i].text.split(" ")[0])
            discounted_prices.append("0 ден")
    link_list = soup.select(".product-wrapper .hover-img a")
    add_to_cart_buttons = soup.select(".wd-add-btn a")
    print()
    for k in range(len(link_list)):
        link = link_list[k].get("href")
        product_title = product_titles[k].text
        regular = regular_prices[k]
        discounted = discounted_prices[k]
        shopping_cart = add_to_cart_buttons[k].get("href")
        dictionary = {
        "Product title": product_title,
            "Regular product price": regular,
            "Discounted product price": discounted,
            "Shopping cart ID": shopping_cart,
            "Link for the product": link
        }
        data.append(dictionary)
    counter_for_pages += 1
data_frame = pd.DataFrame(data)
data_frame.to_csv("data.csv", index=False)

# for i,j,k in zip(regular_prices, discounted_prices, product_titles):
#   print(f"Title: {k.text} --> Regular: {i} - Discounted: {j}")

# print(len(link_list))
# print(link_list[0].get("href"))


# add_to_cart_buttons = soup.select(".wd-add-btn a")
# print(len(add_to_cart_buttons))
#treba da dodadam samo za novire i da ja napraam lisara so e 2 min rabota
