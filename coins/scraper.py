import requests
import re
from bs4 import BeautifulSoup
import json


def scrape():
    try:
        data = requests.get("https://coinmarketcap.com/")
        if data.status_code == 200:
            soup = BeautifulSoup(data.text, 'html.parser')
            coins_table = soup.find("table", attrs={
                "class": "keBvNC"
            })
            coins_tbody = coins_table.find("tbody")
            coins_tr = coins_tbody.find_all("tr")
            coins_span = [td.find_all("td")[3].find("span") for td in coins_tr[1:11]]
            coins_p = [p.find_all("p", attrs={'class': 'coin-item-name'}) for p in coins_tr[1:11]]
            price = re.findall(r"\$[\d\.\,]+", str(coins_span))
            names = re.findall(r"(?<=>)[A-Za-z]+", str(coins_p))
            return json.dumps({"message": "success", "data": list(zip(names, price))})
        return json.dumps({"message": "connection error", "status": data.status_code})
    except Exception as e:
        return json.dumps({"message": "invalid url", "error": str(e)})
