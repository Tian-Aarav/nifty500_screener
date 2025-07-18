def generate_signal(row, fundamentals):
    rsi = row.get('rsi', 50)
    pe = fundamentals.get('PE', 25)

    if rsi < 30 and pe < 20:
        return 'BUY'
    elif rsi > 70:
        return 'SELL'
    return 'HOLD'