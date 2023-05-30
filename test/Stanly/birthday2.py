import datetime

# Dictionary to store birthdays
birthdays = {}

def get_todays_date():
    now = datetime.datetime.now()
    return now.date()

def get_upcoming_birthdays():
    today = get_todays_date()
    upcoming = []
    for name, dob in birthdays.items():
        next_birthday = datetime.date(today.year, dob.month, dob.day)
        if next_birthday < today:
            next_birthday = datetime.date(today.year + 1, dob.month, dob.day)
        days_until_birthday = (next_birthday - today).days
        upcoming.append((name, next_birthday, days_until_birthday))
    upcoming.sort(key=lambda x: x[2])  # Sort by days until birthday
    return upcoming

def add_birthday():
    name = input("Enter the name: ")
    dob = input("Enter the date of birth (YYYY-MM-DD): ")
    year, month, day = map(int, dob.split('-'))
    birthday = datetime.date(year, month, day)
    birthdays[name] = birthday
    print("Birthday added successfully!")

def print_birthdays():
    upcoming = get_upcoming_birthdays()
    print("Upcoming Birthdays:")
    for name, next_birthday, days_until_birthday in upcoming:
        print(f"{name}: {next_birthday.strftime('%B %d')}, {days_until_birthday} days to go")

# Main program loop
while True:
    print("\n1. Add Birthday")
    print("2. View Birthdays")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        add_birthday()
    elif choice == '2':
        print_birthdays()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

