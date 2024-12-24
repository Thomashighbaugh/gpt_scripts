# prompting/prompt_optimization.py
# llm_tui/prompting/prompt_optimization.py
from utils.ollama_utils import query_ollama
from utils.menu_utils import get_user_input
from utils.display_utils import display_output

def optimize_prompt(model):
    user_prompt = get_user_input("Enter the prompt you would like to optimize")
    prompt = f"Optimize the following prompt: {user_prompt}"
    output  = query_ollama(model, prompt)
    if output:
        display_output(output, save_path="prompt_optimization_output.txt")
    else:
        print("No output generated.")
