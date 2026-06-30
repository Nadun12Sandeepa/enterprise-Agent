import ccxt
import pandas as pd

exchange = ccxt.binance()

def fetch_market_data(symbol, timeframe, limit):

    candles = exchange.fetch_ohlcv(
        symbol,
        timeframe=timeframe,
        limit=limit
    )

    df = pd.DataFrame(
        candles,
        columns=[
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]
    )

    return df