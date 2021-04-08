import smtplib
import time
import requests as rq
from bs4 import BeautifulSoup

site = "https://www.asos.com/nike-football/nike-football-strike-21-joggers-in-black-and-purple/prd/21304440?colourwayid=60155166&SearchQuery=nike%20joggers"

header = {'user_agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}


def get_price():
    html = rq.get(site)
    soup = beautifulsoup(http, 'html.parser')
    price = [i.get_text() for i in soup.find_all('span', {'class':"text: priceText(), css: {'product-price-discounted' : isDiscountedPrice }, markAndMeasure: 'pdp:price_displayed'"})]

    final_price = "".join(price)[0:5]
    final_price = int(final_price.replace("," , ""))

   # print(final_price)


    if final_price < 47.95:
        send_email()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('*********@gmail.com', 'password')

    subject = "Price gone down"
    body = "https://www.asos.com/nike-football/nike-football-strike-21-joggers-in-black-and-purple/prd/21304440?colourwayid=60155166&SearchQuery=nike%20joggers"
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail('*********@gmail.com',
                    '*********@yahoo.com', msg)

    print("Hey, email has been sent!")
    server.quit()

    while True:
        get_price()
        time.sleep(60 * 60 * 24)




print(get_price())
