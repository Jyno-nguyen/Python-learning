#Cho một danh sách khách hàng gồm cả người lớn và trẻ em 
#Hãy dùng vòng lặp và if-else để tách họ vào 2 List riêng biệt: nguoi_lon và tre_em
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

#!HOẶC
ds_lon=[i for i in ds if int(i.split('_')[1])>18]
ds_tre=[i for i in ds if int(i.split('_')[1])<=18]

#!HOẶC
ds_=[i.split("_") for i in ds] #*[['Tuấn', '25'], ['Hoa', '10'], ['Nam', '30']]
ds_lon=[ten for ten,tuoi in ds_ if int(tuoi)>18]
ds_tre=[ten for ten,tuoi in ds_ if int(tuoi)<=18]


#!HOẶC
ds_={1:[],0:[]}
for user in ds:
    ten,tuoi=user.split("_")
    ds_[int(tuoi)>18].append(ten) #Nếu tuổi lớn hơn thì thêm vào ds_[True]=[]
                                  #Nếu tuổi nhỏ hơn thì thêm vào ds_[False]=[]
print(f"ds trẻ em: {ds_[False]}")
print(f"ds người lớn: {ds_[True]}")










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

#* TỐI ƯU
ds= ["Nam", "Hoa", "Lan", "Tuấn"]
so=[i for i in range(1,len(ds)+1)]
ds_so=[[k,v] for k,v in zip(ds,so) ] #!có thể dùng enumerate() để tối ưu
import random as r
while len(ds_so):
    rand=r.randint(0,len(ds_so)-1) #!phải chạy random một lần
    ten,stt=ds_so.pop()
    print(ten,stt)


#*CODE CHUẨN NHẤT
ds= ["Nam", "Hoa", "Lan", "Tuấn"]
ds_so=list(enumerate(ds,start=1)) #[(1, 'Nam'), (2, 'Hoa')]
                            #Tạo thành các cặp với stt tăn dần từ start
import random as r
r.shuffle(ds_so)            #Tráo các phần tử trong danh sách số
while len(ds_so):
    stt,ten=ds_so.pop()
    print(ten,stt)

#!Có thể dùng for
r.shuffle(ds)
for stt,ten in enumerate(ds,start=1):
    print(ten,stt)










#Cho người dùng nhập số điện thoại vào một danh sách
#Nếu số nhập vào đã tồn tại, hãy báo lỗi. Nếu chưa, hãy lưu vào một Set để đảm bảo không bao giờ có sự trùng lặp
ds_sdt={"0348597151","0347649851"}
so=input()
if not so.startswith("0"):
    so="0"+so
if so in ds_sdt:
    print("số điện thoại đã tồn tại")
else:
    ds_sdt.add(so)



#Cho một Dict thông tin cá nhân, trong đó có một số giá trị bị để trống (chuỗi rỗng "")
#Hãy dùng vòng lặp để tìm và xóa các Key có giá trị rỗng đó.
dic = {"k1":1, "k2":'', "k3":3, "k4":None, "k5":0,"k6":"      "}
ep=list(dic.items())
i=0
while i<len(ep):
    if str(ep[i][1]).strip()=='' or ep[i][1] is None :
        xoa=ep.pop(i)
    else:
        i+=1
print(dict(ep))



#!Cách làm pro: Dict conprehension
dic = {"k1":1, "k2":'', "k3":3, "k4":None, "k5":0,"k6":"      "}

# "Tạo dict mới gồm k và v, lấy từ dic1, với điều kiện v khác rỗng"
sach_se = {k: v for k, v in dic.items() if v or v ==0} #! nhưnng như vậy sẽ lấy " ", dù loại bở None và giữ lại số 0
sach_se_nhat={k: v for k, v in dic.items() if v is not None and str(v).strip()}
          #(keys:value) tương ứng với (key, value) in dic.items() 
print(sach_se)


dic={"k1":1,"k2":2,"k3":3,"k4":"","k5":"","k6":"    ","k7":None }
moi={}
for k in dic:
    if str(dic[k]).strip()!='' and dic[k] is not None:
        moi.update({k:dic[k]})
print(moi)

for k,v in dic.items():
    if v is not None and str(v).strip():
        moi[k]=v




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
print(dict(ds))

    #!C2: Dùng zip: ghép 2 danh sách riêng biệt(keys và values) thành từng cặp tạo dict
    #?: dict(zip(keys,values))
ds_1=dict(zip(d.values(),d.keys()))

    #!C3: Dict conprehension
ds_2={v:f for f,v in d.items()}

    #!C4:
ds={}
for k,v in d.items():
    ds[v]=k




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

