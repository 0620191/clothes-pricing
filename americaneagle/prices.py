#  Copyright Beverly Xin Chong Tan (c) 2020.

from bs4 import BeautifulSoup


def get_prices_for(file):
    soup = BeautifulSoup(open(file), "html.parser")

    # Find the price tags
    prices = [
        float(price.text.replace("$", "").replace(" USD", ""))
        for price in soup.findAll(
            "div", {"class": "product-list-price product-list-price-on-sale ember-view"}
        )
    ]
    return prices
