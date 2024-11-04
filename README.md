# CODESHAKESPEARE

![Workflow Status](https://github.com/software-students-fall2024/3-python-package-wear/actions/workflows/event-logger.yml/badge.svg?branch=main)

## TABLE OF CONTENTS
1. [Description](#description)
2. [PyPI Page](#pypi-page)
3. [Installation](#installation)
4. [Virtual Environment & Dependencies](#virtual-environment--dependencies)
5. [Build, Test, and Run the CodeShakespeare Package](#build-test-and-run-the-codeshakespeare-package)
6. [Usage Examples](#usage-examples)
7. [Contributing](#contributing)
8. [Team Members](#team-members)

## Description
CodeShakespeare is a Python package designed to bring the wit and humor of Shakespearean language to modern programming. This package offers functions to transform comments, error messages, and commit messages into Shakespearean prose, adding a unique twist to your coding experience.

## Table of Contents
1. [Description](#description)
2. [PyPI Page](#pypi-page)
3. [Installation](#installation)
4. [Virtual Environment & Dependencies](#virtual-environment--dependencies)
5. [Build, Test, and Run the CodeShakespeare Package](#build-test-and-run-the-codeshakespeare-package)
6. [Usage Examples](#usage-examples)
7. [Contributing](#contributing)
8. [Team Members](#team-members)

## Description

CodeShakespeare is a Python package designed to bring the wit and humor of Shakespearean language to modern programming. This package offers functions to transform comments, error messages, and commit messages into Shakespearean prose, adding a unique twist to your coding experience. 

## PyPi Page
You can find CodeShakespeare on PyPI here: [Link](https://pypi.org/project/CodeShakespeare/)

To work on this project, it’s recommended to use a virtual environment to isolate dependencies. Follow these steps to create, activate, deactivate, and install all dependencies.

## Installation
Developers can import the Shakespeare Quotes Generator package into their own projects using pip. Below is how to install the package:

**1. Install the package from PyPI**
```
pip install CodeShakespeare
```

**2. Import the functions in your Python code**
```
from codeshakespeare import to_shakespeare, to_shakespeare_error, get_random_shakespeare_quote, generate_shakespearean_commit_message
```

## Virtual Environment & Dependencies

To work on this project, it’s recommended to use a virtual environment to isolate dependencies. Follow these steps to create, activate, deactivate, and install all dependencies.

**1. Update Pip and Python:** 

```
python3 -m pip --version
```

**2. ***Update SetupTools and Wheel:**

 ```
 python3 -m pip install --upgrade pip setuptools wheel
```

**3. Install pipenv locally:** 

```
python3 -m pip install --user pipenv
```

**4. Navigate to project directory**
   
- **Mac:** 

```
cd ~/Desktop/3-python-package-wear-main
```
   
- **Windows:** 
```
cd %UserProfile%\Desktop\3-python-package-wear-main
```

**5. Create a Virtual Environment**

- **Mac/Linux:**
  ```
  python3 -m venv myenv
  source myenv/bin/activate
  ```

- **Windows**
    ```
      python -m venv myenv
      myenv\Scripts\activate
    ```
```
pip install -r requirements.txt
```

**6. Create and Activate a Virtual Environment with Pipenv**
Use pipenv to set up a virtual environment and install development dependencies:

```
pipenv install --dev
pipenv shell 
```

**7. Install Dependencies Loaclly**
```
pip install .
```

**8. Deactivate when Done**
```
deactivate
```

## Build, Test, and Run the CodeShakespeare Package

Follow these steps to build, test, and run the CodeShakespeare package using `pipenv`, `build`, and `twine`. 

**1. Set Up the Development Environment**
First, create a virtual environment and install dependencies:

```
pipenv install --dev 
```

**2. Install build and twine**
To build and upload the package, install build and twine:

```
pipenv install --dev build
pipenv install --dev twine
```

**3. Build the Package**
```
pipenv run python -m build
```

**4. Testing the Package**
```
python3 -m venv test_env
source test_env/bin/activate
pip install CodeShakespeare
python test_shakespeare.py 
deactivate
```


## Usage Examples - Running example python

To run our example program, (see [example_shakespeare.py](./example_shakespeare.py)) you can run the follwing commands in your terminal:

**1. Open a new virtual environment**
```
python3 -m venv myenv
```

**2. Activate the environment**
```
source myenv/bin/activate
```

**3. pip install the package**
```
pip install CodeShakespeare
```
**4. run our examply python code**
```
python example_shakespeare.py
```


#### 1. to_shakespeare(message: str, formality: str) -> str

This function allows user to transform regular commpent into Shakesperean prose with varying formality. The different options for formality include: 
    
noble, courtly, dramatic.
```
print(to_shakespeare("This is a test comment", formality="noble"))
```
#### 2. to_shakespeare_error(message: str, severity: str) -> str
    
This function turns an error message into Shakesperean style with varying levels of severity. The different options for severity include:

tragedy, comedy, history
```
print(to_shakespeare_error("File not found", severity="tragedy"))
```

#### 3. get_random_shakespeare_quote(style: str) -> str
This function returns a random Shakesperean quote in different styles. The different options for styles include:

playful, serious, melancholic
```
print(get_random_shakespeare_quote(style="playful"))
```
#### 4. generate_shakespearean_commit_message(emotion: str)-> str
This function generates a Shakespearean commit message based on emotion. Differnt options for emotions include:

victory, defeat, reflection

```
print(generate_shakespearean_commit_message(emotion="victory"))
```


## Contributing

If you'd like to contribute to the project, follow these steps to sset up the development enviroment and get started:

#### 1. Clone the Repository:
```
git clone https://github.com/software-students-fall2024/software-engineering-fall-2024-3-python-package-python-package-exercise

cd 3-python-package-wear
```
#### 2. Create a Virtual Enviroment:
```
python3 -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
```

#### 3. Install Dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Build and test the package
```
python -m build
pip install .  # Install the package locally for testing
python -m unittest discover -s tests -p "test_codeshakespeare.py"
```

## TEAM MEMBERS

- ***Emily Huang:*** ([emilyjhuang](https://github.com/emilyjhuang))
- ***Wenli Shi:*** ([WenliShi2332](https://github.com/WenliShi2332))
- ***Alex Hsu:*** ([hsualexotake](https://github.com/hsualexotake))
- ***Reese Burns:*** ([reeseburns](https://github.com/reeseburns))
