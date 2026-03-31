import os
import re
import subprocess

# ===== 1. INPUT ĐỀ BÀI =====
de_bai = """
Bài 4: Viết chương trình nhập một số nguyên dương và kiểm tra xem số đó có chia hết cho 2 hoặc cho 3 hoặc cả hai hay không?
Bài 5: Viết chương trình giải phương trình bậc 2: a*x*x + b*x + c = 0. Trong đó 3 tham số a,b,c được nhập từ bàn phím.
"""

# ===== 2. TÁCH BÀI =====
bai_list = re.findall(r"Bài\s*(\d+):(.+?)(?=Bài|\Z)", de_bai, re.S)

# ===== 3. HÀM SINH CODE =====
def generate_code(bai_so, noi_dung):
    if bai_so == "4":
        return '''n = int(input("Nhập số nguyên dương: "))

if n % 2 == 0 and n % 3 == 0:
    print("Chia hết cho cả 2 và 3")
elif n % 2 == 0:
    print("Chia hết cho 2")
elif n % 3 == 0:
    print("Chia hết cho 3")
else:
    print("Không chia hết cho 2 và 3")
'''
    elif bai_so == "5":
        return '''import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Vô số nghiệm")
        else:
            print("Vô nghiệm")
    else:
        print("Nghiệm x =", -c/b)
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("2 nghiệm:", x1, x2)
    elif delta == 0:
        print("Nghiệm kép:", -b/(2*a))
    else:
        print("Vô nghiệm")
'''
    else:
        return "# Chưa hỗ trợ bài này"

# ===== 4. TẠO FILE =====
for bai_so, noi_dung in bai_list:
    filename = f"Bai{bai_so}.py"
    code = generate_code(bai_so, noi_dung.strip())

    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"Đã tạo {filename}")

# ===== AUTO GIT (FIX CHUẨN) =====
def run_git(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

try:
    print("🔄 Kiểm tra thay đổi...")

    subprocess.run(["git", "add", "."], check=True)

    status = run_git(["git", "status", "--porcelain"])

    if status.stdout.strip() == "":
        print("✅ Không có thay đổi → không cần commit")
    else:
        print("📦 Có thay đổi → đang commit...")
        subprocess.run(["git", "commit", "-m", "Auto update code"], check=True)

    print("⬇️ Đang pull từ GitHub...")
    subprocess.run(["git", "pull", "--rebase"], check=True)

    print("⬆️ Đang push lên GitHub...")
    subprocess.run(["git", "push"], check=True)

    print("🚀 Hoàn tất!")

except subprocess.CalledProcessError as e:
    print("❌ Lỗi Git:", e)

except Exception as e:
    print("❌ Lỗi hệ thống:", e)