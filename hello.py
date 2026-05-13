print("hello, I'm Jyno")
a=input() #luôn trả về kiểu chuỗi
#notes
'''notes'''
""" notes"""

""" type(<ten bien>) kiểm tra kiểu dữ liệu biến """

"""số thực chỉ lấy được 15 số sau dấu phảy, nếu muốn lấy thêm thì phải dùng thư viện decimal"""


    #PHÂN SỐ
from fractions import*
e=Fraction(6,9)
print(e)


    #SỐ PHỨC
c=complex(2,5)
print(c)
print(c.real) #in phần thực
print(c.imag) #in phần ảo


    #TOÁN TỬ
""" Toán tử số học
x + y   # cộng
x - y   # trừ
x * y   # nhân
x / y   # chia (kết quả float) LUÔN TRẢ VỀ SỐ THỰC FLOAT
x // y  # chia lấy phần nguyên
x % y   # chia lấy phần dư
x ** y  # lũy thừa (x mũ y) LẤY TỪ TRÁI SANG PHẢI NẾU NHIỀU LUỸ THỪA
                            1e3=1*10**3
# Thứ tự: ** → * / % // → + -

    Toán tử so sánh ( kết quả true false ) MỌI GIÁ TRỊ SỐ BẰNG 0 ĐỀU TRẢ VỀ FALSE(CẦN LÀM THÊM BÀI TẬP)
x == y  # bằng
x != y  # khác
x > y   # lớn hơn 
x < y   # nhỏ hơn
x >= y  # lớn hơn hoặc bằng
x <= y  # nhỏ hơn hoặc bằng
x is y  #!Kiểm tra xem hai biến xem có cùng trỏ đến 1 đối tượng hay không
        #!Đừng bao giờ sử dụng toán tử is đối với 2 biến thuộc kiểu số hoặc 2 biến thuộc kiểu chuỗi. 
        #!Việc so sánh như vậy không mang lại bất kì ý nghĩa nào cả. Nếu muốn so sánh, hãy sử dụng các toán tử khác.
        #?Các phép so sánh giữa một biến với giá trị None luôn được thực hiện bằng toán tử is.
        
PYTHON HỖ TRỢ SO SÁNH LIÊN TIẾP (10>5>2 TRẢ VỀ TRUE)
    Toán tử gán:
x = 5    # gán
x += 5   # x = x + 5
x -= 5   # x = x - 5
x *= 5   # x = x * 5
x /= 5   # x = x / 5
 không thể gán trong biểu thức (CẦN XEM LẠI)
    
    Toán tử logic:(CẦN XEM LẠI)
x and y  # cả 2 đều True
x or y   # 1 trong 2 True
not x    # đảo ngược True/False

"""

import math
# muốn sử dụng hàm nào trong math thì dùng math.<tên hàm>