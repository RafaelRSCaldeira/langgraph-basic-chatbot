from graph.graph import graph

config = {"configurable": {"thread_id": "1"}}


def main():
    while True:
        try:
            user_input = input("User: ")
            result = graph.invoke({"name": user_input}, config=config)
            print(result)
        except:
            import traceback
            traceback.print_exc()
            break


if __name__ == "__main__":
    main()
