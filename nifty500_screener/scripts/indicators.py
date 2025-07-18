import pandas_ta as ta

def compute_indicators(df):
    df['rsi'] = ta.rsi(df['Close'])
    df['sma_20'] = df['Close'].rolling(20).mean()
    df['sma_50'] = df['Close'].rolling(50).mean()
    df['sma_200'] = df['Close'].rolling(200).mean()
    df.ta.macd(close='Close', append=True)
    df.ta.bbands(close='Close', append=True)
    return df