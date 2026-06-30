from tools.market_tools import fetch_market_data
from core.config import SYMBOL, TIMEFRAME, LIMIT

def market_agent(state):

    df = fetch_market_data(
        SYMBOL,
        TIMEFRAME,
        LIMIT
    )

    return {
        "market": {
            "data": df
        }
    }