# Convert Cypress Specs to Gherkin Syntax

A Python-based tool that automates the conversion of Cypress test specifications (`.cy.ts` files) into Behaviour-Driven Development (BDD) Gherkin syntax using the OpenAI API. This tool bridges the gap between technical test automation and business-readable test documentation.

## Overview

This application provides two modes of operation:
- **GUI Mode**: Interactive tkinter-based interface for easy file s****election and conversion
- **CLI Mode**: Command-line interface for scriptable batch processing

The tool leverages OpenAI's GPT-4 model to intelligently convert Cypress test code into well-structured Gherkin scenarios following BDD best practices.

## Core Functionality
### 1. Cypress to Gherkin Conversion:

- Recursively scans the selected source directory for `.cy.ts` files.
- Reads the test content and sends it to the OpenAI API for Gherkin-style conversion.
- Saves the converted Gherkin syntax to corresponding files in the destination directory.

### 2. Multithreading Execution:

- The conversion process runs in a separate thread to prevent the GUI from freezing, ensuring a smooth user experience.

### 3. Graphical User Interface (GUI) 🎯

- Built with [`tkinter`](https://docs.python.org/3/library/tkinter.html) for user-friendly interaction.
- Allows users to:
  - Select source and destination directories.
  - Start the conversion process.
  - View a log output of the conversion process.
  - Preview the last converted file’s Gherkin syntax in a scrollable window.

### ⚙️ Key Components & Features
#### File Handling:
   - Uses `os.walk()` to traverse directories and find Cypress test files.
   - Writes the converted Gherkin content into `.txt` files.
#### Threading:
   - The conversion process runs in a background thread to avoid freezing the GUI.
   - API Interaction:
     - Uses openai for Gherkin conversion by calling the `generate_gherkin_syntax()` function.
#### Error Handling:
   - Displays error messages for invalid directory selections.
   - Provides success messages upon completion.
#### User Experience:
   - Displays real-time log updates and previews the Gherkin output of the latest file.

## 🚀 Purpose

This script automates the tedious process of converting Cypress test specs into readable Gherkin syntax (e.g., Given-When-Then scenarios), improving test documentation and readability.

## 📁 Repository Structure

```
convert-to-gherkin-syntax/
├── script/                      # Main application code
│   ├── __init__.py             # Package initializer
│   ├── main.py                 # GUI application entry point
│   └── conversion.py           # Core conversion logic and API integration
├── data/                        # Configuration and prompts
│   └── prompt.py               # OpenAI prompt template for conversion
├── xray/                        # Xray Test Management integration
│   └── test_repository/        # Scripts for Xray API interactions
│       └── get_tests_in_folder.py  # Fetch tests from Xray folders
├── .github/                     # GitHub workflows and CI/CD
│   └── workflows/
│       └── pylint.yml          # Python linting workflow
├── .env.example                 # Environment variables template
├── Pipfile                      # Pipenv dependency specification
├── Pipfile.lock                 # Locked dependencies
├── requirements.txt             # Pip requirements file
├── .pylintrc                    # Pylint configuration
└── README.md                    # This file
```

### Key Files

- **script/main.py**: GUI application using tkinter for interactive conversion
- **script/conversion.py**: Core functions for reading Cypress files, calling OpenAI API, and generating Gherkin syntax
- **data/prompt.py**: Contains the system prompt that guides GPT-4 in converting tests to Gherkin format
- **xray/test_repository/get_tests_in_folder.py**: Optional integration with Xray Test Management via GraphQL

⸻
# Getting Started

## Clone Repository

    git clone git@github.com:oponcefranco/convert-to-gherkin-syntax.git

## Pre-Requirements

In order to start from the very beginning we need to install the following tools:
[`pyenv`](https://github.com/pyenv/pyenv) To manage the different Python interpreter version.
[`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv) To manage the virtual environment on which the framework is going to work.
[`pyenv-virtualenvwrapper`](https://github.com/pyenv/pyenv-virtualenvwrapper) To make the operations described above easier.
Assuming you have [`brew`](https://brew.sh/) installed in your system on macOS.
First, check whether these brew formulas are already installed in your system.

    brew info pipenv pyenv pyenv-virtualenv pyenv-virtualenvwrapper

Currently, using the following versions:

    brew list --versions pipenv pyenv pyenv-virtualenv pyenv-virtualenvwrapper 

    pipenv 2024.4.1
    pyenv 2.5.4
    pyenv-virtualenv 1.2.4
    pyenv-virtualenvwrapper 20140609

[`Pipenv`](https://github.com/pypa/pipenv) is our Python dependency management tool.

    brew install pipenv

If you need to install all of these brew formulas to your system, proceed with the following command:

    brew install pipenv pyenv pyenv-virtualenv pyenv-virtualenvwrapper

*Disclaimer: the setup instructions is based from the article,* [*"The definitive guide to set up my Python
workspace"*](https://medium.com/@henriquebastos/the-definitive-guide-to-setup-my-python-workspace-628d68552e14)

### Create Virtual Environment

_You may have different directory name for your projects. For this example, we use `workspace` for the directory containing the (cloned) automation repo._

* [`pyenv`](https://github.com/pyenv/pyenv) is used to install Python interpreters, and manage Python versions on a per-project basis.
    * the fundamental concept behind `pyenv` is a shim.
      ❯ _"A shim is a small library or program that transparently intercepts calls and changes the arguments passed, handles the operation itself or redirects the operation elsewhere."_

      `pyenv` creates a directory of shim commands that the same names as all the executables (such as pydoc) distributed with all the installed Python versions.
    * `pyenv` will first use the *shell* Python specified by the `PYENV_VERSION` environment variable.
    * alternatively, it will use the *local* Python specified by the `.python-version` file in the current directory.
* [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv) is used to configure the _"global environment." `pyenv-virtualenv` is basically a `pyenv` plugin that provides features to manage
  virtualenvs environments for Python on UNIX-like systems._
* [`pyenv-virtualenvwrapper`](https://github.com/pyenv/pyenv-virtualenvwrapper) is a `pyenv` plugin which provides a `pyenv virtualenvwrapper` command to manage your `virtualenvs` with
  `virtualenvwrapper`.
* With `virtualenvwrapper` all `virtualenvs` are kept on the same directory and your projects' code on another.

        # virtualenvs will be on...
        mkdir ~/.ve
        # projects will be on...
        mkdir ~/workspace

Additionally, add the following commands to `.bash_profile` or `.zshrc` to initialize `pyenv` when you start the terminal.

    export WORKON_HOME=~/.ve
    export PROJECT_HOME=~/workspace
    eval "$(pyenv init -)"
    pyenv virtualenvwrapper_lazy 

Install Python version:

    pyenv install --list # list all available versions
    pyenv install 3.13.0/

Change directory:

    cd ~/workspace/convert-to-gherkin-syntax

Set `pyenv local` version:

    pyenv local 3.13.0

This command will create the hidden file `.python-version` with the value of `3.13.0/`, which contains the specific version of Python required to execute this project. Note that the
`.python-version` file is added to `.gitignore` and it is not added to the repo.

Create a `virtualenv` to work on it:

    $ pyenv virtualenv     
    ❯ mkvirtualenv -a ~/workspace/convert-to-gherkin-syntax -p python3.13 convert-to-gherkin-syntax

*NOTE:* be sure `~/workspace/convert-to-gherkin-syntax` is the same path as the folder where you checked out this repo.

This will create a `virtualenv` with `Python 3` at `~/.ve/convert-to-gherkin-syntax`, and associating it to the project directory `~/workspace/convert-to-gherkin-syntax`.

Shortcut to virtual environment:

    $ workon convert-to-gherkin-syntax
    ❯ ~/workspace/convert-to-gherkin-syntax 

### Requirements

Verify the version of `Python` being used by `pyenv`:

    $ pyenv version
    ❯ 3.13.0/ (set by PYENV_VERSION environment variable)

    $ pyenv shell 3.13.0
    $ echo $PYENV_VERSION
    ❯ 3.13.0

    $ pyenv local
    ❯ 3.13.0

Install all packages specified in `Pipfile.lock.`:

    pipenv install

Checks for `PyUp` Safety security vulnerabilities and against `PEP 508` markers provided in `Pipfile`:

    pipenv check

Installs all packages specified in `Pipfile.lock`:

    pipenv sync

Displays currently-installed dependency graph information:

    pipenv graph

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root directory based on `.env.example`:

```bash
cp .env.example .env
```

Edit the `.env` file and add your API keys:

```bash
# Required for Cypress to Gherkin conversion
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Only needed if using Xray Test Management integration
XRAY_CLIENT_ID=your_xray_client_id
XRAY_CLIENT_SECRET=your_xray_client_secret
```

**Getting an OpenAI API Key:**
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key to your `.env` file

## 🚀 Running the Application

### Method 1: GUI Mode (Recommended for Interactive Use)

Launch the graphical user interface:

```bash
python -m script.main
```

**GUI Features:**
- Browse and select source directory containing `.cy.ts` files
- Choose destination directory for converted Gherkin files
- Real-time conversion progress log
- Live preview of converted Gherkin syntax
- User-friendly error messages and success notifications

**Using the GUI:**
1. Click "Browse" next to "Select Source Directory" and choose the folder containing your Cypress tests
2. Click "Browse" next to "Select Destination Directory" and choose where to save the Gherkin files
3. Click "Start Conversion" to begin the process
4. Monitor progress in the "Process Log" section
5. View the converted Gherkin syntax in the "Gherkin Output Preview" section

### Method 2: CLI Mode (Recommended for Automation)

Run the conversion via command line:

```bash
python -m script.conversion
```

You'll be prompted to enter the directory path:
```
Enter the directory containing Cypress test files: /path/to/cypress/tests
```

The converted files will be saved in a `gherkin_output/` directory maintaining the original folder structure.

### Method 3: Using Python Interactive Mode

```python
from script.conversion import process_directory

# Process all .cy.ts files in the specified directory
process_directory('/path/to/cypress/tests')
```

## 📝 Example Usage

### Input: Cypress Test File

Given a Cypress test file like the one you provided (`TC_05_duplicate_feed.cy.ts`):

```javascript
describe('Articles', { tags: ['@articles', '@home-feed'] }, () => {
  it('Duplicate Draft Section NUMBERED LIST', () => {
    cy.percySnapshot('duplicate_section_draft')
    selectMenuOption({ selector: 'feeds_link' })
    addFeedDraft({
      path: 'goat-home-feed',
      title: `Add Section - ${timestamp()}`
    })
    addSectionNumberedList({ section: 'Numbered List', index: 0 })
    duplicateFeedDraft({ section })
  })
})
```

### Output: Gherkin Syntax

The tool will generate a Gherkin feature file:

```gherkin
Feature: Articles Management

  Background:
    Given the user is authenticated in the CMS
    And the user has switched to the correct namespace

  Scenario: Duplicate a numbered list section in a feed draft
    Given the user navigates to the feeds section
    When the user creates a new feed draft with title "Add Section"
    And the user adds a numbered list section at position 0
    And the user duplicates the feed draft section
    Then the section is successfully duplicated
```

## 🔧 Advanced Features

### Xray Test Management Integration

The `xray/test_repository/get_tests_in_folder.py` script allows you to fetch test cases from Xray Test Management:

1. Configure Xray credentials in your `.env` file:
   ```bash
   XRAY_CLIENT_ID=your_client_id
   XRAY_CLIENT_SECRET=your_client_secret
   ```

2. Edit the script to specify your project and folder:
   ```python
   project_key = "YOUR_PROJECT"
   folder_path = "/YOUR_FOLDER"
   ```

3. Run the script:
   ```bash
   python xray/test_repository/get_tests_in_folder.py
   ```

This will fetch all tests from the specified Xray folder in JSON format.

## 🛠️ Development

### Code Quality

The project uses `pylint` for code quality checks. Run linting with:

```bash
pipenv run pylint script/ data/ xray/
```

Configuration is available in `.pylintrc`.

### CI/CD

GitHub Actions automatically runs pylint on pull requests. See `.github/workflows/pylint.yml` for details.

## 📋 Dependencies

Core dependencies:
- **openai**: OpenAI API client for GPT-4 integration
- **python-dotenv**: Environment variable management
- **tkinter**: GUI framework (included with Python)
- **gql**: GraphQL client for Xray integration
- **aiohttp**: Async HTTP client for API calls
- **requests**: HTTP library for REST API calls

See `Pipfile` for complete dependency list and versions.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request

## 📄 License

See the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

**Issue: "OpenAI API key not found" error**
- Solution: Ensure your `.env` file exists and contains `OPENAI_API_KEY=your_key`

**Issue: "ModuleNotFoundError: No module named '_tkinter'" or GUI window doesn't appear**
- Solution: tkinter needs to be installed separately depending on your Python installation
- **On macOS with Homebrew Python**: `brew install python-tk@3.13` (replace 3.13 with your Python version)
- On Ubuntu/Debian: `sudo apt-get install python3-tk`
- On macOS with Python from python.org: tkinter is included by default
- **Alternative**: Use CLI mode instead: `python -m script.conversion`

**Issue: Conversion produces poor quality Gherkin**
- Solution: The quality depends on the GPT-4 model's understanding. You can:
  - Modify the prompt in `data/prompt.py` to be more specific
  - Increase `max_tokens` in `script/conversion.py` for longer scenarios
  - Update to a newer GPT model if available

**Issue: Rate limiting from OpenAI API**
- Solution: Add delays between requests or upgrade your OpenAI plan
