    #?List là 1 container trong Python: Giới hạn bên trong cặp ngoặc vuông[]
#Các phần tử của list cách nhau bởi dấu phảy và có thể chứa mọi giá trị, đối tượng trong Python bao gồm cả chính nó
a=[] #! List rỗng
b=[[[1,2,4],['nguyen viet ha','dep trai']],1,5]
c=[i for i in range(5)] #tạo ra một list nằm trong phạm vi từ (0-30)
print(c) #[0,1,2,3,4]=range(5)=range(0,5): tức lấy [0;5)
#range(n,m): lấy từ [n;m) (nếu không điền n thì mặc định là 0)

d=[[n,n*2,n*3] for n in range(1,4)]
#[[1, 2, 3], [2, 4, 6], [3, 6, 9]]

matrix = [[i for i in range(2)] for j in range(3)]
print(matrix) #[[0, 1], [0, 1], [0, 1]]
        #? Còn nhiều dạng kết hợp nữa





#? e=list(iterable): Nghiên cứu thêm sau
list=list('nguyen viet ha') #!đây gọi là list contructor
print(list) #['n', 'g', 'u', 'y', 'e', 'n', ' ', 'v', 'i', 'e', 't', ' ', 'h', 'a']


list1=[1,2,3]
list2=list1
print(list1)
print(list2)
list2[2]='nguyen'
print(list1)
print(list2)
'''[1, 2, 3]
   [1, 2, 3]
   [1, 2, 'nguyen']
   [1, 2, 'nguyen']'''
    #? Tại sao chỉ thay đổi list2 mà list1 cũng thay đổi: Vì khi gán list2=list1 thì cả 2 đều trỏ vào một vị trí list đó( tức là cả 2 đang dùng trung 1 list)
    #? Vậy muốn tách biệt 2 list
list3=[1,2,3]
list4=list(list3)
print(list1)
print(list2)
list2[2]='nguyen'
print(list1)
print(list2)
''' [1, 2, 3]
    [1, 2, 3]
    [1, 2, 3]
    [1, 2, 'nguyen']'''







import copy
# 1. GÁN TRỰC TIẾP (Assignment) - Dùng chung vùng nhớ
# Thay đổi một biến sẽ làm biến kia thay đổi theo
a = [[1, 2], [3, 4]]
b = a 
b[0][0] = 99
print(f"Gốc a: {b}") # Bị đổi thành [[99, 2], [3, 4]]
print(f"Bản b: {a}") # Bị đổi tương tự

# 2. SAO CHÉP NÔNG (Shallow Copy) - Chỉ nhân bản lớp vỏ
# Dùng: list(); .copy(). hoặc slicing [:]
c = [[1, 2], [3, 4]]
d = list(c) # Hoặc d = c.copy()

# Trường hợp A: Thay đổi phần tử lớp ngoài (Số, Chuỗi)
d.append("New Item") 
# -> c không đổi, vì lớp vỏ (danh sách lớn) đã độc lập.

# Trường hợp B: Thay đổi phần tử bên trong List con
d[0][0] = 77 
print(f"Gốc c: {d}") # BỊ ĐỔI thành [[77, 2], [3, 4]]
print(f"Bản d: {c}") # Đã đổi

# 3. SAO CHÉP SÂU (Deep Copy) - Nhân bản toàn bộ mọi cấp độ
# Cần import copy
e = [[1, 2], [3, 4]]
f = copy.deepcopy(e)

f[0][0] = 100
print(f"Gốc e: {e}") # KHÔNG ĐỔI: [[1, 2], [3, 4]]
print(f"Bản f: {f}") # Đã đổi thành [[100, 2], [3, 4]]

#!Sử dụng hàm copy()
fruits = ["Táo", "Chuối"]
new_fruits = fruits.copy() 
new_fruits.append("Xoài") #Tác dụng của .append("items"): Thêm một phần tử mới vào vị trí cuối cùng của List.
                          #Đặc điểm: Nó làm thay đổi trực tiếp List hiện tại (Mutable), bạn không cần gán ngược lại
print(fruits)     # ["Táo", "Chuối"] (Không đổi)
print(new_fruits) # ["Táo", "Chuối", "Xoài"]






