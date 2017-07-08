

while True:
    first, last = input("Whats your first and last name: ").split()
    response= input("Do you have an email y/n?: ")
    if response.lower() == "y" or response.lower().startswith('y'):
        email = input("Please type your email?: ")
        print(f"OK your first name is {first} and your last name is {last} and your email is {email}.")
    else:
        print(f"Ok have a good day {first} {last}.")
        break

