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
#LƯU Ý: khi làm tròn với round(1.5)=2 và round(2.5)=2 vì Python ưu tiên làm tròn đến số chẵn gần nhất .5
#Hoặc dùng format:
print(f"{x:.2f}")  # 3.33
print(f"{x:.4f}")  # 3.3333



import math
# muốn sử dụng hàm nào trong math thì dùng math.<tên hàm>

import math

math.sqrt(16)      # căn bậc 2 → 4.0
math.pow(2, 10)    # lũy thừa → 1024.0
math.pow(2,3,4)   #(2**3)%4
math.fabs(-5)       # trị tuyệt đối → 5
math.ceil(3.2)     # làm tròn lên → 4
math.pi            # số pi → 3.14159...
math.e             # số e → 2.71828...
math.log(100, 10)  # log cơ số 10 → 2.0
math.log2(8)       # log cơ số 2 → 3.0
math.factorial(5)  # giai thừa → 120
#hàm logarit chỉ cơ số 2 và cơ số 10 được phép viết tắt kiểu log2(x), log10(x)
#hàm loge thì viết là log(x)
math.trunc(3.9) #trả về số nguyên là phần nguyên của số x 
math.gcd(6.4) #trả về số nguyên là ước chung lớn nhất của 2 số x và y
