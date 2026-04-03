# B5: Đếm số lần xuất hiện của các từ trong file

# Đọc file
with open("demo_file2.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Tách các từ
words = content.split()

# Đếm số lần xuất hiện
count_dict = {}

for word in words:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

# In kết quả
print(count_dict)