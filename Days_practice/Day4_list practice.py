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


#! 2. Bẫy "Biến đổi tại chỗ" (In-place vs New Object)
#Bẫy này xuất hiện khi có nhiều biến cùng trỏ vào một List.
a = [1, 2]
b = a # b và a dùng chung một List

    #* Trường hợp A: Dùng += hoặc *=
a *= 2 # Sửa trực tiếp trên cái túi cũ (nên nếu gán cho 1 chuỗi khác thì cả 2 chuỗi sẽ bị sửa)
print(b) # Kết quả: [1, 2, 1, 2] -> b bị ảnh hưởng!

    #* Trường hợp B: Dùng phép gán + hoặc *
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

#?Cách 1:
nums = [5, 2, 9, 1, 7, 6]
nums_chuan=list(set(nums))
sx=list.sort()
if len(sx)<2:
    print("không có số lớn t2")
else:
    print(sx[-2])


#!HOẶC: remove(max(sx))
nums=[1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,9,9,9,9,9]
nums_chuan=list(set(nums))
nums_chuan.remove(max(nums_chuan))
print(max(nums_chuan))




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
nums_unique=set(nums)
chan=[i for i in nums_unique if i%2==0 ]
le=[i for i in nums_unique if i%2!=0]
print(chan, le)


#!HOẶC
dic={0:[],1:[]}
for i in nums_unique:
    dic[i%2].append(i) #[i%2] nếu chẵn trả về 0 thì append(i) chui vô 0:[]
                       #[i%2] nếu lẻ trả về 1 thì append(i) chui vô 1:[]
print(dic)



from collections import defaultdict  #!Tạo dict thông qua i%2: tức là i%2=0 hoặc 1 chúng sẽ tạo key thay cho mình, không phải khởi tạo
nums = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,9,9,9,9,9]
phan_loai = defaultdict(list)
# Chỉ duyệt qua các giá trị duy nhất để tối ưu hiệu suất
for i in set(nums):
    # i % 2 trả về 0 hoặc 1, dùng nó làm key để append luôn
    phan_loai[i % 2].append(i)
chan = phan_loai[0]
le = phan_loai[1]




#? lấy ra số nguyên rồi bình phương chúng tạo thành 1 list mới
mixed = [2, 4, "", 6, "", 2, 8, " ", "Python"]
ket_qua = [i*i for i in mixed if isinstance(i,int)] #!nhưng chuỗi "34" thì không được
final=[int(i)**2 for i in mixed if str(i).isdigit()]



# 4. Sắp xếp tăng dần trước
ket_qua.sort()

# 5. Đảo ngược để có danh sách giảm dần
ket_qua.reverse()

print("Kết quả cuối cùng:", ket_qua)





# In ra kết quả: ["Trái 1", "Phải 1", "Trái 2", "Phải 2", "Trái 3", "Phải 3"]
trai = ["Trái 1", "Trái 2", "Trái 3"]
phai = ["Phải 1", "Phải 2", "Phải 3"]
ket_qua = []

for i in range(len(trai)): #lặp gián tiếp qua số thứ tự
    ket_qua.append(trai[i])
    ket_qua.append(phai[i])

#!HOẶC
#? list(zip(trai, phai))= [('Trái 1', 'Phải 1'), ('Trái 2', 'Phải 2'), ('Trái 3', 'Phải 3')]
for t, p in zip(trai, phai):
    ket_qua.append(t)
    ket_qua.append(p)


#!HOẶC
ket_qua = [item for pair in zip(trai, phai) for item in pair]
#for "pair" in zip(trai, phai) lấy từng cặp ('Trái 1', 'Phải 1')
#for item in pair:('Trái 1', 'Phải 1') lấy 'Trái 1' rồi tiếp theo lấy 'Phải 1'













