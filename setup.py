from setuptools import setup, find_packages

# Read the README.md file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="CodeShakespeare",
    version="0.1.2",
    description="A package for generating Shakespearean-style quotes and comments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Emilt Huang, Reese Burns, Wenli Shi, Alex Hsu",
    author_email="eh96@nyu.edu",
    url="https://github.com/software-students-fall2024/3-python-package-wear",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)