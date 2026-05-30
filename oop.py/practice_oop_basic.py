
"""BÀI 1: Quản lý Tài khoản Chiến thần (Cơ bản về Class & Object)
Yêu cầu: Tạo một class TaiKhoanGame để quản lý người chơi.
Thuộc tính: ten_tai_khoan, cap_do (mặc định ban đầu là 1), và vang (mặc định ban đầu là 0).
Phương thức:
nhan_thuong(so_vang): Cộng thêm số vàng nhận được vào thuộc tính vang.
tang_cap(): Tăng cap_do lên 1 cấp, đồng thời thưởng thêm cho người chơi 500 vàng.
Thử thách: Đúc ra 2 đối tượng người chơi khác nhau, cho một người nhận thưởng, một người tăng cấp và in thuộc tính của họ ra màn hình để kiểm tra dữ liệu."""
class TKG:
    def __init__(self,ten_tai_khoan):
        self.ten_tai_khoan=ten_tai_khoan
        self.cap_do=1
        self.vang=0

    def nhan_thuong(self,so_vang):
        self.vang+=so_vang
        print(f"{self.ten_tai_khoan} hiện đang có số vàng {self.vang}")

    def tang_cap(self):
        self.cap_do+=1
        self.vang+=500
        print(f"{self.ten_tai_khoan} đã tăng lên cấp độ {self.cap_do}: vàng hiện có {self.vang}")

if __name__=="__main__":
    per1=TKG("nvh_đẹp_trai")
    per2=TKG("Đức_Anh_ngu")

    per1.nhan_thuong(1000) #nvh_đẹp_trai hiện đang có số vàng 1000
    per2.tang_cap()        #Đức_Anh_ngu đã tăng lên cấp độ 2: vàng hiện có 500
    
    per1.nhan_thuong(1000) #nvh_đẹp_trai hiện đang có số vàng 2000
    print(per1.__dict__) #{'ten_tai_khoan': 'nvh_đẹp_trai', 'cap_do': 1, 'vang': 2000}
    print(per2.__dict__) #{'ten_tai_khoan': 'Đức_Anh_ngu', 'cap_do': 2, 'vang': 500}









"""BÀI 2: Quản lý Kho xe của Đại lý (Biến Class vs Biến Instance)
Yêu cầu: Tạo một class XeHoi để quản lý các xe trong showroom.
Biến của Class (Class Variable): Tạo một biến chung đặt tên là tong_so_xe ban đầu bằng 0 để đếm tổng số xe đại lý đang có.
Thuộc tính riêng (Instance Variable): Mỗi khi đúc một con xe (__init__), người dùng phải truyền vào ten_xe và gia_ban. Đồng thời, cứ mỗi lần có xe mới được đúc ra, biến tong_so_xe của Class phải tự động tăng lên 1.
Thử thách: Tạo ra 3 con xe khác nhau. Sau đó in ra màn hình biến tong_so_xe trực tiếp từ Class để xem máy tính có đếm chuẩn là 3 hay không."""

class XeHoi:
    tong_so_xe=0
    def __init__(seft,ten_xe,gia_ban,so_luong):
        seft.ten=ten_xe
        seft.gia=gia_ban
        seft.soluong=so_luong
        XeHoi.tong_so_xe+=so_luong
if __name__=="__main__":
    xe1=XeHoi("Civic",1000,5)
    xe2=XeHoi("Rolls Royce",10000,1)
    xe3=XeHoi("Bentayga",9000,2)
    print(XeHoi.tong_so_xe) #8
    print(xe1.__dict__)
    print(xe2.__dict__)
    print(xe3.__dict__)









