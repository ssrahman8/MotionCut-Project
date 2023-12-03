import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(characters) for _ in range(length))
    return secure_password

def main():
    print("Welcome to the Secure Password Generator!")
    print("This tool will generate strong and secure passwords.")

    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the length of each password: "))

        if num_passwords <= 0 or password_length <= 0:
            raise ValueError("Number of passwords and password length must be positive integers.")

        print("\nGenerated Passwords:")
        for _ in range(num_passwords):
            password = generate_password(password_length)
            print(password)

    except ValueError as e:
        print(f"Error: {e}")
        print("Please enter valid positive integers for the number of passwords and password length.")

if __name__ == "__main__":
    main()