k=range(5) 
print(list(k)) #[0, 1, 2, 3, 4]
print(list(range(2,5))) #[2, 3, 4]
print(list(range(4,1,-1))) #[4, 3, 2]
#! range(start,stop-step,step)
print(list(range(2,-3,-1))) #[2, 1, 0, -1, -2]


#*Toán tử in
m=range(100)
print(99 in m) #True


#!Vòng lặp for với range
lst=[4,(1,2,4,4),{'abc','xyz'}]
for i in len(lst):
    print(lst[i]) #!Không thể chạy được vì vòng lặp for không thể chạy trên một con số đơn lẻ len(lst)=3

for item in lst:
    print(item)   #Chạy bình thường in ra từng phần tử của list

for i in range(len(lst)):
    print(lst[i]) #*Cũng chạy bình thường và in ra từng phần tử của list





#!Tham chiếu và biến tạm
lst1=[2,3,4]
for v in lst1: #!v lúc này chỉ copy giá trị từ list chứ không thay đổi giá trị trong list
    v+=1.      #!sequence scan: Khi bạn chỉ cần dùng giá trị của phần tử, hoặc khi phần tử đó là kiểu dữ liệu thay đổi được (như List con ở bài dưới) và bạn muốn sửa bên trong nó.
               #!tức là muốn thay đổi phần tử nào đó cần phải dùng đến index
print(lst1) #lst1=[2,3,4]


for v in range(len(lst1)): #!v lúc này lấy giá trị của list từ index và thay đổi chứ không phải bản sao 
    v+=1.                  #!indexing scan: Khi bạn cần biết chính xác vị trí của phần tử để làm việc khác, hoặc khi bạn muốn thay thế hoàn toàn phần tử đó bằng một giá trị mới.
print(lst1) #lst1=[3,4,5]

lst2=[[1,3,4],[4,5,6]]
for lis in lst2: #!sequence scan
    lis[0]=1
print(lst2) #![[1, 3, 4], [1, 5, 6]]