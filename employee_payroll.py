# Employee payroll program
import random

print("Welcome to employee payroll program")
random_number = random.randint(0, 1)

if random_number == 0:
    print("Employee is absent")
elif random_number == 1:
    print("Employee is present")
else:
    print("Invalid")

