#!Tuple gần y chang như list
#! được bọc bởi cặp () và ngăn cách nhau bởi dấu phảy
#! có khả năng chứa mọi giá trị, truy xuất nhanh hơn list và chiếm ít bộ nhớ hơn list
#! bảo vệ dữ liệu của bạn không bị thay đổi và có thể làm key của dictionary


tup=()
print(tup()) #()
#!tup=(1),tup=("nguyenvie") khi khởi tạo tuple với 1 phần tử thì kiểu dữ liệu sẽ là của phần tử đó(int,str)
#! vì vậy khi muốn khởi tạo tuple với 1 phần tử duy nhất ta cần thêm dấu phảy tup(1,)


tup=(i for i in range (10)) #tuple không khai báo được kiểu này
                            #muốn làm được phải thông qua một bước trung gian
b=tuple(tup) #(0,1,2,3,4,5,6,7,8,9)

tup=(i for i in range (10) if i%2==0)
c=tuple(tup) #(0,2,4,6,8)
a=tuple([1,2,3]) #a=(1,2,3)  #tuple constructor giống hệt list contructor
a=tuple((1,2,4)+('nguye',4))
a=tuple([1,2,3]+["nguyen",5])
a=1,2,3,4 #!cũng tạo thành 1 tuple (LƯU Ý: DẤU PHẢY TẠO RA TUPLE CHỨ KHÔNG PHẢI DẤU NGOẶC)
a=1,      #! cũng tạo ra 1 tuple   




#?Toán tử trong tuple giống toán tử trong chuỗi

#?Indexing trong tuple giống trong chuỗi

#?Thay đổi phần tử trong tuple: theo lý thuyết là không vì tuple giống chuỗi là phần tử hashable
#còn list thay đổi được vì nó là phần tử unhashable



#!như đã nói tuple và list có thể chứa mọi phần tử nên trong tuple có thể chứa list và ngược lại
#! và list bên trong 1 tuple có thể thay đổi được tương tự thì tuple bên trong list cũng không thể thay đổi được

