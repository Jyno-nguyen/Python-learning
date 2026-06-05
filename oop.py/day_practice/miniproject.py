
"""Project 1: Bank Account
- Class BankAccount
- Deposit, withdraw, check balance
- Không cho rút quá số dư
- Lưu lịch sử giao dịch
"""
#* Vì deposit và withdraw là nạp và rút tiền nếu ta lạm dụng setter thì lệnh gán deposit bằng sẽ không hợp quy chuẩn, khiến người đọc bị rối
#* Nên hạn chế tối đa việc tạo ra giá trị thừa như trong bài này, chỉ cần biến balance hoạt động không cần thêm deposit và withdraw để làm gì
class BankAccount:
    def __init__(self,initial_deposit):
        self.stt=1
        self._history=[]
        self._balance=0
        self.deposit(initial_deposit)
    @property
    def balance(self):
        return self._balance #! giá trị balance nên để số thay chuỗi vì có thể phục vụ cho tính toán
        
    @property
    def history(self):
        return self._history
    
    def deposit(self,amount):
        if not isinstance(amount,(int,float)) or amount<=0:
            raise ValueError("Số tiền nạp là số nguyên lớn hơn 0")
        self._balance+=amount
        self.history.append(f"Giao dịch {self.stt}: +{amount}")
        self.stt+=1
    
    def withdraw(self,amount):
        if not isinstance(amount,(int,float)) or amount<=0:
            raise ValueError("Số tiền rút là số nguyên lớn hơn 0")
        if amount>self._balance:
            raise ValueError("Số dư không đủ")
        self._balance-=amount
        self.history.append(f"Giao dịch {self.stt}: -{amount}")
        self.stt+=1
    def __str__(self):
        return f"Bank Account | Balance: {self._balance:,}"
        #* Nếu có f"{self}" sẽ dẫn đến vòng lặp vô tận vì sẽ tìm __str__(self) để chạy















"""Project 2: Student Management
- Class Student (tên, tuổi, điểm 3 môn)
- Tính GPA, xếp loại tự động
- Class Classroom chứa danh sách Student #!Chứ không phải là kế thừa
#* quan hệ kế thừa "is A" ví dụ trong trường hợp này là Classroom is Student: nhưng classroom không thể là 1 student
#* Classroom chứa Student là quan hệ "has A" tức chứa đối tượng của class Student chứ không kế thừa
- Tìm thủ khoa, sắp xếp theo GPA"""

class Student:
    def __init__(self, name, age, math_score, literature_score, english_score):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Tên không hợp lệ")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Tuổi không hợp lệ")
            
        self.name = name

        self.age = age
        # Nạp điểm qua setter để tự động kích hoạt hàm check dữ liệu bẩn
        self.math_score = math_score
        self.literature_score = literature_score
        self.english_score = english_score
    
    @staticmethod
    def _check(value):
        if not isinstance(value,(float,int)):
            raise ValueError("Điểm phải là số")
        if not 0 <= value <= 10:
            raise ValueError("Điểm có giá trị nằm trong khoảng từ 0 - 10")
        return value
    
    @property 
    def math_score(self): return self._math_score
    @math_score.setter
    def math_score(self, value): self._math_score = Student._check(value)

    @property 
    def literature_score(self): return self._literature_score
    @literature_score.setter
    def literature_score(self, value): self._literature_score = Student._check(value)

    @property 
    def english_score(self): return self._english_score
    @english_score.setter
    def english_score(self, value): self._english_score = Student._check(value)

    # --- TÍNH TOÁN TỰ ĐỘNG ---
    @property
    def gpa(self):
        return round((self._math_score + self._literature_score + self._english_score) / 3, 2)
    
    @property
    def xep_loai(self):
        if self.gpa >= 8: return "Gioi"
        elif self.gpa >=5: return "Kha"
        else: return "Yeu"
    
    def __str__(self):
        return f"{self.name} | GPA: {self.gpa} | {self.xep_loai}"


class Classroom: #!Khởi tạo classroom
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []  
        

    def add_student(self, student):
        if isinstance(student, Student) and student not in self.students: #! isinstance lúc này hoạt động như thế nào
            #isinstance sẽ dựa vào param bên phải là class Student để tìm đặc điểm cần có của đối tượng bên phải rồi sẽ so sánh xem chúng có đặc điểm đó không

            self.students.append(student) #* nó không tạo ra ĐỐI TƯỢNG MỚI mà chỉ lấy sợi dây trỏ thẳng vào đối tượng cũ, nên khi thay đổi giá trị đối tượng bên class student thì giá trị trong danh sách cũng thay đổi theo
            #self.students.append(student.__dict__): thì nó chỉ lấy những thuộc tính từ __init__ ra để thêm vào, và cũng tương tự nếu thuộc tính ấy thay đổi thì [] chứa những đối tượng cũng sẽ thay đổi thuộc tính đó
            print(f"Đã thêm học sinh {student.name} vào lớp.")
            
    def sap_xep_theo_gpa(self):
        #self.students sẽ là danh sách các đối tượng, lấy ra đối tượng s, và lấy ra thuộc tính s.gpa
        return sorted(self.students, key=lambda s: s.gpa, reverse=True)
    
    def tim_thu_khoa(self):
        if not self.students: 
            return []
        max_gpa = max(s.gpa for s in self.students)
        return [s for s in self.students if s.gpa == max_gpa]
    
    #* Lấy danh sách điểm toán nhưng tại sao lại dùng math_score mà không dùng luôn _math_score
    #* _math_score giống như biến ẩn(Protected/private) nếu truy cập trực tiếp ở class khác thì giống như đi cửa sau là điều không nên
    #* thay vào đó nên đi thẳng cửa chính math_score 
    #! Hay vì 1 điều kiện an toàn hơn là nếu ở getter math_score không return về _math_score mà là một biểu thức nào đó thì sẽ sai hoàn toàn
    def ds_diem_toan(self):
        return [score.math_score for score in self.students]
# 1. Tạo lớp học
my_class = Classroom("12A1")

