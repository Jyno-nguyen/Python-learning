
#* CLASS: Ở đó ta khai báo các thuộc tính (attribute) và phương thức (method) nhằm miêu tả để từ đó ta tạo ra được những object (đối tượng)
class SieuNhan:
    pass

sieu_nhan_A = SieuNhan() # sieu_nhan_A chính là một object thuộc lớp SieuNhan

#!trong Python, bạn hoàn toàn có thể tự ý gán thêm thuộc tính cho một đối tượng ở bên ngoài mà không cần khai báo trước nó trong class
#!Người ta gọi đây là Thuộc tính động (Dynamic Attributes).
sieu_nhan_A.ten = "Sieu nhan do"
sieu_nhan_A.vu_khi = "Kiem"
sieu_nhan_A.mau_sac = "Do"

print("Ten cua sieu nhan la:",sieu_nhan_A.ten)
print("Sieu nhan mau:", sieu_nhan_A.mau_sac)
print("Su dung vu khi:", sieu_nhan_A.vu_khi)

sieu_nhan_B=SieuNhan()
print(sieu_nhan_B.ten) #!Lỗi vì 'SieuNhan' object has no attribute 'ten'




#* Mở rộng vấn đề, ta cần khai báo khoảng 1000 siêu nhân
#* Giải sử một siêu nhân có 3 thuộc tính như trên vị chi ta sẽ mất 3000 dòng khai báo
#* Đôi lúc những thuộc tính của đối tượng không dễ dàng để khai báo một cách đơn giản như vậy.

#?Hàm constructor (initialize method)
class SieuNhan:
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = "Sieu nhan " + para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    def xin_chao(self):
        return "Xin chao, ta chinh la " + self.ten

sieu_nhan_A = SieuNhan("do", "Kiem", "Do")

print("Ten cua sieu nhan la:",sieu_nhan_A.ten)
print("Sieu nhan mau:", sieu_nhan_A.mau_sac)
print("Su dung vu khi:", sieu_nhan_A.vu_khi)
print(sieu_nhan_A.xin_chao()) # vì nó là hàm nên nhớ là hãy thêm () để gọi hàm





#* Bạn nên nhớ rằng mỗi khi có một đối tượng nào đó gọi một hàm thì luôn luôn tối thiểu sẽ có một argument được gửi vào hàm đó chính là chính đối tượng đó
#* Nếu hàm đó không có parameter nhận thì sẽ sinh lỗi, còn nếu dư argument 
#* (vì ta không lường trước được có một argument là chính đối tượng được ngầm gửi vào) thì vẫn sẽ có lỗi tràn argument. Còn nếu mà gửi vào vẫn không có lỗi thì…Bug này nặng khó fix đây.
class SieuNhan:
    # Bạn cố tình không viết chữ 'self' vào ngoặc
    def tung_chieu(): 
        print("Tung chiêu!")

sieu_nhan_A = SieuNhan()
sieu_nhan_A.tung_chieu() 
# 🚨 SẬP CODE NGAY! Lỗi: TypeError: tung_chieu() takes 0 positional arguments but 1 was given
#!Bạn thấy trong ngoặc tung_chieu() rõ ràng trống không (0 tham số). Nhưng Python ngầm ném sieu_nhan_A vào, khiến máy tính hiểu là có 1 argument được gửi vào. 1 gửi vào mà 0 nhận → Sập.

class SieuNhan:
    # Hàm này thiết kế chỉ nhận đúng 1 chiêu thức b, cộng với self là 2
    def tung_chieu(self, ten_chieu):
        print(f"Tung {ten_chieu}")

sieu_nhan_A = SieuNhan()
sieu_nhan_A.tung_chieu("Đấm móc", "Đá xoáy")
# 🚨 SẬP CODE! Lỗi: TypeError: tung_chieu() takes 2 positional arguments but 3 were given











#? KHAI BÁO THUỘC TÍNH LỚP TRONG OOP
#? KHAI BÁO THUỘC TÍNH NGAY TRONG LỚP KHÔNG CẦN THÔNG QUA CONSTRUCTOR

class SieuNhan:
    sm=50
    def __init__(seft,khai_bao_ten,khai_bao_vu_khi,khai_bao_mau):
        seft.ten=khai_bao_ten
        seft.vu_khi=khai_bao_vu_khi
        seft.mau=khai_bao_mau
sieunhan_A=SieuNhan("Siêu nhân đỏ","Súng","Vàng")
print(sieunhan_A.ten)
print(sieunhan_A.sm) #50
print(SieuNhan.sm)   #50

SieuNhan.sm=40 #!TUY NHIÊN CÁCH NÀY THƯỜNG KHÔNG ĐƯỢC SỬ DỤNG MÀ SẼ DÙNG @classmethods
print(sieunhan_A.sm) #40
print(SieuNhan.sm)   #40
#! khi thay đổi giá trị một thuộc tính được khai báo trong lớp thông qua lớp thì thuộc tính ở toàn bộ đối tượng thuộc lớp đó sẽ được cập nhật lại giá trị mới được thay đổ


