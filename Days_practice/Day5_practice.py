#Cho một danh sách khách hàng gồm cả người lớn và trẻ em 
#(ví dụ: ["Tuấn_25", "Hoa_10", "Nam_30"]). Hãy dùng vòng lặp và if-else để tách họ vào 2 List riêng biệt: nguoi_lon và tre_em
ds = ["Tuấn_25", "Hoa_10", "Nam_30"]
nguoilon, trem = [], []
i = 0

while i < len(ds):
    # Ta "mở gói" thẳng vào 2 biến ten và tuoi
    ten, tuoi = ds[i].split("_")
    # Ép kiểu tuoi sang int để so sánh
    if int(tuoi) >= 18:
        nguoilon.append(ten)
    else:
        trem.append(ten)
    i += 1

print("Người lớn:", nguoilon)
print("Trẻ em:", trem)





#cho một danh sách với số thứ tự từ 1-n, mỗi lần xoá 1 tên và in ra Tên & STT cho đến hết ds
import random
ds= ["Nam", "Hoa", "Lan", "Tuấn"]
ds_id=[]
i=0
while i<len(ds):
    ds_id.append((ds[i],i+1)) #thêm 1 lần ngoặc tròn bên ngoài để coi (ds[i],i+1) là một phần tử
    i+=1
count=1
while len(ds_id)>0:
    r=random.randint(0,len(ds_id)-1)
    choose=ds_id.pop(r)       #list có thể xoá thứ tự tuỳ ý
    ten,stt=choose            #unpacking: ten,stt= "Nam,1"
    print(f"lần thứ: {count}, Name: {ten}, STT: {stt} ")
    count+=1




#Cho người dùng nhập số điện thoại vào một danh sách
#Nếu số nhập vào đã tồn tại, hãy báo lỗi. Nếu chưa, hãy lưu vào một Set để đảm bảo không bao giờ có sự trùng lặp
ds_sdt={"0348597151","0347649851"}
so=input()
if so in ds_sdt:
    print("số điện thoại đã tồn tại")
else:
    ds_sdt.add(so)



#Cho một Dict thông tin cá nhân, trong đó có một số giá trị bị để trống (chuỗi rỗng "")
#Hãy dùng vòng lặp để tìm và xóa các Key có giá trị rỗng đó.
dic={"k1":1,"k2":2,"k3":3,"k4":"","k5":""}
ep=list(dic.items())
i=0
while i<len(ep):
    if ep[i][1]=='':
        xoa=ep.pop(i)
    else:
        i+=1
print(dict(ep))

#!Cách làm pro: Dict conprehension
dic = {"k1":1, "k2":'', "k3":3, "k4":"", "k5":''}

# "Tạo dict mới gồm k và v, lấy từ dic1, với điều kiện v khác rỗng"
sach_se = {k: v for k, v in dic.items() if v != ""}
          #(keys:value) tương ứng với (key, value) in dic.items() 
print(sach_se)




#Cho một Dict d = {"A": 1, "B": 2}. Hãy tạo một Dict mới sao cho Key là số còn Value là chữ: {1: "A", 2: "B"}.
d = {"A": 1, "B": 2}
    #!C1: dùng while
d_list=list(d.items())
ds=[]
i=0
while i<len(d_list):
    k,v=d_list[i]
    ds.append((v,k))
    i+=1
print(set(ds))

    #!C2: Dùng zip: ghép 2 danh sách riêng biệt(keys và values) thành từng cặp tạo dict
    #?: dict(zip(keys,values))
ds_1=dict(zip(d.values(),d.keys()))

    #!C3: Dict conprehension
ds_2={v:f for f,v in d.items()}




#Cho một List chứa các Tuple dạng (tên_món_ăn, giá_tiền). Hãy dùng vòng lặp để chuyển nó thành một Dict để dễ tra cứu giá
menu=[("nem",13),("đậu",15),("canh",20)]
#!Có thể dùng dict(menu) hoặc .update(menu) để tạo ra nhưng đề yêu cầu dùng vòng lặp

menu=[("nem",13),("đậu",15),("canh",20)]
ds_mon={}
i=0
while i<len(menu):
    mon,gia=menu[i]
    ds_mon[mon]=gia
    i+=1
