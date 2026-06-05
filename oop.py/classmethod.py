
"""1. #*Hàm khởi tạo thay thế (Alternative Constructor) + Bộ lọc dữ liệu nâng cao
Như bạn đã biết, nó tạo ra các "cửa phụ" để biến đổi dữ liệu bẩn/lạ thành đối tượng sạch. Để giải quyết triệt để vấn đề "chuỗi thừa/lỗi" mà bạn vừa lo lắng
người ta sẽ kết hợp @classmethod với khối lệnh try-except hoặc if-else.
Nếu dữ liệu hợp lệ, nó trả về đối tượng. Nếu dữ liệu rác, nó từ chối khởi tạo và ném ra cảnh báo sạch sẽ thay vì làm sập app.

2. #*Quản lý cấu hình toàn hệ thống (Global Configuration)
Khi bạn muốn thay đổi một cài đặt nào đó mà tất cả các đối tượng sinh ra sau đó đều phải tuân theo, bạn sẽ dùng @classmethod để thay đổi biến Class.
Ví dụ thực tế: Cài đặt tỷ giá USD của ngân hàng, cài đặt chế độ hiển thị (Sáng/Tối) của một ứng dụng, hoặc cài đặt kết nối Database.

3. #!Hỗ trợ kế thừa thông minh (Inheritance Friendly)
Đây là lý do vì sao Python đẻ ra @classmethod (dùng cls) thay vì dùng @staticmethod (hàm tĩnh không truyền gì).
Khi một Class Con kế thừa từ Class Cha, nếu Class Con gọi @classmethod của Cha, tham số cls sẽ tự động biến thành Class Con
Nhờ vậy, đối tượng được sinh ra sẽ mang đúng dòng máu của Class Con chứ không bị ép làm Class Cha."""







"""Cấu hình tỷ giá ngân hàng (CurrencyConverter)
Đầu vào: __init__(self, amount_usd)
Yêu cầu: Tạo một biến class usd_to_vnd = 25000. Viết một @classmethod tên là update_exchange_rate(cls, new_rate) để ngân hàng cập nhật tỷ giá mới khi thị trường biến động. Viết một hàm to_vnd(self) để quy đổi số tiền USD của đối tượng ra VND dựa trên tỷ giá chung hiện tại."""
class CurrencyConverter:
    usd_to_vnd = 25000

    def __init__(self, amount_usd):
        if amount_usd < 0:
            raise ValueError("Số tiền USD không được âm!")
        self.amount_usd = amount_usd

    @classmethod
    def update_exchange_rate(cls, new_rate):
        if not isinstance(new_rate, (int, float)) or new_rate <= 0:
            raise ValueError("Tỷ giá mới phải là một số dương!")
        cls.usd_to_vnd = new_rate
        print(f"[Hệ Thống Ngân Hàng]: Tỷ giá vừa được cập nhật mới: 1 USD = {new_rate:,} VND")

    def to_vnd(self):
        return self.amount_usd * CurrencyConverter.usd_to_vnd









"""Bài 4: Đăng ký tài khoản từ Cú pháp SMS (UserAccount)
Đầu vào __init__: username, phone_number
Yêu cầu: Viết một @classmethod tên là from_sms(cls, sms_text). Khách hàng đăng ký qua SMS gõ cú pháp: "DK tùng_đẹp_trai 0912345678". Hàm này phải tự tách chuỗi, bỏ chữ "DK", lấy ra username và sđt để tự tạo đối tượng UserAccount."""
class UserAccount:
    def __init__(self,username,phone_number):
        self.username=username
        self.phone_number=phone_number
    @classmethod
    def from_sms(cls,sms_text):
        try:
            data=[d for d in sms_text.split()]
            if len(data)!=3 or data[0].upper()!="DK":
                print("Cu phap khong hop le.")
                return None
            
            username=data[1]
            phone_number=data[2] #!Nên để số điện thoại là 1 chuỗi
            if not phone_number.isdigit():
                print("Số điện thoại chỉ bao gồm các số")
                return None
            
            return cls(username,phone_number)
        except Exception: #!Đại diện cho tất cả các lỗi runtime nên nếu lạm dụng sẽ không biết đang mắc lỗi gì mà sửa
            print("Khong the xu ly chuoi rac.")
            return None

    def __str__(self):
        return f"Người dùng: {self.username} | SĐT : {self.phone_number}"
    




#* Đặt phòng khách sạn
class HotelRoom:
    _book_room=[]
    def __init__(self,room_number):
        self.room_number=room_number
        #HotelRoom._book_room.append(room_number) #!Nếu để đây sẽ lỗi vì nhập gì cũng sẽ append
    @classmethod
    def book_room(cls,room_number):
        if room_number in cls._book_room:
            print("Phong da co nguoi dat")
            return None
        HotelRoom._book_room.append(room_number)
        return cls(room_number)
    def __str__(self):
        return f"Phòng số: {self.room_number} đã đặt thành công"
    

#*SmartDate
class SmartDate:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
    @classmethod
    def from_strg(cls,date_str):
        data=date_str.split("/")
        day,month,year=map(int,data)
        return cls(day,month,year)
# Gọi cửa phụ để nạp chuỗi thô
ngay_le = SmartDate.from_strg("30/04/1975")

# In kiểm tra thuộc tính riêng của đối tượng xem đã được ép thành số nguyên chưa
print(ngay_le.day)   # Kết quả kỳ vọng: 30 (kiểu int)
print(ngay_le.month) # Kết quả kỳ vọng: 4  (kiểu int)
print(ngay_le.year)  # Kết quả kỳ vọng: 1975 (kiểu int)
print(type(ngay_le.day))
        




