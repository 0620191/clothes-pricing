#  Copyright Beverly Xin Chong Tan (c) 2020.

import statistics

from abercrombie import prices as abercrombie
from abercrombie import urls as af_url
from americaneagle import prices as ae
from americaneagle import urls as ae_url
from hollister import prices as hollister
from hollister import urls as hol_url
from nike import prices as nike
from nike import urls as nike_urls
from urbanoutfitters import prices as uo
from urbanoutfitters import urls as uo_url
from zara import prices as zara
from zara import urls as zara_url


def process_all():
    # Zara prices
    zara_jackets = zara.get_prices_for(zara_url.jackets)
    zara_coats = zara.get_prices_for(zara_url.coats)
    zara_tshirts = zara.get_prices_for(zara_url.tshirts)
    zara_jeans = zara.get_prices_for(zara_url.jeans)

    # A&F
    ab_coats = abercrombie.get_prices_for(af_url.coats)
    ab_jackets = abercrombie.get_prices_for(af_url.jackets)
    ab_tshirts = abercrombie.get_prices_for(af_url.tshirts)
    ab_jeans = abercrombie.get_prices_for(af_url.jeans)

    # Hollister
    hol_jacketscoats = hollister.get_prices_for(hol_url.jacketscoats)
    hol_tshirts = hollister.get_prices_for(hol_url.tshirts)
    hol_jeans = hollister.get_prices_for(hol_url.jeans)

    # American Eagle
    ae_tshirts = ae.get_prices_for(ae_url.tshirts)
    ae_jeans = ae.get_prices_for(ae_url.jeans)
    ae_jackets_coats = ae.get_prices_for(ae_url.jacketscoats)

    # Urban Outfitters
    uo_jacketscoats_files = [
        uo_url.jacketscoats,
        uo_url.jacketscoats2,
        uo_url.jacketscoats3,
    ]
    uo_tshirts_files = [uo_url.tshirts, uo_url.tshirts2, uo_url.tshirts3]
    uo_jeans_files = [uo_url.jeans, uo_url.jeans2]
    uo_jacketscoats = uo.get_prices_for(uo_jacketscoats_files)
    uo_tshirts = uo.get_prices_for(uo_tshirts_files)
    uo_jeans = uo.get_prices_for(uo_jeans_files)

    # Nike
    nike_jacketscoats_files = [nike_urls.coats, nike_urls.coats2]
    nike_jackets_coats = nike.get_prices_for(nike_jacketscoats_files)
    nike_tshirts = nike.get_prices_for([nike_urls.tshirts])
    nike_jeans = nike.get_prices_for([nike_urls.jeans])

    results = {
        "Zara": {
            "Jackets & Coats": {
                "data": zara_jackets + zara_coats,
                "mean": round(statistics.mean(zara_jackets + zara_coats), 2),
                "median": round(statistics.median(zara_jackets + zara_coats), 2),
            },
            "T-Shirts": {
                "data": zara_tshirts,
                "mean": round(statistics.mean(zara_tshirts), 2),
                "median": round(statistics.median(zara_tshirts), 2),
            },
            "Jeans": {
                "data": zara_jeans,
                "mean": round(statistics.mean(zara_jeans), 2),
                "median": round(statistics.median(zara_jeans), 2),
            },
        },
        "Abercrombie & Fitch": {
            "Jackets & Coats": {
                "data": ab_jackets + ab_coats,
                "mean": round(statistics.mean(ab_jackets + ab_coats), 2),
                "median": round(statistics.median(ab_jackets + ab_coats), 2),
            },
            "T-Shirts": {
                "data": ab_tshirts,
                "mean": round(statistics.mean(ab_tshirts), 2),
                "median": round(statistics.median(ab_tshirts), 2),
            },
            "Jeans": {
                "data": ab_jeans,
                "mean": round(statistics.mean(ab_jeans), 2),
                "median": round(statistics.median(ab_jeans), 2),
            },
        },
        "Hollister": {
            "Jackets & Coats": {
                "data": hol_jacketscoats,
                "mean": round(statistics.mean(hol_jacketscoats), 2),
                "median": round(statistics.median(hol_jacketscoats), 2),
            },
            "T-Shirts": {
                "data": hol_tshirts,
                "mean": round(statistics.mean(hol_tshirts), 2),
                "median": round(statistics.median(hol_tshirts), 2),
            },
            "Jeans": {
                "data": hol_jeans,
                "mean": round(statistics.mean(hol_jeans), 2),
                "median": round(statistics.median(hol_jeans), 2),
            },
        },
        "American Eagle": {
            "Jackets & Coats": {
                "data": ae_jackets_coats,
                "mean": round(statistics.mean(ae_jackets_coats), 2),
                "median": round(statistics.median(ae_jackets_coats), 2),
            },
            "T-Shirts": {
                "data": ae_tshirts,
                "mean": round(statistics.mean(ae_tshirts), 2),
                "median": round(statistics.median(ae_tshirts), 2),
            },
            "Jeans": {
                "data": ae_jeans,
                "mean": round(statistics.mean(ae_jeans), 2),
                "median": round(statistics.median(ae_jeans), 2),
            },
        },
        "Urban Outfitters": {
            "Jackets & Coats": {
                "data": uo_jacketscoats,
                "mean": round(statistics.mean(uo_jacketscoats), 2),
                "median": round(statistics.median(uo_jacketscoats), 2),
            },
            "T-Shirts": {
                "data": uo_tshirts,
                "mean": round(statistics.mean(uo_tshirts), 2),
                "median": round(statistics.median(uo_tshirts), 2),
            },
            "Jeans": {
                "data": uo_jeans,
                "mean": round(statistics.mean(uo_jeans), 2),
                "median": round(statistics.median(uo_jeans), 2),
            },
        },
        "Nike": {
            "Jackets & Coats": {
                "data": nike_jackets_coats,
                "mean": round(statistics.mean(nike_jackets_coats), 2),
                "median": round(statistics.median(nike_jackets_coats), 2),
            },
            "T-Shirts": {
                "data": nike_tshirts,
                "mean": round(statistics.mean(nike_tshirts), 2),
                "median": round(statistics.median(nike_tshirts), 2),
            },
            "Jeans": {
                "data": nike_jeans,
                "mean": round(statistics.mean(nike_jeans), 2),
                "median": round(statistics.median(nike_jeans), 2),
            },
        },
    }
    return results
