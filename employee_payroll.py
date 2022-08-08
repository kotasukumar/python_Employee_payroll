# Employee payroll program
import random


def employee():
    WAGE_PER_HOUR = 20
    FULL_WORKING_HOUR = 8
    PART_TIME_WORKING_HOURS = 4
    total_wage = 0
    for i in range(20):
        random_number = random.randint(0, 2)
        if random_number == 0:
            total_wage += FULL_WORKING_HOUR * WAGE_PER_HOUR
            print("Full time Employee is absent and his wage is: ", FULL_WORKING_HOUR * WAGE_PER_HOUR)
        elif random_number == 1:
            total_wage += PART_TIME_WORKING_HOURS * WAGE_PER_HOUR
            print("Part time Employee is present and his wage is: ", PART_TIME_WORKING_HOURS * WAGE_PER_HOUR)
        elif random_number == 2:
            print("Employee is absent wage is zero")
        else:
            print("Invalid")

    return total_wage


if __name__ == "__main__":
    print("Welcome to employee payroll program")
    print(employee())