print(ds_mon)





#cho một câu tiếng anh, đếm ký tự in ra dict
#! Làm cách này mỗi lần đến ký tự tiếp theo lại phải chạy i một vòng ( sẽ có những thao tác thừa)
cau=input().lower()
dic={}
i=97
print(cau)
while 97<=i<=122:
    kytu=chr(i)
    dem=cau.count(kytu)
    if dem:
        dic[kytu]=dem
    i+=1
print(dic)

#! Cách tối ưu hơn: Dùng get(key,default)
cau=input().lower()
dic={}
i=0
while i<len(cau):
    kt=cau[i]
    if kt!=' ':
        dic[kt]=dic.get(kt,0)+1
    i+=1
print(dict(sorted(dic.items()))) #!sorted hàm sắp xếp áp dụng được với mọi đối tượng
print(dic)                     #!không làm thay đổi bản gốc 

#!Cách khác:
cau=input().lower()
dic={}
for ktu in cau:       #for chạy từng ký tự trong cau
    if ktu.isalpha(): #kiểm tra xem có phải chữ hay không
        dic[kt]=dic.get(ktu,0)+1
print(dict(sorted(dic.items())))




#Gộp đơn hàng: Có 2 bạn cùng đi chợ, mỗi bạn có một Dict danh sách đồ cần mua và số lượng
#Hãy gộp 2 Dict này lại thành một. Nếu trùng món, hãy cộng dồn số lượng chứ không phải ghi đè.
don1={"A":1,"B":2,"C":5,"D":6}
don2={"S":1,"B":4,"C":1}
for k,v in don1.items():
    if k in don2:
        don2[k]+=don1[k]
    else:
        don2[k]=don1[k]
print(don2)

#!Cách 2:
for k,v in don1.items():
    #get update vào don2:{k:don2.get(k,0)+v}
    don2.update({k:don2.get(k,0)+v})
print(don2)

#!Counter from collections
from collections import Counter
ket_qua=Counter(don1)+Counter(don2)
print(dict(ket_qua))




#Tách biệt kiểu dữ liệu: Cho một List "hỗn loạn" gồm cả số nguyên, số thực và chuỗi
#Hãy chia chúng vào 3 List riêng biệt dựa trên kiểu dữ liệu của chúng.
lis = [3, 5, 5.6, "zxc", 10.5, 'Jyno']
i = 0
nguyen, thuc, chuoi = [], [], []
while i < len(lis):
    item = lis[i]
    #! isinstance có thể kiểm tra isinstance(item, (int,float,...))
    if isinstance(item, int):# Kiểm tra nếu là số nguyên
        nguyen.append(item)
    elif isinstance(item, float):# Kiểm tra nếu là số thực
        thuc.append(item)
    elif isinstance(item, str):# Kiểm tra nếu là chuỗi
        chuoi.append(item)        
    i += 1
print("Nguyên:", nguyen) 
print("Thực:", thuc)     
print("Chuỗi:", chuoi)




#máy chọn nước :dict{"đồ uống":[giá,số lượng]}
#!Máy bán hàng tự động
menu = {
    "coca": [10, 5], 
    "pepsi": [10, 2], 
    "fanta": [11, 3], 
    "nước lọc": [12, 10]
}
so_du=int(input("Nhập tiền nạp: "))
while True:
    print(menu)
    do_uong=input("Nhập đồ uống: ")
    if do_uong not in menu:
        print("Không có đồ uống: ")
        continue
    else:
        so_luong=int(input("Nhập số lượng; "))
        if so_luong<1:
            print("vui lòng nhập lại: ")
            continue
        else:
            con_lai=menu[do_uong][1]-so_luong
            if con_lai<0:
                print("Số lượng không đủ: ")
                continue
            elif so_du-menu[do_uong][0]*so_luong<0:
                print("số dư không đủ")
            else:
                menu[do_uong][1]=menu[do_uong][1]-so_luong
                tien_tru=so_luong*menu[do_uong][0]
                so_du_cl=so_du-tien_tru
                so_du=so_du_cl
                print("Số dư còn lại:",so_du_cl)
                continue





