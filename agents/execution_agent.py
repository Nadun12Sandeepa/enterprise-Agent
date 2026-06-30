from rich import print

def execution_agent(state):

    risk = state["risk"]

    print("\n[green]EXECUTING TRADE[/green]\n")

    print(risk)

    return {
        "execution": {
            "status": "EXECUTED"
        }
    }