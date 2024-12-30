# User authentication

email = input("Enter your email: ")
password = input("Enter your password: ")

if '@' not in email:
    print("Invalid email")
else: 
    if email == "email" and password == "12345678":
        print("User logged in")
    elif email == "email":
        print("Password incorrent")
        password = input("Enter password again: ")
        if password == "12345678":
            print("User logged in successfully")
        else:
            print("Incorrect password")
    else:
        print("Invalid email or password")