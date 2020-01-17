#  Copyright Beverly Xin Chong Tan (c) 2020.

from bs4 import BeautifulSoup


def get_prices_for(files):
    prices = []
    for file in files:
        soup = BeautifulSoup(open(file), "html.parser")

        # Find the price tags
        prices_parsed = [
            float(price.text.replace("$", ""))
            for price in soup.findAll("div", {"data-test": "product-price"})
        ]
        for price in prices_parsed:
            prices.append(price)

    return prices
