from tools.indicators import add_indicators

def technical_agent(state):

    df = state["market"]["data"]

    df = add_indicators(df)

    latest = df.iloc[-1]

    signal = "HOLD"

    if latest["rsi"] < 30:
        signal = "BUY"

    elif latest["rsi"] > 70:
        signal = "SELL"

    if latest["ema20"] > latest["ema50"]:
        trend = "BULLISH"
    else:
        trend = "BEARISH"

    return {
        "technical": {
            "signal": signal,
            "trend": trend,
            "rsi": round(latest["rsi"], 2),
            "price": float(latest["close"])
        }
    }