# Random Password Generator

![Python](https://img.shields.io/badge/python-3.x-blue.svg)

A simple and customizable random password generator written in Python. This script allows you to generate strong and secure passwords with various configurations.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Introduction

In today's digital world, having strong and unique passwords is essential to protect your online accounts and sensitive information. This random password generator is a Python script that allows you to create secure passwords with different lengths and character sets. It ensures that each generated password includes at least one character from each selected set, making them harder to crack.

## Features

- Customizable password length
- Options to include or exclude digits, uppercase letters, lowercase letters, and symbols in the password
- Random shuffling of characters to improve security
- Simple and easy-to-use Python script

## Installation

1. Make sure you have Python 3.x installed on your system.

2. Clone this repository to your local machine:

```
git clone https://github.com/anmolranjan1/random-password-generator.git
```

3. Navigate to the project directory:

```
cd random-password-generator
```

## Usage

The script provides a function `generate_password` that generates a random password based on the specified parameters. You can use the function by importing it into your Python code.

```python
import random_password_generator

# Generate a password with default settings (length=12, include all character sets)
password = random_password_generator.generate_password()
print("Generated Password:", password)
```

You can customize the password generation by passing optional arguments to the `generate_password` function:

```python
# Generate a password with a length of 16 characters, excluding digits
password = random_password_generator.generate_password(length=16, use_digits=False)
print("Generated Password:", password)
```

## Examples

Below are some example usages of the random password generator:

```python
import random_password_generator

# Example 1: Generate a 12-character password with all character sets
password1 = random_password_generator.generate_password()
print("Generated Password 1:", password1)

# Example 2: Generate a 16-character password with digits and symbols only
password2 = random_password_generator.generate_password(length=16, use_uppercase=False, use_lowercase=False)
print("Generated Password 2:", password2)
```

## License

This project is licensed under the [MIT License](LICENSE).