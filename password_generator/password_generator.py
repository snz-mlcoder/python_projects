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
        raise ValueError("Please select at least one character type.")


    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    score = 0
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1

    length = len(password)

    if length >=12 and score ==4 :
        return "Strong"
    if length >=8 and score >=3 :
        return "Moderate"
    else:
        return "weak"



# example of run
if __name__ == "__main__":
    print("📌 Password Generator")
    while True:
        try:
            length = int(input('\nEnter desired password lenght:'))
        except ValueError:
            print('please enter a valid number')
            continue

        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        try:

            password = generate_password(length, use_upper, use_digits, use_symbols)
        except ValueError as e:
            print(e)
            continue

        print("\n✅ Your generated password:", password)
        print("📊 Password strength:", password_strength(password))

        again = input('/nGenerate another password ? (y/n): ').lower()
        if again != 'y' :
            print("Goodbye")
            break

