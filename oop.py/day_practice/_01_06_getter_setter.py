
"""Cặp đôi "Tự động dịch đơn vị" (Nhiệt độ C và F)
Giả sử bên trong kho ẩn, bạn luôn lưu trữ nhiệt độ theo độ C (self._do_c). 
Nhưng bạn muốn người dùng ở ngoài có thể đọc và ghi theo độ F (do_f). 
Lúc này, mọi công thức tính toán biến đổi chỉ xoay quanh đúng một mình dữ liệu nhiệt độ này thôi:"""

class NhietDo:
    def __init__(self,do_c_ban_dau):
        self._do_c=do_c_ban_dau
    @property
    def do_f(self):
        return (self._do_c*9/5)+32
    @do_f.setter
    def do_f(self,do_f_moi):
        do_c_moi=(do_f_moi-32)*5/9
        if do_c_moi<-273.15:
            raise ValueError("Nhiệt độ không thể dưới độ âm tuyệt đối!")
        self._do_c=do_c_moi
t = NhietDo(25) # Khởi tạo 25 độ C
print(f"Độ F hiện tại: {t.do_f}°F") # Đầu ra: 77.0°F

t.do_f = 104 # Người dùng đổi hẳn sang 104 độ F -> Kích hoạt Setter tính toán bẻ ngược
print(f"Kho ẩn độ C thực tế lúc này: {t._do_c}°C") # Đầu ra: 40.0°C (Tự động chuyển về 40 độ C!)









"""Bạn hãy tạo một Class TaiKhoanNganHang gồm:
Hàm __init__(self, chu_tai_khoan, so_du_ban_dau): Ép dữ liệu phải đi qua bộ gác cổng ngay từ đầu.
Cặp Getter/Setter cho so_du:
Setter: Phải kiểm tra xem số dư mới nạp vào có phải là số (int hoặc float) hay không và có lớn hơn hoặc bằng 0 hay không. Nếu sai thì raise ValueError("Số dư không hợp lệ").
Một Getter đứng một mình tên là trang_thai_tai_khoan:
Hàm này sẽ tính toán động dựa trên so_du: Nếu số dư > 1.000.000.000 (1 tỷ), trả về chuỗi "VIP". Ngược lại, trả về chuỗi "STANDARD"."""

class TaiKhoanNganHang:
    def __init__(self, chu_tai_khoan, so_du_ban_dau):
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du_ban_dau # Ép qua setter

    @property
    def so_du(self):
        return self._so_du

    @so_du.setter
    def so_du(self, so_tien_nap):
        if not isinstance(so_tien_nap, (int, float)):
            raise TypeError("Số dư phải là số!")
        if so_tien_nap < 0:
            raise ValueError("Số tiền nạp phải lớn hơn hoặc bằng 0!")
        self._so_du = so_tien_nap

    @property
    def trang_thai_tai_khoan(self):
        # Tính toán động chuẩn xác dựa trên số ẩn
        return "VIP" if self._so_du > 1000000000 else "STANDARD"

TK_A = TaiKhoanNganHang("Nguyen Van A", 1000000)

# Muốn in ra đẹp? Ta format ngay tại lệnh print ở ngoài
print(f"Số dư: {TK_A.so_du:,}đ") # Số dư: 1,000,000đ
print(f"Trạng thái: {TK_A.trang_thai_tai_khoan}") # STANDARD

TK_A.so_du += 500000 
print(f"Số dư sau khi nạp thêm: {TK_A.so_du:,}đ") # 1,500,000đ









"""Hệ thống chấm điểm và Học lực (StudentReport)
Đề bài: Tạo class StudentReport để quản lý điểm số của một học sinh.
Thuộc tính đầu vào: math_score (Điểm Toán) và literature_score (Điểm Văn).
Yêu cầu cho Setter:
Cả 2 đầu điểm phải là số và nằm trong đoạn từ 0 đến 10. Nếu sai, ném lỗi ValueError.
Yêu cầu cho Getter đứng một mình (Tính toán động liên hoàn):
Thuộc tính average_score: Tự động tính điểm trung bình hệ số 1: ĐTB,xếp loại"""

