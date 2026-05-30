
#* inheritance: Kế thừa 
#* Ví dụ như siêu nhân gao đều có thuộc tính của siêu nhân, và có thêm những thuộc tính nâng cao hơn

#?
class sieu_nhan:
    sm=100
    def __init__(seft,ten,mau):
        seft.ten=ten
        seft.mau=mau
class sieu_nhan_gao(sieu_nhan): #!sieu_nhan_gao là phần kế thừa thuộc tính của sieu_nhan
    pass
gao_do=sieu_nhan_gao("Siêu nhân gao đỏ","Đỏ") #!Cách tạo đối tượng 
print(gao_do.ten)

#Nếu muốn thêm param trong constructor thì có 2 cách
#!C1
class sieu_nhan:
    sm=100
    def __init__(seft,ten,mau):
        seft.ten=ten
        seft.mau=mau
class sieu_nhan_gao(sieu_nhan): 
    def __init__(seft,ten,mau,vk):
        seft.ten=ten
        seft.mau=mau
        seft.vk=vk
gao_do=sieu_nhan_gao("Siêu nhân gao đỏ","Đỏ","Búa") 
print(gao_do.vk)

#!C2
class sieu_nhan:
    sm=100
    def __init__(seft,ten,mau):
        seft.ten=ten
        seft.mau=mau
class sieu_nhan_gao(sieu_nhan):  
    def __init__(seft,ten,mau,vk):
        super().__init__(ten,mau) #class cha có gì thì cần truyền hết vào không hơn không kém
        seft.vk=vk                #Thêm phần còn thiếu
gao_do=sieu_nhan_gao("Siêu nhân gao đỏ","Đỏ","Búa") 


#!Vậy nếu muốn thêm nhưng cũng có thuộc tính mà mình không muốn lấy thì làm thế nào
class sieu_nhan:
    sm=100
    def __init__(seft,ten,mau):
        seft.ten=ten
        seft.mau=mau
class sieu_nhan_gao(sieu_nhan):  
    def __init__(seft,ten,vk):
        super().__init__(ten,mau="") #Tôi không muốn lấy màu vậy tôi sẽ gán cứng giá trị của màu
                                     #Có thể để "Không có" để khi in ra thì mn biết
                                     #! Không nên để None vì nếu lỡ truyền vào và có liên quan đến tính toán có thể sai
gao_do=sieu_nhan_gao("Siêu nhân gao đỏ","Đỏ","Búa") 
print(gao_do.mau) # chuỗi rỗng 






#? KẾ THỪA PHƯƠNG THỨC
class cha:
    def thong_tin(self):
        print("Đang đi đón con")
class con(cha):
    def thong_tin(self):
        print("Đang chờ cha đón")
#? ƯU TIÊN DÙNG PHƯƠNG THỨC CỦA CON NẾU CON CÓ PHƯƠNG THỨC TRÙNG TÊN VỚI PHƯƠNG THỨC CỦA CHA
father=cha()
boy=con()
father.thong_tin() # Đang đi đón con
boy.thong_tin()    # Đang chờ cha đón

#? CÒN NẾU MUỐN THÊM PHƯƠNG THỨC THÌ THÊM THÔI
class cha:
    def thong_tin(self):
        print("Nhà nhiều tiền")
class con(cha):
    pass
father.thong_tin() # Nhà nhiều tiền
boy.thong_tin()    # Nhà nhiều tiền

#! Thêm phương thức cho con
class cha:
    def thong_tin(self):
        print("Nhà nhiều tiền")
class con(cha):
    def deptrai(self):
        return True
    

#!Nếu muốn gọi method cha trong lúc đang thực hiện method của con
class cha:
    def thong_tin(self):
        print("Nhà nhiều tiền")
class con(cha):
    def co_nguoi_yeu(self):
        super().thong_tin()
        print("Lại còn đẹp trai")
boy=con()
boy.co_nguoi_yeu() #Nhà nhiều tiền \ Lại còn đẹp trai

