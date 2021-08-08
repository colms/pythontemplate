# PythonTemplate

**Table of contents**

* [Installation](#installation)
* [Usage](#usage)
* [Testing](#testing)
* [Format](#format)
* [Virtual Environment](#virtual-environments)

## Installation

Requirements:

- Python >3.9

### From Source

#### Getting the code

```bash
git clone https://github.com/colms/pythontemplate.git
cd pythontemplate
```

#### Setting up Python

```bash
pyenv install 3.9.6
pyenv local 3.9.6
```

### Installing from pip

```
pip install pythontemplate
```

#### Development

Get the code:
```bash
git clone https://github.com/colms/pythontemplate.git
cd pythontemplate
```

[Run](#virtual-environment-setup) the virtual environment before installing the pip.

```bash
python3 setup.py sdist
pip3 install -e .
```

## Usage

After the package is installed:
```bash
pythontemplate --foo 2
```

## Testing

First, setup the [virtual environment](#virtual-environment-setup).

Run all unit tests:
```
python -m unittest discover
```

Run tests for a specific file:
```bash
python3 -m unittest tests.test_me
```

## Format

In the [virtual environment](#virtual-environment-setup), install `yapf`:
```bash
pip install yapf
```

Run with:
```bash
yapf -ir src tests
```

## Virtual Environments

### Virtual Environment Setup

```bash
python3 -m venv env
source env/bin/activate
```

### Virtual Environment Exit

```bash
deactivate
```