#!HOẶC
for k,v in menu:
    ds_mon[k]=v
print(ds_mon)

#!HOẶC
menu_moi={k:v for k,v in menu}

    





#cho một câu tiếng anh, đếm ký tự in ra dict
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
print(dic)                       #!không làm thay đổi bản gốc 

#!Cách khác:
cau="hhsdahhac jacsjdacajs "
dic={}
for char in cau.strip().lower():
    if char.strip()!='':          #bỏ dấu cách
        dic[char]=dic.get(char,0)+1
print(dict(sorted(dic.items())))




#Gộp đơn hàng: Có 2 bạn cùng đi chợ, mỗi bạn có một Dict danh sách đồ cần mua và số lượng
#Hãy gộp 2 Dict này lại thành một. Nếu trùng món, hãy cộng dồn số lượng chứ không phải ghi đè.
don1={"A":1,"B":2,"C":5,"D":6}
don2={"S":1,"B":4,"C":1}
for k,v in don1.items():
    don2[k]=don2.get(k,0) +don1[k]
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

#!HOẶC
lis1=[i for i in lis if isinstance(i,int)]
lis2=[i for i in lis if isinstance(i,float)]
lis3=[i for i in lis if isinstance(i,str)]

#! C1 duyệt qua một lần nhưng phải quản lý qua biến đếm thủ công, duyệt qua 3 lần nếu nhiều biến làm giảm hiệu suất
lis = [3, 5, 5.6, "zxc", 10.5, 'Jyno']
nguyen, thuc, chuoi = [], [], []
for item in lis:
    if isinstance(item, int):# Kiểm tra nếu là số nguyên
        nguyen.append(item)
    elif isinstance(item, float):# Kiểm tra nếu là số thực
        thuc.append(item)
    elif isinstance(item, str):# Kiểm tra nếu là chuỗi
        chuoi.append(item)        






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



inventory = {"Coca": [15, 5],"Pepsi": [15, 0],"Water": [10, 2],"Coffee": [20, 10]}
menu=list(enumerate(inventory.keys(),1))
while True:
    for i,item in menu:
        cost, quantity=inventory[item]
        status=f"{cost}k" if quantity>0 else "Out of stock"
        print(f"{i}.{item:<10}:{quantity:^3}|{status:<10}")
    try:
        print("0.Exit system")
        choice=int(input("\nOption: "))
        if choice==0:
            break
        idx = choice -1
        if not 0<=choice -1<len(menu):
            print("The option does not exist.")
            continue
        else:
            beverage=menu[idx][1]
            gia,sl=inventory[beverage]
        while True:
            sl_m=int(input("Nhập số lượng mua: "))
            if not 0<sl_m<=sl:
                print("Nhập lại số lượng mua: ")
                continue
            else:
                thanh_toan=sl_m*gia
                print(f"Số tiền cần thanh toán: {thanh_toan}")
                inventory[beverage][1]-=sl_m
                break
    except ValueError:
        print("Please enter your selection.")
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

gioi,tb,yeu=[],[],[]
for u in ds_hs:
    ten=u["ten"] #!AN TOÀN HƠN NẾU DÙNG: a,b,c=u.values() !Nếu ai đó thay đổi thứ tự trong dict thì sẽ làm sai phép tính
    diem_tb=round(u["diem"]*0.7+0.3*u["chuyen_can"],1)
    gioi.append(ten) if diem_tb>8 else yeu.append(ten) if diem_tb<=5 else tb.append(ten)





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
        nguoi_dang_nhap_max=user["user"] #!lấy tên người đăng nhập nhiều nhất
        max2=user["lan_dang_nhap"]
print("số lần đăng nhập nhiều nhất:",max2)
print("trung bình lượng đăng nhập:",round(tong_dn/(len(he_thong_user))))
print(nguoi_dang_nhap_max)


#!HOẶC
print("|{:10}|{:^20}|{:>10}|".format("user","độ dài pass","đánh giá"))
tong_dn=0
for user in he_thong_user:
    ten,mk=user["user"],user["pass"]

    muc_do="mạnh" if len(mk)>10 else "yếu" if len(mk)<6 else "trung bình"
    print(f"|{ten:10}|{len(mk):^20}|{muc_do:>10}|")

    tong_dn+=user["lan_dang_nhap"]
    
dn_max=max(he_thong_user, key=lambda x:x["lan_dang_nhap"])
print(f"{dn_max['user']} với số lần đăng nhập max: {dn_max['lan_dang_nhap']}")
print(f"Số lần đăng nhập tb: {tong_dn//len(he_thong_user)}")





