"""Bài 1: Hệ thống Quản lý Tài khoản Ngân hàng (Bank Account)
Kết hợp: __init__, Phương thức nội bộ, __str__
Yêu cầu: Tạo class TaiKhoan. Khi khởi tạo nhận vào ten_chu_tk và so_du_ban_dau.
Hàm nội bộ: Viết phương thức ẩn _kiem_tra_so_tien_hop_le(self, so_tien) để kiểm tra số tiền nạp/rút phải lớn hơn 0.
Hành động: Viết phương thức nap_tien(self, so_tien) và rut_tien(self, so_tien). Cả hai hàm này phải gọi hàm ẩn ở trên để kiểm tra trước khi cộng/trừ tiền. Nếu rút tiền, phải kiểm tra thêm điều kiện số dư có đủ không.
Hiển thị (__str__): Khi in tài khoản ra, nó phải ẩn bớt tên để bảo mật và định dạng tiền đẹp đẽ. Ví dụ: Tài khoản: N***** A | Số dư: 1,500,000 VND."""

class TaiKhoan:
    def __init__(self,ten_chu_tk,so_du_ban_dau):
        self.ten_chu_tk=ten_chu_tk
        self.so_du=so_du_ban_dau
    """def _kiem_tra_so_tien_hop_le(self,so_tien):
        return so_tien if so_tien>0 else None #! Hàm gác cổng kiểm tra nên trả về giá trị True/False
                                              #! thường với các dự án họ sẽ đánh lỗi nếu dữ kiện không hợp lý để tránh VD: AI học từ những dữ kiện lỗi nếu lỡ chạy, hệ thống sẽ sập ngay để chúng ta sửa code"""
    def nap_tien(self,so_tien_nap): 
        if so_tien_nap<=0:
            raise ValueError("Dữ liệu nhập không hợp lý")
        self.so_du+=so_tien_nap
    def rut_tien(self,so_tien_rut):
        if so_tien_rut<=0 or so_tien_rut>self.so_du:
            raise ValueError("Dữ liệu nhập không hợp lý")
        self.so_du-=so_tien_rut
    def __str__(self):
        return f"tên tài khoảng: {self.ten_chu_tk}\nSố dư tk: {self.so_du:,}"
    
tk_A=TaiKhoan(ten_chu_tk="A",so_du_ban_dau=1000)
try:
    tk_A.nap_tien(0)
    print("Nap tien thanh cong")
except ValueError as e:
    print(f"Thong bao: {e}") # Thong bao: Dữ liệu nhập không hợp lý









"""Bài 2: Hộp Quản lý Điểm Nhân viên (Performance Tracker)
Kết hợp: __init__, __setitem__, __getitem__, __str__
Yêu cầu: Tạo class BangDanhGia. Ban đầu, thuộc tính self.diem_so = [5, 6, 7, 8] (đại diện cho điểm 4 quý trong năm).
Bọc lót Đọc/Ghi (__getitem__, __setitem__): * Khi người dùng đọc hoặc ghi điểm theo quý (index từ 0 đến 3), phải viết điều kiện chặn nếu index tràn phạm vi.
Đặc biệt ở hàm Ghi (__setitem__): Điểm đánh giá chỉ được phép nằm trong đoạn từ 0 đến 10. Nếu người dùng truyền vào số rác hoặc điểm âm, dùng return tắt hàm ngay và báo lỗi.
Hiển thị (__str__): Khi in cái bảng này ra, nó phải tự tính Điểm trung bình cả năm và xếp loại luôn. Ví dụ: Điểm các quý: [5, 6, 7, 8] -> ĐTB: 6.5 (Loại: Khá).
"""
class BangDanhGia: #Tạo ra một cái hộp to tên là BangDanhGia
    def __init__(self):
        self.bang_diem=[5,6,7,8] #Tạo ra cái ngăn tên bang_2025 rồi nhét cái list[5,6,7,8]
                                 #vậy nên khi muốn dùng cần ghi đầy đủ #! self.bang_diem[index]
    def _ktra(self,index):
        if index>=len(self.bang_diem) or index<-len(self.bang_diem):
            return False
        return True
    def __getitem__(self,index):
        if not self._ktra(index):
            raise ValueError("Không có vị trí này")
        return self.bang_diem[index]
    def __setitem__(self,index,value):
        if not self._ktra(index):
            raise ValueError("Không có vị trí này")
        if not 0<=value<=10:
            raise ValueError("Báo lỗi")
        self.bang_diem[index]=value
    def __str__(self):
        dtb=sum(self.bang_diem)/len(self.bang_diem)
        xeploai="gioi" if dtb>8 else "yeu" if dtb<=5 else "Kha"
        return f"Điểm tb của quý: {dtb}\nXếp loại: {xeploai}"
