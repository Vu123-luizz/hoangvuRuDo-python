class HocVien:
    # a) Khởi tạo class với các thuộc tính tương ứng
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) Phương thức show_info trả về đầy đủ thông tin
    def show_info(self):
        info = (f"--- Thông tin học viên ---\n"
                f"Họ tên: {self.ho_ten}\n"
                f"Ngày sinh: {self.ngay_sinh}\n"
                f"Email: {self.email}\n"
                f"Điện thoại: {self.dien_thoai}\n"
                f"Địa chỉ: {self.dia_chi}\n"
                f"Lớp: {self.lop}\n")
        return info

    # c) Phương thức change_info với tham số mặc định
    def change_info(self, dia_chi='Yên Bài', lop='IT14.1'):
        self.dia_chi = dia_chi
        self.lop = lop
        print(f"-> Đã cập nhật thông tin mới cho học viên {self.ho_ten}!")

# d) Chương trình chính
if __name__ == "__main__":
    
    hv1 = HocVien(
        ho_ten="Đoàn Hoàng Vũ", 
        ngay_sinh="22/07/2005", 
        email="20230488@eaut.edu.vn", 
        dien_thoai="0779318057", 
        dia_chi="Yên Bái", 
        lop="IT14.1"
    )

    # Gọi phương thức hiển thị thông tin ban đầu
    print(hv1.show_info())

    # Gọi phương thức thay đổi thông tin (sử dụng tham số mặc định)
    hv1.change_info()

    # Hiển thị lại thông tin sau khi thay đổi
    print(hv1.show_info())