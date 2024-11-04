# CODESHAKESPEARE

![Workflow Status](https://github.com/software-students-fall2024/3-python-package-wear/actions/workflows/event-logger.yml/badge.svg)

## TABLE OF CONTENTS
1. [Description](#description)
2. [PyPI Page](#pypi-page)
3. [Installation](#installation)
4. [Virtual Environment & Dependencies](#virtual-environment--dependencies)
5. [Build, Test, and Run the CodeShakespeare Package](#build-test-and-run-the-codeshakespeare-package)
6. [Usage Examples](#usage-examples)
7. [Contributing](#contributing)
8. [Team Members](#team-members)

## DESCRIPTION

CodeShakespeare is a Python package designed to bring the wit and humor of Shakespearean language to modern programming. This package offers functions to transform comments, error messages, and commit messages into Shakespearean prose, adding a unique twist to your coding experience. 

### CodeShakespeare PyPI [Link](https://pypi.org/project/CodeShakespeare/)

## INSTALLATION
Developers can import the Shakespeare Quotes Generator package into their own projects using pip. Below are examples for all major functions:

#### 1. Install the package from PyPI
```
pip install CodeShakespeare
```

#### 2. Import the functions in your Python code
```
from codeshakespeare import to_shakespeare, to_shakespeare_error, get_random_shakespeare_quote, generate_shakespearean_commit_message
```

## USAGE EXAMPLES

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

#### For a complete example, see [testing_shakespeare.py](./example_shakespeare.py)


## CONTRIBUTING

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

## HOW TO CONFIGURE & RUN CODESHAKESPEARE

#### 1. Update Pip and Python
   ```
   python3 -m pip --version
   ```

#### 2. Update SetupTools and Wheel
   ```
   python3 -m pip install --upgrade pip setuptools wheel
   ```

#### 3. Install pipenv locally
   ```
   python3 -m pip install --user pipenv
   ```

#### 4. Navigate to project directory
   *Mac:* 
   ```
   cd ~/Desktop/3-python-package-wear-main
   ```
   
   *Windows:* 
   ```
   cd %UserProfile%\Desktop\3-python-package-wear-main
   ```

#### 5. Create & activate virtual env
   ```
   pipenv shell
   ```

#### 6. Install all Dependencies
   ```
   pipenv install --dev
   ```

#### 7. Install PyTest for testing
   ```
   pipenv install pytest --dev
   ```

#### 8. Run tests
   
   *Mac:* 
   ```
   PYTHONPATH=src pytest tests/test_codeshakespeare.py
   ```
   
   *Windows:* 
   ```
   $env:PYTHONPATH="src"; pytest tests/test_codeshakespeare.py
   ```

## TEAM MEMBERS

- ***Emily Huang:*** ([emilyjhuang](https://github.com/emilyjhuang))
- ***Wenli Shi:*** ([WenliShi2332](https://github.com/WenliShi2332))
- ***Alex Hsu:*** ([hsualexotake](https://github.com/hsualexotake))
- ***Reese Burns:*** ([reeseburns](https://github.com/reeseburns))
