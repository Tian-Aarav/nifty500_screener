import yfinance as yf

def fetch_technical_data(symbol):
    try:
        data = yf.download(f"{symbol}.NS", period='6mo', interval='1d', progress=False)
        return data
    except Exception as e:
        print(f"Failed to fetch data for {symbol}: {e}")
        return None