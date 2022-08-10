# Employee payroll program
import random
import sys


class Employee:

    def __init__(self, company_name, min_working_hours, min_working_days, wage):
        self.MIN_WORKING_DAYS = min_working_days
        self.MIN_WORKING_HOUR = min_working_hours
        self.WAGE_PER_HOUR = wage
        self.company_name = company_name
        self.returned_value = self.calculate()

    def calculate(self):
        FULL_WORKING_HOUR = 8
        PART_TIME_WORKING_HOURS = 8
        total_wage = total_hours = total_days = 0
        daily_wage = []
        while total_hours <= self.MIN_WORKING_HOUR and total_days <= self.MIN_WORKING_DAYS:
            random_number = random.randint(0, 2)
            if random_number == 0:
                total_hours += FULL_WORKING_HOUR
                total_days += 1
                total_wage += FULL_WORKING_HOUR * self.WAGE_PER_HOUR
                daily_wage.append(FULL_WORKING_HOUR * self.WAGE_PER_HOUR)
            elif random_number == 1:
                total_hours += PART_TIME_WORKING_HOURS
                total_days += 1
                total_wage += PART_TIME_WORKING_HOURS * self.WAGE_PER_HOUR
                daily_wage.append(FULL_WORKING_HOUR * self.WAGE_PER_HOUR)
            elif random_number == 2:
                daily_wage.append(0)
            else:
                print("Invalid")

        details = [self.company_name, total_wage, total_hours, total_days, daily_wage]
        return details


if __name__ == "__main__":
    print("Welcome to employee payroll program")
    company_list = []
    while True:
        user_input = int(input("Choice a number\n 0: Enter the details\n 1: To exit\n"))
        if user_input == 0:
            name = str(input("Enter name of the company: "))
            minimum_working_hours = int(input("Enter minimum working hours of your company: "))
            minimum_working_days = int(input("Enter minimum working days of your company: "))
            per_day_wage = int(input("Enter per day wage of your company: "))
            result = Employee(name, minimum_working_hours, minimum_working_days, per_day_wage)
            company_list.append(result.returned_value)
            print("Monthly wage and details of the employee is", company_list)
        else:
            sys.exit()

