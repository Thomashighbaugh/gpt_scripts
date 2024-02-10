import g4f

chatbot_prompt = """
I want you to act as a mental health therapist. I will provide you with an individual looking for guidance and advice on managing their emotions, stress, anxiety and other mental health issues. You should use your knowledge of cognitive behavioral therapy, meditation techniques, mindfulness practices, and other therapeutic methods in order to create strategies that the individual can implement in order to improve their overall wellbeing while being attentive and sensitive to their feelings in the process. You will begin by asking the user how they are feeling emotionally and base your responses on the user input you receive as a result.
<conversation_history>
User: <user input>
Therapist:"""


def get_response(conversation_history: str, user_input: str) -> str:
    therapist_prompt = chatbot_prompt.replace(
        "<conversation_history>", conversation_history
    ).replace("<user input>", user_input)

    response = g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": therapist_prompt}],
    )

    # Extract the response from the response object
    chatbot_response = response

    return chatbot_response


def main() -> None:
    conversation_history = ""
    print(f"<<< Tell me, how are you feeling today?")
    while True:
        user_input = input(">>> ")
        if user_input == "exit":
            break
        chatbot_response = get_response(conversation_history, user_input)
        print(f"<<< {chatbot_response}")
        conversation_history += f"User: {user_input}\nTherapist: {chatbot_response}\n"


if __name__ == "__main__":
    main()
