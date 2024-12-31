import openai
import json

# Load configuration
with open("config.json") as config_file:
    config = json.load(config_file)

openai.api_key = config["openai_api_key"]

def ask_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    print(ask_chatgpt(user_input))
