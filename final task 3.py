username = input(str("Please enter a username with a capital letter and a number: "))
for char in username:
    if len(username)>=21 and len(username) <= 1 and username.islower() and "1234567890" not in username:
        print("Your username must be at least one number and at least one capitalized letter (min:2 max:20)")
        username = input("try again: ")
    else:
      print("welcome")