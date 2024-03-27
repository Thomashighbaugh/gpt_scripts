import g4f


def generate_optimize_prompt(user_query):
    # Create a conversation history string
    conversation_history = "\n".join(
        [
            "Act as though you are a very experienced veteran of prompt engineering. You have a deep understanding of exactly what makes a strong, engaging, and effective prompt to query AI models for the perfect completions every time.",
            "You will be provided with a user's prompt and your task is to optimize it to insure it obtains the desired resulting assuming that the model being queried is gpt-4-turbo. Please use the following format and writing instruction when optimizing the user's provided prompt. It is very important that you follow this format exactly.",
            "0. Consider these factors in optimizing the prompt.\n Analysis: Assess the prompt using scoring criteria, which include both Constants and Variables.\n\nConstants:\n- Clarity\n- Relevance\n- Guidance\n- Understandability\n- Appropriateness\n- Completeness\n- Grammar\n- Goal Alignment\n\nVariables:\n- Innovation\n- Length\n- Format\n- Goal Orientation\n- Openness\n- Neutrality\n- Entertainment\n- Practicality\n- Timeliness \n\n Organizing: Suggest improvements for any aspects that do not score perfectly and provide justifications for these modifications.\n\n"
            "1. Analyze the input prompt and identify errors or inconsistencies.",
            "2. Highlight areas that need attention.",
            "3. Make necessary corrections to ensure clarity and coherence.",
            "4. Offer final suggestions to enhance the prompt further.",
            "5. Apply last alterations and optimize the prompt.",
            "6. Provide a summary of the changes made and a rough draft of the prompt with fixes applied.",
            "The user's prompt is:",
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
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": conversation_history}],
        )

        # Return the generated response
        return response
    except g4f.ApiException as e:
        print("An error occurred: {}".format(e))
        return ""


def main() -> None:
    print("What prompt would you like me to optimize?")
    user_query = input(">>> ")
    optimize_prompt = generate_optimize_prompt(user_query)
    print(f"Your optimized prompt is:")
    print(optimize_prompt)


if __name__ == "__main__":
    main()
