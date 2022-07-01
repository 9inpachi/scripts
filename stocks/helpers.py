import requests
import constants


"""
Helper Functions
"""


# Time Complexity = O(1)
# Space Complexity = O(1)
def make_get_request(url, params):
    """
    Make get request to a URL with specified parameters.

    Arguments:
        url: URL to send the request to.
        params: Parameters of the get request.
    Returns:
        Response of the request as a JSON dictionary.
    """
    try:
        return requests.get(url, headers=constants.auth_header, params=params).json()
    except requests.exceptions.RequestException as exception:
        raise SystemExit(exception)


# Time Complexity = O(stock_symbols.size()) = O(n)
# Space Complexity = O(stock_symbols.size()) = O(n)
def get_tech_stocks():
    """
    Get current price of tech stocks and details of the most volatile stock.

    Returns:
        current_prices: Current prices of all tech stocks.
        most_volatile_stock: Details of the most volatile stock among all tech stocks.
    """
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

    return current_prices,  most_volatile_stock


# Time Complexity = O(1)
# Space Complexity = O(1)
def write_stock_details_to_csv(filename, stock_details):
    """
    Write details of a stock to a file.

    Arguments:
        filename: Name of the csv file (without extension) to write the stock details to.
        stock_details: Dictionary containing the details of the stock.
    """
    stock_details_mapped = {
        "stock_symbol": stock_details["symbol"],
        "percentage_change": str(stock_details["dp"]),
        "current_price": str(stock_details["c"]),
        "last_close_price": str(stock_details["pc"])
    }

    headers = stock_details_mapped.keys()
    values = stock_details_mapped.values()

    file = open(filename + ".csv", "w")
    file.writelines([
        ",".join(headers),
        "\n",
        ", ".join(values)
    ])
    file.close()
