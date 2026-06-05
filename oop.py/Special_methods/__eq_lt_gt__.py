
"""
__eq__: for equality(=)
__lt__: for less than(<)
__gt__: for greater than(>)

#* Việc so sánh instance của class là so sánh giá trị, .... hay so sánh gì?
- Với các dữ liệu có sẵn như str ngắn hay từ số -5 đến 256 thì Python gom chúng vào cùng một ô nhớ vì chúng là dữ liệu bất biến (immutable) và quá phổ biến.Python làm vậy để tiết kiệm RAM

- Đối với instance của một class, khi bạn tạo một instance thì chúng sẽ phải xin Python một mảnh đất mới trên thanh RAM để xây dựng đối tượng đó
- Nên bạn chỉ so sánh 2 instance thì Python sẽ không biết bạn muốn so sánh cái gì của hàm nên sẽ trả về False
- Còn đối với chuỗi str,int,... thì Python đã viết sẵn phương thức __eq__ cho nó rồi và dấu == là cách để thực thi phương thức
"""
class tk:
    def __init__(self,user,email):
        self.username=user
        self.email=email
user1=tk("Viet Ha","nguyenviethahaha49@gmail.com")
user2=tk("Viet Ha","nguyenviethahaha49@gmail.com")
print(user1==user2) #False vì chúng có 2 ô nhớ riêng biệt mà == trong trường hợp này sẽ so sánh ô nhớ trên thanh RAM

#*Vậy để so sánh giá trị thì chúng ta sẽ làm ntn?
class tk:
    def __init__(self,user,email):
        self.username=user
        self.email=email
    def __eq__(self,other): #self là đối tượng bên trái dấu ==
                            #other là đối tượng bên phải dấu ==
        return self.username==other.username 
user1=tk("Viet Ha","nguyenviethahaha49@gmail.om")
user2=tk("Viet Ha","nguyenviethahaha49@gmail.com")
print(user1==user2) #True


class tau:
    def __init__(self,so_toa,so_ghe):
        self.toa=so_toa
        self.ghe=so_ghe
    def __eq__(self,other):
        return self.toa==other.toa and self.ghe==other.ghe
ghe1=tau(so_toa=5,so_ghe=12) #!Truyền theo keyword argument(NÊN DÙNG): vì chúng tránh việc nhầm lẫn khi có quá nhiều args, và người đọc có thể biết ngay là bạn truyền giá trị cho cái gì
ghe2=tau(so_toa=5,so_ghe=13) 

#*kết hợp với sorted()
class gamethu:
    def __init__(self,ten,diem_rank):
        self.ten=ten
        self.diem_rank=diem_rank
    def __lt__(self,other):
        return self.diem_rank < other.diem_rank
    def __gt__(self,other):
        return self.diem_rank > other.diem_rank
gamethu1=gamethu(ten="Việt Hà",diem_rank=1000)
gamethu2=gamethu(ten="Jyno",diem_rank=10000)
print(gamethu1<gamethu2) #True

ds_game_thu=[gamethu("Asuna",1000),gamethu("Kirito",2000),gamethu("Klein",500)]
bxh=sorted(ds_game_thu)
for player in bxh:
    print(f"Username: {player.ten}\nSức mạnh: {player.diem_rank}")



#? VD so sánh thời gian
class thoigian:
    def __init__(self,gio,phut,giay):
        self.gio=gio
        self.phut=phut
        self.giay=giay
    def so2(self,other):
        if self.gio>other.gio:
            return True
        elif self.gio<other.gio:
            return False
        else:
            pass # Vẫn còn nhiều lần so sánh nữa để ra được kết quả tối ưu
                 #! Vậy chủng ta có thể quy đỏi ra đơn vị so sánh nhỏ nhất để tối ưu hơn chỉ cần 1 lần so sánh
                 # và sau bạn muốn xem kết quả cần t1.so2(t2) nhìn nó sẽ không tuyệt vời bằng việc bạn dùng dấu ==,>,<
                
class thoigian:
    def __init__(self,gio,phut,giay):
        self.gio=gio
        self.phut=phut
        self.giay=giay
    def quy_doi_s(self):
        return self.gio*3600+self.phut*60+self.giay
    def __gt__(self,other):
        return self.quy_doi_s() > other.quy_doi_s()
t1=thoigian(gio=1,phut=30,giay=59)
t2=thoigian(gio=1,phut=30,giay=58)
print(t1>t2) #True

