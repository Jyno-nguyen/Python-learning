#Basic 
age = 20
if age < 18:
    print("Trẻ em")
elif age < 60:
    print("Người lớn")
else:
    print("Người già")

#Ternary Operator (Toán tử ba ngôi)
#Viết if-else trên 1 dòng để code sạch sẽ (Clean Code) hơn. Rất hay dùng khi gán giá trị cho biến.

    #! giá_trị_nếu_đúng if điều_kiện else giá_trị_nếu_sai
score=float(input("Nhap diem so cua ban: "))
status = "Đỗ" if score >= 5 else "Trượt"

""" Viết chương trình yêu cầu người dùng nhập mật khẩu.
    Nếu mật khẩu ít hơn 8 ký tự: In ra "Mật khẩu quá ngắn".
    Nếu mật khẩu có chứa khoảng trắng (dùng in): In ra "Mật khẩu không được chứa khoảng trắng".
    Nếu mật khẩu là "admin123": In ra "Mật khẩu quá yếu, vui lòng chọn mã khác".
    Ngược lại: In ra "Mật khẩu hợp lệ". """
password=input("Nhap mat khau: ")
if len(password)<8: 
    print("Mật khẩu quá ngắn")
elif len(password.replace(" ",''))<8: 
    print("mật khẩu không được chứa khoảng trắng")
elif password.isalnum():
    print("mật khẩu quá yếu")
else: print("mật khẩu hợp lệ")

#!Bản code tối ưu hơn
password=input("Nhap mat khau: ")
if len(password)<8: 
    print("Mật khẩu quá ngắn")
elif ' ' in password: 
    print("mật khẩu không được chứa khoảng trắng")
elif password.isdigit() or password.isalpha():
    print("mật khẩu quá yếu")
elif password.isalnum():
    print("mật khẩu trung bình")
else: 
    print("mật khẩu mạnh")


""" Bài 2: Chuyển đổi định dạng tên (Cấp độ 1 & 2)
    Cho người dùng nhập vào họ tên đầy đủ.
    Loại bỏ khoảng trắng thừa ở hai đầu.
    Nếu tên nhập vào là chuỗi rỗng: In ra "Bạn chưa nhập tên!".
    Nếu hợp lệ, dùng toán tử ba ngôi để kiểm tra: Nếu độ dài tên > 20 ký tự thì in ra bản rút gọn (10 ký tự đầu + "..."), ngược lại in ra toàn bộ tên đã viết hoa chữ cái đầu"""

name=input("nhập họ và tên: ").strip()
if not name: #Nếu name là rỗng thì nó trở thành FALSE, sau đó not FALSE sẽ trở thành TRUE và chạy code bên trong if
    print("Bạn chưa nhập tên")
else: print(name[:10].title()+"...") if len(name)>20 else print(name.title())


""" Bài 3: Bộ lọc ngôn từ 
    Viết chương trình nhập vào một câu bình luận.
    Tạo một biến bad_word = "xau".
    Sử dụng toán tử ba ngôi để tạo biến output. Nếu bad_word xuất hiện trong bình luận, output sẽ là chuỗi đã được thay thế từ đó bằng dấu ***. Nếu không có, output giữ nguyên bình luận gốc.
    In output ra màn hình."""

nhapbinhluan=input()
bad_word="xau" 
#Dùng toán tử 3 ngôi để xử lý giá trị trước rồi sau đó mới in thay vì để print làm việc vất vả trong toán tử 3 ngôi: print(nhapbinhluan.replace(bad_word,'***')
check=nhapbinhluan.replace(bad_word,'***')if bad_word in nhapbinhluan else print(nhapbinhluan)
print(check)


""" Bài 5: Tính tiền điện "Mini" (Phối hợp logic)
    Nhập vào số điện tiêu thụ (kWh).
    Nếu số điện <= 50: Giá là 1.678đ/kWh.
    Nếu số điện > 50: Giá là 2.014đ/kWh cho toàn bộ số điện.
    Yêu cầu: Sử dụng input(), ép kiểu sang int, dùng if-else để tính tổng tiền và in ra chuỗi định dạng: "Tổng tiền: [số tiền] VNĐ"."""

tiendien=float(input())
if tiendien<50:
    Tong_tien_dien=tiendien*1.678
else:
    Tong_tien_dien=50*1.678+(tiendien-50)*2.014
print(Tong_tien_dien)



