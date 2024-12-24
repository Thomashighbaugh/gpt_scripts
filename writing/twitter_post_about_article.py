# writing/twitter_post_about_article.py
# llm_tui/writing/twitter_post_about_article.py
from utils.ollama_utils import query_ollama
from utils.menu_utils import get_user_input
from utils.display_utils import display_output

def generate_twitter_post(model):
    article_text = get_user_input("Enter the article text to create a Twitter post about")
    prompt = f"Generate a tweet about the following article: {article_text}"
    output = query_ollama(model, prompt)
    if output:
        display_output(output, save_path="twitter_post_output.txt")
    else:
        print("No output generated.")
