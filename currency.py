import requests

API_KEY = "fca_live_ntCkPpn2EfBuycwlncx51cOHq9IztK7J5OIvll57"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["GBP", "EUR", "USD", "AUD", "MXN", "PLN"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid Currency.")
        return None

while True:
    base = input("Please enter a base currency to convert ( Press q to Quit:)""\t").upper()

    if base == "Q":
        break

    data = convert_currency(base)  
    if not data:
        continue

    del data[base]      
    for ticker, value in data.items():
        print(f"{ticker}: {value}")