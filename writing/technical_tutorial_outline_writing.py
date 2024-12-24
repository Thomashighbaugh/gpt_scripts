# writing/technical_tutorial_outline_writing.py
# llm_tui/writing/technical_tutorial_outline_writing.py
from utils.ollama_utils import query_ollama
from utils.menu_utils import get_user_input
from utils.display_utils import display_output

def generate_technical_tutorial(model):
    topic = get_user_input("Enter the topic for the technical tutorial")
    outline_prompt = f"Generate a technical tutorial outline about the following topic: {topic}"
    outline_output = query_ollama(model, outline_prompt)
    if outline_output:
         display_output(outline_output, save_path="technical_tutorial_outline.txt")
         full_tutorial_prompt = f"Expand the following outline into a full technical tutorial: {outline_output}"
         full_tutorial_output = query_ollama(model, full_tutorial_prompt)
         if full_tutorial_output:
             display_output(full_tutorial_output, save_path="technical_tutorial_output.txt")
         else:
             print("No output generated for full tutorial.")
    else:
        print("No output generated for outline.")
