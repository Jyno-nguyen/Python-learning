
#? __init__ là người đi gom nguyên liệu (thuộc tính)
#? __dict__ chính là cái kho (tập từ điển) lưu trữ lại toàn bộ số nguyên liệu đó

class TaiKhoanGame:
    def __init__(self, ten_tai_khoan):
        self.ten_tai_khoan = ten_tai_khoan
        self.cap_do = 1
        self.vang = 0

if __name__ == "__main__":
    p1 = TaiKhoanGame("Yasuo_Ganh_Team") # Đúc một nhân vật
    print(p1.__dict__) #{'ten_tai_khoan': 'Yasuo_Ganh_Team', 'cap_do': 1, 'vang': 0}


#* Vậy nếu có nhiều intance thì sao, Mỗi intance sẽ có 1 __dict__ riêng biệt độc lập
class XeHoi:
    def __init__(self, ten_xe, gia_ban):
        self.ten_xe = ten_xe
        self.gia_ban = gia_ban

if __name__ == "__main__":
    # Đúc ra 3 chiếc xe khác nhau (3 instance)
    xe_1 = XeHoi("VinFast VF8", 1200)
    xe_2 = XeHoi("Toyota Camry", 1000)
    xe_3 = XeHoi("Porsche 911", 7000)

    print("Dict xe 1:", xe_1.__dict__)
    print("Dict xe 2:", xe_2.__dict__)
    print("Dict xe 3:", xe_3.__dict__)
