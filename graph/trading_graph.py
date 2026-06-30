from langgraph.graph import StateGraph, END

from core.state import TradingState

from agents.market_agent import market_agent
from agents.technical_agent import technical_agent
from agents.sentiment_agent import sentiment_agent
from agents.orderflow_agent import orderflow_agent
from agents.macro_agent import macro_agent
from agents.critic_agent import critic_agent
from agents.strategy_agent import strategy_agent
from agents.risk_agent import risk_agent
from agents.execution_agent import execution_agent
from agents.memory_agent import memory_agent

workflow = StateGraph(TradingState)

workflow.add_node("market", market_agent)

workflow.add_node("technical", technical_agent)

workflow.add_node("sentiment", sentiment_agent)

workflow.add_node("orderflow", orderflow_agent)

workflow.add_node("macro", macro_agent)

workflow.add_node("critic", critic_agent)

workflow.add_node("strategy", strategy_agent)

workflow.add_node("risk", risk_agent)

workflow.add_node("execution", execution_agent)

workflow.add_node("memory", memory_agent)

workflow.set_entry_point("market")

workflow.add_edge("market", "technical")

workflow.add_edge("technical", "sentiment")

workflow.add_edge("sentiment", "orderflow")

workflow.add_edge("orderflow", "macro")

workflow.add_edge("macro", "critic")

workflow.add_edge("critic", "strategy")

workflow.add_edge("strategy", "risk")

workflow.add_edge("risk", "execution")

workflow.add_edge("execution", "memory")

workflow.add_edge("memory", END)

graph = workflow.compile()