# 2. Tạo các học sinh
st1 = Student("Vũ", 18, 9, 10, 7)    # GPA = 8.67
st2 = Student("An", 18, 10, 9, 10)  # GPA = 9.67
st3 = Student("Bình", 18, 5, 6, 5)  # GPA = 5.33

# 3. Thêm học sinh vào lớp
my_class.add_student(st1)
my_class.add_student(st2)
my_class.add_student(st3)

for hs in my_class.sap_xep_theo_gpa():
    print(f"Tên: {hs.name} | GPA: {hs.gpa} | Xếp loại: {hs.xep_loai}")

for tk in my_class.tim_thu_khoa():
    print(f"Chúc mừng Thủ Khoa: {tk.name} với số điểm GPA tuyệt đối: {tk.gpa}")















"""- Class Product (tên, giá, số lượng)
- Thêm/xóa/cập nhật sản phẩm
- Tìm sản phẩm hết hàng
- Tính tổng giá trị kho"""

#*cập nhật sản phẩm
class Product:
    def __init__(self,name,price,stock):
        if  not isinstance(name,str) or not name.strip(): #!lƯU Ý: NẾU ĐỂ name.strip() trước mà name không phải chuỗi sẽ lỗi nên phải để sau
            raise ValueError("loi nhap ten san pham")
        self.name=name
        self.price=price
        self.stock=stock
    
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        if not isinstance(value,(float,int)):
            raise ValueError("Gia phai la so")
        if value <0:
            raise ValueError("Gia phai lon hon = 0")
        self._price=value
    
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self,amount):
        if not isinstance(amount,int):
            raise ValueError("So luong phai la so")
        if amount < 0:
            raise ValueError("So luong phai lon hon = 0")
        self._stock=amount
        

#*Kho hàng
class Warehouse:
    def __init__(self,name):
        self.name=name
        self.khohang=[]

    def add_product(self,product):
        if not isinstance(product,Product):
            raise ValueError("Khong tim thay san pham")
        if not product.name in [sp.name for sp in self.khohang]:
            self.khohang.append(product)
            print(f"Đã thêm sản phẩm {product.name} vào kho hàng {self.name}")
            return

        else:
            for sp in self.khohang:
                if sp.name==product.name:   # lấy giá trị stock cũ bên trong kho hàng
                    sp.stock+=product.stock # cộng giá trị stock mới để cập nhật
                    print("Sản phẩm đã có trong kho hàng, số lượng đã được cập nhật")
                    return

    #* remove_product
    def remove_product(self,name):
        for sp in self.khohang:
            if sp.name==name:
                self.khohang.remove(sp)
                print(f"Đã xóa sản phẩm {name} ra khỏi kho.")
                return
        print(f"Không tìm thấy sản phẩm nào tên là {name} để xóa.")
        return None
    
    #* update_product
    def update_product(self,name):
        for sp in self.khohang:
            if sp.name==name:
                choice=input("1.Thay đổi số lượng | 2.Thay đổi giá: ")
                if choice=='1':
                    try:
                        sl=int(input("Nhập số lượng: ")) #!không cần điều kiện vì tí nhảy vào setter thì sẽ có điều kiện để kiểm tra nếu có lỗi sẽ nhảy xuống except
                        sp.stock=sl
                        print("Sản phẩm đã có trong kho hàng, số lượng đã được cập nhật")
                    except ValueError as E:
                        print(f"{E}")
                    return
                
                if choice=='2':
                    try:
                        gia=int(input("Nhập số giá: "))
                        sp.price=gia
                        print("Sản phẩm đã có trong kho hàng, giá đã được cập nhật")
                    except ValueError as E:
                        print(f"{E}")
                    return
        print("Không tìm thấy sản phẩm")

    def get_out_of_stock(self):
        return [sp for sp in self.khohang if sp.stock==0]
    
    def get_total_value(self):
        return sum(sp.price*sp.stock for sp in self.khohang)


kho_shopee= Warehouse("Kho Hà Nội")


#!LƯU Ý:
p1 = Product("iPhone 15", 20000000, 10)  # ô nhớ A
kho_shopee.add_product(p1)   # kho giữ reference đến ô nhớ A

p1 = Product("iPhone 15", 20000000, 11)  # ô nhớ C mới
# p1 giờ trỏ sang C
# kho vẫn trỏ vào A → không đổi!

# Nhưng nếu:
p1.stock = 11  # thay đổi TRỰC TIẾP qua instance
# p1 và kho cùng trỏ A → cả 2 đều thấy thay đổi!

#* Đây gọi là:
# - Reference — biến chỉ là "sợi dây" trỏ vào ô nhớ
# - Mutable object — object có thể thay đổi nội dung bên trong
# - Aliasing — nhiều biến cùng trỏ 1 ô nhớ 














"""- Class Animal (tên, tuổi, tiếng kêu)
- Class Dog, Cat, Bird kế thừa Animal
- Override method speak() cho từng loại
- Polymorphism: gọi speak() cho list nhiều loại"""

class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound  
    def speak(self):
        #Báo lỗi nếu không override
        raise NotImplementedError("Subclass phải override method này!")   
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, sound="Gâu Gâu!")
    def speak(self):
        return f"{self.name} ({self.age} tuổi) {self.sound}!"
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, sound="Meo Meo!")
    def speak(self):
        return f"{self.name} ({self.age} tuổi) {self.sound}!"
class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, sound="Chíp Chíp!")
    def speak(self):
        return f"{self.name} ({self.age} tuổi) {self.sound}!"
if __name__ == "__main__":
    so_thu = [Dog("Cậu Vàng", 3),Cat("Miu Miu", 2),Bird("Họa Mi", 1),Dog("Mực", 5)]
    for con_vat in so_thu:
        print(con_vat.speak())

#!HOẶC NẾU BẮT BUỘC PHẢI THEO CẤU TRÚC CỦA CHA GHI ĐÈ override
from abc import ABC, abstractmethod
class Animal(ABC):  
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound 
    @abstractmethod #!Lệnh bắt buộc những thằng con phải có speak()
    def speak(self):
        return f"{self.name} ({self.age} tuổi)"

