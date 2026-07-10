from core.assistant import Veridion


def main() -> None:
    assistant = Veridion()

    print("Welcome to Veridion!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("> ")

        if user_input.lower() == "exit":
            break

        response = assistant.chat(user_input)

        print(response)
        print()


if __name__ == "__main__":
    main()