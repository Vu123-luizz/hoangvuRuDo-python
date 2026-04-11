from .employee import Employee

class Intern(Employee):
    def __init__(self, emp_id, name, age, salary):
        super().__init__(emp_id, name, age, salary)

    def calculate_salary(self):
        return self.salary