#  Copyright Beverly Xin Chong Tan (c) 2020.

from bs4 import BeautifulSoup


def get_prices_for(files):
    prices = []
    for file in files:
        soup = BeautifulSoup(open(file), "html.parser")

        # Find the price tags
        prices_sale = [
            price.text.replace("$", "")
            for price in soup.findAll(
                "span", {"class": "c-pwa-product-price__original"}
            )
        ]
        prices_non_sale = [
            price.text.replace("$", "")
            for price in soup.findAll("span", {"class": "c-pwa-product-price__current"})
        ]

        preprocess_prices = prices_sale + prices_non_sale

        # Take the mid of price ranges
        for price in preprocess_prices:
            if " – " in price:
                process = price.split(" – ")
                difference = float(process[1]) - float(process[0])
                mid_price = float(process[0]) + (0.5 * difference)
                prices.append(mid_price)
            else:
                prices.append(float(price))

    return prices
