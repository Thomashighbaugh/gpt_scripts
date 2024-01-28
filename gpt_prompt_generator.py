import os
import g4f
from typing import List

chatbot_prompt: str = """
I want you to become my Prompt Creator. Your goal is to help me craft the best possible prompt for my needs. The prompt will be used by you and/or ChatGPT. You will follow the following process: 
        1. Your first response will be to ask me what the prompt should be about. I will provide my answer, but we will need to improve it through continual iterations by going through the next steps. 
        2. Based on my input, you will generate 3 sections each spaced apart by 2 blank lines. 
            a) Revised prompt (provide your rewritten prompt. It should be clear, concise, and easily understood by you)
            b) Suggestions (provide suggestions on what details to include in the prompt to improve it)
            c) Questions (ask any relevant questions pertaining to what additional information is needed from me to improve the prompt)
        3. We will continue this iterative process with me providing additional information to you and you updating the prompt in the Revised prompt section until it's complete, which I will indicate to you with the keyword DONE.

<conversation_history>
User: <user input>
Prompt Generator:"""


def get_response(user_input: str) -> str:
    prompt: str = chatbot_prompt.replace("<user input>", user_input)

    # Get the response from GPT-3
    response: str = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": prompt}],
    )

    # Return the response as is, chat completions are already formatted as strings by default
    chatbot_response: str = response

    return chatbot_response


def main() -> None:
    conversation_history: str = ""
    print(
        f"<<< Please provide a description of the prompt you would like me to generate."
    )
    while True:
        user_input: str = input(">>> ")
        if user_input == "exit":
            break
        chatbot_response: str = get_response(user_input)
        print(f"<<< Generated Prompt: {chatbot_response}")


main()

