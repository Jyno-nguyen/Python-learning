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
he_thong_user = [
    {"user": "admin", "pass": "123456", "lan_dang_nhap": 150},
    {"user": "manager", "pass": "p@ssword123", "lan_dang_nhap": 45},
    {"user": "guest", "pass": "qwerty", "lan_dang_nhap": 10},
    {"user": "dev_root", "pass": "secure_r00t_2026", "lan_dang_nhap": 80},
    {"user": "hr_dept", "pass": "123", "lan_dang_nhap": 5}
]

print("|{:10}|{:^15}|{:>10}|".format("User", "Độ dài Pass", "Đánh giá"))
print("-" * 39) # Kẻ đường gạch ngang cho đẹp

for u in he_thong_user:
    ten, mk = u["user"], u["pass"]
    # Logic 1 dòng cực gọn
    muc_do = "Mạnh" if len(mk) > 10 else "Yếu" if len(mk) < 6 else "T.Bình"
    
    print(f"|{ten:10}|{len(mk):^15}|{muc_do:>10}|")

# Dùng nháy đơn 'user' bên trong f-string để tránh lỗi
dn_max = max(he_thong_user, key=lambda x: x["lan_dang_nhap"])
tong_dn = sum(u["lan_dang_nhap"] for u in he_thong_user)
#!
lis_yeu=[u["user"] for u in he_thong_user if len(u["pass"])<6] #! tạo list những người có mật khẩu yếu
dict_yeu = {u["user"]: u["pass"] for u in he_thong_user if len(u["pass"]) < 6} #! tạo dict những người có mật khẩu yếu

# Lọc ra toàn bộ dữ liệu của những người mật khẩu yếu
dict_yeu = {k: v for u in he_thong_user if len(u["pass"]) < 6 for k, v in u.items()}
#!lần đầu duyệt: u in he_thong_user if len(u["pass"]) < 6: 
#!bóc tách: k, v in u.items() rồi gán cho k,v
#!VÌ MỖI LẦN BÓC LẠI GÁN CHO k,v nên trùng key vì vậy nếu có nhiều người thì sau cũng dict vẫn chỉ có 1 người

print("-" * 39)
print(f"User tích cực nhất: {dn_max['user']} ({dn_max['lan_dang_nhap']} lần)")
print(f"Trung bình đăng nhập: {tong_dn // len(he_thong_user)} lần")








# ĐỀ BÀI: QUẢN LÝ KHO HÀNG (FINAL)
# Cấu trúc: List chứa các Dictionary {tên, giá, số lượng}.
# Menu chính: 1.Bán hàng | 2.Thống kê | 3.Thoát.
# Logic Bán hàng:
#  - Tìm SP (không phân biệt hoa/thường).
#  - Kiểm tra kho (Hết hàng? Đủ số lượng?).
#  - Cho phép chọn: Thanh toán (trừ kho) | Đổi số lượng | Đổi SP khác.
#  - Xử lý lỗi: Dùng try-except để chặn việc nhập chữ thay vì nhập số.
# Thống kê:
#  - In danh sách kho.
#  - Tính tổng trị giá kho (sum).
#  - Tìm SP đắt nhất (max + lambda)"""
kho_hang = [
    {"ten": "Samsung S24", "gia": 25000000, "so_luong": 5},
    {"ten": "iPhone 15", "gia": 22000000, "so_luong": 8},
    {"ten": "Oppo Reno", "gia": 10000000, "so_luong": 12},
    {"ten": "Xiaomi 14", "gia": 15000000, "so_luong": 0}]
print("=== QUẢN LÝ KHO HÀNG (FINAL) ===")
while True:
    nhap=input("\n1:Bán hàng\n2:Thống kê\n3.Thoát\n")
    if nhap=='1':
        while True:
            sp=input("Tìm kiếm / Thoát: ").strip().lower()
            sp_ton_tai = None
            if sp=="Thoát".lower():
                break
            for hang in kho_hang:
                if sp==hang["ten"].strip().lower():
                    sp_ton_tai=hang #! sp_ton_tai={"ten": ,"gia": ,"so_luong": }
                    gia,sl=hang["gia"],hang["so_luong"]
                    break
            if sp_ton_tai:
                if sp_ton_tai["so_luong"]==0:
                    print("Sản phẩm đã hết hàng.")
                    continue
                while True:
                    sl_mua=input(f"Sản phẩm {sp_ton_tai["ten"]} còn {sp_ton_tai["so_luong"]}. Nhập số lượng mua / Thay đổi sản phẩm (Nhập exit): ")
                    if sl_mua=="exit":
                        break
                    try:
                        sl_mua_int=int(sl_mua)
                        if sl_mua_int>sp_ton_tai["so_luong"] or sl_mua_int <=0:
                            print("Vui lòng nhập lại")
                            continue
                        else:
                            khac=input("0.Thanh toán | 1.Thay đổi số lượng | 2.Thay đổi sản phẩm")
                            if khac=="0":
                                tien=sl_mua_int*sp_ton_tai["gia"]
                                sp_ton_tai["so_luong"]-=sl_mua_int
                                print(f"Thành tiền: {tien:,}") #!{:,} để khi in ra từ 25000=25,000
                                break
                            if khac=="1":
                                continue
                            if khac=="2":
                                break
                    except ValueError:
                        print("Vui lòng nhập lại")
                        continue
                break
            else:
                print("Không tìm thấy sản phẩm trong kho.")
                continue
    if nhap=='2':  
        for ton in kho_hang:
            print(f"Sản phẩm: {ton["ten"]}, giá: {ton["gia"]}, số lượng: {ton["so_luong"]}")
        best=sum(sp1["so_luong"]*sp1["gia"] for sp1 in kho_hang)
        max_=max(kho_hang, key=lambda x:x["gia"])
        print(f"Tổng tiền sản phẩm: {best:,}")
        print(f"Sản phẩm đắt nhất là {max_['ten']}: {max_['gia']:,}")
    if nhap=='3':
        break
