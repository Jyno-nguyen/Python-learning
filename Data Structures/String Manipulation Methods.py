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
              #Nếu điền nhiều ký tự bên trong nó sẽ phân tách ra từng ký tự rồi xoá nếu có 
print("apple".strip("lpea")) #kết quả là rỗng
    #lstrip(): chỉ xoá khoảng trắng bên trái/xảy ra tương tự nếu điều ký tự/chuỗi bên trong strip()
    #rstrip(): chỉ xoá khoảng trắng bên phải/xảy ra tương tự nếu điền ký tự/chuỗi bên trong strip()


    #join(['a','b','c']): lấy từng phần tử trong ngoặc cộng lần lượt với chuỗi
g="NVH-"
h=g.join(['a','b','c'])
#h= 'aNVH-bNVH-c'


    #replace('a','b',c): thay thế ký tự/chuỗi (a) bằng ký tự/chuỗi (b) với số lần thay thế = c( c không điền thì mặc định thay thế hết)

    #split(): xoá các ký tự đặt trong dấu ngoặc và chia thành các chuỗi nhỏ hơn nếu có
k=c.split() #['nguyen','viet','ha','dep','trai']
l=c.split('e') #['nguy','n vi','t ha d','p trai']
m=c.split('e',2) #chỉ cắt 2 lần (nếu để không coi như cắt hết)
    #rsplit(): cắt từ bên phải qua
#? Lấy phần tử bên trong && và %%: s='jhahsfhAKFSJFJSf &&1234%% JJADHJAJD'
# code = s.split('&&')[-1].split('%%')[0]


    #partition():tìm ký tự/chuỗi trong ngoặc để cắt ('phần đầu của chuỗi',   'ký tự/chuỗi trong ngoặc',   'phần sau của chuỗi')
n=c.partition('e') #('nguy','e','n viet ha dep trai')
o=c.partition('k') #('','','nguyen viet ha dep trai')
    #rpartition(): tương tự nhưng từ bên phải sang


    #count('ký tự/chuỗi',start, end): đếm ký tự/chuỗi (nếu điền 1 trong 2 bắt buộc phải điền start, end có thể điền hoặc không)
    #startswith('ký tự',start,end): xem chuỗi bắt đầu từ "start" có bắt đầu từ ký tự kiểm tra hay không >>> trả về kết quả TRUE OR FALSE 
print("nguyen viet ha".startswith('ngu')) #TRUE 
    #endswith( tương tự ): chuỗi có kết thúc bằng ký tự/chuỗi đấy hay không 
        #LƯU Ý: count(),startswith() và endswith(): ('',start,end) có thể dùng số âm như phần đánh số các ký tự chuỗi
               #Đầu tiên sẽ lấy những ký tự trong chuỗi theo số thứ tự start, end mà bạn nhập sau đó mới xét xem bắt đầu hoặc kết thúc có đúng chuỗi/ký tự đó không


    #find(): tìm ký tự hoặc chuỗi và ghi ra màn hình số thứ tự của ký tự/chuỗi đó, nếu không có kết quả ra -1 (0 đến n-1)
    #rfind(): tìm từ phải sang trái số thứ tự vẫn tính từ trái sang với (0 đến n-1)
print("asdfghf".find("f")) #3
print("asdfghf".rfind("f")) #6
    #index()/rindex(): y hệt như find()/rfind() nhưng nếu không tìm ra sẽ hiện lỗi
    #zfill(): thêm số không vào bên trái cho đủ độ dài
print("42".zfill(7)) #0000042



    #islower(): kiểm tra xem có viết thường hết không >>> trả về true or false
    #isupper(): kiểm tra xem có viết hoa hết hay không >>>
    #isdigit(): kiểm tra xem có là số hết không, có thể chứa các ký tự đặc biệt như số mũ (có dấu cách cũng cho kết quả FALSE)(TRUNG CẤP) VD: 
    #isspace(): kiểm tra xem chuỗi tất cả có phải khoảng trắng hay không
    #isalpha(): kiểm tra xem có toàn chữ cái hay không( dấu cách cũng tính là FALSE)
    #isalnum(): kiểm tra xem chỉ có chữ và số (có dấu cách cũng cho kết quả FALSE) VD:12hdfshf;HDH88;...
    #isdecimal(): kiểm tra xem có phải chỉ là số không( không được chứa cả dấu chấm,chỉ chứa ký tự số dạng thập phând )(NGHIÊM NGẶT NHẤT) VD: 123;54;78
    #isnumeric(): kiểm tra xem số có phải dạng chuỗi hay không (có thể có phân số)(RỘNG NHẤT) VD:1/2;số la mã;...
    #!Lưu ý: chỉ kiểm tra được CHUỖI, KIỂM TRA SỐ SẼ BỊ MẮNG

    #sorted(): sắp xếp lại thứ tự ký tự từ thấp lên cao


