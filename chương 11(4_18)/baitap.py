
import sqlite3

# Kết nối database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# =============================
# Tạo bảng (nếu chưa có)
# =============================
cursor.execute("""
CREATE TABLE IF NOT EXISTS department (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT,
    location TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    job TEXT,
    salary REAL,
    dept_id INTEGER,
    FOREIGN KEY(dept_id) REFERENCES department(dept_id)
)
""")

# =============================
# Thêm dữ liệu mẫu (tránh trùng)
# =============================
cursor.execute("""
INSERT OR IGNORE INTO department (dept_id, dept_name, location)
VALUES (10, 'HR', 'Hanoi'),
       (20, 'Finance', 'HCM'),
       (30, 'Sales', 'Danang'),
       (50, 'IT', 'Hanoi')
""")

cursor.execute("""
INSERT OR IGNORE INTO employee (emp_id, name, job, salary, dept_id)
VALUES (1, 'KING', 'MANAGER', 3000, 10),
       (2, 'CLARK', 'MANAGER', 2000, 20),
       (3, 'MILLER', 'CLERK', 1000, 30)
""")

# =============================
# A) Lấy danh sách MANAGER
# =============================
print("=== DANH SÁCH MANAGER ===")
cursor.execute("SELECT * FROM employee WHERE job = 'MANAGER'")
for row in cursor.fetchall():
    print(row)

# =============================
# B) Thêm phòng ban của bạn
# =============================
cursor.execute("""
INSERT OR IGNORE INTO department (dept_id, dept_name, location)
VALUES (?, ?, ?)
""", (99, "MyDept", "Hanoi"))

# =============================
# C) Thêm bản thân (không trùng)
# =============================
cursor.execute("""
INSERT OR IGNORE INTO employee (emp_id, name, job, salary, dept_id)
VALUES (?, ?, ?, ?, ?)
""", (999, "Hoang Vu", "DEVELOPER", 1000, 99))

# =============================
# D) Update CLARK → thành bạn
# =============================
cursor.execute("""
UPDATE employee
SET name = ?, job = ?, salary = ?, dept_id = ?
WHERE name = 'CLARK'
""", ("Hoang Vu", "DEVELOPER", 1500, 99))

# =============================
# E) Xóa MILLER
# =============================
cursor.execute("DELETE FROM employee WHERE name = 'MILLER'")

# =============================
# Hiển thị kết quả cuối
# =============================
print("\n=== DANH SÁCH NHÂN VIÊN SAU KHI XỬ LÝ ===")
cursor.execute("SELECT * FROM employee")
for row in cursor.fetchall():
    print(row)

# Lưu & đóng
conn.commit()
conn.close()

print("\n=== HOÀN THÀNH ===")
