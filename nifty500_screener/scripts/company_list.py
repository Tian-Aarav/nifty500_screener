import pandas as pd

def get_nifty500_symbols():
    url = 'https://en.wikipedia.org/wiki/NIFTY_500'
    try:
        tables = pd.read_html(url)
        df = tables[0]
        return df['Symbol'].dropna().tolist()
    except Exception as e:
        print(f"Error fetching NIFTY 500: {e}")
        return []