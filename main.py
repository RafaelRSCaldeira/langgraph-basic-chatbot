from graph.graph import graph

config = {"configurable": {"thread_id": "1"}}

def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}, config=config):
        for value in event.values():
            print("Assistant:", value["messages"][-1])

def main():
    while True:
        try:
            user_input = input("User: ")
            stream_graph_updates(user_input)
        except:
            import traceback
            traceback.print_exc()
            break


if __name__ == "__main__":
    main()
