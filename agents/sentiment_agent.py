from core.llm import llm
from tools.sentiment_tools import fake_news

def sentiment_agent(state):

    news = fake_news()

    prompt = f"""
    Analyze the market sentiment.

    News:
    {news}

    Return:
    - bullish/bearish
    - confidence score
    - short explanation
    """

    response = llm.invoke(prompt)

    return {
        "sentiment": {
            "analysis": response.content
        }
    }