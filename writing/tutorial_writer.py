import os
from typing import Dict, Any

import g4f

chatbot_prompt = """
I want you to act as a technical writer who is technically competent, fully literate and has bountiful technical experience across all domains and in all relevant programming languages, technologies and computer science as an academic subject. The user will provide you with a technical object, goal or task which you are to write a blog post that serves as a tutorial for how to achieve/complete that object, goal or task. For instance, if you are provided with input such as "how to build your own NAS server at home cheaply" you would describe the means of acquiring low-cost hardware for use in the server, the process of setting up the server's operating system, the process of connecting the server to the home network and include relevant links and codeblocks as a means for the reader to do the thing. Use a technical but friendly and approachable tone while maintaining a professional voice that doesn't take itself too seriously. Make sure to creatively title the tutorial and each one of its sections, which should be numbered as one numbers the steps to complete a task. Sound as natural and organic as possible in writing the tutorial such as to make the tutorial appear as if it was written by a human being. Reason the steps out one by one in composing the tutorial.
User: <user input>
Technical Writer:"""


def get_response(conversation_history: str, user_input: str) -> Dict[str, Any]:
    prompt = chatbot_prompt.replace("<user input>", user_input)

    # Get the response from GPT-3
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": prompt}],
    )

    chatbot_response: Dict[str, Any] = response

    return chatbot_response


def main() -> None:
    conversation_history = ""
    print(f"\n<<< Please provide the subject you would like a tutorial written about:")
    while True:
        user_input = input(">>> ")
        if user_input == "exit":
            break
        chatbot_response = get_response(conversation_history, user_input)
        print(chatbot_response)
        break


if __name__ == "__main__":
    main()