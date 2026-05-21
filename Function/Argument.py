
#* Positional argument và keyword argument
sorted([3, 4, 1], reverse=True)
sorted([3, 4, 1], True) #!Không thể pass argument cho parameter reverse theo positinal argument
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must use keyword argument for key function"""


def Teo(a, b=2, c=3, d=4): #!CÁC GIÁ TRỊ BÊN TRONG NGOẶC() CHỈ LÀ CÁC PARAMETER VÀ b,c,d CÓ GIÁ TRỊ DEFAULT
                           #!(Khi gọi hàm): Cách bạn truyền vào mới tạo ra ARGUMENT
    f = (a + d) * (b + c)
    print(f)
Teo(1)       #Positional Argument (truyền theo vị trí)
Teo(a=1)     #Keyword Argument (truyền bằng tên biến)
Teo(1,2,3,5) #Positional Argument (truyền theo vị trí) d=5
Teo(1,c=4)   #Kết hợp

def kteam(pos_or_key_arg, *, key_arg1, key_arg2):#!Khi tạo một hàm mà có một parameter *(hoặc *identifier)
                                                 #!Thì Python sẽ hiểu đó không phải là parameter mà chính là syntax 
                                                 #!rồi nó biến các parameter sau * thành các KEYWORD ONLY ARGUMENT (chỉ nhận giá trị theo kiểu keyword argument)
    print(pos_or_key_arg)
    print(key_arg1)
    print(key_arg2)
kteam(1, key_arg1=2, key_arg2='Kteam')

"""
>>> kteam(1, 2, key_arg2='Kteam') #!Vì không có giá trị default nên phải truyền đủ và theo key word argument
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kteam() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given

