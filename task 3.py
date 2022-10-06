username = str(input("Enter your username: "))

if username <= 1:
    print("Sorry, username must be longer then 1 word")
elif username >= 21:
    print("Sorry, the username cannot be more then 20 Character")
elif len(username) >= 21 and username <=1: 
    username == str(input("Enter password that include 1 uppercase alphabate and atleast 1 number: "))
if username.islower() and "0123456789" not in username:
        print("you must include 1 Uppercase letter and number")
        username = input("please try again: ")
