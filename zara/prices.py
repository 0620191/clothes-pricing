#  Copyright Beverly Xin Chong Tan (c) 2020.

from bs4 import BeautifulSoup


def get_prices_for(file):
    # Get the URL page
    soup = BeautifulSoup(open(file), "html.parser")

    # Find the price tags
    prices = [
        float(price["data-price"].replace(" USD", ""))
        for price in soup.findAll("span", {"class": "main-price"})
    ]
    return prices