#Từ điển Anh-Việt: Cho người dùng nhập cặp từ vựng. Lưu vào Dict. Sau đó cho phép người dùng nhập từ tiếng Anh để tra nghĩa.
#Nếu tra sai 3 lần (dùng biến đếm), khóa không cho tra nữa.
ds={}
while True:
    word=input("words: ").strip().lower()
    if word=="end":
        break
    mean=input(f"Nghĩa cuả từ {word}: ")
    ds[word]=mean
count=0
while ds and count<3:
    nhap=input("nhập từ tiếng anh: ").strip().lower()
    if nhap not in ds:
        count+=1
        print(f"nhập sai {count}/3")
        continue
    else:
        nghia=ds.pop(nhap)
        print(f"nghĩa của từ {nhap}: {nghia}")
if count==3:
    print("học lại")
else:
    print("chúc mừng")






#Quản lý điểm số: Tạo một List chứa các Dict. Mỗi Dict là một học sinh: {"tên": "An", "điểm": 8}. 
#Hãy duyệt qua và in ra tên những bạn có điểm trên 5, bạn nào dưới 5 thì thêm vào một Set "cần phụ đạo"
danh_sach_hs = [
    {"ten": "An", "diem": 8.5, "chuyen_can": 10},
    {"ten": "Bình", "diem": 4.0, "chuyen_can": 9},
    {"ten": "Chi", "diem": 9.0, "chuyen_can": 7},
    {"ten": "Dũng", "diem": 6.5, "chuyen_can": 8}
]
i=0
gioi, kha, yeu=[],[],[]
for hs in danh_sach_hs:
    ten=hs["ten"]
    diem_tong=hs["diem"]*0.7+0.3*hs["chuyen_can"]
    if diem_tong>=8:
        xep_hang='gioi'
    elif diem_tong<5:
        xep_hang='yeu'
    else:
        xep_hang='kha'
    print(f"Họt sinh: {ten:<6}\nXếp hạng: {xep_hang} với điểm tổng là: {round(diem_tong,1):<4} ")
    #!Căn lề bằng f-string: {biến:[ký tự lấp đầy][căn lề][độ rộng] }, ở 2 bên ngoài cùng nếu chuỗi tự căn cái, nếu số tự căn phải





# CÂU 14: PHÂN TÍCH HỆ THỐNG USER
# 1. Đánh giá mật khẩu: 
#    - < 6 ký tự: "Yếu"
#    - 6-10 ký tự: "Trung bình"
#    - > 10 ký tự: "Mạnh"
# 2. Thống kê (Vòng lặp):
#    - Tìm người có 'lan_dang_nhap' nhiều nhất (lấy cả Tên và Số lần).
#    - Tính Trung bình cộng số lần đăng nhập cả hệ thống.
# 3. Định dạng:
#    - In bảng dùng F-string căn lề (Tên: 10, Độ dài: 15, Đánh giá: Phải).
he_thong_user = [{"user": "admin", "pass": "123456", "lan_dang_nhap": 150},{"user": "manager", "pass": "p@ssword123", "lan_dang_nhap": 45},{"user": "guest", "pass": "qwerty", "lan_dang_nhap": 10},{"user": "dev_root", "pass": "secure_r00t_2026", "lan_dang_nhap": 80},
    {"user": "hr_dept", "pass": "123", "lan_dang_nhap": 5}
]
print("|{:10}|{:^20}|{:>10}|".format("user","độ dài pass","đánh giá"))
max2=0
tong_dn=0
for user in he_thong_user:
    ten=user["user"]
    mk=user["pass"]
    if len(mk)<=6:
        muc_do="yếu"
    elif len(mk)>10:
        muc_do="mạnh"
    else:
        muc_do="trung bình"
    print(f"|{ten:10}|{len(mk):^20}|{muc_do:>10}|")
    tong_dn+=user["lan_dang_nhap"]
    if user["lan_dang_nhap"]>max2:
        nguoi_dang_nhap_max=user["user"]
        max2=user["lan_dang_nhap"]
print("số lần đăng nhập nhiều nhất:",max2)
print("trung bình lượng đăng nhập:",round(tong_dn/(len(he_thong_user))))
print(nguoi_dang_nhap_max)





