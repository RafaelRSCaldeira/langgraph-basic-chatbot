from state.state import OverallState, OutputState

def final_node(state: OverallState) -> OutputState:
    """Ends conversation"""
    print("Estado final: ", state)
    return OutputState({
        "answer": "Resposta"
    })