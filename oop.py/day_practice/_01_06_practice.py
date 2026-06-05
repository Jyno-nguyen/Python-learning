
"""Bài 1: Bộ lọc bài viết diễn đàn (ForumPost)
Đầu vào: title (tiêu đề) và content (nội dung bài viết).
Setter: Chặn không cho title vượt quá 50 ký tự. Chặn content nếu chứa các từ nhạy cảm cấm như ["hack", "cheat", "scam"]. Nếu dính từ cấm, ném lỗi ValueError.
Getter: content khi xuất ra sẽ tự động thay thế các từ nhạy cảm (nếu lỡ lọt lưới) thành dấu ***.
Deleter: Khi gọi del post.content, hệ thống không xóa biến mà reset nội dung thành chuỗi rỗng ""."""
class ForumPost:
    def __init__(self,title,content):
        self.title=title
        self.content=content
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,inputs):
        if not inputs or len(inputs)>50:
            raise ValueError("loi")
        self._title=inputs
    
    @property
    def content(self): #!tuyệt đối không được gán self._content = vì đây là getter chỉ đọc
        chuoi_goc=self._content
        chuoi_ha_bac=chuoi_goc.lower() #! Lỗi ngay vì chuỗi hạ bậc không thay đổi nên find(word) luôn ở 1 vị trí
        for word in ["hack", "cheat", "scam"]:
            while True:
                chuoi_ha_bac=chuoi_goc.lower() #!Chuỗi hạ bậc này phải nằm bên trong vòng lặp nếu nằm hẳn bên ngoài thì chuỗi gốc có thay đổi nhưng chuỗi hạ bậc vẫn dữ nguyên
                vi_tri=chuoi_ha_bac.find(word)
                if vi_tri==-1: #khi find không tìm thấy nữa trả về -1
                    break
                chuoi_goc = (chuoi_goc[:vi_tri] + "*" * len(word) + chuoi_goc[vi_tri + len(word):])
                #cách này triệt để vì từ dính liền nhau cũng có thể thay thế
        
        #*HOẶC: replace cách hiệu quả hơn và không có vòng lặp lồng nháu.
        chuoi_goc = self._content

        for word in ["hack", "cheat", "scam"]:
            chuoi_ha_bac = chuoi_goc.lower()
            
            # Nếu từ cấm xuất hiện trong chuỗi hạ bậc
            if word in chuoi_ha_bac:
                vi_tri = chuoi_ha_bac.find(word)
                
                # Trích xuất chính xác từ lóng gốc (Ví dụ: "ChEaT", "cHeAt")
                tu_long_goc = chuoi_goc[vi_tri : vi_tri + len(word)]
                
                # Dùng .replace() đập thẳng vào từ lóng gốc đó trên TOÀN BỘ văn bản
                chuoi_goc = chuoi_goc.replace(tu_long_goc, "*" * len(word))
    @content.setter
    def content(self,inputs):
        if not inputs :
            raise ValueError("loi")
        self._content=inputs
    @content.deleter
    def content(self):
        self._content=""










"""Bài 3: Ví tín dụng thông minh (CreditCard)
Đầu vào: limit (Hạn mức thẻ, ví dụ 50 triệu) và spent (Số tiền đã tiêu, ban đầu = 0).
Setter: Gác cổng spent, không cho phép số tiền đã tiêu vượt quá limit. Nếu người dùng cố tình quẹt thẻ quá hạn mức, ném lỗi ValueError("Thẻ từ chối giao dịch: Vượt hạn mức!").
Getter đứng một mình: Thuộc tính available_balance (Số dư còn lại có thể tiêu) = limit - spent. Thuộc tính này phải tự cập nhật động mỗi khi spent thay đổi.
Deleter: Khi gọi del card.spent, hãy reset số tiền đã tiêu về 0 (Coi như kỳ thanh toán mới bắt đầu).
"""
class CreditCard:
    def __init__(self,spent):
        self._limit=50000000
        self._spent = 0
        self.spent=spent


    @property
    def spent(self):
        return self._spent
    @spent.setter
    def spent(self,chi_tieu):
        if chi_tieu+self._spent>self._limit or chi_tieu<0:
            raise ValueError("loi")
        self._spent+=chi_tieu #Cộng vào chi tiêu chứ không ghi đè
    @spent.deleter
    def spent(self):
        self._spent=0
    @property
    def available_balance(self):
        return self._limit - self._spent