#!HOẶC DÙNG SEFT VÌ thằng con được kế thừa từ cha nên seft có thể dùng để gọi phương thức của cha
#!Với mục đích là kết hợp nhiều hành động liên tiếp
class cha:
    def thong_tin(self):
        print("Nhà nhiều tiền")
class con(cha):
    def co_nguoi_yeu(self):
        self.thong_tin() 
        print("Lại còn đẹp trai")
boy=con()
boy.co_nguoi_yeu() #Nhà nhiều tiền \ Lại còn đẹp trai


#!VẬY NẾU KHÔNG MUỐN LẤY PHƯƠNG THỨC CỦA CHA THÌ SAO, MUỐN CHE GIẤU,....
class SieuNhanCha:
    def bien_hinh_khong_lo(self):
        print("🌋 Biến khổng lồ 50m!")# Tuyệt chiêu gốc của Cha (Ai cũng thấy)

    # 1. TUYỆT CHIÊU CHE GIẤU: Thêm __ vào trước tên hàm
    def __gong_noi_luc_bi_truyen(self): # Con hoàn toàn "bị mù", không hề biết sự tồn tại của hàm này để kế thừa
        print("🧘 Đang vận công bí mật...")

class SieuNhanTiHon(SieuNhanCha):
    # 2. TUYỆT CHIÊU GHI ĐÈ ĐỂ CHẶN: Viết trùng tên phương thức của Cha
    def bien_hinh_khong_lo(self): # Nhưng bên trong dùng 'raise AttributeError' để chủ động đánh sập code nếu cố tình gọi
        raise AttributeError("❌ Lỗi logic: Siêu nhân tí hon không thể biến khổng lồ!")

ant_man = SieuNhanTiHon()

    # THỬ NGHIỆM 1: Cố tình gọi hàm đã BỊ CHẶN ở Class Con
ant_man.bien_hinh_khong_lo() # Dòng này chạy sẽ SẬP CODE ngay lập tức và in ra dòng chữ báo lỗi do bạn thiết kế

    # THỬ NGHIỆM 2: Cố tình gọi hàm đã BỊ GIẤU từ Class Cha
#ant_man.__gong_noi_luc_bi_truyen() # Dòng này chạy cũng SẬP CODE vì Python báo không tìm thấy phương thức này tồn tại








#? NÓ ĐÃ CÓ CHA RỒI BÂY CÓ CẢ MẸ THÌ SAO: "Multiple Inheritance"
class SieuNhanCha:
    def __init__(self):
        print(" Khởi tạo gen của Cha")
    def tan_cong(self):
        print(" Đấm phát chết luôn (Tuyệt chiêu của Cha)!")
    def thong_tin_chung(self):
        print(" Ta là Cha đây!")
class SieuNhanMe:
    def __init__(self):
        print(" Khởi tạo gen của Mẹ")
    def hoi_mau(self):
        print(" Tự động hồi 100% máu (Phép thuật của Mẹ)!")
    # Hàm này trùng tên hoàn toàn với hàm bên phía Class Cha
    def thong_tin_chung(self):
        print(" Ta là Mẹ đây!")


#* Quy tắc: Thằng nào viết bên TRÁI trước (SieuNhanCha) sẽ có quyền ưu tiên cao hơn!
class SieuNhanCon(SieuNhanCha, SieuNhanMe):
    def __init__(self):
        # Khi đa kế thừa, super() mặc định chỉ gọi đến __init__ của Class đầu tiên (Cha)
        super().__init__() 
        print("👶 Đứa Con xuất hiện!")

dua_be = SieuNhanCon()

dua_be.tan_cong()  # Xài được chiêu của Cha
dua_be.hoi_mau()   # Xài được chiêu của Mẹ
dua_be.thong_tin_chung()   # "Ta là Cha đây!" vì SieuNhanCha được viết trước bên trái.

print(SieuNhanCon.__mro__) # Dòng này để xem thứ tự ưu tiên tìm kiếm phương thức của Python
                           #<class '__main__.SieuNhanCon'>, <class '__main__.SieuNhanCha'>, <class '__main__.SieuNhanMe'>, <class 'object'>)
