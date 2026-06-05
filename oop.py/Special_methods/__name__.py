
#? __name__ là 1 biến ẩn(special variable) - Python sẽ tự gán cho mỗi file.py khi file đó hoạt động
#? Giá trị của biến __name__ không cố định. Nó thay đổi tùy thuộc vào việc file đó tự chạy hay bị file khác gọi ké.

# __main__ là chuỗi đặc biệt do Python quy ước sẵn
# có nghĩa là luồng chính. file nào TRỰC TIẾP BẤM RUN thì __main__ sẽ đóng mác vào biến __name__

# File: toan_hoc.py
def tinh_tong(a, b):
    return a + b
# Phép so sánh bằng ở cuối file
if __name__ == "__main__": #!chạy trực tiếp 
    print("Test thử hàm: ", tinh_tong(5, 5))

# File: thuvien_game.py
# In thử xem giá trị __name__ của file này hiện tại là gì
print(f"[Bên trong thuvien_game.py] Biến __name__ đang có giá trị là: '{__name__}'")
if __name__ == "__main__": #!nếu chạy trong file khác được import thì __name__ sẽ khác __main__ nên dòng này sẽ không chạy
    print("Lệnh này CHỈ CHẠY khi bạn bấm nút RUN trực tiếp tại file thuvien_game.py!")

# File: __name__.py
import thuvien_game  
print(f"[Bên trong main.py] Biến __name__ đang có giá trị là: '{__name__}'")

#!Khi bấm run ở file __name__.py, VÌ IMPORT FILE CON NÊN NHỮNG GÌ CHẠY ĐƯỢC TRONG FILE CON SẼ CHẠY HẾT 
#-> [Bên trong thuvien_game.py] Biến __name__ đang có giá trị là: 'thuvien_game'
#-> [Bên trong main.py] Biến __name__ đang có giá trị là: '__main__'

#* Chức năng chính, tối cao và duy nhất của "công tắc" if __name__ == "__main__": là:
#* CHẶN không cho những đoạn code chạy thử (hoặc code vãng lai) tự động kích hoạt ngoài ý muốn khi file đó bị một file khác import vào.






#? import file.py






#* .__name__ : dunder attribute 

class Shape:
    pass
    
class Circle(Shape):
    pass

class Rectangle(Shape):
    pass

class Triangle(Shape):
    pass
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

#* Ví dụ KHI DÙNG VỚI HÀM.__name__
def nap_tien():
    pass

def rut_tien():
    pass

def nhat_ky_he_thong(ham_muc_tieu):
    # ham_muc_tieu là một cái hàm được truyền vào như một tham số
    ten_ham = ham_muc_tieu.__name__ # Ta dùng .__name__ để bóc ra cái tên dạng chữ của hàm đó
    print(f"🚨 CẢNH BÁO: Người dùng vừa kích hoạt tính năng -> [{ten_ham}]")
    
if __name__ == "__main__":
    nhat_ky_he_thong(nap_tien) #🚨 CẢNH BÁO: Người dùng vừa kích hoạt tính năng -> [nap_tien]
    nhat_ky_he_thong(rut_tien) #🚨 CẢNH BÁO: Người dùng vừa kích hoạt tính năng -> [rut_tien]
 
