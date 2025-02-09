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

## Integrating OpenAI API with Python

To integrate the OpenAI API with Python, follow these steps:

1. Install the OpenAI Python package by adding `openai` to your `requirements.txt` file and running `pip install -r requirements.txt`.
2. Obtain your OpenAI API key and add it to a configuration file, such as `config.json`.
3. Import the OpenAI package in your Python script, as shown in `bot.py`.
4. Load your API key from the configuration file and set it using `openai.api_key`.
5. Use the `openai.ChatCompletion.create` method to interact with the OpenAI API, as demonstrated in the `ask_chatgpt` function in `bot.py`.

## GitHub Actions Workflow

This repository includes a GitHub Actions workflow to automate the process of checking code quality, running tests, validating the environment, and preparing the project for deployment.

### Workflow Steps

1. **Checkout the code**: Uses the `actions/checkout@v3` action to checkout the repository code.
2. **Set up Python**: Uses the `actions/setup-python@v4` action to set up Python 3.9.
3. **Install dependencies**: Installs the required dependencies from `requirements.txt`.
4. **Run linter for code quality**: Uses `flake8` to check the code quality.
5. **Run tests**: Uses `pytest` to run the tests.
6. **Build Docker image (optional)**: Builds a Docker image for the project.
7. **Validate environment variables**: Checks for the existence of the `.env` file.
8. **Run final pre-deployment checks**: Ensures all components are ready for deployment.

### Tools Used

- **flake8**: For code quality checks.
- **pytest**: For running tests.
- **Docker**: For containerization (optional).

### Triggering the Workflow

The workflow is triggered on every push to the `main` branch and on every pull request to the `main` branch.

