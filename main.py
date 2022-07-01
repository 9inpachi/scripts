#!/usr/bin/env python
from helpers import get_stock_prices, write_stock_details_to_file

"""
Main Program
"""

if __name__ == "__main__":
    stock_prices = get_stock_prices()
    latest_prices = stock_prices["current_prices"]
    most_volatile_stock = stock_prices["most_volatile_stock"]

    write_stock_details_to_file(most_volatile_stock)
