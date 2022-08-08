# Employee payroll program
import random


def employee(random_number):
    WAGE_PER_HOUR = 20
    WORKING_HOUR = 8
    if random_number == 0:
        print("Employee is absent and his wage is: ", WORKING_HOUR * WAGE_PER_HOUR)
    elif random_number == 1:
        print("Employee is present and his wage is zero")
    else:
        print("Invalid")


if __name__ == "__main__":
    print("Welcome to employee payroll program")
    number = random.randint(0, 1)
    employee(number)
