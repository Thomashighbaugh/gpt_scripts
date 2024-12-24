# prompting/prompt_generation.py
from utils.ollama_utils import query_ollama
from utils.menu_utils import get_user_input
from utils.display_utils import display_output

def generate_prompt(model):
    user_input = get_user_input("Describe the kind of prompt you want to generate")
    prompt = f"Generate a prompt based on the following description: {user_input}"
    output = query_ollama(model, prompt)
    if output:
       display_output(output, save_path="prompt_generation_output.txt")
    else:
        print("No output generated.")
