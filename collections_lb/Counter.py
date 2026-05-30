
#*Counter: Bỏ gì vào cũng đếm được
#?Đếm các phần tử trong 1 list
from collections import Counter
dem_lst=Counter([1,2,3,1,5,1,4,1,4]) #tạo thành 1 sổ sớ liệu: Counter()
print(dem_lst) #Counter({1: 4, 4: 2, 2: 1, 3: 1, 5: 1}) 
print(dem_lst[1]) #4

#?Đếm từng lý tự trong 1 chuỗi
dem_str=Counter("nguyen viet ah dz")
print(dem_str) #Counter({' ': 3, 'n': 2, 'e': 2, 'g': 1, 'u': 1, 'y': 1, 'v': 1, 'i': 1, 't': 1, 'a': 1, 'h': 1, 'd': 1, 'z': 1, '.': 1})

#?Khởi tạo trực tiếp bằng từ khoá
khoi_tao=Counter(cats=4,dogs=7)
print(khoi_tao) #Counter({'dogs': 7, 'cats': 4})



#? (.most_common(n)): Hàm này giúp bạn tìm ra n phần tử đứng đầu bảng xếp hạng về số lần xuất hiện.
num_counts = Counter([1, 2, 2,2, 3, 3, 3, 4, 4, 4, 4])
print(num_counts.most_common(2)) # Tìm 2 số xuất hiện nhiều nhất
# Kết quả: [(4, 4), (2, 3)] -> (Số 4 xuất hiện 4 lần, Số 3 xuất hiện 3 lần)
#!Phần tử nào xuất hiện trong list trước tức index bé hơn và có cùng số phần tử sẽ được ưu tiên

# Nếu không điền số n, nó sẽ trả về toàn bộ bảng xếp hạng từ cao xuống thấp
print(num_counts.most_common()) #[(4, 4), (2, 3), (3, 3), (1, 1)]

num_counts1 = Counter([1,2,2,3,3,4,4,4,3,2])
print(num_counts1.most_common()) #[(2, 3), (3, 3), (4, 3), (1, 1)]


#!Không bị lỗi khi không có key
counts = Counter("aabbb")
print(counts["b"])  # Kết quả: 3
print(counts["z"])  # Kết quả: 0 (Không bị lỗi như dict thường)



#? elements(): đảo ngược lại quá trình đếm, trả lại về iterable cần ép kiểu list để xem
counts = Counter(a=2, b=3)
print(list(counts.elements())) 
# Kết quả: ['a', 'a', 'b', 'b', 'b'] (Thứ tự có thể ngẫu nhiên)



#? update():
counts = Counter(['apple', 'banana'])
counts.update(['apple', 'orange']) # Nhồi thêm 1 list mới vào
print(counts) # Kết quả: Counter({'apple': 2, 'banana': 1, 'orange': 1})


#?Thực hiện toán tử
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2, c=4)

# Cộng dồn kết quả đếm của cả 2
print(c1 + c2)  # Counter({'a': 4, 'b': 3, 'c': 4})
# Trừ bớt số lần xuất hiện #!Nếu kết quả <= 0, phần tử tự động bị xóa bỏ

print(c1 - c2)  # Counter({'a': 2}) (b bị trừ về 0 nên biến mất)

# Phép Giao & #!(Lấy phần tử chung và giữ lại số lần xuất hiện NHỎ HƠN)
print(c1 & c2)  # Counter({'a': 1, 'b': 1})

# Phép Hợp | #!(Lấy tất cả các phần tử và giữ lại số lần xuất hiện LỚN HƠN)
print(c1 | c2)  # Counter({'c': 4, 'a': 3, 'b': 2})
