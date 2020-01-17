#  Copyright Beverly Xin Chong Tan (c) 2020.

from bs4 import BeautifulSoup


def get_prices_for(file):
    # Get the URL page
    soup = BeautifulSoup(open(file), "html.parser")

    # Find the price tags for non-sale items
    non_sale_prices = [
        price.text
        for price in soup.findAll(
            "span", {"class": "product-price-text ds-override", "data-state": ""}
        )
    ]
    sale_prices = [
        price.text
        for price in soup.findAll(
            "span",
            {"class": "product-price-text ds-override", "data-state": "original"},
        )
    ]
    prices = non_sale_prices + sale_prices

    prices = [float(price.replace("\n\t$", "").replace("\n", "")) for price in prices]
    return prices