#Dùng .append('items')
groups = [["An", "Bình"], ["Chi", "Dũng"]]
# Thêm "Giang" vào cuối List con thứ 2 (Index 1)
groups[1].append([1,2,3])
print(groups) 
# Kết quả: [['An', 'Bình'], ['Chi', 'Dũng', [1,2,3]]]
list3=[[1,2,4],1,4,5]
list4=list(list3)
print(list3)
print(list4)
list4[0].append("deptraivcl")
print(list3)
print(list4)
''' [[1, 2, 4], 1, 4, 5]
    [[1, 2, 4], 1, 4, 5]
    [[1, 2, 4, 'deptraivcl'], 1, 4, 5]
    [[1, 2, 4, 'deptraivcl'], 1, 4, 5]'''
#!Cũng thay đổi cả bản gốc nếu chỉnh sửa sâu bên trong






        #?Toán tử với list
e=[1,2]
f=["nguyen","viet"]
cong=e+f #có thể cộng nhiều chuỗi với nhau: [1,2,"nguyen","viet"]
e += 'abc'  # cộng List và chuỗi
#[1, 2, 'a', 'b', 'c']
chuoi='abc' + [1, 2]  # List cộng chuỗi cho phép, chuỗi cộng List thì không.

nhan=e*2 #[1,2,1,2] nhưng không thể nhân 2 list với nhau 

    #Toán tử in
print(1 in e)  #toán tử in kiểm tra xem có nằm trong list không
'a' in [['a'], 'b', 'c'] # chỉ có ['a'] thôi, không có 'a'>>> False

    #Toán tử so sánh
[1,2,3]==[1,2,3] #True
[1,2,3]==[1,3,2] #False
[4] > [3, 4]     #True
['b', 'c', 'd'] < ['x', 'y', 'z'] #True






#? indexing in list: gần như là tương tự với cắt chuỗi
g=[1,2,4,5,'nguyen','viet',[67,5]]
print(g[6][1]) #5( cũng có thể dùng index âm tương tự như chuỗi )
print(len(g)) # bằng số phần tử trừ 1

#?list có thể thay đổi giá trị bên trong
g[1]='deptrai' #g=[1,'deptrai',4,5,'nguyen','viet',[67,5]]





        #? Matrix
        #?Phương thức kết hợp với list
    #count(chỉ điền phần tử): đếm phần tử có trong list, các giá trị logic True=1,False=0 khi đếm 0 hoặc 1 giá trị vẫn tính
    #index(): tìm số thứ tự của phần tử từ trái sang phải, không có sẽ hiện lỗi 
    #extend([1,2,3]): thay vì thêm cả list mới vào list cũ thì nó thêm từng phần tử [.....,1,2,3]
#extend([1,2,[4,5,6]]): [.....,1,2,[4,5,6]] sẽ không thêm từng phần tử của các list nhỏ hơn bên trong
    #insert(vị trí,phần tử thêm vào)
i=[1,2,4,5,6]
i.insert(0,'vietha') #thêm vào bên trái "vị trí 0" phần tử "viet ha" 

    #pop()
y=i.pop(0) #lấy phần tử ở vị trí 0 rồi gán cho y và xoá khỏi list, nếu không ghi vị trí mặc định lấy ra phần tử cuối
print(y)   #1

    #remove(): loại bỏ phần tử đầu tiên từ trái sang (bỏ qua phần tử trong list con)  
    #reverse(): đảo ngược lại phần tử trong list

    #! Lưu ý về cấu trúc sử dụng: append, extend, insert, remove, clear
    #! i.append/extend/insert/remove/clear làm thay đổi trực tiếp list hiện tại nên không cần phải gán

    #!clear(): xoá các phần tử bên trong list (CHỈ HỖ TRỢ XOÁ LIST >>> SỐ phần tử riêng bên trong list thì sẽ không xoá được)
# Phải để phần tử đầu tiên là một List con
goc = [[1, 2], [3, 4]] 
ban_sao = goc.copy()

# Bây giờ ban_sao[0] là List [1, 2]
ban_sao[0].clear() 

