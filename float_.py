  #MUỐN MỞ RÔNG THÊM PHẦN HIỆN CHỮ SỐ ĐẰNG SAU
  #thêm thư viện decimal
from decimal import* #từ thư viện decimal import (*) mọi thứ vào(THƯỜNG SẼ KHÔNG NÊN DÙNG VÌ DỄ BỊ TRÙNG TÊN BIẾN)
from decimal import Decimal
import decimal #nhưng chưa lấy Decimal ra nên khi nhập cần thêm vd d=decimal.Decimal(10)
  #lấy 30 số phần nguyên và phần thập phân
getcontext().prec=3 #hàm này chỉ cần thiết khi bạn cần lấy đúng bao nhiêu số phần nguyên và phần thập phân
d=Decimal(10)/3
print(d)
print(type(d))
""" hello, I'm Jyno
3.33
<class 'decimal.Decimal'>"""
  #thường nếu dùng cộng trưc tiếp sẽ có sai số nên có thể dùng Decimal 0.1+0.2=0.300000000000004
from decimal import Decimal
print(Decimal("0.1")+Decimal("0.2"))

#MUỐN THU HẸP THÊM CHỮ SỐ ĐẰNG SAU
x = 10 / 3
print(x)           # 3.3333333333333335
print(round(x, 2)) # 3.33 (làm tròn 2 chữ số)
print(round(x, 4)) # 3.3333
  #LƯU Ý:#Có sai số vd 3.455=3.4549999999 nên muốn làm tròn chính xác có thể dùng Decimal("số cần làm tròn")
         #khi làm tròn với round(1.5)=2 và round(2.5)=2 vì Python ưu tiên làm tròn đến số chẵn gần nhất .5
  #Hoặc dùng format: GIÁ TRỊ THẬT VẪN GIỮ NGUYÊN, chỉ thay đổi hiển thị
print(f"{x:.2f}")  # 3.33
print(f"{x:.4f}")  # 3.3333



import math
# muốn sử dụng hàm nào trong math thì dùng math.<tên hàm>

import math as m #!Thay vì viết math. đổi thành m.(VÀ KHÔNG ĐƯỢC VIẾT math.)
                 #! as: chỉ có tác dụng bên trong khối lệnh
abs(-3+4j)         #luôn trả về float
m.sqrt(16)      # căn bậc 2 → 4.0
m.pow(2, 10)    # lũy thừa → 1024.0
m.pow(2,3,4)   #(2**3)%4
m.fabs(-5)       # trị tuyệt đối → 5
m.ceil(3.2)     # làm tròn lên → 4
m.floor(4.9)    # làm tròn xuống -> 4
m.pi            # số pi → 3.14159...
m.e             # số e → 2.71828...
m.log(100, 10)  # log cơ số 10 → 2.0
m.log2(8)       # log cơ số 2 → 3.0
m.factorial(5)  # giai thừa → 120
#hàm logarit chỉ cơ số 2 và cơ số 10 được phép viết tắt kiểu log2(x), log10(x)
#hàm loge thì viết là log(x)
m.trunc(3.9) #trả về số nguyên là phần nguyên của số x 
m.gcd(6.4) #trả về số nguyên là ước chung lớn nhất của 2 số x và y
              #Thuật toán Euclid là phương pháp hiệu quả nhất để tìm ước chung lớn nhất (ƯCLN) của hai số nguyên dương 
              #a và b bằng cách liên tục chia số lớn cho số nhỏ và lấy phần dư. Thuật toán dừng lại khi số dư bằng 0, và ƯCLN là số chia cuối cùng khác 0
""" 
float("1,000"): ERROR vì không dùng dấu , để ngăn cách hàng nghìn
"""