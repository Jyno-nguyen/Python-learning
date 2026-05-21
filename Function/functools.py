
#* map(func,iterable) trả về một map oject(một dạng generator)
def mymap(func,iterable):
    for x in iterable: #lấy từng phần tử trong iter
        yield func(x)  #xử lý bằng func rồi trả về yield

def inc(x):
    return x+1
lst=[1,2,3,4]
print(list(map(inc,lst))) # 2,3,4,5
                          # Tại sao lại truyền vào inx mà không phải inc(x)
                          # Vì mình chỉ cần truyền vào công thức func còn số liệu tính toán nằm ở iterable
#!HOẶC
print(list(map(lambda x:x+1,lst)))
#!HOẶC
inx=lambda x: x+1
print([inc(x) for x in lst]) #!Chậm hơn map,tạo ra list 
print((inc(x) for x in lst)) #có thể tương đương với map và nhanh ngang bằng vì cũng tạo ra một generator expression

#*Nhiều iterable map(func,*iterable)
#!Lưu ý khi pass vào nhiều container thì các container phải cùng số lượng giá trị tức là cùng độ dài len
func=lambda x,y:x+y
lst1=[1,2,3,4]
lst2=[5,4,3,2]
print(list(map(func,lst1,lst2))) #[6, 6, 6, 6]
print(list(map(pow,[1,2,3],[2,3,4]))) #[1, 8, 81]





#* filter(func or None,iterable): trả về filter oject(là một generator)
#!iterale ở đây là 1 container không có packing agruments
#*Hàm filter lấy từng giá trị trong iterable, sau đó gửi vào hàm
#*nếu như giá trị hàm trả ra là một giá trị mà khi chuyển sang kiểu dữ liệu boolean là True thì sẽ yield giá trị đó, nếu không thì bỏ qua.
func=lambda x:x>0
lst3=[1,2,3,4,0,-1,-2,-3,-6]
print(list(filter(func,lst3))) #[1, 2, 3, 4]
print([x for x in lst3 if x>0])

#!Nhưng
print(list(filter(None,lst3))) #[1,2,3,4,-1,-2,-3,-6]
                               #(None,lst3): Hãy giữ lại những phần tử nào ĐÚNG (Truthy) và loại bỏ những phần tử nào SAI (Falsy)".






#* reduce(func, sequence[,initial]): trả về một giá trị
#! from functools import reduce
#! sequence: kiểu dữ liệu dạng chuỗi/dãy
#? TRACE: hàm reduce sẽ lần lượt lấy hai giá trị đầu tiên của sequence (index 0, index 1) và đưa vào hàm function
          #?Hàm function này sẽ trả ra một giá trị (ta kí hiệu là A). Sau đó lấy tiếp giá trị thứ ba của sequence (index 2), 
          #?rồi gửi vào function cũng theo thứ tự (A, index 2), rồi lại lặp lại như thế cho tới khi hết sequence.
from functools import reduce
lst_add=lambda x,y:x+y
lst4=[1,2,3,4]
print(reduce(lst_add,lst4)) #(((1+2)+3)+4)=10

lst_multi=lambda x,y:x*y
print(reduce(lst_multi,lst4)) #1*2*3*4=24

#*Truyền argument cho param initial
lst_add=lambda x,y:x+y
lst4=[1,2,3,4]
print(reduce(lst_add,lst4,10)) #((((10+1)+2)+3)+4)=20

lst_multi=lambda x,y:x*y
print(reduce(lst_multi,lst4)) #10*1*2*3*4

