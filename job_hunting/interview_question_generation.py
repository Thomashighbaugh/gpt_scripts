# job_hunting/interview_question_generation.py
from utils.ollama_utils import query_ollama
from utils.menu_utils import get_user_input
from utils.display_utils import display_output

def generate_interview_questions(model):
    user_input = get_user_input("Enter details about the interview (e.g., job title, company, role)")
    prompt = f"Generate interview questions based on the following details: {user_input}"
    output = query_ollama(model, prompt)
    if output:
        display_output(output, save_path="interview_questions_output.txt")
    else:
        print("No output generated.")
