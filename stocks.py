#!/usr/bin/env python
import requests
import os

"""
Constants
"""

finnhub_base_url = "https://finnhub.io/api/v1/"
auth_header = {
    "X-Finnhub-Token": os.getenv("API_KEY")
}
stock_symbols = {
    "Apple": "AAPL",
    "Amazon": "AMZN",
    "Meta": "META",
    "Netflix": "NFLX",
    "Google": "GOOGL"
}

"""
Endpoints
"""

quote_endpoint = finnhub_base_url + "quote"

"""
Functions
"""


def make_get_request(url, params):
    return requests.get(url, headers=auth_header, params=params).json()


def get_stock_prices():
    current_prices = {}
    max_percent_change = 0
    most_volatile_stock = ""

    for company, stock_symbol in stock_symbols.items():
        params = {"symbol": stock_symbol}
        quote_response = make_get_request(quote_endpoint, params)
        current_prices[company] = quote_response["c"]

        percent_change = abs(quote_response["pc"])
        max_percent_change = max_percent_change if percent_change < max_percent_change else percent_change

        if max_percent_change == percent_change:
            most_volatile_stock = stock_symbol

    return {"current_prices": current_prices, "most_volatile_stock": most_volatile_stock}


stock_prices = get_stock_prices()

print(stock_prices["current_prices"])
print(stock_prices["most_volatile_stock"])
