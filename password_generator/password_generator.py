import random
import string


def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    characters = list(string.ascii_lowercase)

    if use_upper:
        characters += list(string.ascii_uppercase)
    if use_digits:
        characters += list(string.digits)
    if use_symbols:
        characters += list("!@#$%^&*()_+-=[]{}|;:,.<>?")

    if not characters:
        return "Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# example of run
if __name__ == "__main__":
    print("📌 Password Generator")
    length = int(input("Enter desired password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print("\n✅ Your generated password:", password)
