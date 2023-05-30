from datetime import datetime

# List to store birthdays in the format (name, date)
birthdays = []

def add_birthday():
    name = input("Enter the person's name: ")
    date_str = input("Enter the birthday (DD-MM-YYYY): ")
    date = datetime.strptime(date_str, "%d-%m-%Y")
    birthdays.append((name, date))
    print("Birthday added successfully!")

def view_birthdays():
    print("Birthdays:")
    for name, date in birthdays:
        print(f"{name}: {date.strftime('%d-%m-%Y')}")

def check_birthday():
    name = input("Enter the person's name: ")
    today = datetime.now().date()

    for b_name, b_date in birthdays:
        if b_name.lower() == name.lower():
            if b_date.month < today.month or (b_date.month == today.month and b_date.day < today.day):
                print(f"{name}'s birthday has already passed.")
            else:
                remaining_days = (b_date) -(today)
                print(f"{name}'s birthday is in {remaining_days} day(s).")
            return

    print("Birthday not found.")

while True:
    print("\nMenu:")
    print("1. Add a birthday")
    print("2. View birthdays")
    print("3. Check if a birthday has passed")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_birthday()
    elif choice == "2":
        view_birthdays()
    elif choice == "3":
        check_birthday()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


1.start
2.WHILE True
    print()
    READ FEEt
    IF FEET<0 THEN
        PRINT
    ENDIF
    IF FEEt ==string
        THEN 
        BREAK
    ENDIF