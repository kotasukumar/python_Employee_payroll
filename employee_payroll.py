# Employee payroll program
import random


class Employee:
    MIN_WORKING_DAYS = 20
    MIN_WORKING_HOUR = 100
    WAGE_PER_HOUR = 20
    FULL_WORKING_HOUR = 8
    PART_TIME_WORKING_HOURS = 8
    total_wage = total_hours = total_days = 0

    while total_hours <= MIN_WORKING_HOUR and total_days <= MIN_WORKING_DAYS:
        random_number = random.randint(0, 2)
        if random_number == 0:
            total_hours += FULL_WORKING_HOUR
            total_days += 1
            total_wage += FULL_WORKING_HOUR * WAGE_PER_HOUR
            print("Full time Employee is present and his wage is: ", FULL_WORKING_HOUR * WAGE_PER_HOUR)
        elif random_number == 1:
            total_hours += PART_TIME_WORKING_HOURS
            total_days += 1
            total_wage += PART_TIME_WORKING_HOURS * WAGE_PER_HOUR
            print("Part time Employee is present and his wage is: ", PART_TIME_WORKING_HOURS * WAGE_PER_HOUR)
        elif random_number == 2:
            print("Employee is absent wage is zero")
        else:
            print("Invalid")


if __name__ == "__main__":
    print("Welcome to employee payroll program")
    result = Employee()
    print("Monthly wage and details of the employee is", result.total_wage)