>>> kteam(1, 2, 'Kteam')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kteam() takes 1 positional argument but 3 were given"""


#* Xem cấu trúc lệnh help()
help(sorted) #sorted(iterable, /, *, key=None, reverse=False)
"""Giải thích
Đằng trước dấu /: Là vùng Positional-Only (Cấm tuyệt đối không được gõ tên biến).
Đằng sau dấu / (nhưng trước dấu *): Là vùng tự do (Truyền kiểu vị trí hay gõ tên biến đều được).
Đằng sau dấu *: Là vùng Keyword-Only (Bắt buộc 100% phải gõ tên biến).
"""


#* Unpacking argument * và **
def tinh_the_tich(dai, rong, cao):
    return dai * rong * cao
kich_thuoc = [10, 5, 2]

# Cách thủ công, mất thời gian:
the_tich = tinh_the_tich(kich_thuoc[0], kich_thuoc[1], kich_thuoc[2])

# Cách Unpacking siêu gọn:
the_tich = tinh_the_tich(*kich_thuoc) 
print(the_tich) # Kết quả: 100

#!Nếu điền theo positinal sẽ gán theo thứ tự
def Teo(a, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")
kich_thuoc = [10]
Teo(*kich_thuoc) # Kết quả in ra: a=10, b=2, c=3
Teo(*kich_thuoc,3) # a=10, b=3, c=3

#!
def Teo(a, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")
kich_thuoc = [10,11]
Teo(*kich_thuoc) # Kết quả in ra: a=10, b=11, c=3
Teo(*kich_thuoc,4) # a=10, b=11, c=4

#!khi có dấu * ngăn cách positinal và keyword thì list chỉ được bằng số param trước dấu sao
def Teo(a,*, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")
kich_thuoc = [10,11]
Teo(*kich_thuoc) #!tức là chỉ những gì bên trái dấu * mới được lấy giá trị trong *kich_thuoc

def Teo(*a,b=2, c=3): # *a sẽ gom hết những positinal args, còn param sau dấu * đều là KEYWORD ONLY ARGUMENT 
    print(f"a={a}, b={b}, c={c}")
kich_thuoc = [10,11]
Teo(*kich_thuoc,12) #a=(10, 11, 12), b=2, c=3

#!param phía trước sẽ lấy giá trị rồi sau đó *b gom phần còn lại
def Teo(a,*b, c=3): # *b sẽ gom hết những positinal args
    print(f"a={a}, b={b}, c={c}")
kich_thuoc = [10,11,12,14]
Teo(*kich_thuoc,15) #a=10,b=(11,12,14,15), c=3

#!gom list
def Teo(a,*b, c): 
    print(f"a={a}, b={b}, c={c}")
Teo(*(x for x in range(7)),c=3) # a=0, b=(1, 2, 3, 4, 5, 6), c=3

#!magic
def Teo(a,*b, c): 
    print(f"a={a}, b={b}, c={c}")
kich_thuoc = [10,11,12,14]
Teo(*kich_thuoc,*(x for x in range(7)),c=3) # a=10, b=(11, 12, 14, 0, 1, 2, 3, 4, 5, 6), c=3
 
#!Nếu không unpack nó vẫn là cái bọc và gán toàn bộ
def Teo(a,*b, c): 
    print(f"a={a}, b={b}, c={c}")
kich_thuoc = [10,11,12,14]
Teo(kich_thuoc,*(x for x in range(7)),c=3)# a=[10, 11, 12, 14], b=(0, 1, 2, 3, 4, 5, 6), c=3

#!hay không
def Teo(*a,b, c):
    print(f"a={a}, b={b}, c={c}")
kich_thuoc = [10,11,12,14]
Teo(kich_thuoc,*(x for x in range(7)),b=2,c=3) #a=([10, 11, 12, 14], 0, 1, 2, 3, 4, 5, 6), b=2, c=3


#* Dict: unpacking **

def Teo(a):
    print(a)
Teo(a="hhhhh") #!Chỉ in ra hhhhh

def Teo(**a):
    print(a)
Teo(a="hhhhh") #!In ra dict {'a':hhhhh} 

def dic(a,b):
    print(a,b)
dic1={'a':2,"b":3}
dic(*dic1) #a,b
dic(*dic1.items()) #('a',2),('b',3)
dic(*dic1.values()) # 2,3


def tinh_the_tich(dai, rong, cao):
    return dai * rong * cao
hop_qua = {'dai': 10, 'rong': 5, 'cao': 2}
# Cách Unpacking Dict:
the_tich = tinh_the_tich(**hop_qua) # 100

#!Thiếu giá trị trong dict
def Teo(a, b, c): # Cả 3 đều bắt buộc
    print(a, b, c)
cau_hinh = {'a': 10, 'b': 20}
Teo(**cau_hinh)# 🔴 Lỗi: TypeError: Teo() missing 1 required positional argument: 'c'

#!Thừa giá trị trong dict
def Teo(a,b):
    print(a,b)
cau_hinh={'a':10,"b":8,"c":5}
Teo(**cau_hinh)# 🔴 Lỗi: TypeError: Teo() got an unexpected keyword argument 'c'

#!Packing kwargs
def Teo(a,b,**kwargs):
    print(a,b)
    for k, v in kwargs.items():
        print(k,"=>",v)
dic={"a":1,"b":2,"c":3,"d":4,"e":5}
Teo(**dic)

#! multiple value cho 1 param
def Teo(a, b, c):
    print(a, b, c)
cau_hinh = {'a': 10, 'b': 20}
# Bạn vừa giải nén 'b' từ dict (b=20), vừa cố tình ghi đè b=99 ở ngoài
Teo(**cau_hinh, b=99, c=30)# 🔴 Lỗi: TypeError: Teo() got multiple values for keyword argument 'b'

#!Nhiều dict
def Teo(a,b,c,d):
    print(a,b,c,d)
dic1={"a":1,"b":2}
dic2={"c":3,"d":4}
Teo(**dic1,**dic2)

#!unpacking list và dict
def Teo(a, b, c, d):
    print(a, b, c, d)
list_truoc = [10]
dict_sau = {'c': 30, 'd': 40}
Teo(20, *list_truoc, **dict_sau) # Nhưng dict_sau lại chứa key 'c' và 'd'. Kết quả in ra: 20 10 30 40

#!kết hợp
def Teo(a, *b, c, d):
    print(a, b, c, d)
list_truoc = [10]
dict_sau = {'c': 30, 'd': 40}
Teo(20, *list_truoc, **dict_sau) #20 (10,) 30 40 

#!Lưu ý: vị trí param
def Teo(a, *b, c,**d): # không được để param nào sau **c (a,*b,**c,d)
    print(a, b, c, d)
list_truoc = [10]
dict_sau = {'c': 30, 'd': 40,'e':50} #và khi gom vào **d thì không cần phải trùng key nếu không thì phải bắt buộc trùng
Teo(20, *list_truoc, **dict_sau) 

#!VD
def Teo(a, *b, d, **c):
    print(a, b, c, d)
Teo(1, 2, 3, x=10, z=20, y=30,d=22)#1 (2, 3) {'x': 10, 'z': 20, 'y': 30} 22


def Teo(a, b, *, c, **kwargs):
    print(a, b, c, kwargs)
list_data = [1]
dict_data = {'c': 3, 'd': 4}
Teo(*list_data, 2, **dict_data)#! c là keyword only agrs và **dict_data nên c sẽ lấy giá trị trong dict 