class Dog(Animal):
    #có thể như này
    def speak(self):
        phandau=super().speak(self)
        return f"{phandau}:{self.sound}!"
    
class Cat(Animal):
    #cũng có thể như này
    def speak(self):
        return f"{self.name} ({self.age} tuổi) {self.sound}!"
class Bird(Animal):
    def speak(self):
        return f"{self.name} ({self.age} tuổi) {self.sound}!"
if __name__ == "__main__":
    so_thu = [Dog("Cậu Vàng", 3),Cat("Miu Miu", 2),Bird("Họa Mi", 1),Dog("Mực", 5)]
    for con_vat in so_thu:
        print(con_vat.speak())

#!HOẶC 
class Animal:
    def __init__(self, name, age, sound="Tiếng kêu mặc định"):
        self.name = name
        self.age = age
        self.sound = sound  

    def speak(self):
        return f"{self.name} ({self.age} tuổi) phát ra tiếng: {self.sound}"
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, sound="Gâu Gâu!")
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, sound="Meo Meo!")
class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, sound="Chíp Chíp!")
if __name__ == "__main__":
    so_thu = [Dog("Cậu Vàng", 3),Cat("Miu Miu", 2),Bird("Họa Mi", 1),Dog("Mực", 5)]
    for con_vat in so_thu:
        print(con_vat.speak())














"""- Class Employee (tên, lương cơ bản)
- Class FullTime, PartTime, Freelancer kế thừa
- Mỗi loại tính lương khác nhau
- Tính tổng lương cả công ty"""

from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,salary_basic):
        if not isinstance(name,str) or not name.strip():
            raise ValueError("Nhập tên không hợp lệ")
        self.name=name
        self.salary_basic=salary_basic

    @abstractmethod
    def calculate_salary(self):
        pass

    @property
    def salary_basic(self):
        return self._salary_basic
    @salary_basic.setter
    def salary_basic(self,salary):
        if not isinstance(salary,(float,int)) or salary<0:
            raise ValueError("Lương không được thấp hơn 0")
        self._salary_basic=salary
#
class Fulltime(Employee):
    def __init__(self,name,salary_basic,bonus):
        super().__init__(name,salary_basic)
        self.bonus=bonus
    
    #! calculate_salary
    def calculate_salary(self):
        return self.salary_basic + self._bonus

    @property
    def bonus(self):
        return self._bonus
    @bonus.setter
    def bonus(self,value):
        if not isinstance(value,(float,int)) or value<0:
            raise ValueError("Bonus không được nhỏ hơn 0")
        self._bonus=value
#  
class Parttime(Employee):
    def __init__(self,name,salary_basic,working_hours,hourly_rate):
        super().__init__(name,salary_basic)
        self.working_hours=working_hours
        self.hourly_rate=hourly_rate
    
    #! calculate_salary
    def calculate_salary(self):
        return self.salary_basic + (self._working_hours*self._hourly_rate)
    
    @property
    def working_hours(self):
        return self._working_hours
    @working_hours.setter
    def working_hours(self,hours):
        if not isinstance(hours,(float,int)) or hours<0:
            raise ValueError("Số giờ không được nhỏ hơn 0")
        self._working_hours=hours
    
    @property
    def hourly_rate(self):
        return self._hourly_rate
    @hourly_rate.setter
    def hourly_rate(self,salary_hour):
        if not isinstance(salary_hour,(float,int)) or salary_hour<0:
            raise ValueError("Lương theo giờ không được nhỏ hơn 0")
        self._hourly_rate=salary_hour
#    
class Freelancer(Employee):
    def __init__(self,name,salary_basic,projects_completed,rate_per_project):
        super().__init__(name,salary_basic)
        self.projects_completed=projects_completed
        self.rate_per_project=rate_per_project
    
    #! calculate_salary
    def calculate_salary(self):
        return self.salary_basic + (self._projects_completed*self._rate_per_project)
    
    @property
    def projects_completed(self):
        return self._projects_completed
    @projects_completed.setter
    def projects_completed(self,count):
        if not isinstance(count,(int)) or count<0:
            raise ValueError("Số dự án không được nhỏ hơn 0")
        self._projects_completed=count

    @property
    def rate_per_project(self):
        return self._rate_per_project
    @rate_per_project.setter
    def rate_per_project(self,money):
        if not isinstance(money,(float,int)) or money<0:
            raise ValueError("Số tiền dự án không được nhỏ hơn 0")
        self._rate_per_project=money
#  
class Company:

    def __init__(self,name_company):
        self.name_company=name_company
        self.employee_list=[]
    def add_employee(self,emp):
        if not isinstance(emp,Employee): 
            raise ValueError("Nhân viên không có trong công ty")
        if emp in self.employee_list:
            print("Nhân viên đã có trong bảng lương")
            return 
        self.employee_list.append(emp)
    
    def get_total_payroll(self):
        return sum(emp.calculate_salary() for emp in self.employee_list)
    def __str__(self):
        return f"{self.get_total_payroll():,}"

cong_ty_shopee = Company("Shopee Việt Nam") # 1. Khởi tạo công ty

nv1 = Fulltime("Nguyễn Văn A", 10000000, bonus=2000000)        # Lương = 10tr + 2tr = 12tr
nv2 = Parttime("Trần Thị B", 2000000, working_hours=80, hourly_rate=50000) # Lương = 2tr + (80*50k) = 6tr
nv3 = Freelancer("Lê Văn C", 0, projects_completed=3, rate_per_project=4000000) # Lương = 3*4tr = 12tr

cong_ty_shopee.add_employee(nv1)
cong_ty_shopee.add_employee(nv2)
cong_ty_shopee.add_employee(nv3)

print(f"Tổng lương công ty phải chi: {cong_ty_shopee} VNĐ") # Kết quả kỳ vọng: 12tr + 6tr + 12tr = 30,000,000 VNĐ














"""- Class Shape (abstract)
- Class Circle, Rectangle, Triangle kế thừa
- Override area(), perimeter() cho từng loại
- Tìm hình có diện tích lớn nhất"""