bang_2025=BangDanhGia() #Tạo ra cái ngăn tên bang_2025 rồi nhét cái list[5,6,7,8]

try:
    bang_2025[4]
except ValueError as v:
    print(f"Thông báo: {v}")

#!HOẶC CÓ THỂ KẾ THỪA LIST
class BangDanhGia(list): #! Vì dùng tính kế thừa nên bản thân BangDanhGia lúc này là 1 cái list
    def __init__(self):
        super().__init__([5,6,7,8]) # [5,6,7,8] đổ vào cái BangDanhGia
    def __setitem__(self,index,value):
        if not 0<=value<=10:
            raise ValueError("Giá trị chuyền vào không hợp lệ.")
        try:
            super().__setitem__(index,value)
        except IndexError as v: #! Lỗi ban đầu phát hiện sẽ là index
                                #! Nhưng mình đã định nghĩa lại lỗi là ValueError nên khi kiểm tra hoặc dùng các lệnh khác có lien quan thì phải để except ValueError để dễ kiểm soát và phân biệt với những lỗi khác
            raise ValueError("Không có vị trí này")
    def __str__(self):
        dtb=sum(self)/len(self)
        xeploai="gioi" if dtb>8 else "yeu" if dtb<=5 else "Kha"
        return f"Điểm tb của quý: {dtb}\nXếp loại: {xeploai}"
    








"""Bài 3: Kho Hàng Linh Kiện Máy Tính (Tối ưu hóa dữ liệu)
Kết hợp: __init__, logic so sánh toán học, __str__
Yêu cầu: Tạo class LinhKien gồm: ten, gia_usd, và ty_gia_vnd (ví dụ: 25000).
Tư duy tối ưu: Giống như bài toán đổi về đơn vị nhỏ nhất bạn từng nghĩ ra, hãy viết một phương thức nội bộ _quy_doi_ra_vnd(self) để tự tính toán giá tiền Việt.
Logic so sánh (__eq__, __lt__): Khi so sánh hai linh kiện với nhau (ví dụ: lk1 < lk2), Python phải tự động chạy hàm nội bộ quy đổi ra tiền VND rồi so sánh giá trị tiền VND của chúng với nhau.
Hiển thị: In linh kiện ra phải hiện đầy đủ thông tin định dạng: Linh kiện: Card RTX 4060 | Giá: 350 USD (~8,750,000 VND)."""

class LinhKien:
    def __init__(self,ten,gia_usd):
        if not isinstance(gia_usd,(int,float)):
            raise TypeError("Dữ kiện nhập không hợp lệ")
        if gia_usd<=0:
            raise ValueError("Giá tiền không hợp lệ")
        self.ten_lk=ten
        self.gia_usd=gia_usd
        self.ty_gia_vnd=25000
    def _quy_doi_ra_vnd(self):
        return self.gia_usd*self.ty_gia_vnd
    def __eq__(self,other):
        if not isinstance(other,LinhKien):
            raise TypeError("Không thể so sánh LinhKien với kiểu dữ liệu khác!")
        return self._quy_doi_ra_vnd() == other._quy_doi_ra_vnd()
    def __lt__(self,other):
        if not isinstance(other,LinhKien):
            raise TypeError("Không thể so sánh LinhKien với kiểu dữ liệu khác!")
        return self._quy_doi_ra_vnd() < other._quy_doi_ra_vnd()
    def __str__(self):
        return f"Linh kien: {self.ten} | Gia: {self.gia_usd}USD ({self._quy_doi_ra_vnd})"
        
