import ta

def add_indicators(df):

    df["rsi"] = ta.momentum.RSIIndicator(
        close=df["close"]
    ).rsi()

    macd = ta.trend.MACD(df["close"])

    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()

    df["ema20"] = ta.trend.EMAIndicator(
        df["close"],
        window=20
    ).ema_indicator()

    df["ema50"] = ta.trend.EMAIndicator(
        df["close"],
        window=50
    ).ema_indicator()

    bb = ta.volatility.BollingerBands(df["close"])

    df["bb_upper"] = bb.bollinger_hband()
    df["bb_lower"] = bb.bollinger_lband()

    return df