"""BÀI 3: Nhà máy Chế tạo Chiến giáp (Ứng dụng Class Method)
Yêu cầu: Tạo một class ChienGiap.
Thuộc tính gốc: ten_giap, he_phong_thu.
Nhiệm vụ: Viết một @classmethod tên là tu_chuoi_thong_tin(cls, chuoi_nhap). Phương thức này sẽ nhận vào một chuỗi văn bản dạng "Gundam-Vũ Trụ".
Logic xử lý: Bên trong classmethod, bạn hãy dùng lệnh .split("-") để băm chuỗi đó ra thành tên và hệ, sau đó chủ động gọi hàm khởi tạo để đúc và trả về (return) một đối tượng ChienGiap mới toanh.
Thử thách: Tạo đối tượng bằng cách gọi trực tiếp: giap_vip = ChienGiap.tu_chuoi_thong_tin("IronMan-Công Nghệ")."""
class ChienGiap:
    def __init__(self,ten_giap,he_thong_thu):
        self.ten=ten_giap
        self.giap=he_thong_thu
    @classmethod
    def tu_chuoi_thong_tin(cls, chuoi_nhap):
        ten_giap,he_thong_thu=chuoi_nhap.strip().split("-")
        return cls(ten_giap,he_thong_thu)
if __name__=="__main__":
    giap_vip=ChienGiap.tu_chuoi_thong_tin("IRonMan-Công Nghệ")
    print(giap_vip.__dict__)









"""BÀI 4: Tiến hóa Thú cưng (Kế thừa & Ghi đè Phương thức)
Yêu cầu: * Tạo Class Cha là ThuCung có thuộc tính ten. Class này có một phương thức tên là tan_cong() → In ra màn hình: "Cào cào cấu cấu!".
Tạo Class Con là KhungLong kế thừa từ ThuCung. Vì là Khủng Long nên bạn phải ghi đè (override) lại phương thức tan_cong() → Định nghĩa lại logic để in ra: "Phun lửa thiêu rụi đối thủ!".
Thử thách: Đúc 1 con thú cưng thường và 1 con khủng long. Gọi hàm tan_cong() của cả hai để thấy sự khác biệt logic giữa Cha và Con."""

class ThuCung:
    def __init__(self,ten_thu_cung):
        self.ten=ten_thu_cung
    
    def tan_cong(self):
        print("Cào cào cấu cấu.")
    
class KhungLong(ThuCung):
    def __init__(self,ten_khung_long,mau):
        super().__init__(ten_khung_long)
        self.mau=mau
    def tan_cong(self):
        print("Phun lửa để thiêu rụi đối thủ")
        super().tan_cong() #Lấy thêm thuộc tính của thằng cha
if __name__=="__main__":
    tho=ThuCung("Thỏ")
    khung_long=KhungLong("Khủng long Bạo chúa","đen")
    print(khung_long.__dict__)
    tho.tan_cong()
    khung_long.tan_cong()










"""BÀI 5: Gia tộc Ninja (Đa kế thừa & Chống trùng tên)
Yêu cầu: Chúng ta có 2 môn phái lớn:
Class HeHoa: Có phương thức phun_lua() → In ra: "Hỏa độn!". Có phương thức XemThongTin() → In ra: "Hệ Hỏa hệ chiến!".
Class HeThuy: Có phương thức phun_nuoc() → In ra: "Thủy độn!". Có phương thức XemThongTin() → In ra: "Hệ Thủy hệ thủ!".
Nhiệm vụ: Tạo Class Con tên là NinjaTruyenNhan kế thừa từ cả hai hệ trên, nhưng ưu tiên xếp HeThuy đứng trước HeHoa.
Thử thách: 1. Gọi thử xem tên Ninja đó có xài được cả phun_lua() lẫn phun_nuoc() không?
2. Gọi phương thức trùng tên XemThongTin() xem máy tính sẽ in ra dòng chữ của hệ nào?"""

class HeHoa:
    def phun_lua(self):
        print("Hoả độn")
    def xem_thong_tin(self):
        print("Hệ hoả hệ chiến")
class HeThuy:
    def phun_nuoc(self):
        print("Thuỷ độn")
    def xem_thong_tin(self):
        print("hệ nước hệ thủ")
class Ninja(HeHoa,HeThuy):
    pass
if __name__=="__main__":
    ninja_rua=Ninja()
    ninja_rua.phun_lua()      #Hoả độn
    ninja_rua.phun_nuoc()     #Thuỷ độn
    ninja_rua.xem_thong_tin() #Hệ hoả hệ chiến