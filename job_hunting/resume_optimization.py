# job_hunting/resume_optimization.py
# llm_tui/job_hunting/resume_optimization.py
from utils.ollama_utils import query_ollama
from utils.menu_utils import get_user_input
from utils.display_utils import display_output

def optimize_resume(model):
    resume_text = get_user_input("Enter your resume text for optimization")
    prompt = f"Optimize the following resume: {resume_text}"
    output = query_ollama(model, prompt)
    if output:
        display_output(output, save_path="resume_optimization_output.txt")
    else:
        print("No output generated.")
