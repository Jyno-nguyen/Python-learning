#Boolean: Chỉ chứa đúng 2 giá trị: True hoặc False
#? Khi so sánh hai iterable cùng loại. Python sẽ lấy lần lượt từng phần tử trong iterable ra so sánh
"Kteam" == "Kteam" # True
'Free' == 'Education' #False

#!Python so sánh các kí tự với nhau bằng cách đưa chúng về dưới dạng số bằng hàm ord
ord('A') #65
ord('a') #97

#? Toán tử is
#! Khác với toán tử ==: Toán tử is so sánh id chứ không so sánh giá trị của biến 
#!NHƯNG VỚI GIÁ TRỊ TỪ [-5;256] HOẶC CHUỖI CÓ SỐ KÝ TỰ DƯỚI 20 CÓ CÙNG MỘT HÀM ID
a,b=13,13
print(a is b) #True
c,d=300,300
print(c is d) #False


#? Các giá trị cũng là các boolean: Mọi giá trị đều trả về True trừ: 0, None ,Rỗng

True + 1 = 2
False + 1 = 1

#? Toán so sánh
print(b < -3 < -1 < -2 < a < 6 ) #True
#! (b < -3) and (-3<-1) and ..... (a<6)


#!Thay vì
k = 4
k == 3 or k == 4 or k == 5
#!
k in (3, 4, 5) # nên dùng () hơn là [] hoặc thứ gì khác




