# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#!parameter: là các biến số được liệt kê trong lời định nghĩa của một hàm
#? objects: packing argument. Ở đây hiểu nôm na sẽ là nó sẽ gom lại các argument của bạn lại thành một Tuple.

#? sep (separate – chia ra, phân ra):Giá trị mặc định của parameter này là một khoảng trắng
print('Kteam' + 'Python') #KteamPython
print('Kteam', 'Python') #Kteam Python
print('Kteam', 'Python',sep="&") #Kteam&Python

#? end: Giá trị mặc định của parameter này là \n

from time import sleep # nhập hàm sleep từ thư viện time
print('start....')
sleep(3) # dừng chương trình 3 giây
print('end...')
#! in ra start.... rồi sau 3s mới in ra end...

from time import sleep # nhập hàm sleep từ thư viện time
print('start....', end='') # in ra nội dung và kết thúc bới một chuỗi  rỗng
sleep(3) # dừng chương trình 3 giây
print('end...')
#! sau 3s thì in ra start....end...
#! LÝ DO LÀ VÌ PRINT() SẼ LƯU VÀO BỘ ĐỆM KHI PHÁT HIỆN \n THÌ MỚI IN RA HOẶC KẾT THÚC TRƯƠNG TRÌNH CHẠY MỚI IN RA

#? File
#Mặc định hàm print sẽ ghi nội dung vào file sys.stdout. Cũng nhờ vậy, bạn mới thấy được nội dung trên shell. 
#Đương nhiên, dựa vào đây, ta cũng có thể sử dụng hàm print như là phương thức write trong việc ghi file.
with open('printtext.txt', 'w') as f:
    print('printed by print function', file=f) #! Tạo 'printtext.txt' rồi lưu vào file f as 'printtext.txt'
with open('printtext.txt') as f:
    f.read() #'printed by print function\n'


#? flush: giá trị mặc định là False
from time import sleep # nhập hàm sleep từ thư viện time

print('start...', end='', flush=True)
sleep(3) # dừng chương trình 3 giây
print('end...') #!start... sau 3s thì end.....
#! print lưu vào bộ đệm và flush=true sẽ bắt xuất ra hết những gì bộ đệm có nên code trên chạy bình thường



#! in ra mỗi chữ cái cách nhau 0.1s : Hello! My name is Jyno
from time import sleep

your_name = "Jyno"
your_great = "Hello! My name is "

for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.1)
print()
