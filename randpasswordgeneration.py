import random
import string


def generate_password(name):
    # Define character sets for each category
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    special_chars = string.punctuation
    digits = string.digits

    # Ensure at least one character from each category
    password = random.choice(uppercase_chars)
    password += random.choice(lowercase_chars)
    password += random.choice(special_chars)
    password += random.choice(digits)

    # Fill the remaining characters randomly
    all_chars = uppercase_chars + lowercase_chars + special_chars + digits
    while len(password) < 8:
        password += random.choice(all_chars)

    # Shuffle the password
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    # Ensure the password length is between 8 and 12 characters
    password = password[:random.randint(8, 12)]

    return password


# Get the user's name as input
name = input("Enter your name: ")

# Generate and display the password
password = generate_password(name)
print(f"Generated password for {name}: {password}")

while True:
    # Get the user's name as input
    name = input("Enter your name (or type 'stop' to quit): ")

    if name.lower() == 'stop':
        break

    # Generate and display the password
    password = generate_password(name)
    print(f"Generated password for {name}: {password}")
