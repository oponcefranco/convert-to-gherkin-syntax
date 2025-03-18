# Convert Cypress Specs to Gherkin Syntax
Python standalone app that converts a Cypress specs into Gherkin syntax language

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

*Disclaimer: the setup instructions is based from the article,* [*"The definitive guide to set up my Python workspace"*](https://medium.com/@henriquebastos/the-definitive-guide-to-setup-my-python-workspace-628d68552e14)

### Create Virtual Environment

_You may have different directory name for your projects. For this example, we use `workspace` for the directory containing the (cloned) automation repo._

* [`pyenv`](https://github.com/pyenv/pyenv) is used to install Python interpreters, and manage Python versions on a per-project basis.
  * the fundamental concept behind `pyenv` is a shim.
     ❯ _"A shim is a small library or program that transparently intercepts calls and changes the arguments passed, handles the operation itself or redirects the operation elsewhere."_
     
     `pyenv` creates a directory of shim commands that the same names as all the executables (such as pydoc) distributed with all the installed Python versions.
  * `pyenv` will first use the *shell* Python specified by the `PYENV_VERSION` environment variable.
  * alternatively, it will use the *local* Python specified by the `.python-version` file in the current directory. 
* [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv) is used to configure the _"global environment." `pyenv-virtualenv` is basically a `pyenv` plugin that provides features to manage virtualenvs environments for Python on UNIX-like systems._
* [`pyenv-virtualenvwrapper`](https://github.com/pyenv/pyenv-virtualenvwrapper) is a `pyenv` plugin which provides a `pyenv virtualenvwrapper` command to manage your `virtualenvs` with `virtualenvwrapper`.
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

This command will create the hidden file `.python-version` with the value of `3.13.0/`, which contains the specific version of Python required to execute this project. Note that the `.python-version` file is added to `.gitignore` and it is not added to the repo.

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

    pipenv sync

Show a graph of your installed dependencies:

    pipenv graph
