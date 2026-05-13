#Dictionary: thay vì dùng index để truy cập phần thử thì dict dùng các key
#! là một unhashable oject
#! Được giới hạn bởi ngoặc {}, ngăn cách nhau bởi dấu phảy
#! Các phần tử phải là 1 cặp key-value(ngăn cách nhau bởi dấu:) và key buộc phải là một hash oject

dic={"ten":"nguyen viet ha","nhìn": "đẹp trai"} 
dic1={"k1":1,"k1":2,"k1":3,"k4":2,"k5":3} # {"k1":3,"k4":2,"k5":3}
dic2={key: value for key, value in[("ten","nguyen viet ha"),("nhìn","đẹp trai")]} #dict conprehension
dic3={}     #tạo dict rỗng
dic4=dict() #tạo dict rỗng
#! Tạo dict từ Mapping oject: Chưa học


#? Khởi tạo bằng iterable:
iter_1 = [('name', 'Kteam'), ('member', 69)]
iter_2=iter_1 = (('name', 'Kteam'), ('member', 69))
dic_i1 = dict(iter_1) #{'name': 'Kteam', 'member': 69}
dic_i2 = dict(iter_2) #{'name': 'Kteam', 'member': 69}


f = [(' 2'), ('cd')] #!Khởi tạo dict bằng chuỗi như trên thì BẮT BUỘC ĐỘ DÀI CHUỖI phải là 2. 
print(dict(f)) #{' ': '2', 'c': 'd'}
               #!Giá trị đầu sẽ là key, giá trị thứ 2 là value.
               #! f= ("a2"), = [("a2")]

#? Khởi tạo bằng biến
name='vietha'
member=36
dic = dict(name='Ha', member=69) #Biến này không bị ảnh hưởng hoặc ảnh hưởng gì đến các biến bên ngoài
print(name,member)                  #'vietha', 36


#? Khởi tạo bằng fromkeys(iterable,default)
iter_ = ('ha', 36)
dic_none = dict.fromkeys(iter_) #{'ha': None, 36: None}
dic = dict.fromkeys(iter_, 'đz') #{'ha': 'đz', 36: 'đz'}


#? Lấy value trong dict
dic={"ten":"vietha","nhìn": "đz"} 
print(dic["ten"]) #vietha


#? Đổi nội dung dict 
dic["ten"]="viet ha" 
#! nếu thay đổi mà khi nhập tên không đúng sẽ tự thêm vào dict một key: value 
#! LƯU Ý: CÁCH NÀY KHÔNG DÙNG ĐỂ KHỞI TẠO 1 DICT MỚI ĐƯỢC
dic["tuoi"]=18 #{'ten': 'viet ha', 'nhìn': 'đz', 'tuoi': 18}

dic["tuoi"]+=1 #{'ten': 'nguyen viet ha dep trai', 'nhìn': 'đẹp trai', 'tuoi': 19}



#? CÁC PHƯƠNG THỨC TRONG DICT
    #copy(): sao chép
    #clear(): xoá dict
    #get(key,default): lấy value từ key
value=dic.get("ten") #viet ha
#! nếu không có ra sẽ hiện None hoặc default
value1=dic.get("name") #None
value2=dic.get("name"," không có dữ liệu") #không có dữ liệu


    #items():Trả về một giá trị thuộc lớp dict_items(là một iterable)
#Các giá trị của dict_items sẽ là một tuple với giá trị thứ nhất là key, giá trị thứ hai là value.
tur=dic.items()
print(tur) #dict_items([('ten', 'viet ha'), ('nhìn', 'đz'), ('tuoi', 19)])
    #! sau đó có thể ép kiểu list,tuple để lấy giá trị 
epkieu=list(tur)
print(epkieu[0][1]) #viet ha


    #keys():Trả về một giá trị thuộc lớp dict_keys. Các giá trị của dict_keys(là một iterable) sẽ là các key trong Dict
k=dic.keys()

    #values():Trả về một giá trị thuộc lớp dict_values. Các giá trị của dict_values(iterable) sẽ là các value trong Dict
v=dic.values()

    #pop(key,default):Bỏ đi phần tử có key và trả về value của key đó.TH không có key hiện KeyError hoặc default
    #popitem():Trả về một 2-tuple với key và value tương ứng BẤT KỲ
    #setdefault(key,default): trả về value nếu thấy key, nếu không thấy thì thêm "key":"default"(nếu không điền default mặc định là None)
dic={"ten":"viet ha","nhìn": "đz","tuoi":19}
set=dic.setdefault("sinhnam",2005) #{"ten":"viet ha","nhìn": "đz","tuoi":19,"sinhnam":2005}


    #update():
user_1 = {"name": "Hà", "age": 20}
new_data = {"age": 21, "city": "Hà Nội"}
user_1.update(new_data) #{'name': 'Hải', 'age': 21, 'city': 'Hà Nội'}

user_1.update(job="Developer", status="Active")

#Truyền một danh sách các Tuple
user_1.update([("phone", "0123"), ("email", "test@gmail.com")])
            #({("phone": "0123"), ("email": "test@gmail.com"}])
            #(phone= "0123", email="test@gmail.com")




#!TỔNG HỢP CÁCH THÊM MỘT KEY: VALUE MỚI
user = {"name": "Jyno"}

# C1: gán trực tiếp (phổ biến nhất)
user["age"] = 21

# C2: update() với dict
user.update({"phone": "0123"})

# C3: update() với list of tuples
user.update([("email", "jyno@gmail.com")])

# C4: update() với keyword arguments
user.update(city="Hanoi")

# C5: setdefault() — chỉ thêm nếu key CHƯA tồn tại
user.setdefault("country", "Vietnam")  # thêm được
user.setdefault("name", "abc")         # không thêm vì "name" đã có!

# C6: merge dict (Python 3.9+)
user = user | {"job": "AI Engineer"}








