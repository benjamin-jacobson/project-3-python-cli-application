# Project 3: Python Application with CLI


# Environment Setup
## Python Manager(within Windows WSL2)
- Installing pyenv
    - curl https://pyenv.run | bash
    - sudo apt update
    - sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    - pyenv install 3.8.13
    - pyenv global 3.8.13
    - pip install pipenv
    - export PIPENV_VENV_IN_PROJECT=1

## Python Environment Manager
- Pipfile. This file contains all of the required Python libraries for your work, and restricts them to the repository that you're working in.
- To install pytest and any other required libraries, simply navigate to a folder with a Pipfile and enter pipenv install:
    - pipenv install
    - pipenv shell ... not sure needed
- Installing packages
    - pipenv install pandas (this will put in the piplock file)


# Running Tests
- pytest -x 



# Resources
- https://www.infoworld.com/article/3561758/how-to-manage-python-projects-with-pipenv.html