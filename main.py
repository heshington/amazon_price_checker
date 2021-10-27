import requests
from pprint import pprint
from bs4 import BeautifulSoup
import smtplib


# target_price = input("Whats the price your willing to pay for this thingy?")
target_price = 100
URL = "https://www.amazon.com/TENDLIN-Compatible-Premium-Flexible-Silicone/dp/B07GZDTTXL/ref=sr_1_6?dchild=1&keywords=iphone%2Bxs%2Bmax%2Bleather%2Bcase&qid=1635283348&sr=8-6&th=1"
headers = {
    "content-type":"text",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9",
}

response = requests.get(URL, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
item_title =  soup.find(name="span", class_= "a-size-large product-title-word-break")
amazon_price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockSalePriceString")


item_title =  item_title.getText().strip()
amazon_price =  amazon_price.getText()
amazon_price = amazon_price.strip("$")
print(amazon_price)
print(item_title)
if float(amazon_price) <= target_price:

    ##Send email
    # Sending Email with Python
    my_email = "FROM_EMAIL"
    password = "EMAIL_PASSWORD"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="TO_SEND_EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n"
                f"{item_title} has fallen below your target price of ${target_price}, it is now ${amazon_price}. \n"
                f"You can buy it now at \n "
                f"{URL}"
        )
