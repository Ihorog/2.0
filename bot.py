import openai
import json
import os
import shutil

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

def create_file(file_path, content=''):
    with open(file_path, 'w') as file:
        file.write(content)

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        return f"Файл {file_path} не знайдено."

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        return f"Файл {file_path} видалено."
    else:
        return f"Файл {file_path} не знайдено."

def create_directory(directory_path):
    os.makedirs(directory_path, exist_ok=True)
    return f"Директорію {directory_path} створено."

def delete_directory(directory_path):
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
        return f"Директорію {directory_path} видалено."
    else:
        return f"Директорію {directory_path} не знайдено."

def list_directory(directory_path):
    if os.path.exists(directory_path):
        return os.listdir(directory_path)
    else:
        return f"Директорію {directory_path} не знайдено."

if __name__ == "__main__":
    while True:
        user_input = input("Введіть команду: ")
        command, *args = user_input.split()

        if command == 'create_file' and args:
            file_name = args[0]
            content = ' '.join(args[1:]) if len(args) > 1 else ''
            create_file(file_name, content)
            print(f"Файл {file_name} створено з вмістом: {content}")
        elif command == 'read_file' and args:
            file_name = args[0]
            content = read_file(file_name)
            print(f"Вміст файлу {file_name}:\n{content}")
        elif command == 'write_file' and args:
            file_name = args[0]
            content = ' '.join(args[1:]) if len(args) > 1 else ''
            write_file(file_name, content)
            print(f"Вміст файлу {file_name} оновлено.")
        elif command == 'delete_file' and args:
            file_name = args[0]
            message = delete_file(file_name)
            print(message)
        elif command == 'create_directory' and args:
            dir_name = args[0]
            message = create_directory(dir_name)
            print(message)
        elif command == 'delete_directory' and args:
            dir_name = args[0]
            message = delete_directory(dir_name)
            print(message)
        elif command == 'list_directory' and args:
            dir_name = args[0]
            content = list_directory(dir_name)
            print(f"Вміст директорії {dir_name}:\n{content}")
        elif command == 'ask' and args:
            prompt = ' '.join(args)
            response = ask_chatgpt(prompt)
            print(f"Відповідь від ChatGPT:\n{response}")
        elif command == 'exit':
            print("Завершення роботи бота.")
            break
        else:
            print("Невідома команда або відсутні аргументи.")
