from state.state import InputState, OverallState

def initial_node(state):
    """Processes the input name and generates initial response."""
    print("Estado inicial: ", state)
    return OverallState({
        "user": "Bob",
        "message": f"Hello!"
    })