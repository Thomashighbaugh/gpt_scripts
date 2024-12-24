# main.py
# llm_tui/main.py
import sys

from utils.ollama_utils import get_available_models
from utils.menu_utils import display_menu
from coding import code_generation, code_explanation, code_optimization, bash_one_liner_generation
from prompting import prompt_generation, prompt_optimization, image_prompt_generation, image_prompt_optimization
from job_hunting import cover_letter_generation, resume_optimization, interview_question_generation
from writing import twitter_post_about_article, linkedin_post_about_article, technical_blog_post_outline_writing, technical_tutorial_outline_writing

def coding_menu(selected_model):
    options = ["Code Generation", "Code Explanation", "Code Optimization", "Bash One-Liner Generation"]
    selected_option_index = display_menu(options)
    if selected_option_index == 0:
         code_generation.generate_code(selected_model)
    elif selected_option_index == 1:
        code_explanation.explain_code(selected_model)
    elif selected_option_index == 2:
        code_optimization.optimize_code(selected_model)
    elif selected_option_index == 3:
        bash_one_liner_generation.generate_bash_one_liner(selected_model)


def prompting_menu(selected_model):
    options = ["Prompt Generation", "Prompt Optimization", "Image Prompt Generation", "Image Prompt Optimization"]
    selected_option_index = display_menu(options)
    if selected_option_index == 0:
        prompt_generation.generate_prompt(selected_model)
    elif selected_option_index == 1:
        prompt_optimization.optimize_prompt(selected_model)
    elif selected_option_index == 2:
        image_prompt_generation.generate_image_prompt(selected_model)
    elif selected_option_index == 3:
        image_prompt_optimization.optimize_image_prompt(selected_model)

def job_hunting_menu(selected_model):
    options = ["Cover Letter Generation", "Resume Optimization", "Interview Question Generation"]
    selected_option_index = display_menu(options)
    if selected_option_index == 0:
        cover_letter_generation.generate_cover_letter(selected_model)
    elif selected_option_index == 1:
        resume_optimization.optimize_resume(selected_model)
    elif selected_option_index == 2:
        interview_question_generation.generate_interview_questions(selected_model)

def writing_menu(selected_model):
    options = ["Twitter Post About Article", "LinkedIn Post About Article", "Technical Blog Post Outline & Writing", "Technical Tutorial Outline & Writing"]
    selected_option_index = display_menu(options)
    if selected_option_index == 0:
        twitter_post_about_article.generate_twitter_post(selected_model)
    elif selected_option_index == 1:
        linkedin_post_about_article.generate_linkedin_post(selected_model)
    elif selected_option_index == 2:
        technical_blog_post_outline_writing.generate_technical_blog_post(selected_model)
    elif selected_option_index == 3:
        technical_tutorial_outline_writing.generate_technical_tutorial(selected_model)

def main():
    models = get_available_models()
    if not models:
        print("No Ollama models found. Please ensure Ollama is installed and running.")
        sys.exit(1)

    selected_model_index = display_menu(models)
    if selected_model_index is None:
        print("Invalid model selection.")
        sys.exit(1)
    selected_model = models[selected_model_index]

    categories = ["Coding", "Prompting", "Job Hunting", "Writing"]
    selected_category_index = display_menu(categories)
    if selected_category_index is None:
        print("Invalid category selection.")
        sys.exit(1)

    if selected_category_index == 0:
        coding_menu(selected_model)
    elif selected_category_index == 1:
        prompting_menu(selected_model)
    elif selected_category_index == 2:
        job_hunting_menu(selected_model)
    elif selected_category_index == 3:
        writing_menu(selected_model)


if __name__ == "__main__":
    main()
