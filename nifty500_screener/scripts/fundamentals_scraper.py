import requests
from bs4 import BeautifulSoup

def scrape_fundamentals(symbol):
    try:
        url = f"https://www.screener.in/company/{symbol}/consolidated/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        ratios = {}
        pe = soup.find(text="P/E").find_next('span').text.strip()
        ratios['PE'] = float(pe) if pe.replace('.', '', 1).isdigit() else None

        roe = soup.find(text="ROE").find_next('span').text.strip('%')
        ratios['ROE'] = float(roe) if roe.replace('.', '', 1).isdigit() else None

        de = soup.find(text="Debt to equity").find_next('span').text.strip()
        ratios['DebtEquity'] = float(de) if de.replace('.', '', 1).isdigit() else None

        return ratios
    except Exception as e:
        print(f"Error scraping fundamentals for {symbol}: {e}")
        return {"PE": None, "ROE": None, "DebtEquity": None}