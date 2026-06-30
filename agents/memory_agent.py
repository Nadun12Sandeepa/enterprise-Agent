import json
from datetime import datetime

def memory_agent(state):

    trade = {
        "time": str(datetime.now()),
        "trade": state.get("risk", {})
    }

    with open("logs/trades.json", "a") as f:

        f.write(json.dumps(trade) + "\n")

    return state