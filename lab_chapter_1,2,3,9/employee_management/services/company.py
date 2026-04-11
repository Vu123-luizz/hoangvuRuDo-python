class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_all(self):
        if not self.employees:
            print("Chưa có nhân viên")
            return

        for emp in self.employees:
            print(emp)

    def find_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None

    def delete_employee(self, emp_id):
        emp = self.find_employee(emp_id)
        if emp:
            self.employees.remove(emp)
        else:
            print("Không tìm thấy nhân viên")