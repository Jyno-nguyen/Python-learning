
#* getter: Chỉ cho đọc
# @property: được gọi là decorator: #?Biến một hàm thành một thuộc tính 
# Bình thường khi gọi hàm cần oject.method() khi qua @property thì oject.attribute và đó là getter 
# ta dùng @property để khai báo một getter
class NhanVien:
    def __init__(self, luong_co_ban):
        self.luong_co_ban = luong_co_ban

    def tinh_luong(self): # Đây là một cái HÀM hành động
        return self.luong_co_ban * 1.2
nv=NhanVien(1000)
nv.tinh_luong() #Buộc phải có ngoặc tròn

class NhanVien:
    def __init__(self, luong_co_ban):
        self.luong_co_ban = luong_co_ban

    @property
    def tinh_luong(self): # Nhờ có @property, hàm này đã bị "hóa phép"
        return self.luong_co_ban * 1.2
nv=NhanVien(1000)
nv.tinh_luong #Biến thành một thuộc tính







#* setter : Cho ghi
#! có thể gán dấu = cho một THUỘC TÍNH nhưng không thể gán dấu = cho HÀM
#* Vậy chúng ta có thể gán dữ liệu thông qua getter vậy setter để làm gì: setter đóng vai trò là kẻ gác cổng, ngăn chặn dữ liệu bẩn khi gán =

#Cách để tạo ra một setter: #* Phải có một getter trước đó
                            #* Hàm Setter phải nằm ngay dưới decorator @tên_thuộc_tính.setter.
                            #* Tên hàm Setter phải giống hệt tên hàm Getter. 

#TRACE CÁCH HOẠT ĐỘNG CỦA GETTER VÀ SETTER
class hcn:
    def __init__(self,dai,rong):
        self.dai=dai
        self.rong=rong

    @property 
    def dai(self):
        return self._dai 
    @dai.setter
    def dai(self,gia_tri):
        if not(isinstance(gia_tri,(float,int))) or gia_tri<=0:
            raise ValueError("Dữ liệu nhập lỗi")
        self._dai=gia_tri

    @property 
    def rong(self):
        return self._rong 
    @rong.setter
    def rong(self,gia_tri):
        if not(isinstance(gia_tri,(float,int))) or gia_tri<=0:
            raise ValueError("Dữ liệu nhập lỗi")
        self._rong=gia_tri
    @property 
    def dien_tich(self):
        return self._rong*self._dai
#1. khi chạy abcd=hcn(5,6) thì sẽ chạy self.dai=5 thì ngay lập tức chạy hàm #! def dai(self,5)
#! lưu ý vì đã có getter nên self.dai=5 tương đương với việc dai(self,5)
#2. Nếu thoả mãn điều kiện trả về self._dai=5 (#!Nếu trả về self.dai=5 sẽ dẫn đến lặp vô hạn)
#3. Tương tự với chiều rộng 
#* lợi thế ở đây là bạn có thể cập nhật thay đổi giá trị linh hoạt
abcd=hcn(5,6)
print(abcd.dien_tich) #30
abcd.dai=6
print(abcd.dien_tich) #36


#? Điều gì xảy ra nếu bạn không dùng setter,getter
# Đầu tiên là cấu trúc gọi hàm sẽ rườm rà hơn, ít tường minh hơn, code có thể ngắn hơn nhưng với những dự án lớn chúng sẽ khó xử lý hơn
# NÊN NHỚ LÀ PYTHON ĐỌC CODE NHIỀU HƠN VIẾT CODE
# LẤY VÍ DỤ VỀ SỰ BẤT LỢI VỚI NHỮNG BÀI CÓ DỮ LIỆU THAY ĐỔI
class tinh_tien:
    def __init__(self,ds_gia):
        self.ds_gia=ds_gia
        self.tong_tien=sum(ds_gia)
gio_hang = tinh_tien([10, 20, 30])
print(gio_hang.tong_tien) # Đầu ra: 60 (Đúng)
gio_hang.danh_sach_gia.append(40) 
print(gio_hang.tong_tien) # Đầu ra: 60 vì init chỉ chạy 1 lần duy nhất nên tong_tien vẫn vậy không thay đổi

#Dùng getter
class GioHangHienDai:
    def __init__(self, danh_sach_gia):
        self.danh_sach_gia = danh_sach_gia

    @property
    def tong_tien(self): # GETTER đóng vai trò tính toán động
        return sum(self.danh_sach_gia)

gio_hang = GioHangHienDai([10, 20, 30])
print(gio_hang.tong_tien) # Đầu ra: 60
gio_hang.danh_sach_gia.append(40)
print(gio_hang.tong_tien) # Đầu ra: 100! Tự cập nhật chính xác tuyệt đối.

        
    
