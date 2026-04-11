from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from services.company import Company
from utils.validators import *

company = Company()

def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Thêm nhân viên")
        print("2. Hiển thị danh sách")
        print("3. Tìm nhân viên")
        print("4. Xóa nhân viên")
        print("5. Thoát")

        try:
            choice = int(input("Chọn: "))

            if choice == 1:
                emp_id = input("ID: ")
                name = input("Tên: ")
                age = int(input("Tuổi: "))
                salary = float(input("Lương: "))

                validate_age(age)
                validate_salary(salary)

                print("1. Manager 2. Developer 3. Intern")
                role = int(input("Chọn chức vụ: "))

                if role == 1:
                    emp = Manager(emp_id, name, age, salary)
                elif role == 2:
                    emp = Developer(emp_id, name, age, salary)
                else:
                    emp = Intern(emp_id, name, age, salary)

                company.add_employee(emp)
                print("✔ Thêm thành công")

            elif choice == 2:
                company.show_all()

            elif choice == 3:
                emp_id = input("Nhập ID: ")
                emp = company.find_employee(emp_id)
                print(emp)

            elif choice == 4:
                emp_id = input("Nhập ID cần xóa: ")
                if company.delete_employee(emp_id):
                    print("✔ Đã xóa")

            elif choice == 5:
                break

        except Exception as e:
            print("❌ Lỗi:", e)

menu()

#--python main.py