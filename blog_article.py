import os
from typing import List, Dict
import g4f  # Assuming 'g4f' is the correct import, but please verify

chatbot_prompt = """
I would like to assume the role of a technical blogger. The user will provide you with a topic, and you will compose an informative and objective article of no less than 1,500 words about that topic. Your article should provide a comprehensive analysis of the key factors that impact the provided topic, including any relevant keywords or subjects relating to the topic provided. To make your article informative and engaging, be sure to discuss the tradeoffs involved in balancing different factors and explore the challenges associated with different approaches. Your article should also highlight the importance of considering the impact when making decisions about the provided topic. Finally, your article should be written in an informative and objective tone that appears to be human-written and is accessible to a general audience unfamiliar with the topic. Be sure to creatively title the blog post and each of its sections. Please format your output as GitHub-flavored Markdown and include a table of contents.
<conversation_history>
User: <user input>
Blogger:"""


def get_response(conversation_history: str, user_input: str) -> Dict:
    prompt = chatbot_prompt.replace("<user input>", user_input)

    # Get the response from GPT-3
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": prompt}],
    )

    return response


def main():
    conversation_history: str = ""
    print(f"Please provide a topic for an informative blog post.")
    while True:
        user_input = input("> ")
        if user_input == "exit":
            break
        chatbot_response = get_response(conversation_history, user_input)
        print(f"Blogger: {chatbot_response}")
        break


if __name__ == "__main__":
    main()
