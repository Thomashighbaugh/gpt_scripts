# coding/code_generation.py
# llm_tui/coding/code_generation.py
from utils.ollama_utils import query_ollama
from utils.menu_utils import get_user_input
from utils.display_utils import display_output

def generate_code(model):
    user_prompt = get_user_input("Describe the code you want to generate")
    prompt = f"Generate code based on the following description: {user_prompt}"
    output = query_ollama(model, prompt)
    if output:
        display_output(output, save_path="code_generation_output.txt")
    else:
         print("No output generated.")
