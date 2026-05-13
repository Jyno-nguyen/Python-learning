#PHÂN TÍCH HỆ THỐNG USER
# 1. Đánh giá mật khẩu: 
#    - < 6 ký tự: "Yếu"
#    - 6-10 ký tự: "Trung bình"
#    - > 10 ký tự: "Mạnh"
# 2. Thống kê (Vòng lặp):
#    - Tìm người có 'lan_dang_nhap' nhiều nhất (lấy cả Tên và Số lần).
#    - Tính Trung bình cộng số lần đăng nhập cả hệ thống.
# 3. Định dạng:
#    - In bảng dùng F-string căn lề (Tên: 10, Độ dài: 15, Đánh giá: Phải).
he_thong_user = [{"user": "admin", "pass": "123456", "lan_dang_nhap": 150},{"user": "manager", "pass": "p@ssword123", "lan_dang_nhap": 45},{"user": "guest", "pass": "qwerty", "lan_dang_nhap": 10},{"user": "dev_root", "pass": "secure_r00t_2026", "lan_dang_nhap": 80},
    {"user": "hr_dept", "pass": "123", "lan_dang_nhap": 5}]
print("|{:10}|{:^20}|{:>10}|".format("user","độ dài pass","đánh giá"))
max2=0
tong_dn=0
for user in he_thong_user:
    ten=user["user"]
    mk=user["pass"]
    if len(mk)<=6:
        muc_do="yếu"
    elif len(mk)>10:
        muc_do="mạnh"
    else:
        muc_do="trung bình"
    print(f"|{ten:10}|{len(mk):^20}|{muc_do:>10}|")
    tong_dn+=user["lan_dang_nhap"] #!Dùng sum sẽ tối ưu hơn

    #! Dùng hàm max sẽ tối ưu hơn
    if user["lan_dang_nhap"]>max2:
        nguoi_dang_nhap_max=user["user"]
        max2=user["lan_dang_nhap"]
print("số lần đăng nhập nhiều nhất:",max2)
print("trung bình lượng đăng nhập:",round(tong_dn/(len(he_thong_user))))
print(nguoi_dang_nhap_max)

#!Code tối ưu
nguoi_dn_max=max(he_thong_user,key=lambda x: x["lan_dang_nhap"])
tong_dn=sum(u["lan_dang_nhap"] for u in he_thong_user)
tbc = tong_dn / len(he_thong_user)
print(f"{'User':<10} | {'Độ dài Pass':^15} | {'Đánh giá':>10}")
for u in he_thong_user:
    length = len(u["pass"])
    danh_gia = "Mạnh" if length > 10 else ("Trung bình" if length >= 6 else "Yếu")
    print(f"{u['user']:<10} | {length:^15} | {danh_gia:>10}")
print(f"Người tích cực nhất: {nguoi_dn_max['user']} ({nguoi_dn_max['lan_dang_nhap']} lần)")
print(f"Trung bình cộng: {tbc:.1f} lần/người")

#?PHƯƠNG THỨC max(),HÀM sum(), SẮP XẾP lambda, forloop: Cần học rõ hơn





# QUẢN LÝ KHO HÀNG (FINAL CHALLENGE)
# 1. Bán hàng: 
#    - Nhập tên SP và số lượng mua.
#    - Kiểm tra: Tồn tại SP? Đủ số lượng?
#    - Nếu OK: Trừ số lượng trong kho, tính tiền khách trả.
# 2. Thống kê (khi thoát):
#    - Tính tổng giá trị kho còn lại (Tổng của tất cả: Số lượng * Giá).
#    - Tìm SP có giá bán cao nhất (Dùng tư duy tìm Max).

kho_hang = [
    {"ten": "iPhone 15", "gia": 25000000, "so_luong": 5},
    {"ten": "Samsung S24", "gia": 22000000, "so_luong": 8},
    {"ten": "Oppo Reno", "gia": 10000000, "so_luong": 12},
    {"ten": "Xiaomi 14", "gia": 15000000, "so_luong": 0}
]
#! Xử lý tìm kiếm sản phẩm
while True:
    nhap=input("Nhập sản phẩm hoặc 'exit' để xem bảng thống kê: ").strip()
    if nhap=="exit":
        break

    #!Phần xử lý cần chú ý vì sử dụng cách hoạt động và gán biến sử dụng None
    sp_nhap=None
    for ten in kho_hang: #ten: đang có vai trò là thông tin 1(4) sản phẩm 
        if ten["ten"].lower()==nhap.lower(): #để ten['ten'] viết thường hết 
            sp_nhap=ten #2 biến đều trỏ vào cùng 1 vi trí và khi thay đổi số lượng thì biến gốc cũng thay đổi
            break
    if not sp_nhap:
        print("không tìm thấy sản phẩm")
        continue
    if sp_nhap["so_luong"]==0:# nên sp_nhap["so_luong"] có thể dùng được và =ten["so_luong"]
        print("sản phẩm đã hết hàng")
        continue


    while True: #!phần xử lý số lượng mua và thanh toán
        print(f"Thông in sản phẩm: {sp_nhap}")
        sl=input("Nhập số lượng mua: (back để quay lại tìm kiếm)")
        if sl=="back":
            break
        if sl.isdigit():
            if int(sl)>sp_nhap["so_luong"]:
                print("sản phẩm trong kho không đủ số lượng")
            elif int(sl)<=0:
                print("số lượng mua phải lớn hơn")
            else:
                tong_tien=sp_nhap["gia"]*int(sl)
                print(f"Tổng tiền cần thanh toán: {tong_tien}")
                sp_nhap["so_luong"]-=int(sl)
                break
        else:
            print("vui lòng nhập số hợp lệ")

for sp_nhap in kho_hang: #!phần in thống kê kho hàng
    print(f"Mặt hàng: {sp_nhap}")
tong_gia_tri=sum(sp_nhap["so_luong"]*sp_nhap["gia"] for sp_nhap in kho_hang)
print(tong_gia_tri)
sp_max=max(kho_hang, key=lambda x:x["gia"])
#!lúc này sp_max là một cái dict muốn lấy ra tên thì sp-max["ten"]
print(sp_max["ten"])
