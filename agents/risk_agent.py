import json

from core.config import (
    ACCOUNT_BALANCE,
    RISK_PER_TRADE
)

from tools.risk_tools import calculate_position_size

def risk_agent(state):

    try:
        decision = state["strategy"]["decision"]

        strategy = json.loads(decision)

        size = calculate_position_size(
            ACCOUNT_BALANCE,
            RISK_PER_TRADE,
            strategy["entry"],
            strategy["stop_loss"]
        )

        strategy["position_size"] = size

        return {
            "risk": strategy
        }

    except Exception as e:

        return {
            "risk": {
                "error": str(e)
            }
        }