# CodeShakespeare

[![CI - Build and Test](https://github.com/software-students-fall2024/software-engineering-fall-2024-3-python-package-python-package-exercise/actions/workflows/ci.yml/badge.svg)](https://github.com/software-students-fall2024/software-engineering-fall-2024-3-python-package-python-package-exercise/actions/workflows/ci.yml)

CodeShakespeare is a Python package designed to bring the wit and humor of Shakespearean language to modern programming. This package offers functions to transform comments, error messages, and commit messages into Shakespearean prose, adding a unique twist to your coding experience. 

### CodeShakespeare PyPI [Link](https://pypi.org/project/CodeShakespeare/)

## Installation
Developers can import the Shakespeare Quotes Generator package into their own projects using pip. Below are examples for all major functions:

1. Install the package from PyPI:
```pip install CodeShakespeare```

2. Import the functions in your Python code:
```from codeshakespeare import to_shakespeare, to_shakespeare_error, get_random_shakespeare_quote, generate_shakespearean_commit_message```


## Usage Examples

### 1. to_shakespeare(message: str, formality: str) -> str

This function allows user to transform regular commpent into Shakesperean prose with varying formality. The different options for formality include: 
    
noble, courtly, dramatic.
```
print(to_shakespeare("This is a test comment", formality="noble"))
```
### 2. to_shakespeare_error(message: str, severity: str) -> str
    
This function turns an error message into Shakesperean style with varying levels of severity. The different options for severity include:

tragedy, comedy, history
```
print(to_shakespeare_error("File not found", severity="tragedy"))
```

### 3. get_random_shakespeare_quote(style: str) -> str
This function returns a random Shakesperean quote in different styles. The different options for styles include:

playful, serious, melancholic
```
print(get_random_shakespeare_quote(style="playful"))
```
### 4. generate_shakespearean_commit_message(emotion: str)-> str
This function generates a Shakespearean commit message based on emotion. Differnt options for emotions include:

victory, defeat, reflection

```
print(generate_shakespearean_commit_message(emotion="victory"))
```

### For a complete example, see [test_codeshakespeare.py](tests/test_codeshakespeare.py)

## Contributing

If you'd like to contribute to the project, follow these steps to set up the development enviroment and get started:

#### 1. Clone the Repository:
```
git clone https://github.com/software-students-fall2024/software-engineering-fall-2024-3-python-package-python-package-exercise

cd 3-python-package-wear
```
#### 2. Create a Virtual Enviroment:
```
python3 -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
```

#### 3. Install Dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Build and test the package
```
python -m build
pip install .  # Install the package locally for testing
python -m unittest discover -s tests -p "test_codeshakespeare.py"
```

## How to Configure & Run Our Package

1. ***Update Pip and Python:*** ```python3 -m pip --version```

2. ***Update SetupTools and Wheel:*** ```python3 -m pip install --upgrade pip setuptools wheel ```

3. ***Install pipenv locally:*** ```python3 -m pip install --user pipenv```

4. ***Navigate to project directory***
   
      *Mac:* ```cd ~/Desktop/Project3```
   
      *Windows:* ```cd %UserProfile%\Desktop\Project3```

5. ***Create & activate virtual env:*** ```pipenv shell```

6. ***Install all Dependencies:*** ```pipenv install --dev```

7. ***Install PyTest for testing:*** ```pipenv install pytest --dev```

8. ***Run tests***
   
      *Mac:* ```PYTHONPATH=src pytest tests/test_codeshakespeare.py```
   
      *Windows:* ```$env:PYTHONPATH="src"; pytest tests/test_codeshakespeare.py```


## Team Members

- ***Emily Huang:*** ([emilyjhuang](https://github.com/emilyjhuang))
- ***Wenli Shi:*** ([WenliShi2332](https://github.com/WenliShi2332))
- ***Alex Hsu:*** ([hsualexotake](https://github.com/hsualexotake))
- ***Reese Burns:*** ([reeseburns](https://github.com/reeseburns))
