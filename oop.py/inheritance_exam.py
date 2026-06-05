
"""Cấu trúc hệ thống:
Tạo một Class Cha tên là Staff. Hàm __init__(self, name, salary) nhận vào Tên và Mức lương cơ bản. Viết một hàm tên là show_info(self) trả về chuỗi: "Nhân viên: [name] | Lương: [salary]".
Tạo một Class Con tên là Manager kế thừa từ Class Staff.
Trong Class Manager, viết thêm một hàm của riêng nó tên là schedule_meeting(self) trả về chuỗi: "[name] đang lên lịch họp đội ngũ."."""

class Staff:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_info(self):
        return f"Nhân viên: {self.name} | Lương: {self.salary}"
class Manager(Staff):
    def schedule_meeting(self):
        return f"{self.name} đang lên lịch họp cho đội ngũ"








"""1. Cấu trúc hệ thống:
Tạo một Class Cha tên là Vehicle. Hàm __init__(self, brand) nhận vào Thương hiệu xe (Ví dụ: "VinFast", "Tesla").
Tạo một Class Con tên là ElectricCar kế thừa từ Vehicle.
Hàm __init__ của ElectricCar sẽ nhận vào 2 tham số: brand và battery_capacity (Dung lượng pin, ví dụ: 75 kWh).
Yêu cầu: Bạn bắt buộc phải dùng hàm super() để đẩy brand lên cho Class Cha xử lý, và tự gán battery_capacity vào self ở Class Con.
Trong Class ElectricCar, viết một hàm tên là drive(self) trả về chuỗi: "[brand] đang chạy bằng viên pin [battery_capacity] kWh."""
class Vehicle:
    def __init__(self,brand):
        self.brand=brand
class ElectricCar(Vehicle):
    def __init__(self,brand,battery_capacity):
        super().__init__(brand)
        self.battery_capacity=battery_capacity
    def drive(self):
        return f"{self.brand} đang chạy bằng viên pin {self.battery_capacity}"
    







"""Cấu trúc hệ thống:
Tạo một Class Cha tên là Notification. Hàm __init__(self, sender) nhận vào tên người gửi. Viết một hàm tên là send(self) trả về chuỗi: "[sender] đang gửi một thông báo chung.".
Tạo một Class Con tên là SMSNotification kế thừa từ Notification.
Hàm __init__ của nó nhận vào 2 tham số: sender và phone_number. Hãy dùng super() để xử lý sender.
Yêu cầu: Hãy Ghi đè (Override) hàm send(self) trong Class SMSNotification sao cho nó trả về chuỗi: "📲 SMS gửi từ [sender] đến số [phone_number]: Hệ thống đã kích hoạt!"""
class Notification:
    def __init__(self,sender):
        self.sender=sender
    def send(self):
        return f"{self.sender} đang gửi một thông báo chung"
class SMSNotification(Notification):
    def __init__(self,sender,phone_number):
        super().__init__(sender)
        self.phone_number=phone_number
    def send(self):
        return f"SMS gửi từ {self.sender} đến {self.phone_number}. Hệ thống kích hoạt"
    







"""Cấu trúc hệ thống:
Tạo một Class Cha tên là Robot. Hàm __init__(self, name) nhận vào tên Robot.
Class Cha Robot có một @classmethod tên là create_robot(cls, name). Hàm này trả về đối tượng bằng lệnh: return cls(name). (Lưu ý: Dùng cls chứ không dùng chữ Robot).
Tạo hai Class Con kế thừa từ Robot là:
Class CombatRobot (Robot chiến đấu). Bên trong chỉ cần ghi pass.
Class WorkerRobot (Robot lao động). Bên trong chỉ cần ghi pass"""
class Robot:
    def __init__(self,name):
        self.name=name
    @classmethod
    def create_robot(cls,name):
        return cls(name)
class CombatRobot(Robot):
    pass
class WorkerRobot(Robot):
    pass
rb1 = CombatRobot.create_robot("Gundam")
rb2 = WorkerRobot.create_robot("Wall-E")







#*Kế thừa đa tầng
class Vehicle:
    def __init__(self,brand):
        self.brand=brand

class ElectricVehicle(Vehicle):
    def __init__(self,brand,battery_capacity):
        super().__init__(brand)
        self.battery_capacity=battery_capacity

class AutonomousSystem:
    def __init__(self,software_version):
        self.software_version=software_version

class HybriautoCar(ElectricVehicle,AutonomousSystem):
    def __init__(self,brand,battery_capacity,software_version,fuel_capacity):
        super().__init__(brand,battery_capacity)
        AutonomousSystem.__init__(self,software_version)#!Bắt buộc phải có self để biết là đang gán cho đối tượng nào
        self.fuel_capacity=fuel_capacity

    def show_spec(self):
        return f"Thương hiệu: {self.brand}\nDung lượng pin: {self.battery_capacity}\nPhiên bản phần mềm: {self.software_version}\nDung tích bình xăng :{self.fuel_capacity}"
