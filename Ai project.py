import calendar
import numpy as np
import random
def event():
    def show_calendar(year, month):
    #    print("\n", calendar.month_name[month], year)
        print(calendar.month(year, month))

    def add_event(events):
        date = input("Enter the date (DD-MM-YYYY) to add an event: ")
        event = input("Enter the event: ")
        print("\n")
        events[date] = event

    def view_event(events):
        date = input("Enter the date (DD-MM-YYYY) to view the event: ")
        if date in events:
            print(f"Event on {date}: {events[date]}\n")
        else:
            print("No event found on this date.\n")

    def main():
        events = {}
        year = 2024
        month = 12
        while True:
            show_calendar(year, month)
            print("\n1. Add Event")
            print("2. View Event")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                add_event(events)
            elif choice == '2':
                view_event(events)
            elif choice == '3':
                break
            else:
                print("Invalid choice.")
    main()

def Sal():
        
    def get_employee_data():
        employee_names = []
        employee_salaries = []

        num_employees = int(input("Enter the number of employees: "))

        for i in range(num_employees):
            name = input("Enter employee name: ")
            salary = float(input(f"Enter salary for {name}: "))
            employee_names.append(name)
            employee_salaries.append(salary)

        return np.array(employee_names), np.array(employee_salaries)

    employee_names, employee_salaries = get_employee_data()

    total_payroll = np.sum(employee_salaries)
    average_salary = np.mean(employee_salaries)

    threshold = 50000
    above_threshold = employee_names[employee_salaries > threshold]
    below_threshold = employee_names[employee_salaries <= threshold]

    print("\nEmployee Salary Management System")
    print("-----------------------------------\n")
    print(f"Total Payroll Cost: INR {total_payroll}")
    print(f"Average Salary: INR {average_salary:.2f}\n")

    print(f"Employees Earning Above INR {threshold}:")
    for name in above_threshold:
        print(f"  - {name}")

    print(f"\nEmployees Earning Below or Equal to INR {threshold}:")
    for name in below_threshold:
        print(f"  - {name}")


def pswd():

    def generate_password(length):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        password = "".join(random.choice(characters) for _ in range(length))
        return password

    while True:
        try:
            length = int(input("\nEnter the desired password length (or '0' to exit): "))
            if length == 0:
                print("Goodbye!")
                break
            elif length < 6:
                print("Password should be at least 6 characters long.")
            else:
                print(f"Generated Password: {generate_password(length)}")
        except ValueError:
            print("Please enter a valid number.")


    
while True:
    print("\n")
    print("press 1 for emplyee salary system")
    print("press 2 for event manager")
    print("press 3 for password generating")
    print("press 0 to exit")
    a=int(input("... :- "))
    if a==0:
        print("Have a nice day!")
        break
    elif a == 1:
        Sal()
    elif a == 2:
        event()
    elif a == 3:
        pswd()
    else:
        print("invalid input")
        