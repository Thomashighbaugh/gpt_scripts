# prompting/image_prompt_optimization.py
from utils.ollama_utils import query_ollama
from utils.menu_utils import get_user_input
from utils.display_utils import display_output

def optimize_image_prompt(model):
    user_prompt = get_user_input("Enter the image prompt you would like to optimize")
    prompt = f"Optimize the following image generation prompt: {user_prompt}"
    output = query_ollama(model, prompt)
    if output:
        display_output(output, save_path="image_prompt_optimization_output.txt")
    else:
        print("No output generated.")
