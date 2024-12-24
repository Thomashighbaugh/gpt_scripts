# writing/technical_blog_post_outline_writing.py
from utils.ollama_utils import query_ollama
from utils.menu_utils import get_user_input
from utils.display_utils import display_output

def generate_technical_blog_post(model):
    topic = get_user_input("Enter the topic for the technical blog post")
    outline_prompt = f"Generate a technical blog post outline about the following topic: {topic}"
    outline_output = query_ollama(model, outline_prompt)
    if outline_output:
        display_output(outline_output, save_path="technical_blog_post_outline.txt")
        full_post_prompt = f"Expand the following outline into a full technical blog post: {outline_output}"
        full_post_output = query_ollama(model, full_post_prompt)
        if full_post_output:
            display_output(full_post_output, save_path="technical_blog_post_output.txt")
        else:
             print("No output generated for full blog post.")
    else:
        print("No output generated for outline.")
