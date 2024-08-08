print("Welcome! create an account")

username = input("Enter username: ")
password = input("Enter password: ")

print("You account has been created successfully!")
print("Login now!")

username2 = input("Enter your username: ")
password2 = input("Enter your password: ")

if username == username2 and password == password2:
    print("You are logged in successfully!")
else:
    print("Invalid credentials!")