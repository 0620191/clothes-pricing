#  Copyright Beverly Xin Chong Tan (c) 2020.

import csv

import process_prices


def main():
    results = process_prices.process_all()

    with open("./output/results.csv", mode="w") as file:
        file_writer = csv.writer(
            file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )

        # Write the product names
        names = [
            "",
            "T-Shirts",
            "",
            "Jackets & Coats",
            "",
            "Jeans",
            "",
            "Mean Average Price (USD)",
        ]
        names2 = [
            "",
            "Total Number",
            "Median Price (USD)",
            "Total Number",
            "Median Price (USD)",
            "Total Number",
            "Median Price (USD)",
            ""
        ]
        file_writer.writerow(names)
        file_writer.writerow(names2)

        for brand in sorted(results):
            prices = [
                brand,
                len(results[brand]["T-Shirts"]["data"]),
                results[brand]["T-Shirts"]["median"],
                len(results[brand]["Jackets & Coats"]["data"]),
                results[brand]["Jackets & Coats"]["median"],
                len(results[brand]["Jeans"]["data"]),
                results[brand]["Jeans"]["median"],
                round(
                    (
                        results[brand]["T-Shirts"]["median"]
                        + results[brand]["Jackets & Coats"]["median"]
                        + results[brand]["Jeans"]["median"]
                    )
                    / 3
                ),
            ]
            file_writer.writerow(prices)


if __name__ == "__main__":
    main()