try:
    lk1 = LinhKien("RTX 4060", 350)
    lk2 = LinhKien("so2", "200") 
    
    print(lk1 == lk2)
except TypeError as e:
    print(f"🚨 Hệ thống chặn đứng: {e}")

try:
    lk_chuan = LinhKien("CPU i5", 200)
    # Đem so sánh với một chuỗi chữ
    print(lk_chuan == "Một chuỗi rác") # Sẽ trả về False an toàn vì có phòng thủ ở __eq__
    print(lk_chuan < "Một chuỗi rác")  # Sẽ sập nguồn vào except vì có phòng thủ ở __lt__
except TypeError as e:
    print(f"🚨 Lưới đỡ bom __lt__ hứng được: {e}")
#!Lưu ý đây chỉ là những bài tập đơn giản và chúng ta đang thử nghiệm trong thực tế không bao giờ dùng try,except kiểm tra kiểu vậy









"""Bài 4: Mô phỏng Lớp Học Trực Tuyến (E-Learning Class)
Kết hợp: __init__, hàm nội bộ, __getitem__, __str__, __repr__
Yêu cầu: Tạo class LopHoc. Khi khởi tạo nhận vào ten_lop. Thuộc tính bên trong là một danh sách học sinh rỗng: self.hoc_sinh = [].
Hành động: Viết hàm them_hoc_sinh(self, ten_hs). Chặn không cho thêm nếu tên là chuỗi rỗng.
Bọc lót chỉ mục (__getitem__): Cho phép người dùng lấy ra học sinh bằng dấu ngoặc vuông lop_học[0]. Nếu lớp chưa có học sinh nào hoặc index vượt quá, trả về chuỗi: "Học sinh không tồn tại".
Hiển thị: * Hàm __str__ trả về bảng danh sách: text Lớp: Python Cơ Bản Sĩ số: 2 học sinh 
Hàm __repr__ (phục vụ lập trình viên nhìn trong List): Trả về tên các học sinh đang có dưới dạng mảng: ['An', 'Bình'].
"""
#!Cách thừa kế này đôi khi không tốt vì nó thừa kế tất cả những gì hàm cha có mà chưa chắc đã dùng hết hàm
class lop_hoc(list):
    def __init__(self):
        super().__init__([])
    def append(self,hs):
        if not isinstance(hs,str) or hs.strip()=="":
            raise ValueError("Tên hs không hợp lệ")
        super().append(hs)
    def extend(self,ds_hs):
        for hs in ds_hs:
            self.append(hs)

    #!HOẶC
    def extend(self,ds_hs):
        if any(not isinstance(hs,str) or hs.strip()=="" for hs in ds_hs):
            raise ValueError("Lỗi")
        super().extend(ds_hs)

    def __str__(self):
        return f"Sỹ số lớp học: {len(self)}"
    def __repr__(self):
        return super().__repr__()
lop_12=lop_hoc()
try:
    lop_12.extend(["Hà", "Linh", "Thảo"])
    print("✅ Thêm danh sách học sinh thành công!")
except ValueError as v:
    print(f"🚨 Lỗi Test 1: {v}")

# Test 2: Thử "vượt ngục" bằng cách thêm tên rỗng hoặc khoảng trắng
try:
    lop_12.append("   ") # Tên chỉ có dấu cách
except ValueError as v:
    print(f"🚨 Hệ thống chặn đứng Test 2: {v}")

# Test 3: Thử truy cập vị trí
try:
    print(f"Học sinh vị trí số 1 là: {lop_12[5]}") # list của Cha tự xử lý IndexError hộ mình luôn
except IndexError as i:
    print(f"🚨 Lỗi vị trí: {i}")

print(lop_12)        # Kích hoạt __str__
print(repr(lop_12))  # Kích hoạt __repr__ để xem toàn bộ mảng     



