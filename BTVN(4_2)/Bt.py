# B1: Đọc n dòng đầu tiên của file

filename = input("Nhập tên file: ")
n = int(input("Nhập số dòng cần đọc: "))

try:
    with open(filename, "r", encoding="utf-8") as f:
        for i in range(n):
            line = f.readline()
            if not line:
                break
            print(line.strip())
except FileNotFoundError:
    print("Không tìm thấy file!")

# B2: Ghi và đọc lại nội dung file

filename = input("Nhập tên file: ")

print("Nhập đoạn văn (kết thúc bằng dòng trống):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

# Ghi vào file
with open(filename, "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

# Đọc lại và hiển thị
print("\nNội dung file:")
with open(filename, "r", encoding="utf-8") as f:
    print(f.read())

# B3a: In nội dung file trên 1 dòng

with open("demo_file1.txt", "r", encoding="utf-8") as f:
    content = f.read().replace("\n", " ")
    print(content)

# B3b: In từng dòng

with open("demo_file1.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())