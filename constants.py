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
