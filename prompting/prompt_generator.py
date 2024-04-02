import g4f


def generate_optimize_prompt(user_query, outcome, model, context):
    # Create a conversation history string
    conversation_history = "\n".join(
        [
            "Act as though you are a very experienced veteran of prompt engineering. You have a deep understanding of exactly what makes a strong, engaging, and effective prompt to query AI models for the perfect completions every time.",
            "Input:",
            f"User's desired prompt: {user_query}",
            f"Desired outcome: {outcome} ",
            f"Target AI model: {model}",
            f"Additional information: {context}",
            "Instructions:",
            "Based on the provided information, generate an optimized prompt that is tailored to the target AI model and maximizes the chances of achieving the desired outcome. Consider the following factors:",
            "Clarity and conciseness: Ensure the prompt is clear, concise, and free of ambiguity.",
            "Relevance: Make sure the prompt is relevant to the capabilities of the target AI model.",
            "Specificity: Include specific details and instructions to guide the AI towards the desired outcome.",
            "Context: Provide relevant context to help the AI understand the user's intent.",
            "Style and tone: Adjust the style and tone of the prompt to match the desired output.",
            "Output:",
            "The optimized prompt, ready to be used with the target AI model.",
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
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": conversation_history}],
        )

        # Return the generated response
        return response
    except g4f.ApiException as e:
        print("An error occurred: {}".format(e))
        return ""


def main() -> None:
    print("What prompt would you like me to make?")
    user_query = input(">>> ")
    print("What is the desired outcome of using this prompt?")
    outcome = input(">>> ")
    print("What AI model will you be using?")
    model = input(">>> ")
    print("Is there any additional context or information you would like to provide?")
    context = input(">>> ")
    optimize_prompt = generate_optimize_prompt(user_query, outcome, model, context)
    print("Your optimized prompt is:")
    print(optimize_prompt)


if __name__ == "__main__":
    main()