super_car = HybriautoCar(brand="Tesla CyberHybrid", 
                         battery_capacity=100, 
                         software_version="FSD v12.5",
                         fuel_capacity=45)
print(super_car.show_spec())




#*
class Warrior:
    def __init__(self,hp):
        self.hp=hp
        self.damage=50
class Mage:
    def __init__(self,mp):
        self.mp=mp
        self.damage=120
class BattleMage(Warrior,Mage):
    def __init__(self,hp,mp):
        super().__init__(hp)
        Warrior_dmg=self.damage #=50
        Mage.__init__(self,mp)
        Mage_dmg=self.damage #=120
        self.damage=Warrior_dmg+Mage_dmg



"""Yêu cầu cấu trúc hệ thống:
Class Cha UserAccount:
Hàm __init__(self, username, max_storage, support_level) nhận vào 3 tham số: Tên tài khoản, Dung lượng lưu trữ tối đa (GB), và Cấp độ hỗ trợ.
Có một @classmethod tên là create_default(cls, username). Hàm này sẽ khởi tạo và trả về một đối tượng bằng cách nạp username cùng với các cấu hình mặc định lấy từ Biến Class thông qua tham số cls.
Biến Class mặc định của UserAccount:
_MAX_STORAGE = 15
_SUPPORT_LEVEL = "Standard"
Hai Class Con kế thừa từ UserAccount:
Class PremiumUser: Định nghĩa lại các biến Class của riêng nó: _MAX_STORAGE = 100, _SUPPORT_LEVEL = "Gold". (Bên trong không viết thêm hàm nào khác).
Class EnterpriseUser: Định nghĩa lại các biến Class của riêng nó: _MAX_STORAGE = 1000, _SUPPORT_LEVEL = "Platinum". (Bên trong không viết thêm hàm nào khác)."""
class UserAccount:
    _MAX_STORAGE=15
    _SUPPORT_LEVEL="Standard"
    def __init__(self,username,max_storage,support_level):
        self.username=username
        self.max_storage = max_storage
        self.support_level = support_level
    @classmethod
    def create_default(cls,name):
        return cls(name,cls._MAX_STORAGE,cls._SUPPORT_LEVEL)
    
class PremiumUser(UserAccount):
    _MAX_STORAGE = 100
    _SUPPORT_LEVEL = "Gold"

class EnterpriseUser(UserAccount):
    _MAX_STORAGE = 1000
    _SUPPORT_LEVEL = "Platinum"









"""Hệ thống Đăng ký và Phân cấp Thành viên (MembershipSystem)
Yêu cầu hệ thống:
Tạo Class Cha Member. Hàm __init__(self, name) nhận vào tên thành viên.
Class Member có một biến Class dạng danh sách là _all_members = [] để lưu tên của tất cả các thành viên đã được tạo ra trong toàn hệ thống.
Viết một @classmethod tên là register(cls, name) nằm ở Class Cha Member. Hàm này làm nhiệm vụ:
Kiểm tra nếu name đã tồn tại trong _all_members thì in ra thông báo lỗi và trả về None.
Nếu chưa tồn tại, nạp name vào danh sách _all_members, sau đó khởi tạo và trả về đối tượng của Class đang gọi nó.
Tạo 2 Class Con kế thừa từ Member là SilverMember và GoldMember (Cả hai đều dùng pass)."""

class Member:
    _all_members=[]
    def __init__(self,name):
        self.name=name
    @classmethod
    def register(cls,name):
        if name in cls._all_members:
            print("Ten da ton tai")
            return None
        cls._all_members.append(name)
        return cls(name)
class SilverMember(Member):
    pass
class GoldMember(Member):
    pass
m1 = SilverMember.register("Alice") 
m2 = GoldMember.register("Bob")     
m3 = SilverMember.register("Alice") # ❌ Báo lỗi trùng tên hệ thống, trả về None

print(type(m1)) # <class '__main__.SilverMember'>
print(type(m2)) # <class '__main__.GoldMember'>
print(Member._all_members) # ['Alice', 'Bob']









