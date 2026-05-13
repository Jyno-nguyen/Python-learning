a=id(5)
print(a) #trả về giá trị duy nhất (int,longint) tuỳ đối tượng sẽ trả về giá trị 

#! toán tử với hashable oject(không thể thay đổi dữ liệu) sẽ làm thay đổi id vì python lấy đủ chỗ nên nếu muốn cộng thêm phải tìm chỗ rộng hơn tức thay đổi id
#! toán tử với unhashable oject(có thể thay đổi dữ liệu) sẽ CÓ THỂ KHÔNG làm thay đổi dữ liệu vì luôn thừa chỗ trống để cộng thêm

a=[1,2,3,4,5]
a=a+[6,7] #! sẽ làm thay đổi id, bạn đã đưa a qua một địa chỉ khác
a+= [6,7] #! sẽ không làm thay đổi id


#? Nghiên cứu thêm các phương thức toán tử với đối tượng: 
#!SAU NÀY HỌC OOP( LẬP TRÌNH ĐỐI TƯỢNG) SẼ ĐƯỢC NGHIÊN CỨU RÕ HƠN 
n = 69
n.__add__(1) # tương tự khi bạn n + 1
n.__sub__(9) # tương tự n - 9
n.__mul__(2) # tương tự n * 2
n.__radd__(1) # tương tự 1 + n
n.__rsub__(9) # tương tự 9 - n
n.__neg__() # tương tự -n

#!những phương thức trên sẽ là thay đổi id tức tạo ra đối tượng mới khi thực hiện phương thức

#!CÁC PHƯƠNG THỨC SAU ĐÂY THÌ KHÔNG
n.__iadd__(1)   # tương tự n += 1 
n.__isub__(9)   # tương tự n -= 9 
n.__imul__(2)   # tương tự n *= 2 
#!i = in-place — thay đổi trực tiếp biến, không tạo object mới!

