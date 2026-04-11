def validate_age(age):
    if age < 18 or age > 65:
        raise ValueError("Tuổi phải từ 18 đến 65")


def validate_salary(salary):
    if salary <= 0:
        raise ValueError("Lương phải > 0")