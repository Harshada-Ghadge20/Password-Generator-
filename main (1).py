# Optimized Password Generator using Python

import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Combine all characters
    all_characters = lowercase + uppercase + digits + symbols

    # Fill remaining password length
    password += random.choices(all_characters, k=length - 4)

    # Shuffle password for randomness
    random.shuffle(password)

    return ''.join(password)


# Main Program
print("===== RANDOM PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length: "))

    generated_password = generate_password(length)

    print("\nGenerated Password:")
    print(generated_password)

except ValueError:
    print("Invalid input! Please enter a valid number.")