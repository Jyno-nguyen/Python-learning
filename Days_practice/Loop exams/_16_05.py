
#* Input: cu=[11,56,11, 14, 756, 34, 90,11, 11, 65, 0, 33,11]
#* Output: cu=[11,0,11, 14, 33, 34, 56,11, 11, 65, 90, 756,11]
#! Ngoài số 11 thì các vị trí khác sắp xếp theo thứ tự từ bé đến lớn
data=[11,56,11, 14, 756, 34, 90,11, 11, 65, 0, 33,11]
sx=sorted(x for x in data if x!=11)
final=[x if x==11 else sx.pop(0) for x in data ]

#!HOẶC
data1=data.copy()
while True:
    data1.remove(11)
    if 11 not in data1:
        break
data1.sort()
for i in range(len(data)):
    if data[i]==11:
        data1.insert(i,11)
print(data1)


"""
#*Tạo ma trận vuông nxn có số tăng tuần tự theo các mép của mảng xoắn bên trong nó
00      01     02      03      04
15      16     17      18      05
14      23     24      19      06
13      22     21      20      07
12      11     10      09      08
"""

n=int(input("Nhập ma trận vuông nxn: "))
matrix=[[0 for _ in range(n)] for _ in range(n)] 
top,bottom=0,n-1
left,right=0,n-1
current_num=0
while top<=bottom and left<=right: #*Cần phải có dấu bằng nếu trường hợp ma trận lẻ thì số chính giữa xảy ra khi top=bottom=left=right=(n-1)/2
    for i in range(left,right+1): 
        matrix[top][i]=current_num 
        current_num+=1
    top+=1
    for i in range(top,bottom+1): 
        matrix[i][right]=current_num 
        current_num+=1
    right-=1
    if top<=bottom:
        for i in range(right,left-1,-1):  #![right, left -1 - (-1)]
            matrix[bottom][i]=current_num
            current_num+=1
        bottom-=1
    if left<=right:
        for i in range(bottom,top-1,-1):   #![bottom, top -1 - (-1)]
            matrix[i][left]=current_num
            current_num+=1
        left+=1
print("\nKết quả của Matrix")
for row in matrix:
    final_row=[f"{num:0>2d}" for num in row]
    print(" ".join(final_row))

#!f-string:
          #*{num:02d}: 0 là ký tự lấp đầy, 2 là độ rộng tối thiểu, d là định dạng số nguyên Demacial 
          #!n=1.234{n:08.5f} => 01.23400 (. cũng tính là 1 ký tự)
          #!n=1.234{n:0<8.2f} => 1.230000 (. cũng tính là 1 ký tự)
          #!{1243143:,} =>1,243,143
          #!{1234.456:0<13,.4f} "1,234.4600000"







