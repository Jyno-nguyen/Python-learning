#Capitalize(): viết hoa chữ cái đầu tiên của chuỗi và các chữ cái còn lại viết thường
c="nguyen viet ha dep trai"
d=c.capitalize() #Nguyen viet ha.... (bắt buộc phải bắt đầu bằng chữ và mọi chữ khác nếu viết hoa ngoài chữ cái đầu sẽ chuyển về viết thường)
                 #c. là để gọi hàm ra kết hợp với nó để thực hiện lệnh
    #Upper(): Tất cả viết hoa
    #Lower(): Tất cả các chữ viết thường
    #swapcase(): Chuyển từ viết hoa thành viết thường và viết thường thành viết hoa
    #title(): trả về tiêu đề ( tức là viết hoa chữ cái đầu tiên của các chữ còn lại là viết thường )
    #center(width,[fillchar]): width: bắt buộc phải điền cái còn lại có hoặc không đều được
e=c.center(30) # chừa 30 ô hiển thị và c nằm giữa, vì fillchar không điền nên nó là khoảng trống
f=c.center(30,'a') # điền a vào khoảng trắng 2 bên và fillchar là chuỗi phải có độ dài là 1 
    #rjust(width,[fillchar]): căn lề trái
    #ljust(width,[fillchar]): căn lề phải
    #strip(): loại bỏ khoảng trắng thừa ( đầu dòng và cuối dòng), nếu điền ký tự bên trong sẽ cắt ký tự 2 đầu đi( nếu có )
            : #Nếu điền nhiều ký tự bên trong nó sẽ phân tách ra từng ký tự rồi xoá nếu có "apple".strip('lpae') >>> kết quả in ra là chuỗi rỗng
    #lstrip(): chỉ xoá khoảng trắng bên trái/xảy ra tương tự nếu điều ký tự/chuỗi bên trong strip()
    #rstrip(): chỉ xoá khoảng trắng bên phải/xảy ra tương tự nếu điền ký tự/chuỗi bên trong strip()

    #join(['a','b','c']): lấy từng phần tử trong ngoặc cộng lần lượt với chuỗi
g="NVH"
h=g.join(['a','b','c'])
#h= 'aNVHbNVHc'

    #replace('a','b',c): thay thế ký tự/chuỗi (a) bằng ký tự/chuỗi (b) với số lần thay thế = c( c không điền thì mặc định thay thế hết)

    #Tách chuỗi