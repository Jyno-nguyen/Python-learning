
#? Thực chất vẫn là tính độ dài list,... thuộc tính của đối tượng,....
#? trong một vài trường hợp __len__ cần thiết còn trong một vài trường hợp thì không

#? TRƯỜNG HỢP KHÔNG CẦN THIẾT
#trong những trường hợp tính toán phức tạp, xử lý tốn thời gian và con số trả về không mang ý nghĩa "độ dài" vật lý
#giá trị trả về có thể là số âm #!vì RETURN TRONG LEN CHỈ TRẢ VỀ GIÁ TRỊ >=0

#? TRƯỜNG HỢP CẦN THIẾT
#Khi class thực sự là một cấu trúc dữ liệu(Container,Collections) và cần tính toán những dữ kiện liên quan đến "độ dài"

class Playlist:
    def __init__(self,ten_ds):
        self.ten=ten_ds
        self.ds_bai_hat=[]
    def them_bai_hat(self,bai_hat):
        self.ds_bai_hat.append(bai_hat)
    def __len__(self):
        return len(self.ds_bai_hat)
my_love_songs = Playlist("Nhạc Lofi Chilling")
my_love_songs.them_bai_hat("Bài Thơ Tình Đầu Tiên")
my_love_songs.them_bai_hat("Ánh Nắng Của Anh")
print(len(my_love_songs)) #3

#!Nhưng nếu bạn bỏ phương thức __len__ bên trong và vẫn Run
print(len(my_love_songs)) # object of type 'Playlist' has no len()
                          # Nó sẽ không biến len(my_love_songs) là bạn muốn đếm ký tự của tên, của bài hát hay số bài hát trong danh sách nên cần 1 __len__ cụ thể


#!Còn nếu bạn thêm 1 cái attribute là một list ,.... thì len vẫn hoạt động bình thường
class Playlist:
    lst=[1,2,3,4,5]
print(len(Playlist.lst)) #5 vì mặc định trong data structure list đã có phương thức len bên trong mặc định là tính độ dài của list rồi


#* LƯU Ý:
class RobotChienDau:
    def __init__(self):
        # Hệ thống có 3 danh sách khác nhau
        self.danh_sach_vu_khi = ["Súng", "Kiếm", "Lựu đạn"] # 👑 List chính
        self.nhat_ky_hanh_trinh = ["Di chuyển đến A", "Tấn công B"] # List phụ 1
        self.he_thong_loi = [] # List phụ 2

    # Định nghĩa len() đại diện cho vũ khí (thằng quan trọng nhất)
    def __len__(self):
        return len(self.danh_sach_vu_khi)

# ----------------------------------------------------
# 🧪 LÚC NÀY BẠN ĐEM RA TEST CODE Ở BÊN DƯỚI:
rb = RobotChienDau()

# Thử nghiệm 1: Gọi len() trực tiếp cho đối tượng rb
# Python sẽ tự động chạy vào hàm __len__ ở trên và đếm vũ khí
print(f"Số lượng vũ khí: {len(rb)}") # Đầu ra: 3 (Mượt mà, không lỗi!)

# Thử nghiệm 2: Muốn đếm Nhật ký hành trình hay Hệ thống lỗi thì sao?
# Bạn chỉ cần gọi len() bọc quanh cái attribute list đó là xong! 
print(f"Số hành trình đã đi: {len(rb.nhat_ky_hanh_trinh)}") # Đầu ra: 2 (Vẫn chạy phăng phăng!)
print(f"Số lỗi đang có: {len(rb.he_thong_loi)}")           # Đầu ra: 0 (Bình an vô sự!)