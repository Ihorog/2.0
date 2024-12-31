# ChatGPT GitHub Integration

## Description
This repository includes a Python script for interacting with OpenAI's GPT-4 model using the OpenAI API.

## How to Use
1. Add your OpenAI API key to `config.json`.
2. Run the bot using `python bot.py`.
3. Input your query and get a response from GPT-4.

## Setup
- Install dependencies: `pip install -r requirements.txt`.

## New Commands and Functionalities
The bot now supports the following commands for file and directory operations:

- `create_file <file_name> [content]`: Creates a file with the specified name and optional content.
- `read_file <file_name>`: Reads the content of the specified file.
- `write_file <file_name> <content>`: Writes the specified content to the file.
- `delete_file <file_name>`: Deletes the specified file.
- `create_directory <directory_name>`: Creates a directory with the specified name.
- `delete_directory <directory_name>`: Deletes the specified directory.
- `list_directory <directory_name>`: Lists the contents of the specified directory.
- `ask <prompt>`: Sends a prompt to GPT-4 and gets a response.
- `exit`: Exits the bot.

## Error Handling
The bot includes error handling mechanisms to ensure stable operation even in unpredictable situations.

## Security
The bot is restricted to access only specific directories and files to avoid accidental or unauthorized access to sensitive data.

## Documentation
Keep the documentation up-to-date regarding the bot's commands and functionalities to simplify its usage and further development.