class StudentReport:
    def __init__(self,math_score,literature_score):
        self.math_score=math_score
        self.literature_score=literature_score
    def _check(self,gia_tri):
        if not isinstance(gia_tri,(int,float)) or not 0<=gia_tri<=10:
            raise ValueError("Dữ liệu nhập không hợp lệ")
        return gia_tri
    @property
    def math_score(self):
        return self._math_score
    @math_score.setter 
    def math_score(self,gia_tri_nhap):
        self._math_score=self._check(gia_tri_nhap)

    @property
    def literature_score(self):
        return self._literature_score
    @literature_score.setter 
    def literature_score(self,gia_tri_nhap):
        self._literature_score=self._check(gia_tri_nhap)
    
    @property
    def dtb(self):
        return round((self._literature_score + self._math_score)/2,2)
    
    @property
    def xep_loai(self):
        # Viết ngắn thì nhanh nhưng chưa tường minh, code dài khó chỉnh sửa
        # return "gioi" if self.dtb>=8 else "yeu" if self.dtb<5 else "kha" 
        diem = self.dtb
        if diem >= 8.0:
            return "GIỎI"
        elif diem >= 5.0:
            return "KHÁ"
        else:
            return "YẾU"
        








"""Hộp số tự động Ô tô (CarGearbox)
Đề bài: Mô phỏng hộp số tự động của một chiếc ô tô thông minh thông qua class CarGearbox.
Thuộc tính đầu vào: current_gear (Số hiện tại, nhận các chuỗi ký tự: "P", "R", "N", "D").
Yêu cầu cho Setter:
current_gear: Phải nằm trong 4 ký tự trên. Nếu nhập ký tự khác, ném lỗi ValueError.
Logic nâng cao: Xe đang chạy thì không được gài số lùi phanh đột ngột. Do đó, nếu số hiện tại đang là "D" (Đang chạy trước), người dùng không được phép chuyển thẳng sang số "R" (Số lùi) hoặc "P" (Đỗ xe). 
Nếu cố tình làm vậy, hãy ném lỗi RuntimeError("Không thể chuyển số nguy hiểm khi đang chạy!"). Muốn chuyển sang "R" hoặc "P", họ phải chuyển về số trung gian "N" trước.
Yêu cầu cho Getter: Trả về số hiện tại kèm theo trạng thái tiếng Việt (Ví dụ: ⚙️ Số hiện tại: D (Chạy thẳng))"""

class RuntimeError(Exception): pass
class CarGearbox:
    def __init__(self,current_gear):
        
        self._current_gear=None
        self.current_gear=current_gear   

    @property
    def current_gear(self):
        return self._current_gear
    
    @current_gear.setter
    def current_gear(self,che_do):
        val=che_do.strip().upper()
        if val not in {"P", "R", "N", "D"}:
            raise ValueError("Khong hop le.")
        if self._current_gear is not None:
            for current,dangerous_new in zip(("R","D"),(("P","D"),("P","R"))):
                if self._current_gear==current and val in dangerous_new:
                    raise RuntimeError("Không thể chuyển số nguy hiểm khi đang chạy!")
        self._current_gear=val

        #!Hoặc dùng tuple
        cac_cap_cam=(("D","R"),("D","P"),("R","D"),("R","P"))
        if self._current_gear is not None:
            cap_hien_tai=(self._current_gear,val)
            if cap_hien_tai in cac_cap_cam:
                raise RuntimeError("Không thể chuyển số nguy hiểm khi đang chạy!")
        self._current_gear=val

        #!HOẶC
        ban_do_cam = {"D": {"R", "P"},
                      "R": {"D", "P"},
                      "N": set(),
                      "P": set()}

        if self._current_gear is not None:
            # Tra cứu thẳng vào bản đồ xem số mới (val) có bị cấm bởi số cũ không
            if val in ban_do_cam[self._current_gear]:
                raise RuntimeError("🚨 CẢNH BÁO: Không thể chuyển số nguy hiểm khi đang chạy!")

        self._current_gear = val


kia_k3=CarGearbox("D")
print(kia_k3.current_gear)
try:
    kia_k3.current_gear="X"
