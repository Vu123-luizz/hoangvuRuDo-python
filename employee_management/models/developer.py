from models.employee import Employee

class Developer(Employee):
    def calculate_salary(self):
        return self.salary * 1.5