from abc import ABC,abstractmethod
import math 
class Shape(ABC):

    @staticmethod
    def _check(value):
        return isinstance(value,(float,int)) and value >0

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
    def __str__(self):
        return f"Area: {self.area()} | Perimeter: {self.perimeter()}"
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return round(self._radius**2*math.pi,2)

    def perimeter(self):
        return round(self._radius*2*math.pi,2)

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,value):
        if not self._check(value):
            raise ValueError("Bán kính hình tròn phải lớn hơn 0")
        self._radius=value

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return round(self._width*self._height,2)

    def perimeter(self):
        return round(2*(self._width+self._height),2)
    
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if not self._check(value):
            raise ValueError("Chiều rộng hcn phải lớn hơn 0")
        self._width=value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if not self._check(value):
            raise ValueError("Chiều dài hcn phải lớn hơn 0")
        self._height=value

class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

        if not self._validate_triangle_rules():
            raise ValueError("Ba cạnh này không thể tạo thành một hình tam giác")

    def area(self):
        p=(self._a+self._b+self._c)/2
        return round(math.sqrt(p*(p-self._a)*(p-self._b)*(p-self._c)),2)

    def perimeter(self):
        return round((self._a+self._b+self._c),2)

    @property
    def a(self):
        return self._a
    @a.setter
    def a(self,value):
        if not self._check(value):
            raise ValueError("Cạnh tam giác phải lớn hơn 0")
        self._a=value
    
    @property
    def b(self):
        return self._b
    @b.setter
    def b(self,value):
        if not self._check(value):
            raise ValueError("Cạnh tam giác phải lớn hơn 0")
        self._b=value

    
    @property
    def c(self):
        return self._c
    @c.setter
    def c(self,value):
        if not self._check(value):
            raise ValueError("Cạnh tam giác phải lớn hơn 0")
        self._c=value
    
    def _validate_triangle_rules(self):
        return (self._a + self._b > self._c) and (self._c + self._b > self._a) and (self._a + self._c > self._b)
if __name__ == "__main__":
    shapes = [Circle(radius=5), Rectangle(width=10, height=5), Triangle(a=3, b=4, c=5)]
area_max=max(shapes,key=lambda s: s.area())
print(f"{type(area_max).__name__} has max area: {area_max.area()}")

#!Muốn lấy tên của class
"""Khi bạn có một Class tên là Circle
   print(Circle) #<class '__main__.Circle'>.
   #*.__name__(một thuộc tính ẩn trong class/dunder attribute), nó chỉ bóc tách đúng cái tên sạch dạng chuỗi ra thôi
   area_max là instance. Hàm type(area_max) sẽ kiểm tra xem instance thuộc Class nào → Nó trả về Class Circle.
   Khi đã có Class Circle rồi, .__name__ để lấy ra chữ "Circle" dạng chuỗi nhằm mục đích in ra màn hình cho đẹp.
   #!Bạn chỉ có thể dùng .__name__ trên Class hoặc Hàm, chứ không thể dùng trực tiếp trên một đối tượng (instance)."""   














"""Project 7: Library System
- Class Book (tên, tác giả, ISBN)
- Class Member (tên, ID)
- Class Library quản lý sách + thành viên
- Mượn/trả sách, kiểm tra sách có sẵn không
- Phạt nếu trả trễ
"""
class Book:
    def __init__(self,title,author,ISBN,quantity): # International Standard Book Number
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.quantity=quantity
        self._borrowed_count=0 #!Ban đầu nhập sách nên sẽ không có số lượng sách đã mượn

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self,num):
        if not isinstance(num,int) or num<0:
            raise ValueError("Số sách trong thư viện phải lớn hơn = 0")
        self._quantity=num
    
    @property
    def borrowed_count(self):
        return self._borrowed_count
    @borrowed_count.setter
    def borrowed_count(self,num):
        if not isinstance(num,int) or num<0:
            raise ValueError("Số sách cho mượn trong thư viện phải lớn hơn = 0")
        if num>self._quantity:
            raise ValueError("Số sách cho mượn không được lớn hơn tổng số sách")
        self._borrowed_count=num

class Member:
    def __init__(self,ID,name):
        self.ID=ID
        self.name=name
        self.borrowed_books=[]


class Library:
    def __init__(self,library):
        self.library=library
        self.books_library=[]
        self.members_list=[]

    def add_book(self,book):
        if not isinstance(book,Book):
            raise ValueError("Không tìm thấy dữ liệu sách")
        if not book.ISBN in [b.ISBN for b in self.books_library]:
            self.books_library.append(book)
            print(f"{book.title} đã được thêm vào trong thư viện")
            return
        else:
            for b in self.books_library:
                if b.ISBN==book.ISBN:
                    b.quantity+=book.quantity
                    # b.borrowed_count+=book.borrowed_count #!Ban đầu nhập sách nên sẽ không có số lượng sách đã mượn
                    print(f"{book.title} đã cập nhật số lượng")
                    return
                
    def add_member(self,member):
        if not isinstance(member,Member):
            raise ValueError("Không tìm thấy thông tin thành viên")
        if not member.ID in [m.ID for m in self.members_list]:
            self.members_list.append(member)
            print(f"{member.name} đã trở thành thành viên")
            return
        print("Bạn đã có trong danh sách thành viên")
    

    def borrow_book(self, member_ID, ISBN, current_date):
        if not member_ID in [m.ID for m in self.members_list]:
            print("Vui lòng đăng ký thành viên để được mượn sách")
            return
        if not ISBN in [b.ISBN for b in self.books_library]:
            print("Không tìm thấy sách")
            return
        
        for book in self.books_library:
            if book.ISBN==ISBN:
                if book.quantity==book.borrowed_count:
                    print("Sách đã được mượn hết")
                    return
                book.borrowed_count+=1
                for member in self.members_list:
                    if member.ID==member_ID:
                        # member.borrowed_books = { "ISBN-111": [1, 5] }
                        if not ISBN in member.borrowed_books.keys():
                            member.borrowed_books[ISBN]=[current_date]
                        else:
                            member.borrowed_books[ISBN].append(current_date)
                        print(f"Thành viên: {member.ID} đã mượn sách thành công")
                        return

                        # member.borrowed_books[ISBN]=current_date #!Nếu mượn 2 quyển cùng loại dẫn đến việc bị ghi đè dẫn đến việc mất ngày cũ
                        # member.borrowed_books.append({"ISBN":ISBN,"date":current_date}) #! Tìm kiếm chậm hơn (phải loop)
                                                                                          #!  Vô tình lấy ngày đầu tiên (bug tiềm ẩn)
                
                    
    def return_book(self, member_ID, ISBN, return_date):
        if not member_ID in [m.ID for m in self.members_list]:
            print("Không có trong danh sách thành viên")
            return
        for member in self.members_list:
            if member.ID==member_ID:
                if ISBN in member.borrowed_books.keys():
                    borrow_day=member.borrowed_books[ISBN].pop(0)
                    if member.borrowed_books[ISBN]==[]:
                        member.borrowed_books.pop(ISBN)
                    for book in self.books_library:
                        if book.ISBN==ISBN:
                            book.borrowed_count-=1 
                            days_overdue=return_date-borrow_day-14
                            if days_overdue>0:
                                fine = days_overdue * 5000
                                print(f"Trả sách thành công. Trễ hạn {days_overdue} ngày. Tiền phạt: {fine} VNĐ")
                            else:
                                print("Trả sách thành công")
                            return
                print("Không tìm thấy trong danh sách mượn")
                return

        
