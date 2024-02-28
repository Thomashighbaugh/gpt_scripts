import g4f

def generate_bash_oneliner(user_query):
    # Create a conversation history string
    conversation_history = "\n".join(
        [
            "Act as though you are a very experienced veteran of the Linux command line. You have a deep understanding of exactly what makes a strong, engaging, and compelling bash one-liner.",
            "Please use the following format and writing instruction when creating the bash one-liner. It is very important that you follow this format exactly.",
            "1. The one-liner should be a single line of bash code.",
            "2. The one-liner should be able to be copied and pasted into a terminal and run without any errors.",
            "3. The one-liner should be able to be understood by a novice Linux user.",
            "4. The one-liner should be able to be used to accomplish a specific task.",
            f"User: {user_query}",
        ]
    )

    # Get the response from the model
    response = get_response(conversation_history)

    return response


def get_response(conversation_history: str) -> str:
    api_instance = g4f.ChatCompletion()
    try:
        # Call the API with the specified parameters
        response = api_instance.create(
            model="gpt-4",
            messages=[{"role": "system", "content": conversation_history}],
        )

        # Return the generated response
        return response
    except g4f.ApiException as e:
        print("An error occurred: {}". format(e))
        return ""


def main() -> None:
    print("What bash one-liner are you looking for?")
    user_query = input(">>> ")
    bash_oneliner = generate_bash_oneliner(user_query)
    print(f"Here is a bash one-liner that {user_query}:")
    print(bash_oneliner)


if __name__ == "__main__":
    main()