#* ƯU TIÊN ĐÓNG GÓI HƠN KẾ THỪA
class LopHoc:
    def __init__(self):
        # Đóng gói một cái list ẩn ở bên trong, không cho người ngoài sờ trực tiếp vào
        self._danh_sach_hs = [] 

    def them_hs(self, hs):
        # Gác cổng cực kỳ gọn gàng
        if not isinstance(hs, str) or hs.strip() == "":
            raise ValueError("Tên học sinh không hợp lệ!")
        
        self._danh_sach_hs.append(hs)

    def them_danh_sach(self, ds_hs):
        for hs in ds_hs:
            self.them_hs(hs) # Bắt đi qua cổng an ninh bên trên

    # 🌟 Vẫn dùng được dấu ngoặc vuông [] nhờ Magic Methods nhưng an toàn 100%
    def __getitem__(self, index):
        try:
            return self._danh_sach_hs[index]
        except IndexError:
            raise IndexError("Lớp học không có vị trí này!")

    def __len__(self): #Tại sao nên dùng: #1 Thiết kế giao diện tường minh
                                          #2 nếu có ai dùng len(lop_12) thì hàm sẽ hiện ra chứ không báo lỗi
                                          #3 Kiểm tra lớp học rỗng if not lop_moi: print("Lớp học đéo có ai") #! Thì máy tính sẽ tìm __len__ để kiểm tra nếu không có thì if not ... sẽ không hoạt động
        return len(self._danh_sach_hs)

    def __str__(self):
        return f"Sĩ số lớp: {len(self)} học sinh"

    def __repr__(self):
        return repr(self._danh_sach_hs)
lop_12=LopHoc()
lop_moi=LopHoc()









"""Boss Cuối - Mô phỏng Mạng Nơ-ron Đơn Giản (Perceptron/Neuron Model)
Bài tập chuẩn vị AI Engineer cho bạn
Yêu cầu: Trong AI, một nơ-ron nhận vào các weights (trọng số - một list các số thực) và một số bias. Hãy tạo class Neuron nhận vào hai thuộc tính này khi __init__.
Hàm nội bộ tính toán: Viết hàm _tinh_tong_tin_hieu(self, inputs). Hàm này nhận vào một list inputs (dữ liệu đầu vào), tiến hành nhân từng phần tử của inputs với weights tương ứng rồi cộng với bias.
Ví dụ: inputs = [1, 2], weights = [0.5, 0.1], bias = 0.2
➡️ Tổng = (1×0.5)+(2×0.1)+0.2=0.9.
Chặn điều kiện lỗi: Trong hàm tính toán trên, nếu chiều dài của list inputs không bằng chiều dài của list weights, dùng return tắt hàm ngay lập tức và trả về None (vì dữ liệu không khớp thì không tính được).
Hiển thị (__str__): In mô hình ra theo chuẩn thông số: Neuron(Số lượng đầu vào: 2 | Bias: 0.2).
"""
class Loi_Tin_Hieu_Dau_Vao(Exception): pass #!Cách tạo tên lỗi riêng để tránh trùng lặp và để người đọc nhìn vào là biết lỗi gì
class Loi_Trong_So(Exception): pass
class Neuron:
    def __init__(self,weight,bias):
        if not all(isinstance(numb,(float,int)) for numb in weight) or not isinstance(bias,(int,float)):
            raise Loi_Trong_So("Trọng số (weight) hoặc bias phải là số thực/số nguyên!")
        
        self.weight_list=weight
        self.bias=bias

    def __len__(self):
        return len(self.weight_list)
    
    def _tinh_tong_tin_hieu(self,inputs):
        if not all([isinstance(numb,(float,int)) for numb in inputs]) or len(self.weight_list)!=len(inputs):
            raise Loi_Tin_Hieu_Dau_Vao ("Mảng inputs không trùng khớp số lượng với mảng weight!")
                                       
        return sum(wei*inp for wei,inp in zip(self.weight_list,inputs))+self.bias
# Test
try:
    neur=Neuron(["a",0.1,0.2,0.3,0.5],0.2)
except Loi_Trong_So as e:
    print(e)

        

    


    

        
