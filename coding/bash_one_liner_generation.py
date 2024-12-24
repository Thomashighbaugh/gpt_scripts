# coding/bash_one_liner_generation.py
# llm_tui/coding/bash_one_liner_generation.py
from utils.display_utils import display_output
from utils.menu_utils import get_user_input
from utils.ollama_utils import query_ollama


def generate_bash_one_liner(model):
    user_prompt = get_user_input("Describe the bash one-liner command you want to generate")
    prompt = f"Generate a bash one-liner command based on the following description: {user_prompt}"
    output = query_ollama(model, prompt)
    if output:
        display_output(output, save_path="bash_one_liner_output.txt")
    else:
         print("No output generated.")
