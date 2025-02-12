print("\tWelcome to the Login System")

username = input("please enter the username : ").lower()
password = input("Please enter the password : ")

if username == "admin" and password == "1234" :
    print("access granted ")
else :
    print("access denied ")
