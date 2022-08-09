# Employee payroll program
import random


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
        while total_hours <= self.MIN_WORKING_HOUR and total_days <= self.MIN_WORKING_DAYS:
            random_number = random.randint(0, 2)
            if random_number == 0:
                total_hours += FULL_WORKING_HOUR
                total_days += 1
                total_wage += FULL_WORKING_HOUR * self.WAGE_PER_HOUR
                print("Full time Employee is present and his wage is: ", FULL_WORKING_HOUR * self.WAGE_PER_HOUR)
            elif random_number == 1:
                total_hours += PART_TIME_WORKING_HOURS
                total_days += 1
                total_wage += PART_TIME_WORKING_HOURS * self.WAGE_PER_HOUR
                print("Part time Employee is present and his wage is: ", PART_TIME_WORKING_HOURS * self.WAGE_PER_HOUR)
            elif random_number == 2:
                print("Employee is absent wage is zero")
            else:
                print("Invalid")

        return total_wage, total_hours, total_days


if __name__ == "__main__":
    print("Welcome to employee payroll program")
    result = Employee("Amazon", 100, 20, 20)
    print("Monthly wage and details of the employee is", result.company_name, result.returned_value)
    result = Employee("flipKart", 200, 20, 30)
    print("Monthly wage and details of the employee is", result.company_name, result.returned_value)