except ValueError:
    pass
kia_k3.current_gear="R"
print(kia_k3.current_gear)









"""Bài 1: Hệ thống quản lý tài khoản User (UserProfile)
Đề bài: Tạo class UserProfile để quản lý thông tin đăng ký của người dùng.
Thuộc tính đầu vào: username và email.
Yêu cầu cho Setter:
username: Phải là một chuỗi có độ dài từ 3 đến 15 ký tự, không được chứa khoảng trắng. Nếu vi phạm, ném lỗi ValueError.
email: Phải là một chuỗi và bắt buộc phải chứa ký tự @ (kiểm tra cơ bản). Nếu không có, ném lỗi ValueError.
Yêu cầu cho Getter:
username: Luôn trả về chuỗi đã được viết thường hoàn toàn (lowercase).
email: Để bảo mật, Getter không trả về email gốc mà trả về dạng ẩn danh (masked). Ví dụ: nguyenvanan@gmail.com ➡️ trả về n...n@gmail.com (chỉ giữ lại ký tự đầu và ký tự cuối của phần tên trước dấu @).
"""
from collections import Counter
class UserProfile:
    def __init__(self,username,email):
        self.username=username
        self.email=email
    @property
    def username(self):
        return self._username.lower()
    @username.setter
    def username(self,user_input):
        data=user_input.strip()
        if " " in data or not 3<=len(data)<=15:
            raise ValueError("loi")
        self._username=data
    def __len__(self):
        return len(self._email)
    @property
    def email(self):

        ten_user, ten_mien = self._email.split("@")
        
        dau = ten_user[0]
        cuoi = ten_user[-1] 
        so_dau_sao = len(ten_user) - 2

        if so_dau_sao <= 0:
            return self._email
            
        return f"{dau}{'*' * so_dau_sao}{cuoi}@{ten_mien}"
    @email.setter
    def email(self,email_input):
        data=email_input.strip()
        data_check=dict(Counter(data))
        if " " in data_check or "@" not in data_check:
            raise ValueError("loi")
        if data_check["@"]>1 or "@gmail.com" not in data:
            raise ValueError("loi")
        self._email=data
user1=UserProfile("Nguyenvietha","nguyenviethahaha49@gmail.com")
print(user1.email)

        
        
    




""" Bài 3: Công cụ dịch dòng điện Máy tính (HexColor)
Đề bài: Trong lập trình giao diện, màu sắc thường được lưu dưới dạng chuỗi Hex (Ví dụ: "#FFFFFF" là màu trắng, "#000000" là màu đen). Hãy tạo class HexColor.
Thuộc tính đầu vào: hex_code.
Yêu cầu cho Setter:
Kiểm tra chuỗi nhập vào có bắt đầu bằng dấu # hay không và tổng độ dài chuỗi có đúng bằng 7 ký tự hay không. Nếu sai, ném lỗi ValueError.
Yêu cầu cho Getter:
hex_code: Luôn trả về chuỗi có các ký tự chữ cái được viết hoa hoàn toàn (uppercase) (Ví dụ: người dùng nhập #ff00aa thì getter trả về #FF00AA).
Getter đứng một mình: Tạo một thuộc tính ảo tên là is_dark_color. Giả sử quy tắc hệ thống quy định: nếu chuỗi hex_code có chứa 2 ký tự đầu tiên (sau dấu #) là "00" (tức là không có sắc đỏ) thì coi đó là màu tối ➡️ trả về True, ngược lại trả về False.
"""

class HexColor:
    def __init__(self,hex_code):
        self.hex_code=hex_code
    
    @property
    def hex_code(self):
        return self._hex_code
    @hex_code.setter
    def hex_code(self,ma_code):
        ma_check=ma_code.strip()
        if not ma_check.startswith("#") or len(ma_check)!=7:
            raise ValueError("Loi ma code")
        self._hex_code=ma_check.upper()
    @property
    def is_dark_color(self):
        return self._hex_code[1:3]=="00"
mau1=HexColor("#001234")
print(mau1.is_dark_color)
        
        

    
    