a=CreditCard(100)
a.spent+=200
print(a.spent)
print(a.available_balance)









"""Bài 4: Quản lý Kho hàng Shopee (ProductInventory)
Đầu vào: product_name, price (giá bán), stock (số lượng tồn kho).
Setter: price và stock phải là số và lớn hơn hoặc bằng 0.
Getter một mình: Thuộc tính inventory_value (Tổng giá trị kho hàng của món này) = price * stock.
Deleter: Khi gọi del product.stock, hãy đưa số lượng tồn kho về 0 và in ra log: "Sản phẩm đã bị gỡ hoặc hết hàng"."""
class shopee:
    def __init__(self,product_name,price,stock):
        self.product_name=product_name
        self.price=price
        self.stock=stock
    @staticmethod
    def _ktra(num):
        if num<0:
            raise ValueError("loi")
        return num
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,num):
        self._price=shopee._ktra(num)

    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self,num):
        self._stock=shopee._ktra(num)
    @stock.deleter
    def stock(self):
        self._stock=0
        print("Sản phẩm đã bị gỡ hoặc hết hàng")
    @property
    def inventory_value(self):
        return self._price*self._stock









"""Bài 6: Đường tròn và các thuộc tính ảo (Circle)
Đầu vào: radius (Bán kính). Setter phải chặn nếu bán kính ≤0.
Getter/Setter lồng nhau: Tạo thuộc tính diameter (Đường kính).
Getter: Tự động tính toán trả về radius * 2.
Setter đặc biệt: Nếu người dùng gán đường kính mới (Ví dụ: c.diameter = 20), Setter này phải tự động lấy số đó chia đôi và cập nhật ngược lại vào kho ẩn của bán kính (self._radius = 10).
Getter một mình: Thuộc tính area (Diện tích) = 3.14×radius2."""

class circle:
    def __init__(self,radius):
        self.radius=radius

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,bk):
        if not isinstance(bk,(float,int)) or bk<0:
            raise ValueError("Loi")
        self._radius=bk

    @property
    def diameter(self):
        return self._radius*2
    @diameter.setter
    def diameter(self,dk):
        if not isinstance(dk,(float,int)) or dk<0:
            raise ValueError("Loi")
        self.radius=dk/2









"""Bài 8: Đồng hồ thông minh 12h (SmartClock)
Đầu vào: hour (giờ) và minute (phút).
Setter tự động nắn dữ liệu: * minute: Nếu người dùng nhập phút > 59 (Ví dụ: 75 phút), Setter tự động lấy phần dư 75 % 60 = 15 phút, và cộng phần nguyên 75 // 60 = 1 tiếng vào cho biến giờ hour.
hour: Nếu giờ vượt quá 12, tự động dùng phép chia lấy dư với 12 để đưa về định dạng đồng hồ 12 giờ"""

"""Ý TƯỞNG THIẾT KẾ & LUẬT VẬN HÀNH ĐỒNG HỒ (SMART CLOCK 12H):
    
    1. Cơ chế Khởi tạo (__init__):
       - 'hour' chạy trước để tạo bệ phóng giờ gốc.
       - 'minute' chạy sau, tự động tính toán và dùng toán tử `+=` để cộng dồn 
         lượng giờ dư thừa (value // 60) vào thẳng 'hour'.

    2. Tính Độc lập & Lưu vết Trạng thái (State Mutation):
       - Khi sửa GIỜ (.hour = val): Chỉ thay đổi nguyên giờ hiện tại, 
         giữ nguyên số phút cũ trong kho để đảm bảo tính độc lập.
       - Khi sửa PHÚT (.minute = val): Giữ nguyên mốc giờ ĐÃ SỬA trước đó. 
         Nếu số phút mới vượt quá 60, lượng giờ thừa sẽ được CHỐT và CỘNG DỒN 
         TIẾP vào mốc giờ hiện tại (qua `+=`). Khi hạ số phút xuống thấp, 
         giờ mới đã chốt sẽ GIỮ NGUYÊN chứ không tự động quay về mốc cũ.

    3. Định dạng đầu ra (Getter):
       - Kho ẩn (_hour, _minute) lưu dữ liệu hệ 24h để tính chính xác AM/PM.
       - Getter của 'hour' đóng vai trò bộ lọc hiển thị (12h): Tự động nắn 
         kết quả phép chia dư sao cho mốc 0h/12h luôn hiển thị là '12' thay vì '00'.
    """
