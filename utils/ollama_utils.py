# utils/ollama_utils.py
import subprocess
import json
import requests

def get_available_models():
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')
        models = [line.split()[0] for line in lines[1:]]
        return models
    except FileNotFoundError:
        print("Error: Ollama is not installed or not in your PATH.")
        return []
    except subprocess.CalledProcessError as e:
         print(f"Error running ollama list: {e}")
         return []

def query_ollama(model, prompt):
    try:
        r = requests.post('http://localhost:11434/api/generate',
                      json={
                          'model': model,
                          'prompt': prompt,
                           'stream': False
                      })
        r.raise_for_status()
        response = r.json()
        return response.get('response', '')
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama: {e}")
        return None

