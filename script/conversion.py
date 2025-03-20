import logging
import os

import openai
from dotenv import load_dotenv

from data.prompt import PROMPT_MESSAGE

# Configure logging
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")


def load_api_key():
    """Load OpenAI API key from environment variables."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Error: OpenAI API key not found. Please set OPENAI_API_KEY in a .env file.")
    return api_key


def get_openai_client():
    """Returns an OpenAI client with API key loaded."""
    return openai.OpenAI(api_key=load_api_key())


def read_cypress_test(file_path):
    """Read the contents of a Cypress test case file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def generate_gherkin_syntax(test_content):
    """Convert Cypress test content to Gherkin syntax using OpenAI."""
    try:
        client = get_openai_client()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": PROMPT_MESSAGE},
                {"role": "user", "content": f"Cypress Test:\n{test_content}\n\nGherkin Syntax:"},
            ],
            max_tokens=500,
        )
        return response.choices[0].message.content.strip()

    except openai.OpenAIError as e:
        # logging.error(f"OpenAI API error: {e}")
        logging.error("%s OpenAI API error: %s", type(e), e)
    except Exception as e:
        # logging.error(f"Unexpected error: {e}")
        logging.error("%s Unexpected error: %s", type(e), e)

    return ""


def process_directory(directory_path):
    """Recursively process all .cy.ts files in the given directory and subdirectories."""
    output_dir = "gherkin_output"
    os.makedirs(output_dir, exist_ok=True)

    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(".cy.ts"):
                file_path = os.path.join(root, file_name)
                test_content = read_cypress_test(file_path)
                gherkin_syntax = generate_gherkin_syntax(test_content)

                if gherkin_syntax:
                    relative_path = os.path.relpath(root, directory_path) if root != directory_path else ""
                    output_subdir = os.path.join(output_dir, relative_path) if relative_path else output_dir

                    os.makedirs(output_subdir, exist_ok=True)
                    output_file = os.path.join(output_subdir, file_name.rsplit(".", 1)[0] + "_gherkin.txt")

                    with open(output_file, "w", encoding="utf-8") as file:
                        file.write(gherkin_syntax)
                    print(f"Gherkin syntax saved to {output_file}")


def main():
    """Main function to process a directory."""
    while True:
        directory_path = input("Enter the directory containing Cypress test files: ").strip()
        if os.path.isdir(directory_path):
            process_directory(directory_path)
            break
        print("Invalid directory. Try again.")


if __name__ == "__main__":
    main()
