from core.llm import llm

def strategy_agent(state):

    prompt = f"""
    You are an elite quantitative trader.

    Technical:
    {state['technical']}

    Sentiment:
    {state['sentiment']}

    Orderflow:
    {state['orderflow']}

    Macro:
    {state['macro']}

    Critique:
    {state['critique']}

    Create final trading decision.

    Return JSON:
    {{
        "action": "BUY/SELL/HOLD",
        "entry": number,
        "stop_loss": number,
        "take_profit": number,
        "confidence": number
    }}
    """

    response = llm.invoke(prompt)

    return {
        "strategy": {
            "decision": response.content
        }
    }