if __name__ == "__main__":
    thu_vien = Library("A")
    sach_1 = Book("Lap trinh Python", "Guido", "ISBN-111", quantity=2)
    sach_2 = Book("Dat rung phuong Nam", "Doan Gioi", "ISBN-222", quantity=1)

    thu_vien.add_book(sach_1) # Kỳ vọng: Thêm thành công
    thu_vien.add_book(sach_2) # Kỳ vọng: Thêm thành công
    
    sach_trung = Book("Lap trinh Python", "Guido", "ISBN-111", quantity=1)
    thu_vien.add_book(sach_trung) # Kỳ vọng: Cập nhật số lượng lên thành 3 cuốn (2 + 1)

    # Thuộc tính member.borrowed_books khởi tạo là một dict trống {} trong __init__
    user_A = Member("TV001", "Nguyen Van A")
    user_B = Member("TV002", "Tran Thi B")
    
    thu_vien.add_member(user_A) # Kỳ vọng: Thành công
    thu_vien.add_member(user_A) # Kỳ vọng: Báo trùng "Bạn đã có trong danh sách..."
    
    thu_vien.borrow_book("TV_LAU", "ISBN-111", current_date=1) 
    # Kỳ vọng: "Vui lòng đăng ký thành viên..."

    thu_vien.borrow_book("TV001", "ISBN-KHONG-CO", current_date=1) 
    # Kỳ vọng: "Không tìm thấy sách"

    thu_vien.borrow_book("TV001", "ISBN-111", current_date=1) 
    # Kỳ vọng: Thành công (Python còn 2 cuốn trên kệ)

    thu_vien.borrow_book("TV001", "ISBN-111", current_date=5) 
    # Kỳ vọng: Thành công (Python còn 1 cuốn trên kệ)
    
    thu_vien.add_member(user_B) # Đăng ký người B
    thu_vien.borrow_book("TV002", "ISBN-111", current_date=10) 
    # Kỳ vọng: Thành công (Python còn 0 cuốn trên kệ)

    thu_vien.borrow_book("TV002", "ISBN-111", current_date=12) 
    # Kỳ vọng: "Sách đã được mượn hết"


    # Người A trả cuốn Python mượn từ ngày 1 vào ngày 10 (Giữ 9 ngày -> Không quá hạn 14 ngày)
    thu_vien.return_book("TV001", "ISBN-111", return_date=10)
    # Kỳ vọng: Trả thành công, không phạt, tăng lại số lượng sách trên kệ.

    # Người A trả cuốn Python mượn từ ngày 5 vào ngày 25 (Giữ 20 ngày -> Quá hạn 6 ngày)
    thu_vien.return_book("TV001", "ISBN-111", return_date=25)
    # Kỳ vọng: Trả thành công, báo phạt trễ hạn 6 ngày * 5000 = 30,000 VNĐ.













"""Project 8: Online Shop
- Class Product, Cart(giỏ hàng), Order, Customer
- Thêm/xóa sản phẩm khỏi giỏ hàng
- Tính tổng tiền, áp dụng mã giảm giá
- Lưu lịch sử đơn hàng của từng khách
"""
# Trace khách hàng CUSTOMER(class customer) có tên, có mã khách hàng + GIỎ HÀNG(class Cart)
# Họ đi chọn đồ và ....(các option liên quan đến những món đồ, class Product, class Store)
# mua đồ chán chê rồi, họ tiến hành đi thanh toán ORDER(class Order) 
# thanh toán (mã giảm giá, trừ sl trong kho, giỏ hàng trở về rỗng) và có thêm bill


#!LƯU Ý: Nên nhận thức được 1 điều là đây chỉ là những project đơn giản, sẽ còn nhiều lỗ hổng mà mình nhìn ra nhưng chỉ nên làm ở mức vừa phải thôi 


#Kho hàng
class Product:
    def __init__(self,name,ID,price,stock):
        if not isinstance(name,str) or not name.strip():
            raise ValueError("Tên sp không hợp lệ")
        if not isinstance(ID,str) or not ID.strip():
            raise ValueError("ID sp không hợp lệ")
        
        self.name=name
        self.ID=ID
        self.price=price
        self.stock=stock

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        if not isinstance(value,(float,int)) or value<0:
            raise ValueError("Giá sản phẩm phải lớn hơn bằng 0")
        self._price=value

    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self,amount):
        if not isinstance(amount,(float,int)) or amount<0:
            raise ValueError("Số lượng tồn kho phải lớn hơn = 0")
        self._stock=amount

