"""
# Welcome to this Mini Project.
- Your best friend is founding a startup and he needs you to help him implement
    a payroll system.
- The developer he hired last month only completed part of the program because 
    he had a personal issue and he had to quit the job before completing it.
- Your task is to:
    - Complete the classes in the existing payroll program by including the
        necessary class attributes.
- Analysis:
    - First, you need to analyze the calculate_payroll function in the code 
        below. 
    - You can also find this function in the downloadable Python file.
    - Based on this code, you must determine the required class attributes. 
        After meeting with your friend, you determined that all the missing 
        attributes are shared by all the instances of each class, so they 
        should be class attributes.
    - Assign realistic values to them.
    - In the payroll function, the class attributes are accessed with the 
        <instance>.<attribute> syntax because we will be working with a 
        list of instances of multiple classes in a for loop.
    - An employee can be either a Programmer or an Assistant in our program 
        but, since the attributes that we will be working with are class 
        attributes, their values will be the same for all the instances of the
        same class.
"""

class Programmer:
    
    # Add the class attributes
    salary = 130000
    monthly_bonus = 5000
    
    def __init__(self, name, age, address, phone, programming_languages):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.programming_languages = programming_languages

class Assistant:
    
    # Add the class attributes
    salary = 70000
    monthly_bonus = 1000
    
    def __init__(self, name, age, address, phone, is_bilingual):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.is_bilingual = is_bilingual

# Function that prints the monthly salary of each worker
# and the total amount that the startup owner has to pay per month.
def calculate_payroll(employees):
    total = 0
    print("\n========= Welcome to our Payroll System =========\n")
    # Iterate over the list of instances to calculate
    # and display the monthly salary of each employee,
    # and add the monthly salary to the total for this month.
    for employee in employees:
        salary = round(employee.salary / 12, 2) + employee.monthly_bonus
        print(employee.name.capitalize() + "'s salary is: $" + str(salary))
        total += salary
    # Display the total
    print("\nThe total payroll this month will be: $", total)

# Instances (employees)
jack = Programmer("Jack", 45, "5th Avenue", "555-563-345", ["Python", "Java"])
isabel = Programmer("Isabel", 25, "6th Avenue", "234-245-853", ["JavaScript"])
nora = Assistant("Nora", 23, "7th Avenue", "562-577-333", True)

# List of instances
employees = [jack, isabel, nora]

# Function call (Passing the list of instances as argument)
calculate_payroll(employees)