import requests
import constants

"""
Helper Functions
"""

def make_get_request(url, params):
    return requests.get(url, headers=constants.auth_header, params=params).json()

def get_stock_prices():
    current_prices = {}
    most_volatile_stock = {}
    max_percent_change = 0

    for company, stock_symbol in constants.stock_symbols.items():
        req_params = {"symbol": stock_symbol}
        quote_response = make_get_request(constants.quote_endpoint, req_params)
        current_prices[company] = quote_response["c"]

        percent_change = abs(quote_response["dp"])
        max_percent_change = max(max_percent_change, percent_change)

        if max_percent_change == percent_change:
            most_volatile_stock = quote_response
            most_volatile_stock["symbol"] = stock_symbol

    return {"current_prices": current_prices, "most_volatile_stock": most_volatile_stock}

def write_stock_details_to_file(filename, stock_details):
    stock_details_mapped = {
        "stock_symbol": stock_details["symbol"],
        "percentage_change": str(stock_details["dp"]),
        "current_price": str(stock_details["c"]),
        "last_close_price": str(stock_details["pc"])
    }

    headers = stock_details_mapped.keys()
    values = stock_details_mapped.values()

    file = open(filename, "w")
    file.writelines([
        ",".join(headers),
        "\n",
        ",".join(values)
    ])
    file.close()