#Của hàng để customer đến mua hàng
class Store:
    def __init__(self,name):
        if not isinstance(name,str) or not name.strip():
            raise ValueError("Tên store không hợp lệ")
        self.name=name
        self.store_products={} #Để ý trước giờ khi lưu vào kho ta toàn dùng list nhưng khi dữ liệu ngày càng lớn thì list truy cập chậm hơn dict rất nhiều
                               #Khi dùng list chúng ta chỉ cần lưu đối tượng vào là xong, dict cũng vậy
                               #* Dict: đối tượng có thể làm key, hoặc làm value đều được quan trọng là làm sao để tối ưu nhất khi hiển thị hoặc tra cứu sản phẩm
    
    def add_product(self,product):
        if not isinstance(product,Product):
            raise ValueError("Không tìm thấy sản phẩm")
        if not product.ID in self.store_products:
            #!Dùng đối tượng là value
            self.store_products[product.ID]=product
            print(f"Sản phẩm {product.ID}:{product.name} đã được thêm vào store {self.name}")
            return
        self.store_products[product.ID].stock+=product.stock
        print(f"Sản phẩm {product.ID}:{product.name} đã được cập nhật thêm số lượng tồn kho.")
        return

    
#Giỏ hàng để đựng đồ
class Cart:
    def __init__(self):
        self.product_cart={}

    def add_to_cart(self,store_obj, product, quantity):
        if not isinstance(product,Product):
            raise ValueError("Không tìm thấy sản phẩm")
        if not product.ID in store_obj.store_products:
            print("Không tìm thấy sản phẩm")
            return False
        
        if quantity<=0:
            raise ValueError("Số lượng phải lớn hơn 0")
        
        current_quantity=self.product_cart.get(product,0)
        total_requested=current_quantity+quantity

        if total_requested > product.stock:
            print(f"Kho không đủ số lượng! Trong kho có {product.stock}, giỏ hàng đã có {current_quantity}")
            return False

        #Lưu vào dict instance: quantity #!Dùng đối tượng làm key
        self.product_cart[product] = total_requested
        print(f"Đã thêm {quantity} {product.name} vào giỏ hàng.")

    
    #Nếu dựa vào ID để tìm đối tượng trong product_cart thì sẽ lâu vì key là 1 đối tượng
    def remove_from_cart(self,store_obj, product_ID, quantity=None):
        product=store_obj.store_products.get(product_ID) #product lúc này là 1 đối tượng
        if not product in self.product_cart:
            raise ValueError("Không tìm thấy sản phẩm trong giỏ hàng")
        
        if quantity is None:
            self.product_cart.pop(product)
            print(f"Đã xóa toàn bộ sản phẩm {product.name} khỏi giỏ hàng.")
            return

        if quantity<=0:
            raise ValueError("Số lượng phải lớn hơn 0")

        difference=self.product_cart[product]-quantity
        if difference<0 :
            raise ValueError("Số lượng không hợp lệ")
        if difference==0:
            self.product_cart.pop(product)
            print(f"Đã xóa sản phẩm {product.name} khỏi giỏ hàng.")
        else:
            self.product_cart[product]=difference
            print(f"Sản phẩm {product.name} số lượng giảm xuống còn {difference}")

    
    #Tính tiền
    def calculate_total(self):
        return sum(sp.price*quantity for sp,quantity in self.product_cart.items())
    
    #Trả về giỏ hàng rỗng nếu thanh toán thành công
    def clear_cart(self):
        return self.product_cart.clear()
    

class Order:
    def __init__(self,order_id,product_cart,total_money):
        self.id=order_id
        self.order_items=product_cart.copy()
        self.total_money=total_money
        self.status="Pending"
        self.is_discounted=False

    
    Coupon_code_set={"GIAM10","GIAM50K","GIAM20","GIAM18","GIAM40K"}
    
    #Đến cổng thanh toán
    def apply_discount(self,coupon_code):
        if coupon_code not in self.Coupon_code_set:
            print("Mã giảm giá không tồn tại")
            return
        if self.is_discounted:
            print("Đơn hàng đã áp mã giảm giá")
            return self.total_money
        if coupon_code.endswith("K"):
            so_tien_giam=int(coupon_code[4:-1])*1000
            if so_tien_giam>self.total_money:
                so_tien_giam=self.total_money
        else:
            so_tien_giam=self.total_money*int(coupon_code[4:])/100
        
        #Tiền cần thanh toán
        self.total_money-=so_tien_giam
        self.is_discounted=True #!Nhỡ khách muốn đổi mã giảm giá thì sao
        return self.total_money
    
                
    
class Customer:
    def __init__(self,customer_id,name):
        self.customer_id=customer_id
        self.name=name
        self.cart=Cart()
        self.order_history=[]
    
    def check_out(self,store_obj,order_id):
        if not self.cart.product_cart:
            print("Giỏ hàng chả có cái gì để thanh toán")
            return
        #Tổng tiền hàng cần thanh toán chưa áp mã giảm giá
        total_money=self.cart.calculate_total()

        #Tạo istance Order mới 
        order_new=Order(order_id,self.cart.product_cart,total_money)

        #!Khúc này thật ra chưa tối ưu vì nhỡ khách trả lại hàng gì đó thì sao 
        order_new.status = "Paid"

        if order_new.status == "Paid":
            for product, quantity in self.cart.product_cart.items():
                store_obj.store_products[product.ID].stock -= quantity

            self.cart.clear_cart()
            self.order_history.append(order_new)
        return order_new
    
    #Bill
    def print_latest_bill(self):
        # Kiểm tra xem khách đã từng mua cái đơn nào chưa
        if not self.order_history:
            print(f"Khách hàng {self.name} chưa có hóa đơn nào cả!")
            return

        # Bốc cái hóa đơn cuối cùng (mới nhất) trong lịch sử ra
        latest_bill = self.order_history[-1]

        print(f"Mã hóa đơn: #{latest_bill.order_id}")
        
        # Duyệt qua các món đồ trong cái hóa đơn đó để in
        for sp, qty in latest_bill.order_items.items():
            print(f"🔹 {sp.name:<15} x{qty:>2} = {sp.price * qty:,}đ")
            
        print(f"💰 Tổng tiền thanh toán : {latest_bill.total_money:,}đ")
        print(f"🏷️ Trạng thái đơn hàng  : {latest_bill.status}")
    













