# Python Password Generator

A simple password generator application built using Python. This project generates strong and random passwords based on user preferences such as password length and character types.

## Features

* Generate random passwords
* Choose password length
* Include uppercase letters
* Include lowercase letters
* Include numbers
* Include special characters
* Simple and user-friendly interface
* Helps create strong passwords

## Technologies Used

* Python 3

## Project Structure

```text
password-generator/
│
├── password_generator.py
└── README.md
```

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/password-generator.git
```

2. Go to the project folder:

```bash
cd password-generator
```

3. Run the Python file:

```bash
python password_generator.py
```

## Usage

After running the program, enter the required password length and choose which character types to include.

Example:

```text
Enter password length: 12
Include uppercase letters? yes
Include lowercase letters? yes
Include numbers? yes
Include special characters? yes

Generated Password: A7@kL9#pQ2$x
```

## Sample Code

```python
import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols=True):
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type."

    password = "".join(random.choice(characters) for _ in range(length))
    return password


length = int(input("Enter password length: "))

password = generate_password(length)

print("Generated Password:", password)
```

## Future Improvements

* Add password strength checker
* Add option to copy password to clipboard
* Create a graphical user interface using Tkinter
* Save generated passwords securely
* Add option to exclude similar characters like `O`, `0`, `l`, and `1`

## Author

Created by **Your Name**

## License

This project is open-source and free to use.