class SmartClock:
    def __init__(self,hour,minute):
        self.hour=hour
        self.minute=minute
        self.session=None
    
    @property
    def hour(self):
        self.session="AM" if 0<=self._hour%24<12 else "PM"
        return 12 if self._hour%12==0 else self._hour%12
    @hour.setter
    def hour(self,value):
        if not isinstance(value,int) or 0>value:
            raise ValueError("incorrect minute")
        self._hour=value

    @property
    def minute(self):
        return self._minute
    @minute.setter
    def minute(self,value):
        if not isinstance(value,int) or 0>value:
            raise ValueError("incorrect hours")
        self._hour+=value//60
        self._minute=value%60

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}{self.session}"
    








"""Bài 9: Bình xăng Ô tô thông minh (FuelTank)
Đầu vào: capacity (Dung tích tối đa của bình, ví dụ: 50 lít) và current_fuel (Lượng xăng hiện tại).
Setter bo tròn: current_fuel không được phép nhỏ hơn 0. Nếu người dùng đổ xăng vượt quá capacity (Ví dụ: bình 50 lít nhưng đòi đổ 60 lít)
Setter không ném lỗi mà tự động bo tròn lượng xăng về tối đa là 50 lít và in ra cảnh báo: "Xăng đã đầy, tràn 10 lít!"."""

class FuelTank:
    def __init__(self,capacity,current_fuel):
        if not isinstance(capacity,(int,float)) or 0>capacity:
            raise ValueError("Dung tich toi da phai la so > 0")
        self.capacity=capacity
        self.current_fuel=current_fuel
    @property
    def capacity(self):
        return self._capacity
    @property
    def current_fuel(self):
        return self._current_fuel
    @current_fuel.setter
    def current_fuel(self,value):
        if not isinstance(value,(int,float)) or 0>value:
            raise ValueError("Dung tich nap phai la so > 0")
        if value>self._capacity:
            print(f"Xang da day va tran {value-self._capacity}")
            self._current_fuel=self._capacity
        else:
            self._current_fuel=value
    
    def refuel(self,amount):
        if not isinstance(amount,(int,float)) or 0>amount:
            raise ValueError("Dung tich do la so > 0")
        self.current_fuel+=amount









"""Bài 10: Vé máy bay linh hoạt (FlightTicket)
Đầu vào: passenger_name và ticket_class (Hạng vé, nhận chuỗi: "ECONOMY" hoặc "BUSINESS").
Setter nâng cao: Hạng vé phải đúng 2 chuỗi trên.
Logic nâng cao: Nếu hạng vé đang là "BUSINESS" (Thương gia), khách hàng không được phép hạ cấpxuống "ECONOMY".
Nếu cố tình làm vậy, ném lỗi PermissionError("Vé thương gia không được phép hạ cấp!"). Khách hàng chỉ có thể giữ nguyên hoặc nâng cấp từ dưới lên trên thôi"""

class FlightTicket:
    def __init__(self, passenger_name, ticket_class):
        if not passenger_name.strip():
            raise ValueError("Khong duoc de trong")
        self.passenger_name = passenger_name
        self._ticket_class = None 
        self.ticket_class = ticket_class.upper()

    @property
    def ticket_class(self):
        return self._ticket_class

    @ticket_class.setter
    def ticket_class(self, new_class):
        new_class = new_class.upper()
        
        # 2. Kiểm tra tính hợp lệ của hạng vé mới
        if new_class not in ["ECONOMY", "BUSINESS"]:
            raise ValueError("Hạng vé không hợp lệ! Chỉ chấp nhận 'ECONOMY' hoặc 'BUSINESS'.")
        
        if self._ticket_class == "BUSINESS" and new_class == "ECONOMY":
            raise PermissionError("Vé thương gia không được phép hạ cấp!")
            
        self._ticket_class = new_class

    def __str__(self):
        return f"Hành khách: {self.passenger_name} | Hạng vé: {self.ticket_class}"

    

        

    

    
    