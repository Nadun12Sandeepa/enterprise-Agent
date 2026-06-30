from core.llm import llm

def critic_agent(state):

    prompt = f"""
    You are a professional hedge fund critic.

    Technical:
    {state['technical']}

    Sentiment:
    {state['sentiment']}

    Orderflow:
    {state['orderflow']}

    Macro:
    {state['macro']}

    Find weaknesses in this trade.
    Detect possible fakeouts.
    """

    response = llm.invoke(prompt)

    return {
        "critique": response.content
    }