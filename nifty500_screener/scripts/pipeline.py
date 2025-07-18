from scripts.company_list import get_nifty500_symbols
from scripts.data_fetcher import fetch_technical_data
from scripts.indicators import compute_indicators
from scripts.fundamentals_scraper import scrape_fundamentals
from scripts.signals import generate_signal
from scripts.scoring import score_stock
from scripts.alerts import send_buy_alerts

import pandas as pd
import os

def run_pipeline():
    symbols = get_nifty500_symbols()[:10]
    results = []

    for sym in symbols:
        data = fetch_technical_data(sym)
        if data is None or data.empty:
            continue

        data = compute_indicators(data)
        latest = data.iloc[-1]
        fundamentals = scrape_fundamentals(sym)

        signal = generate_signal(latest, fundamentals)
        score = score_stock(fundamentals, latest)

        results.append({
            'Symbol': sym,
            'Close': round(latest['Close'], 2),
            'RSI': round(latest['rsi'], 2),
            'PE': fundamentals.get('PE'),
            'ROE': fundamentals.get('ROE'),
            'DebtEquity': fundamentals.get('DebtEquity'),
            'Signal': signal,
            'Score': score
        })

    df = pd.DataFrame(results)
    os.makedirs('exports', exist_ok=True)
    df.to_csv('exports/final_screener.csv', index=False)
    print(df)

    send_buy_alerts(results)