print(goc)     # Kết quả: [[], [3, 4]] -> Bị ảnh hưởng!
print(ban_sao) # Kết quả: [[], [3, 4]]

#!Để không ảnh hưởng đến bản gốc
import copy
ban_sao = copy.deepcopy(goc)
ban_sao[0].clear() # goc sẽ KHÔNG bị ảnh hưởng







    #!sort():đây là một lệnh "sắp xếp có điều kiện". Nó cực kỳ mạnh mẽ nhưng cũng rất "nguyên tắc".
goc = [[1, 2], [3, 4]] 
goc.sort(key=len, reverse=True) #!còn nhiều điều kiện bên trong nữa

    #Dữ liệu đồng nhất
prices = [120, 50, 200, 80]
prices.sort() # [50, 80, 120, 200]
prices.sort(reverse=True) # [200, 120, 80, 50]

names = ["Zoe", "Adam", "Bee"]
names.sort() # ['Adam', 'Bee', 'Zoe']

    #list of lists
students = [[3, "Zoe"], [1, "An"], [2, "Bình"]]
students.sort() 
# Kết quả: [[1, 'An'], [2, 'Bình'], [3, 'Zoe']] (Sắp xếp theo số báo danh 1, 2, 3)

points = [[1, 5], [1, 2], [2, 0]]
points.sort()
# Kết quả: [[1, 2], [1, 5], [2, 0]] (Số 1 bằng nhau nên xét tiếp 2 < 5)

    #Trường hợp dùng key để tùy biến tiêu chuẩn
#!Sắp xếp theo độ dài (len)
words = ["Apple", "Banana", "Cat", "Hi"]
words.sort(key=len) 
# Kết quả: ['Hi', 'Cat', 'Apple', 'Banana'] (Ngắn đứng trước)

#!Sắp xếp không phân biệt Hoa/Thường
tags = ["python", "Java", "c++"]
tags.sort() # ['Java', 'c++', 'python'] (Sai thứ tự từ điển)
tags.sort(key=str.lower) # ['c++', 'Java', 'python'] (Đúng thứ tự từ điển)


    #? sắp xếp bằng lambla
#!Sắp xếp List lồng nhau theo vị trí bất kỳ
# Danh sách: [Tên, Tuổi, Điểm]
students = [["An", 20, 8.5], ["Bình", 18, 9.0], ["Chi", 19, 7.5]]

# Ví dụ 1: Sắp xếp theo Tuổi (Index 1)
students.sort(key=lambda x: x[1])
# Kết quả: [['Bình', 18, 9.0], ['Chi', 19, 7.5], ['An', 20, 8.5]]

# Ví dụ 2: Sắp xếp theo Điểm (Index 2) tăng dần
students.sort(key=lambda x: x[2])
# Kết quả: [['Chi', 19, 7.5], ['An', 20, 8.5], ['Bình', 18, 9.0]]

#!Sắp xếp danh sách Từ điển (List of Dictionaries)
products = [
    {"name": "Laptop", "price": 1500},
    {"name": "Mouse", "price": 20},
    {"name": "Keyboard", "price": 50}
]

# Sắp xếp theo giá (price) từ thấp đến cao
products.sort(key=lambda item: item["price"])

# In kết quả: Mouse (20), Keyboard (50), Laptop (1500)

#!Sắp xếp theo nhiều tiêu chí (Multiple Keys)
# [Tên, Điểm]
data = [["An", 8], ["Bình", 10], ["An", 10], ["Bình", 7]]

# Sắp xếp theo Tên trước, sau đó ai trùng tên thì xếp theo Điểm
data.sort(key=lambda x: (x[0], x[1]))

# Kết quả: [['An', 8], ['An', 10], ['Bình', 7], ['Bình', 10]]

#!Sắp xếp dựa trên một phép toán
# Sắp xếp các số dựa trên giá trị tuyệt đối (cách xa số 0 nhất)
numbers = [-10, 5, -2, 8, 1]
numbers.sort(key=lambda x: abs(x), reverse=True)
# Kết quả: [-10, 8, 5, -2, 1]



#map(hàm, list): có thể biến đổi một list với địng dạng này thành đinh dạng khác
k=[1,2,3,4,6,7]
map(str,k) #k=['1','2',...]