#!Bạn cũng có thể cập nhật trong hàm constructors
class SieuNhan:
    so_thu_tu=1
    def __init__(seft,kb_ten,kb_vu_khi,kb_mau):
        seft.ten=kb_ten
        seft.vu_khi=kb_vu_khi
        seft.mau=kb_mau
        seft.stt=SieuNhan.so_thu_tu
        SieuNhan.so_thu_tu+=1
sieunhan_A=SieuNhan("SN Đỏ","Búa","Đỏ")
sieunhan_B=SieuNhan("SN Vang","Súng","Vàng")
print(sieunhan_A.ten,sieunhan_A.stt) # SN Đỏ 1
print(sieunhan_B.ten,sieunhan_B.stt) # SN Vang 2
print(SieuNhan.so_thu_tu)            # 3


#!Cập nhật giá trị thuộc tính thông qua đối tượng
sieunhan_A.sm=40 #Đã có sự khác biệt. Khi bạn thay đổi giá trị thuộc tính của một đối tượng, thì chỉ có đối tượng đó bị thay đổi, còn cái “khuôn mẫu” của chúng ta vẫn như vậ












#? CÁC PHƯƠNG THỨC TRONG OOP

#? khi gắn một cái mũ @classmethod thì có nghĩa phương thức đặt dứoi nó chỉ phục vụ cho class not seft
class sieunhan:
    stt=1
    @classmethod
    def cap_nhat(cls,stt_new):
        sieunhan.stt=stt_new
sieunhan.cap_nhat(10)

#!Cũng có thể dùng đối tượng trong cls đó
SIEUNHAN=sieunhan()
SIEUNHAN.cap_nhat(10)


#*TUY NHIÊN CHỨC NĂNG CHÍNH CỦA CLASS METHOD LÀ LẬP ĐỐI TƯỢNG

#*ta muốn khởi tạo một siêu nhân, tuy nhiên một số siêu nhân lại có các thông tin không được tường minh rõ ràng mà lại được lưu dưới dạng một list

class sieunhan:
    def __init__(self,kb_ten,kb_vu_khi,kb_mau):
        self.ten=kb_ten 
        self.vk=kb_vu_khi 
        self.mau=kb_mau
    @classmethod
    def from_s(cls,s):
        lst=s.split("-")
        lst_final=[s.strip() for s in lst]
        ten,vu_khi,mau=lst_final
        return cls(ten,vu_khi,mau) # cls(ten,vu_khi,mau) = sieunhan(ten,vu_khi,mau)
s="Siêu nhân đỏ - kiếm - đỏ"
SIEUNHAN_A=sieunhan.from_s(s)
print(SIEUNHAN_A.ten)      #Siêu nhân đỏ
print(SIEUNHAN_A.vk)       #kiếm
print(SIEUNHAN_A.mau)      #đỏ
print(SIEUNHAN_A.__dict__) #'ten': 'Siêu nhân đỏ', 'vk': 'kiếm', 'mau': 'đỏ'}
#!__dict__ ở đâu ra?



"""🔹 Regular Method (Phương thức thông thường / Instance Method)
Đây là loại phương thức mặc định và phổ biến nhất trong Class. Nó đại diện cho hành vi của một đối tượng cụ thể.
Tham số bắt buộc: Phải có self đứng đầu.
Quyền hạn: Có thể đọc và thay đổi toàn bộ thuộc tính riêng của đối tượng đó (thông qua self.ten_thuoc_tinh).
Cách gọi: Bắt buộc phải gọi thông qua một đối tượng đã được đúc ra: doi_tuong.ten_method()."""

"""🔹 Static Method (Phương thức tĩnh)
Khi bạn gắn chiếc mũ @staticmethod lên đầu một hàm trong Class, bạn đang tạo ra một "hàm tự do" đúng nghĩa nhưng được đặt nhờ hộ khẩu bên trong Class.
Tham số bắt buộc: Không có! Không cần self, cũng không cần cls. Nó nhận tham số vào và xử lý như một hàm bình thường ngoài phố.
Quyền hạn: "Vô sản". Nó bị mù thông tin, không biết đối tượng self đang có gì, cũng không biết Class cls đang giữ biến nào. Nó hoàn toàn cô lập.
Cách gọi: Gọi trực tiếp bằng tên Class mà không cần tạo đối tượng: Class_Name.ten_method()."""

class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    @staticmethod
    def bien_hinh():
        print("1, 2, 3. Sieu nhan bien hinh")

sieu_nhan_A = SieuNhan("Sieu nhan do", "Kiem", "Do")
sieu_nhan_A.bien_hinh()
