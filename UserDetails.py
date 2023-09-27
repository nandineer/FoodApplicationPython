import getpass


def user_details():
        print("*" * 50)
        user_name = input("Enter the user name:")
        email = input("Enter the email address:")
        password = getpass.getpass("Enter the password:")
        print("*" * 50)
        print(f"Hi {user_name}, Welcome to Yummy_Eats")
        print("*" * 50)

        return user_name,email