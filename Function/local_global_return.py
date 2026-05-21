
#* LOCAL/GLOBAL
#*Khai báo ngoài hàm
kteam = 'How Kteam'
def say_slogan():
    print("We are", kteam)
say_slogan() #We are How Kteam

#!Khai báo trong hàm
def make_slogan():
    kteam = 'How Kteam'
print(kteam) #Lỗi không tìm thấy tên kteam
#!Biến khai báo ở hàm cha có thể sử dụng trong hàm con nhưng biến ở hàm con không thể sử dụng ở hàm cha.





#*Pass by value: Thay đổi giá trị bản sao của bản gốc
lst = [1, 2, 3]
tup = tuple('Education')
def change(parameter): 
    parameter = 'New value' # Đã gán giá trị param = "New value" nhưng bản gốc vẫn không thay đổi
    print('Changed successfully!')
change(lst) #Changed successfully!
change(tup) #Changed successfully!
print('{}\n{}'.format(lst, tup))
#[1, 2, 3]
#('E', 'd', 'u', 'c', 'a', 't', 'i', 'o', 'n')

#*Pass by reference: Thay đổi giá trị của bản gốc
lst=[1,2,3]
def change(param):
    for i in range(len(lst)):
        param[i]=10-i #!Truy cập vào index rồi thay đổi bản gốc của lst
                      #!tạo ra biến param và cho nó chỉ chung vào list của lst
    return param      #! return trong trường hợp này vô dụng vì bản gốc đã thay đổi nên dùng luôn lst chứ không cần phải return
change(lst)
print(lst)
print(change(lst))

#*có thể dùng biến bên ngoài hàm khi khởi tạo bằng global bên trong hàm def
def make_slogan():
    global kteam        # khởi tạo với global không có giá trị nhé
                        #!HẠN CHẾ SỬ DỤNG VÌ NÓ KHÓ KIỂM SOÁT LÀM CHO CHƯƠNG TRÌNH TRỞ NÊN RỐI HƠN
    kteam = 'How Kteam' # sau khi khởi tạo xong, ta mới gán giá trị
make_slogan()# nhớ là phải chạy hàm nữa
print(kteam) # 'How Kteam'

def make_global():
    global x
    x = 1
def local():
    x = 5 #!BIẾN x Ở BÊN TRONG NHƯNG CŨNG CHẢ LIÊN QUAN GÌ ĐẾN BIẾN x BÊN NGOÀI VÀ NÓ CHỈ TỒN TẠI BÊN TRONG HÀM THÔI
    print('x in local', x)
make_global()
print(x) #1
local()  #5
print(x) #1

#*Hàm locals(), globals()
#Hàm locals cho ta biết được những biến local (những biến được khai báo trong hàm) nằm trong chương trình của chúng ta
#Globals là hàm giúp chúng ta biết được những  biến global trong chương trình.
#!Chỉ những biến globals() có giá trị mới được trả về





#* RETURNNNNNNNNNNNN
def cal_rec_per(width, height):
    per = (width + height) * 2
    return per
rec_1_width ,rec_1_height = 3,5
# khởi tạo một biến để hứng kết quả
rec_1_per = cal_rec_per(rec_1_width, rec_1_height)
print(rec_1_per)
print(cal_rec_per(7, 4)) # trường hợp này là khi bạn không cần tái sử dụng nó ở lần sau

def _return_ter_func():
    print('chúng ta sử dụng return để ngắt hàm') 
    # dòng dưới đây tương tự như bạn viết return None
    return
    print('Hàm print này dĩ nhiên không được gọi')
none = _return_ter_func()
print(type(none)) # <class 'NoneType'>

#*Dùng return nhiều giá trị
def cal_rec_area_per(width, height):
    perimeter = (width + height) * 2
    area = width * height
    return perimeter, area
rec_width ,rec_height = 3,9
rec_per, rec_area = cal_rec_area_per(rec_width, rec_height)
print(rec_per, rec_area)


"""Như các bạn đã biết khái niệm hàm số....
Với hàm số y = f(x) thì đồ thị hàm số y = f(x) đi qua điểm M(x0, y0) nếu như y0 = f(x0).
Cho một list, mỗi phần tử là một tuple gồm hoành độ (x0) và tung độ (y0), kiểm tra xem đồ thị hàm số y = f(x) có đi qua điểm đó hay không. Nếu có thì đưa sang list A, trường hợp không thì đưa phần tử đó sang list B.

Sau khi kết thúc, tính tổng các tung độ (y0) của hai list A và B rồi in ra trị tuyệt đối của hiệu tổng tung độ hai list đó.

"""
#*CÁCH 1:
def ktra(ds_ktra):
    lstA=[]
    lstB=[]
    for a,b in ds_ktra: #! ds_ktra = data = [(-5, -20), (-4, -15), (-3, 4), (-2, 9), (-1, 7), (0, 1), (1, -7), (2, -9), (4, 81), (5, 130)]
                        #! a,b lấy từng số trong tuple kiểm tra
        if b==a**3+2*a**2-4*a+1:
            lstA.append(a,b)
        else:
            lstB.append(a,b)
    tongA=sum(a[1] for a in lstA)
    tongB=sum(b[1] for b in lstB)
    hieu=abs(tongA-tongB)
    return lstA,lstB,hieu
data = [(-5, -20), (-4, -15), (-3, 4), (-2, 9), (-1, 7), (0, 1), (1, -7), (2, -9), (4, 81), (5, 130)]
print(ktra(data))

#*CÁCH 2:
def f_x(x):
    return x**3+2*x**2-4*x+1
def ktra(x,y):
    if y==f_x(x):
        return True
    return False
def fill_point(lst_point):
    lstA=[]
    lstB=[]
    for l in lst_point:
        if ktra(*l):
            lstA.append(l)
            continue
        lstB.append(l)
    return lstA,lstB
def cal_sum(lst):
    s = 0
    for value in lst:
        s += value[1]
    return s
    
lst = [(-5, -20), (-4, -15), (-3, 4), (-2, 9), (-1, 7), (0, 1), (1, -7), (2, -9), (4, 81), (5, 130)]
lst_A_after, lst_B_after = fill_point(lst)
print(abs(cal_sum(lst_A_after) - cal_sum(lst_B_after)))












