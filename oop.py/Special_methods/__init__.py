

#? __init__(seft,...) : initialize - khởi tạo: NHIỆM VỤ LÀ GÁN GIÁ TRỊ BAN ĐẦU (THUỘC TÍNH ) CHO ĐỐI TƯỢNG NGAY KHI VỪA ĐƯỢC KHỞI TẠO
class SieuNhan:
    pass # Class trống rỗng
sn1 = SieuNhan()# Đúc ra một ông trống rỗng
#! Bạn phải tự tay gán từng thuộc tính bên ngoài luồng code chính
sn1.ten = "Siêu Nhân Đỏ"
sn1.mau = 100

class SieuNhan:
    # Định nghĩa sẵn: Đúc siêu nhân là phải có Tên và Máu!
    def __init__(self, ten_nhap_vao, mau_nhap_vao):
        self.ten = ten_nhap_vao  # Gán tên cho ông siêu nhân mới
        self.mau = mau_nhap_vao  # Gán máu cho ông siêu nhân mới

# Giờ gộp tất cả vào đúng 1 dòng lệnh đúc:
sn1 = SieuNhan("Siêu Nhân Đỏ", 100)
sn2 = SieuNhan("Siêu Nhân Xanh", 80)

#!NHỮNG THÔNG TIN MÀ AI CŨNG GIỐNG NHAU KHI MỚI KHỞI TẠO THÌ NÊN GÁN CỨNG LUÔN 
class TaiKhoanGame:
    def __init__(self, ten_tai_khoan):
        self.ten_tai_khoan = ten_tai_khoan
        self.cap_do = 1  # Mặc định gán cứng luôn
        self.vang = 0    # Mặc định gán cứng luôn

#! if - else trong __init__
class tng:
    def __init__(self,ten,so_tien_nap):
        self.ten=ten
        if so_tien_nap< 50000:
            raise ValueError("Số tiền nạp tối thiểu phải là 50,000VNĐ")
        else:
            self.so_tien_nap=so_tien_nap

#!class SieuNhan:
    # Nếu người dùng không truyền 'mau', mặc định ông này sẽ có 100 máu
    def __init__(self, ten, mau=100):
        self.ten = ten
        self.mau = mau
# Cách 1: Truyền đủ cả 2
sn1 = SieuNhan("Đỏ", 150) # sn1 có 150 máu

# Cách 2: Lười truyền máu
sn2 = SieuNhan("Xanh")    # sn2 tự động có 100 máu

#!VÀ ĐẶC BIỆT LƯU Ý __init__ KHÔNG CÓ LỆNH RETURN