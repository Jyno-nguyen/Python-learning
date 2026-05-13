a = [[0]] * 3
a[0].append(1)
b = a
print(b)
      
        
# Bạn muốn tạo một ma trận 3x1 toàn số 0
matrix = [[0]] * 3 
# Kết quả nhìn có vẻ đúng: [[0], [0], [0]]

matrix[0].append(1)
print(matrix) # [[0, 1], [0, 1], [0, 1]]
#!Phép nhân * không tạo ra 3 cái List con độc lập. Nó chỉ tạo ra 3 bản sao của cùng một địa chỉ vùng nhớ.
#!Cả 3 phần tử trong matrix đều đang trỏ vào đúng một cái "túi" duy nhất.

# Tạo ra 3 cái túi hoàn toàn riêng biệt
matrix = [[0] for _ in range(3)] #!cách tạo list chỉ có [0] với số lần lặp n
matrix[0].append(1)
    # Kết quả: [[0, 1], [0], [0]] -> Đúng ý bạn!


### 2. Bẫy "Biến đổi tại chỗ" (In-place vs New Object)
#Bẫy này xuất hiện khi có nhiều biến cùng trỏ vào một List.


a = [1, 2]
b = a # b và a dùng chung một List

    # Trường hợp A: Dùng += hoặc *=
a *= 2 # Sửa trực tiếp trên cái túi cũ (nên nếu gán cho 1 chuỗi khác thì cả 2 chuỗi sẽ bị sửa)
print(b) # Kết quả: [1, 2, 1, 2] -> b bị ảnh hưởng!

    # Trường hợp B: Dùng phép gán + hoặc *
a = [1, 2]
b = a
a = a * 2 # Tạo ra một cái túi mới hoàn toàn và gán cho a
print(b) # Kết quả: [1, 2] -> b không bị ảnh hưởng!

#!Lời khuyên: Nếu bạn muốn thay đổi List mà không làm ảnh hưởng đến các biến khác đang tham chiếu tới nó, hãy luôn tạo ra một bản sao mới (new object) thay vì dùng các toán tử gán tại chỗ như `+=` hay `*=`.

### 3. Bẫy "Số thực và Số âm"

    #!Nhân với số thực:** 
[1, 2] * 1.5  #$\rightarrow$ Lỗi `TypeError`. Python chỉ chấp nhận số nguyên (int) cho phép nhân List.
    #!Nhân với số âm hoặc số 0:**
[1, 2, 3] * -5 ,[1, 2, 3] * 0 #$\rightarrow$ Kết quả luôn là một >>> List rỗng `[]`
    #!Điều này đôi khi làm chương trình của bạn chạy sai logic mà không hề báo lỗi, dẫn đến việc đi tìm lỗi (debug) rất cực khổ.


#?Số, Chuỗi (Immutable)** | `[0] * 5` | **An toàn** |
#?List, Dict (Mutable)** | `[[]] * 5` | **CỰC KỲ NGUY HIỂM** |
#?Ma trận/List lồng** | `[[0]] * 5` | **CỰC KỲ NGUY HIỂM** |

#!Mỗi khi bạn định gõ dấu `*` cho List, hãy khựng lại 1 giây và tự hỏi: "Trong List này có chứa một cái List khác không?". Nếu có, hãy chuyển sang dùng **List Comprehension** ngay lập tức!







# max(),min()
lst = ["100", "2", "30"]
print(min(lst,key=int)) #phải chuyển về int vì nếu so sánh dạng chuỗi thì '30'>'100'
print(max(lst)) #in ra "30"
#? min(), max(): sẽ lỗi nếu thực hiện trên 1 chuỗi rỗng
names = ["An", "Bình", "Cường"]
print(min(names)) # Kết quả: "An"
print(max(names)) # Kết quả: "Cường"








nums = [5, 2, 9, 1, 7, 6]
# yêu cầu tìm số thứ 2 mà không dùng max (chú ý trường hợp có 2 hay nhiều số trùng nhau)

#?Cách 1: hướng giải sẽ tạo ra 1 chuỗi rỗng rồi sau đó thêm lần lượt các số vào nếu trùng thì bỏ
list_rong=[]
for i in nums: #
    if i not in list_rong:
        list_rong.append(i)
#sắp xếp list
list_rong.sort()

#nếu ít hơn 2 số thì không có số lớn thứ 2
if len(list_rong)<2:
    print("không có số lớn thứ 2")
else:
    print(list_rong[-2])

#?Cách 2: dùng max và second max
#khởi tạo 2 biến cực nhỏ
max1=max2=float('-inf')

for i in nums:
    if i>max1:
        max2=max1 #Đẩy max2 xuống rồi cho max1 bằng giá trị lớn nhất
        max1=i
    else:
        max2=i
print("số lớn thứ 2 là: ",max2)






#?Tách chẵn lẻ thành 2 chuỗi khác nhau
nums=[1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,9,9,9,9,9]
list_rong_c=[]
list_rong_l=[]
for i in nums[:]:
    if i % 2==0:
        if i not in list_rong_c:
            list_rong_c.append(i)
    else:
        if i not in list_rong_l:
            list_rong_l.append(i)
print(list_rong_c)
print(list_rong_l)






#? lấy ra số nguyên rồi bình phương chúng tạo thành 1 list mới
mixed = [2, 4, "", 6, "", 2, 8, " ", "Python"]
ket_qua = []

for i in mixed: #lặp trực tiếp qua phần tử
    # 1. Kiểm tra nếu i là số nguyên (loại bỏ chuỗi, khoảng trắng...)
    if type(i) == int:
        
        # 2. Tính bình phương
        i_binh_phuong = i * i
        
        # 3. Kiểm tra trùng: Nếu kết quả này chưa có trong list thì mới thêm vào
        if i_binh_phuong not in ket_qua:
            ket_qua.append(i_binh_phuong)

# 4. Sắp xếp tăng dần trước
ket_qua.sort()

# 5. Đảo ngược để có danh sách giảm dần
ket_qua.reverse()

print("Kết quả cuối cùng:", ket_qua)





# In ra kết quả: ["Trái 1", "Phải 1", "Trái 2", "Phải 2", "Trái 3", "Phải 3"]
trai = ["Trái 1", "Trái 2", "Trái 3"]
phai = ["Phải 1", "Phải 2", "Phải 3"]
ket_qua = []

# Dùng range để tạo ra các số 0, 1, 2 (tương ứng với các vị trí index)
for i in range(len(trai)): #lặp gián tiếp qua số thứ tự
    # Lấy phần tử ở vị trí i của list trai thêm vào
    ket_qua.append(trai[i])
    
    # Lấy phần tử ở vị trí i của list phai thêm vào ngay sau đó
    ket_qua.append(phai[i])

print(ket_qua)