"""Bài số 12: Bộ giải mã Giao thức Mạng đa tầng (NetworkProtocol)
Cấu trúc phả hệ: Device (Ông nội) → Router (Cha) → SmartRouter (Con).
Thuộc tính khởi tạo:
Device: ip (str), model (str).
Router: Có thêm max_connections (int).
SmartRouter: Có thêm firmware_version (str).
Yêu cầu: Viết một @classmethod tên là from_packet(cls, packet_str) tại Class Device
Nhận vào chuỗi thô dạng: "IP|Model|MaxConn|Firmware". Tự bóc tách, ép kiểu và trả về đúng đối tượng của Class gọi nó."""
class Device:
    def __init__(self,ip,model):
        self.ip=ip
        self.model=model
    @classmethod
    def from_packet(cls, packet_str):
        data = packet_str.split("|")
        ip, model = data[0], data[1]
        max_connections = int(data[2]) 
        firmware_version = data[3]
        return cls(ip, model, max_connections, firmware_version)
class Router(Device):
    def __init__(self,ip,model,max_connections):
        super().__init__(ip,model)
        self.max_connections=max_connections
class SmartRouter(Router):
    def __init__(self,ip,model,max_connections,firmware_version):
        super().__init__(ip,model,max_connections)
        self.firmware_version=firmware_version

packet = "192.168.1.1|Asus-RT|128|v5.2.1"
my_router = SmartRouter.from_packet(packet)

print(type(my_router))      # Kỳ vọng: <class '__main__.SmartRouter'>
print(my_router.ip)          # Kỳ vọng: 192.168.1.1 (str)
print(my_router.max_connections) # Kỳ vọng: 128 (int)
print(my_router.firmware_version) # Kỳ vọng: v5.2.1 (str)









"""Bài số 13: Xung đột Giá và Thuế (ECommerceSystem)
Class Cha 1 (TaxableProduct): Biến Class _TAX_RATE = 0.1. Hàm __init__(self, price). Hàm get_final_price(self) trả về price×(1+_TAX_RATE)
Class Cha 2 (LuxuryProduct): Biến Class _LUXURY_RATE = 0.2. Hàm __init__(self, luxury_fee). Hàm get_final_price(self) trả về luxury_fee×(1+_LUXURY_RATE) 
Class Con (PremiumItem): Đa kế thừa từ 2 Cha trên.
Hàm __init__(self, price, luxury_fee) nạp đủ thuộc tính cho các Cha.
Ghi đè hàm get_final_price(self) để trả về tổng giá trị sau thuế/phí của cả 2 Cha cộng lại."""
class TaxableProduct:
    _TAX_RATE=0.1
    def __init__(self,price):
        self.price=price
    def get_final_price(self):
        return self.price*(1+TaxableProduct._TAX_RATE)
    
class LuxuryProduct:
    _LUXURY_RATE=0.2
    def __init__(self,luxury_fee):
        self.luxury_fee=luxury_fee
    def get_final_price(self):
        return self.luxury_fee*(1+LuxuryProduct._LUXURY_RATE)

class PremiumItem(TaxableProduct,LuxuryProduct):
    def __init__(self,price,luxury_fee):
        super().__init__(price)
        LuxuryProduct.__init__(self,luxury_fee)
    def get_final_price(self):
        tax=TaxableProduct.get_final_price(self)
        luxury=LuxuryProduct.get_final_price(self)
        return tax+luxury
    
item = PremiumItem(price=100, luxury_fee=200)
# Giá trị TaxableProduct nhận: 100 * 1.1 = 110
# Giá trị LuxuryProduct nhận: 200 * 1.2 = 240
print(item.get_final_price()) # Kỳ vọng: 350 (110 + 240)









"""Bài số 14: Cấp phép Tài nguyên Bảo mật (SecurityAccess)
Class Cha (SecuritySystem): Biến Class _SECURE_KEY = "SECRET_123". Hàm __init__(self) tự gán self.is_authenticated = True.
Class Con (AdminSecurity): Định nghĩa lại biến Class _SECURE_KEY = "ADMIN_456".
Yêu cầu: Viết một @classmethod tên là request_access(cls, user_key) tại Class Cha. Nếu user_key khớp với _SECURE_KEY của Class đang gọi thì khởi tạo và trả về đối tượng cls(). Nếu sai, in thông báo từ chối và trả về None."""
class SecuritySystem:
    _SECURE_KEY = "SECRET_123"
    def __init__(self):
        self.is_authenticated = True
    @classmethod
    def request_access(cls,user_key):
        if user_key==cls._SECURE_KEY:
            return cls()
        print("Tu choi")
        return None
class AdminSecurity(SecuritySystem):
    _SECURE_KEY = "ADMIN_456"
# Thử bẻ khóa Admin bằng mã của User thường
attempt1 = AdminSecurity.request_access("SECRET_123") # Kỳ vọng: Từ chối, trả về None

# Đăng nhập đúng mã của Admin
attempt2 = AdminSecurity.request_access("ADMIN_456") 
print(type(attempt2))             # Kỳ vọng: <class '__main__.AdminSecurity'>
print(attempt2.is_authenticated) # Kỳ vọng: True
    