"""- Class Account (số tài khoản, PIN, số dư)
- Class ATM quản lý nhiều tài khoản
- Đăng nhập bằng PIN (sai 3 lần khóa tài khoản)
- Rút/nạp/chuyển tiền giữa tài khoản
- In sao kê giao dịch
"""
#!LƯU Ý: các lỗi gặp phải trong khi test chương trình, có thể nên đặt một tên riêng class ...(exception) để bài code trở nên tường minh nhất trong các dự án lớn, NÓI CHUNG LÀ SAU NÀY LÀM DỰ ÁN LỚN SẼ RÕ HƠN

class Account:
    def __init__(self,account_number,PIN,balance=0):
        self.account_number=account_number
        self.PIN=PIN
        self.balance=balance
        self.is_locked=False 
        self.attempts=0 #Đếm số lần nhập sai mã PIN
        self.history=[]
    
    @property
    def PIN(self):
        return self._PIN
    @PIN.setter
    def PIN(self,pin_code):
        if not pin_code.isdigit() or len(pin_code)!=4:
            raise ValueError("Mã PIN là số có 4 chữ số")
        self._PIN=pin_code

    #!sẽ đỡ điều kiện ở deposit,withdraw hay transfer nên dùng nhưng trong thực tế tốn 1 chút chi phí vận hành try except 
    #!ngoài ra thông báo văn ra có phần chung chung, nếu nhiều lỗi nhỏ thì sẽ khó sửa

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,value):
        if not isinstance(value,(float,int)) or value<0:
            raise ValueError("Số tiền không hợp lệ")
        self._balance=value
    
    
    def account_locked(self):
        if self.attempts>=3:
            self.is_locked=True
        
    def __str__(self):
        return f"ACCOUNT: {self.account_number}\nBALANCE: {self.balance}"


class ATM:
    def __init__(self):
        self.accounts={}
        self.current_account=None
    

    def add_account(self,account):
        if not isinstance(account,Account):
            raise ValueError("Tài khoảng không tồn tại.")  
        if not account.account_number in self.accounts:
            self.accounts[account.account_number]=account
            print("Đã cập nhật tài khoản lên hệ thống")
            return 
        print("Tài khoản đã có trên hệ thống")
    
    #Đăng nhập tài khoản
    def login(self,account_number,PIN):
        if self.current_account is not None:
            raise ValueError("Hiện đang có tài khoản đăng nhập")

        #Kiểm tra xem có tài khoản trên hệ thống không
        if account_number not in self.accounts:
            raise ValueError("Không tìm thấy tài khoản trên hệ thống")
        
        #Lấy tài khoản ra để kiểm tra xem có đang bị khoá không
        account=self.accounts.get(account_number)
        if account.is_locked:
            raise ValueError("Tài khoản của bạn đã bị khoá. Vui lòng thử lại")
        
        #So khớp mã PIN
        if account.PIN!=PIN:
            account.attempts+=1
            account.account_locked()
            raise ValueError("Mã PIN không hợp lệ.")
        self.current_account=account
        account.attempts=0

    
    #Nạp tiền
    def deposit(self,amount):
        if self.current_account is None:
            raise ValueError("Vui lòng đăng nhập tài khoản")
        
        try:
            self.current_account.balance+=amount
            self.current_account.history.append(f"+{amount:,}")
        except ValueError:
            print("Không biết lỗi gì để in ra số nhỏ hơn 0 hay kiểu dữ liệu không lợp lý")
            #!bạn có thể dùng class ...(exception) để tạo ra lỗi tiêng nhưng tôi không chắc nó đã tối ưu chưa

    #Rút tiền
    def withdraw(self,amount):
        if self.current_account is None:
            raise ValueError("Vui lòng đăng nhập tài khoản")
        if not isinstance(amount,(float,int)) or amount<=0:
            raise ValueError("Số tiền rút phải lớn hơn 0")
        if amount>self.current_account.balance:
            raise ValueError("Tài khoản không đủ số dư")
        
        self.current_account.balance-=amount
        self.current_account.history.append(f"-{amount:,}")

    #transfer
    def transfer(self,target_account_number,amount):
        if self.current_account is None:
            raise ValueError("Vui lòng đăng nhập tài khoản")
        if not target_account_number in self.accounts or target_account_number==self.current_account.account_number:
            raise ValueError("Không tìm thấy tài khoản giao dịch")
        if not isinstance(amount,(float,int)) or amount<=0:
            raise ValueError("Số tiền chuyển phải lớn hơn 0")
        if amount>self.current_account.balance:
            raise ValueError("Tài khoản không đủ số dư")
        receiving_account=self.accounts.get(target_account_number)

        #Giao dịch
        self.current_account.balance-=amount
        receiving_account.balance+=amount

        #Lưu giao dịch
        self.current_account.history.append(f"-{amount:,}")
        receiving_account.history.append(f"+{amount:,}")
    
    def print_statement(self):
        if self.current_account is None:
            raise ValueError("Vui lòng đăng nhập tài khoản")
        for trans in self.current_account.history:
            print(f"Tài khoản {self.current_account.account_number} đã thực hiện giao dịch: {trans}")

    def logout(self):
        self.current_account=None














"""Project 10: Hospital Management
- Class Person (abstract)
- Class Doctor, Patient, Nurse kế thừa
- Class Appointment (bác sĩ + bệnh nhân + thời gian)
- Kiểm tra lịch trùng nhau
- Class Hospital quản lý tất cả
- Tìm bác sĩ rảnh theo chuyên khoa
"""
from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    @abstractmethod
    def get_details(self):
        pass

class Doctor(Person):
    def __init__(self,name,age,gender,doctor_id,specialty):
        super().__init__(name,age,gender)
        self.doctor_id=doctor_id
        self.specialty=specialty #chuyên khoa

    def get_details(self):
        return f"Bác sĩ {self.name} là bác sĩ chuyên khoa {self.specialty}"


