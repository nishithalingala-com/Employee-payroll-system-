class EmployeePayroll:

    def __init__(self, name, emp_id, basic_salary, bonus, deduction):
        self.name = name
        self.emp_id = emp_id
        self.basic_salary = basic_salary
        self.bonus = bonus
        self.deduction = deduction

    def calculate_salary(self):
        gross_salary = self.basic_salary + self.bonus
        net_salary = gross_salary - self.deduction
        return net_salary

    def display_details(self):
        net_salary = self.calculate_salary()

        print("\n===== EMPLOYEE PAYROLL DETAILS =====")
        print(f"Employee Name : {self.name}")
        print(f"Employee ID   : {self.emp_id}")
        print(f"Basic Salary  : ₹{self.basic_salary}")
        print(f"Bonus         : ₹{self.bonus}")
        print(f"Deduction     : ₹{self.deduction}")
        print(f"Net Salary    : ₹{net_salary}")


while True:

    name = input("Enter Employee Name: ")
    emp_id = input("Enter Employee ID: ")

    basic_salary = float(input("Enter Basic Salary: "))
    bonus = float(input("Enter Bonus Amount: "))
    deduction = float(input("Enter Deduction Amount: "))

    employee = EmployeePayroll(
        name,
        emp_id,
        basic_salary,
        bonus,
        deduction
    )

    employee.display_details()

    choice = input("\nDo you want to add another employee? (yes/no): ")

    if choice.lower() != "yes":
        print("Exiting Payroll System...")
        break
