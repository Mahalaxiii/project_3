class Employee:
    def __init__(self, emp_id: str, name: str, base_salary: float):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self) -> float:
        return self.base_salary

    def generate_payslip(self) -> str:
        return (
            f"--- Payslip ---\n"
            f"Employee ID: {self.emp_id}\n"
            f"Name: {self.name}\n"
            f"Net Salary: ${self.calculate_salary():.2f}"
        )


class FullTimeEmployee(Employee):
    def __init__(self, emp_id: str, name: str, base_salary: float, bonus: float = 0.0):
        super().__init__(emp_id, name, base_salary)
        self.bonus = bonus

    def calculate_salary(self) -> float:
        return self.base_salary + self.bonus

    def generate_payslip(self) -> str:
        return (
            f"--- Full-Time Employee Payslip ---\n"
            f"Employee ID: {self.emp_id}\n"
            f"Name: {self.name}\n"
            f"Base Salary: ${self.base_salary:.2f}\n"
            f"Bonus: ${self.bonus:.2f}\n"
            f"Total Net Salary: ${self.calculate_salary():.2f}"
        )


class PartTimeEmployee(Employee):
    def __init__(self, emp_id: str, name: str, hourly_rate: float, hours_worked: float):
        super().__init__(emp_id, name, 0.0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self) -> float:
        return self.hourly_rate * self.hours_worked

    def generate_payslip(self) -> str:
        return (
            f"--- Part-Time Employee Payslip ---\n"
            f"Employee ID: {self.emp_id}\n"
            f"Name: {self.name}\n"
            f"Hourly Rate: ${self.hourly_rate:.2f}\n"
            f"Hours Worked: {self.hours_worked}\n"
            f"Total Net Salary: ${self.calculate_salary():.2f}"
        )


class PayrollSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee: Employee):
        if employee.emp_id in self.employees:
            raise ValueError("Employee ID already exists.")
        self.employees[employee.emp_id] = employee

    def search_employee(self, emp_id: str) -> Employee:
        if emp_id not in self.employees:
            raise KeyError("Employee not found.")
        return self.employees[emp_id]

    def save_payroll_data(self) -> dict:
        return {
            emp_id: {
                "name": emp.name,
                "salary": emp.calculate_salary()
            }
            for emp_id, emp in self.employees.items()
        }


def main():
    payroll = PayrollSystem()

    while True:
        print("\n--- Employee Payroll System ---")
        print("1. Add Full-Time Employee")
        print("2. Add Part-Time Employee")
        print("3. Calculate Salary")
        print("4. Generate Payslip")
        print("5. Search Employee")
        print("6. Save & View Payroll Data")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        try:
            if choice == '1':
                emp_id = input("Enter Employee ID: ").strip()
                name = input("Enter Name: ").strip()
                base_salary = float(input("Enter Base Salary: "))
                bonus = float(input("Enter Bonus: ") or 0.0)
                
                emp = FullTimeEmployee(emp_id, name, base_salary, bonus)
                payroll.add_employee(emp)
                print(f"Success: Full-time employee {name} added.")

            elif choice == '2':
                emp_id = input("Enter Employee ID: ").strip()
                name = input("Enter Name: ").strip()
                hourly_rate = float(input("Enter Hourly Rate: "))
                hours_worked = float(input("Enter Hours Worked: "))
                
                emp = PartTimeEmployee(emp_id, name, hourly_rate, hours_worked)
                payroll.add_employee(emp)
                print(f"Success: Part-time employee {name} added.")

            elif choice == '3':
                emp_id = input("Enter Employee ID: ").strip()
                emp = payroll.search_employee(emp_id)
                print(f"Calculated Salary for {emp.name}: ${emp.calculate_salary():.2f}")

            elif choice == '4':
                emp_id = input("Enter Employee ID: ").strip()
                emp = payroll.search_employee(emp_id)
                print("\n" + emp.generate_payslip())

            elif choice == '5':
                emp_id = input("Enter Employee ID: ").strip()
                emp = payroll.search_employee(emp_id)
                print(f"Found: ID -> {emp.emp_id}, Name -> {emp.name}, Salary -> ${emp.calculate_salary():.2f}")

            elif choice == '6':
                data = payroll.save_payroll_data()
                print("\n--- Saved Payroll Data Summary ---")
                for emp_id, info in data.items():
                    print(f"ID: {emp_id} | Name: {info['name']} | Salary: ${info['salary']:.2f}")

            elif choice == '7':
                print("Exiting Payroll System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
