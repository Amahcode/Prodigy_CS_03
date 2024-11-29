import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check password length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    else:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine password strength
    if strength == 5:
        password_strength = "Strong"
    elif strength >= 3:
        password_strength = "Medium"
    else:
        password_strength = "Weak"

    return password_strength, feedback

def main():
    password = input("Enter your password: ")
    password_strength, feedback = assess_password_strength(password)

    print(f"\nPassword Strength: {password_strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"* {item}")

if __name__ == "__main__":
    main()


