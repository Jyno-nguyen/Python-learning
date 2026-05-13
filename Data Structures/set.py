#set là một container nhưng không được sử dụng nhiều như list or tuple
#! được giới hạn bởi cặp ngoặc {} và ngăn cách nhau bởi dấu phảy
#! không chứ nhiều hơn 1 phần tử trùng lặp
#! CHỈ CÓ THỂ chứa HASH OJECT nhưng chính nó lại không phải là hash oject => không thể chứa set trong 1 set
#! không quan tâm đến thứ tự phần tử(xếp lung tung)

set1={1,2}
set2={1,2,3,4,(1,2,4)}
set3={1,1,1,1,1}    #set3={1}
set4={([2,3],4),3}  #!không thể chứa bất kỳ một list hay một set nào bên trong
set5={}             #{}: vẫn in ra nhưng set không thể EMPTY SET tạo mà nó là <class'dict'>
set6={ i for i in range(10)} #set conprehension
set5=set() #! có thể tạo EMPTY SET từ set contructer



#? Toán tử trong set
set7={1,2}-{1,2}                #set()
set8={1,2}-{1,2,3,4,5}          #set()
set1.difference(set1, set2,...) #set()= set1-set2-set3 

#? TOÁN TỬ VÀ: '&' lấy phần tử cùng tồn tại trong các set
print(set1 & set2 & set3)     #{1}
set1.intersection(set2, set3) #{1}

#? TOÁN TỬ HOẶC: '|' lấy hết phần tử tồn tại trong các set
print(set1 | set2 | set3) #set2={1,2,3,4,(1,2,4)}
va=set1.union(set2, set3) #set2={1,2,3,4,(1,2,4)}

#! TOÁN TỬ XOR: '^' lấy phần tử chỉ tồn tại 1 trong các set
print(set1 ^ set2 ^ set3)       #(set1^set2)={3,4,(1,2,4)} 
                                #{3,4,(1,2,4)}^set3={1,3,4,(1,2,4)}
set1.symmetric_difference(set2) #{3,4,(1,2,4)}
                                #!Chỉ thực hiện với 2 set

#? Toán tử in: Kiểm tra xem có nằm trong set không 





#?CÁC PHƯƠNG THỨC
#clear():   xoá set
#pop():     #! vì set không có thứ tự nên mặc định sẽ xoá phần tử đầu tiên của set
            #cho một danh sách với số thứ tự từ 1-n, mỗi lần xoá 1 tên và in ra Tên & STT cho đến hết ds
#remove():  xoá phần tử muốn
            #!không có sẽ báo lỗi
#discard(): xoá phần tử muốn ( không có giá trị trong set không sao)
#copy(): 
#add():     thêm giá trị vào trong set (thêm ở cuối set)
#update(iterable_1, iterable_2,…)
set1={1,2}
set1.update('def', [1, 2, 3], (4, 5, 6)) #{1, 2, 3, 4, 5, 6, 'a', 'e', 'b', 'f', 'd', 'c'}


#issubset — A có NẰM TRONG B không?
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
A.issubset(B)    # True  — A ⊆ B
B.issubset(A)    # False — B không nằm trong A

# issuperset — A có CHỨA B không?
B.issuperset(A)  # True  — B ⊇ A
A.issuperset(B)  # False — A không chứa B




