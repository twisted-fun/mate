# pylint: disable=undefined-variable
import sys
from setuptools import setup, find_packages

# Get version and author information
with open("mate/__version__.py", "r") as f:
    exec(f.read())

def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

requirements = read_requirements()

setup(
    name="mate",
    license="GPL",
    version=__version__,
    author=__author__,
    url="https://github.com/twisted-fun/mate",
    project_url={
        "Source Code": "https://github.com/twisted-fun/mate",
        "Documentation": "https://github.com/twisted-fun/mate/README.md"
    },
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["mate = mate.__main__:main"]},
)