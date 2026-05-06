print("hello, I'm Jyno")
#notes
'''notes'''
""" notes"""

""" type(<ten bien>) kiểm tra kiểu dữ liệu biến """

"""số thực chỉ lấy được 15 số sau dấu phảy, nếu muốn lấy thêm thì phải dùng thư viện decimal"""

#thêm thư viện decimal
from decimal import*#từ thư viện decimal import (*) mọi thứ vào
#lấy 30 số phần nguyên và phần thập phân
getcontext().prec=3 #hàm này chỉ cần thiết khi bạn cần lấy đúng bao nhiêu số phần nguyên và phần thập phân
d=Decimal(10)/3
print(d)
print(type(d))
""" hello, I'm Jyno
3.33
<class 'decimal.Decimal'>"""

#PHÂN SỐ
from fractions import*
e=Fraction(6,9)
print(e)
