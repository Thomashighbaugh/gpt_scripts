# coding/code_explanation.py
# llm_tui/coding/code_explanation.py
from utils.ollama_utils import query_ollama
from utils.menu_utils import get_user_input
from utils.display_utils import display_output

def explain_code(model):
    code_snippet = get_user_input("Enter the code you want to explain")
    prompt = f"Explain the following code snippet: {code_snippet}"
    output = query_ollama(model, prompt)
    if output:
        display_output(output, save_path="code_explanation_output.txt")
    else:
         print("No output generated.")
