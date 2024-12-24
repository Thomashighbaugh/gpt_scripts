# job_hunting/cover_letter_generation.py
# llm_tui/job_hunting/cover_letter_generation.py
from utils.ollama_utils import query_ollama
from utils.menu_utils import get_user_input
from utils.display_utils import display_output

def generate_cover_letter(model):
    user_input = get_user_input("Enter details for generating a cover letter (e.g., job description, your experience)")
    prompt = f"Generate a cover letter based on the following details: {user_input}"
    output = query_ollama(model, prompt)
    if output:
        display_output(output, save_path="cover_letter_output.txt")
    else:
        print("No output generated.")
