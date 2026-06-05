
"""
__getitem__: kích hoạt khi bạn muốn LẤY gái trị ra bằng []
__setitem__: kích hoạt khi bạn muốn GÁN/THAY ĐỔI giá trị bằng cách []=giá trị

"""
class lophoc:
    def __init__(self):
        self.ds_hs=["A","b","c","d"]
    def __getitem__(self,index):
        if index>=len(self.ds_hs) or index<-len(self.ds_hs):
            return "Khong tim thay hs o vi tri nay"
           #return self.ds_ds[-1] #!hoac tra ve nguoi cuoi cung
        return self.ds_hs[index]
    def __setitem(self,index,value):
        #!Cũng cần có điều kiện nhưng lười viết
        self.ds_hs[index]=value

#!Hoặc dùng 1 phương thức riêng để kiểm tra index
class lop_hoc:
    def __init__(self):
        self.ds=['a','b','c','d','e','f']
    def _is_invaild_index(self,index):
        return index>=len(self.ds) or index<-len(self.ds)
    def __getitem__(self,index):
        if self._is_invaild_index(index):
            return "Không có vị trí này trong lớp học"
        return self.ds[index]
    def __setitem__(self,index,value):
        if self._is_invaild_index(index):
            return "Không có vị trí này trong lớp học"
        self.ds[index]=value
lop_12A=lop_hoc
print(lop_12A[1]) #b




#* Với dict
class TuDienCongNghe:
    def __init__(self):
        self.data={"AI":"Trí tuệ nhân tạo",
                   "OOP":"Lập trình hướng đối tượng"}
    def __getitem__(self,key):
        return self.data.get(key,"Không tìm thấy key")
    def __setitem__(self,key,value):
        self.data[key]=value
tu_dien_001=TuDienCongNghe()
print(tu_dien_001["AI"]) # Trí tuệ nhân tạo
print(tu_dien_001["A1"]) # Không tìm thấy key
tu_dien_001["RAM"]="Bộ nhớ truy cập ngẫu nhiên"
print(tu_dien_001["RAM"])# Bộ nhớ truy cập ngẫu nhiên




#*Tuỳ chỉnh logic
class BangCuuChuong:
    def __init__(self,so_nhan):
        self.so_nhan=so_nhan
    def __getitem__(self,index):
        return f"{self.so_nhan} x {index} = {self.so_nhan*index}"
bcc_5=BangCuuChuong(so_nhan=5)
for i in range(1,11):
    print(bcc_5[i])



#*Bảo vệ dữ liệu
class NhatKy:
    def __init__(self):
        self.nk=["Hôm nay trời đẹp","Hôm nay khá năng suất"]
    def __getitem__(self,index):
        return self.nk[index]
    def __setitem__(self,index,value):
        if value=="":
            print("Không được để trống nội dung nhật ký")
            return #!Lệnh return có tác dụng ngắt luồng chạy, không cho chạy những dòng code bên dưới
        self.nk[index]=value
my_diary=NhatKy()
my_diary[1]=""     # Không được để trống nội dung nhật ký
print(my_diary[1]) # Hôm nay khá năng suấ 