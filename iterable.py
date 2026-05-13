danh_sach = [1, 2, 3] #! đây là 1 iterable oject chưa phải iterator
for so in danh_sach:
    print(so)
# Kết quả:
# 1
# 2
# 3
#? Python lần lượt lấy từng số ra → đó chính là iteration.
#? Và cách nó hoạt động
danh_sach = [10, 20, 30]
# Python thực ra làm thế này:
iterator = iter(danh_sach)   # Tạo iterator

print(next(iterator))  # 10  ← lần lặp 1
print(next(iterator))  # 20  ← lần lặp 2
print(next(iterator))  # 30  ← lần lặp 3
# next() tiếp → báo lỗi StopIteration (hết rồi)
#!Giả dụ nếu không biết bao nhiêu lần print(next())
ite=iter(x for x in range(10)) 
while 1:
    try:
        print(next(ite))
    except StopIteration as e: #khi gặp lỗi thì chạy khối lệnh bên dưới
        #! as : chỉ có tác dụng bên trong khối lệnh
        print(f"Máy tính báo lỗi: {e}") #StopIteration 
        break



#? Vòng for chỉ là cách viết gọn hơn của quá trình trên.

# String
for ky_tu in "Python":
    print(ky_tu)  # P, y, t, h, o, n

# Tuple
for x in (1, 2, 3):
    print(x)

# Dictionary
for key in {"ten": "An", "tuoi": 20}:
    print(key)  # ten, tuoi

# Range
for i in range(3):
    print(i)  # 0, 1, 2



#? Cách để tạo ra 1 iterator
itera=(x for x in range(5))
print(itera) #! sẽ không hiện gì mà phải thông qua hàm next(), không thể truy xuất trực tiếp thông qua index
print(next(itera)) #0
print(next(itera)) #1


#!CÁC HÀM NÀY DÙNG GIÁ TRỊ CỦA ITERABLE ĐỂ XỬ LÝ NÊN NẾU ĐƯA VÀO 1 ITERATOR THÌ SẼ KHÔNG SỬ DỤNG ITERATOR ĐÓ ĐƯỢC NỮA
#!ĐÂY CHỈ LÀ MỨC ĐỘ XỬ DỤNG CƠ BẢN CẦN HỌC THÊM
#? sum(iterable, start=0)
sum([1, 6, 3])          #10
sum([1, 6, 3], 10)      #10+10=20
sum(iter([6, 3, 9]))
it = (x for x in range(3))
sum(it) 
next(it) #lúc này con trỏ đã đưa về cuối nên next() sẽ không trả về giá trị nào cả 


#? max/min(iterable, *[, default=obj, key=func]): tìm max/min và trả về default nếu không có giá trị
max([1, 2, 3]) #3
min([1, 2, 3], default='default value') #1
max([], default='default value') #'default value'


#? max/min(arg1, arg2, *args, *[, key=func])
max(1, 2, 3) #3
min(1, 2) #1


#? sorted(iterable, /, *, key=None, reverse=False)
sorted([1, 6, 7, 2]) #[1, 2, 6, 7]
sorted([1, 6, 7, 2], reverse=True) #[7, 6, 2, 1]










