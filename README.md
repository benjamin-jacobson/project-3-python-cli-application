# Project 3: Python Application with CLI + ORM

![CLI](https://github.com/benjamin-jacobson/project-3-python-cli-application/blob/main/images/cli_prototype.JPG?raw=true)


## Application Description:
- This program has user, vendors and their appointments. You can add, delete, and see information for each, among other methods.
- The program launches and the user can select from a menu of options to pull information from the local database.

## Running the Applicaion
- python lib/cli.py

## Data Model
- There are three classes: User, Vendor and Appointment.
- User is in a one to many relationship with Appointment
- Vendor is in a one to many relationship with Appointment
- User and Vendor are in a many to many relationship.
- Property methods are included for class attributes, and each class has ORM CRUD methods among others such as get_all_...

## Files
- lib/seed.py to seed the database with fake data.
- lib/cli.py: runs the CLI
- lib/helpers.py: helper functions for mvp functionality

## Environment Setup
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

## Database Local Setup
- See below for setting up SQLite on WSL2
- sqlite3 version 3.31.1
- Creating database:
    - sqlite3 testb1.db

## Running Tests
- Some tests were implemented in development, and can be ran with the following.
- pytest -x 

## Future iterations
- Rather than delete from database, use a flag such as status "active" or "deactivated".
- Also use time in a more suffisticated manner. 
- Add aggregate class methods for more summary statistics and information.

### Resources
- https://www.infoworld.com/article/3561758/how-to-manage-python-projects-with-pipenv.html
- https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database#install-sqlite

### Curicullum Resources
- https://learning.flatironschool.com/courses/6550/pages/phase-3-cli+orm-project-template?module_item_id=598926