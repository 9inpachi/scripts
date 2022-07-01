#!/usr/bin/env python
from helpers import get_tech_stocks, write_stock_details_to_csv


"""
Main Program
"""

if __name__ == "__main__":
    stock_prices = get_tech_stocks()

    # `latest_prices` contains the current price of each company's stock. It's not used anywhere.
    latest_prices, most_volatile_stock = stock_prices

    filename = "most_volatile_stock"
    write_stock_details_to_csv(filename, most_volatile_stock)

    print("Most volatile stock was: " + most_volatile_stock["symbol"])
    print("Data written to: ./" + filename + ".csv")
