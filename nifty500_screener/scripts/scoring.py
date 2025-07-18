def score_stock(fundamentals, technicals):
    score = 0

    if fundamentals.get('PE') and fundamentals['PE'] < 20:
        score += 10
    if fundamentals.get('ROE') and fundamentals['ROE'] > 15:
        score += 10
    if fundamentals.get('DebtEquity') and fundamentals['DebtEquity'] < 1:
        score += 5
    if technicals.get('rsi') and technicals['rsi'] < 30:
        score += 10

    return score