class Patient(Person):
    def __init__(self,name,age,gender,patient_id,disease):
        super().__init__(name,age,gender)
        self.patient_id=patient_id
        self.disease=disease  #bệnh lý
        self.time_slots=[]

    def get_details(self):
        return f"Bệnh nhân {self.name} đang mắc bệnh lý {self.disease}"
    
    





class Appointment:
    def __init__(self,appointment_id,doctor,patient,time_slot,status="Chờ khám"):
        self.appointment_id=appointment_id
        self.doctor=doctor
        self.patient=patient
        self.time_slot=time_slot
        self.status=status
        self.prescription=""
        self.note=""

    def cancal_appoint(self):
        if self.status == "Đã huỷ":
            print("Cuộc hẹn này đã được huỷ trước đó rồi!")
            return
        if self.time_slot in self.patient.time_slots:
            self.patient.time_slots.remove(self.time_slot)

        self.status = "Đã huỷ"
        print(f"Đã huỷ thành công cuộc hẹn {self.appointment_id}")
        
    def complete_examination(self,prescription,note):
        self.prescription=prescription
        self.note=note
        self.status="Đã khám"
        self.patient.time_slots.remove(self.time_slot)
        self.time_slot=None
        
    def __str__(self):
        information=f"Bác sĩ {self.doctor.name} - {self.doctor.doctor_id} đã khám cho Bệnh nhân {self.patient.name} - {self.patient.patient_id}"
        return f"{self.appointment_id}: {information}\nĐơn thuốc: {self.prescription}\nNote: {self.note}"
    




class Hospital:
    def __init__(self):
        self.doctors={}
        self.patients={}
        self.appointments={}
        self.doctor_id_list={} #Tạo ra để kiểm tra doctor_id cho nhanh
    

    def add_doctor(self,doctor):
        if not isinstance(doctor,Doctor):
            raise ValueError("Không tìm thấy thông tin bác sĩ")
        
        #setdefault luôn không cần check 
        self.doctors.setdefault(doctor.specialty,{}) #! self.doctors = {specialty:{ID:instance}}
        
        #lưu ý: cái này trong khuân khổ mỗi bác sĩ chỉ có 1 chuyên khoa và không được đổi chuyên khoa
        if doctor.doctor_id in self.doctors[doctor.specialty]:
            print("Bác sĩ đã có tên trong danh sách")
            return
        self.doctors[doctor.specialty][doctor.doctor_id]=doctor
        self.doctor_id_list[doctor.doctor_id]=doctor.specialty
        print("Đã thêm bác sĩ thành công")
        

    
    def add_patient(self,patient):
        if not isinstance(patient,Patient):
            raise ValueError("Không tìm thấy thông tin bệnh nhân")
        if patient.patient_id not in self.patients:
            self.patients[patient.patient_id]=patient
            print("Đã thêm bệnh nhân thành công")
            return
        print("Bệnh nhân đã có tên trong danh sách")

    # self.appointment = {"ID":[1,2,3],....}
    def find_available_doctors(self,specialty,time_slot):
        if specialty not in self.doctors:
            raise ValueError("Không tìm thấy chuyên khoa này")
        if time_slot not in [1,2,3,4]:
            raise ValueError("Không có ca làm việc này")
        
        available_slots=[]
        suggestions=[]
        
        #!Chỉ lặp qua một lần duy nhất
        for doctor in self.doctors[specialty].values():
            busy_slots = [appoint.time_slot for appoint in self.appointments.get(doctor.doctor_id,[]) if appoint.status!="Đã huỷ"]
            free_slots = [s for s in [1, 2, 3, 4] if s not in busy_slots]
            if time_slot in free_slots:
                available_slots.append(doctor)
            elif free_slots:
                suggestions.append((doctor,free_slots))
        if available_slots:
            for d in available_slots:
                print(f"Bác sĩ {d.name} - ID: {d.doctor_id} ca {time_slot} còn trống")
            return
        if suggestions:
            print(f"Không có bác sĩ rảnh ca {time_slot}, gợi ý:")
            for d, slots in suggestions:
                print(f"Bác sĩ {d.name} - ID: {d.doctor_id} - Ca trống: {slots}")
        else:
            print(f"Không có bác sĩ chuyên khoa {specialty} nào có lịch trống")


    
    #Tạo cuộc hẹn
    def create_appointment(self,appointment_id,doctor_id,patient_id,time_slot):
        if patient_id not in self.patients:
            raise ValueError("Không thấy bệnh nhân trong danh sách")
        
        #Kiểm tra bác sĩ dùng vòng lặp 
        if not any(doctor_id in sub_dict for sub_dict in self.doctors.values()):
            raise ValueError("Không tìm thấy vị bác sĩ này")
        
        #!Hoặc kiểm tra qua self.doctor_id_list
        if doctor_id not in self.doctor_id_list:
            raise ValueError("Không tìm thấy vị bác sĩ này")
        
        specialty=self.doctor_id_list[doctor_id]
        doctor=self.doctors[specialty][doctor_id]
        patient=self.patients[patient_id]

        if time_slot in patient.time_slots:
            raise ValueError("Bệnh nhân đã có lịch khám khung giờ này")

        #!Chúng ta lưu vào đối tượng của Appointment sẽ tối ưu hơn
        busy_slots=[appoint.time_slot for appoint in self.appointments.get(doctor.doctor_id,[])]
        if time_slot in busy_slots:
            raise ValueError("Bác sĩ đã có lịch hẹn khung giờ này")
        
        patient.time_slots.append(time_slot)
        appointment_created=Appointment(appointment_id,doctor,patient,time_slot)
        
        #dùng setdefault vì nếu không có thì tạo {"doctor_id":[]}
        #dùng get chỉ trả về giá trị chứ không thêm vào dict gốc
        self.appointments.setdefault(doctor_id,[]).append(appointment_created)

        return appointment_created
        
        

        


        

                      
    

        

        

        


        


        
    





















        


    



        

            
        
        

        
        


    



        











    
    

    
    

