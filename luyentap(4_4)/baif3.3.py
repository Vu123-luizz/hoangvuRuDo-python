_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

_new_list = []
for x in _tuple:
    # Nếu x chưa có trong list mới thì mới thêm vào
    if x not in _new_list:
        _new_list.append(x)

_new_tuple = tuple(_new_list)
print("Kết quả (loại bỏ trùng lặp):", _new_tuple)

