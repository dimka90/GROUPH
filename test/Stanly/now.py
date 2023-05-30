import datetime

def get_birthday():
    # Prompt the user to input their birthday
    year = int(input("Enter the year you were born (YYYY): "))
    month = int(input("Enter the month you were born (MM): "))
    day = int(input("Enter the day you were born (DD): "))

    # Return the birthday as a date object
    return datetime.date(year, month, day)

# Create a dictionary to store birthdays
birthdays = {}

while True:
    # Prompt the user to enter a command
    print("Enter a command:")
    print("1. Add a birthday")
    print("2. View all birthdays")
    print("3. Exit")
    
    command = int(input(">>>"))

    if command == 1:
        # Prompt the user to input their name and birthday
        name = input("Enter your name: ")
        birthday = get_birthday()
        birthdays[name] = birthday

        print("Birthday added for {}".format(name))
        
    elif command == 2:
        # Print a list of all birthdays
        if len(birthdays) == 0:
            print("There are no birthdays to display.")
        else:
            print("Birthdays:")
            today = datetime.date.today()
            for name, birthday in birthdays.items():
                next_birthday = datetime.date(today.year, birthday.month, birthday.day)
                days_until_birthday = (next_birthday - today).days
                if days_until_birthday < 0:  # birthday has already occurred this year
                    next_birthday = datetime.date(today.year + 1, birthday.month, birthday.day)
                    days_until_birthday = (next_birthday - today).days
                
                if days_until_birthday == 0:
                    print("- {} : Happy birthday today!".format(name))
                else:
                    print("- {} : {} days until next birthday".format(name, days_until_birthday))
                
    elif command == 3:
        # Exit the program
        print("Goodbye!")
        break
    else:
        # Invalid command
        print("Invalid command. Please try again.")