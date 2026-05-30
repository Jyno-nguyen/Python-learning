"""Project 5: Trình phân tích & Chiết xuất dữ liệu học viên (Grade Analyzer Pro)

Yêu cầu hệ thống:
Hệ thống lưu trữ thông tin của một lớp học gồm Tên học viên và Điểm số của 3 môn học: Toán, Văn, Anh.
Bạn phải xây dựng các tính năng sau:
Tính điểm trung bình (GPA) của từng học viên và tự động xếp loại học lực theo quy tắc: GPA≥8.0: Giỏi; 5.0≤GPA<8.0: Khá; GPA<5.0: Yếu.
Tìm và in ra thông tin (Tên, Điểm các môn, GPA) của học viên có GPA cao nhất (Thủ khoa) và học viên có GPA thấp nhất.
Xuất ra một danh sách tổng hợp tất cả học viên được sắp xếp theo thứ tự điểm GPA từ cao xuống thấp.
"""

database = {
    "Nguyen Van An": {"Toan": 8.5, "Van": 7.2, "Anh": 9.0},
    "Tran Thi Binh": {"Toan": 4.5, "Van": 5.0, "Anh": 4.0},
    "Le Hoang Chuong": {"Toan": 9.5, "Van": 8.8, "Anh": 10.0},
    "Pham Minh Duc": {"Toan": 6.0, "Van": 6.5, "Anh": 5.5}}
def thong_ke(**data):
    for ten,thong_tin in data.items():
        gpa=round((thong_tin["Toan"]+thong_tin["Van"]+thong_tin["Anh"])/3,2)
        status="Xuat Sac" if gpa>=9 else "Yeu" if gpa<5 else "Gioi"
        thong_tin["đánh giá"]={"gpa":gpa,"xếp loại":status}

    gpa_max=max(data.values(),key=lambda diem: diem["đánh giá"]["gpa"])
    per_max=[ten for ten,thong_tin in data.items() if thong_tin["đánh giá"]["gpa"]==gpa_max["đánh giá"]["gpa"]]

    gpa_min=min(data.values(),key=lambda diem: diem["đánh giá"]["gpa"])
    per_min=[ten for ten,thong_tin in data.items() if thong_tin["đánh giá"]["gpa"]==gpa_min["đánh giá"]["gpa"]]

    return sorted(data.items(),key=lambda hs: hs[1]["đánh giá"]["gpa"],reverse=True),f"Những người có GPA cao nhất:{per_max}",f"Những người có GPA thấp nhất:{per_min}"
print(*thong_ke(**database),sep="\n")
#!Chưa tối ưu, chạy quá nhiều lần vòng lặp
#!truy cập sâu nhiều lần và dễ sai


database = {
    "Nguyen Van An": {"Toan": 8.5, "Van": 7.2, "Anh": 9.0},
    "Tran Thi Binh": {"Toan": 4.5, "Van": 5.0, "Anh": 4.0},
    "Le Hoang Chuong": {"Toan": 9.5, "Van": 8.8, "Anh": 10.0},
    "Pham Minh Duc": {"Toan": 6.0, "Van": 6.5, "Anh": 5.5}}
def thong_ke(data):
    gpa_min=11
    gpa_max=-1
    for ten,diem in data.items():
        gpa=round((diem["Toan"]+diem["Van"]+diem["Anh"])/3,2)

        diem["gpa"]=gpa
        diem["xep_loai"]="Xuat Sac" if gpa>=8 else "Yeu" if gpa<5 else "Gioi"

        gpa_min=gpa if gpa<gpa_min else gpa_min
        gpa_max=gpa if gpa>gpa_max else gpa_max

    thu_khoa=[ten for ten,diem in data.items() if diem["gpa"]==gpa_max]
    thap_nhat=[ten for ten,diem in data.items() if diem["gpa"]==gpa_min]
    ds_sx=sorted(data.items(),key=lambda diem: diem[1]["gpa"],reverse=True)
    return ds_sx,f"Thủ khoa: {thu_khoa}",f"Yếu nhất: {thap_nhat}"
print(*thong_ke(database),sep="\n")

















"""Project 2: Trò chơi Đoán số & Lưu vết tư duy (Smart Number Guessing Game)
Yêu cầu hệ thống:
Máy tính sinh ngẫu nhiên một số nguyên bí mật trong đoạn [1,100].
Người chơi có tối đa 7 lượt nhập số để đoán.
Với mỗi lượt nhập, hệ thống phải xử lý:
Nếu số nhập vào nằm ngoài khoảng [1,100], báo lỗi nhập sai quy chế và vẫn trừ 1 lượt đoán.
Nếu số nhập vào nhỏ hơn hoặc lớn hơn số bí mật, in ra thông báo tương ứng "Số bạn đoán quá thấp" hoặc "Số bạn đoán quá cao".
Trò chơi kết thúc khi người chơi đoán đúng hoặc hết 7 lượt. Tại thời điểm kết thúc, hệ thống bắt buộc phải in ra:
Kết quả chung cuộc (Thắng/Thua) kèm số bí mật.
Danh sách toàn bộ các số mà người chơi đã thử đoán theo đúng thứ tự thời gian.
"""
count=0
ls=[]
import random
r=random.randint(1,100)
print("Bạn có tối đa 7 lần đoán")
while count<7:
    count+=1
    try:
        n=int(input(f"Nhập số lần thứ {count}: "))
        ls.append(n)
        if n<=0 or n>100:
            print("Vui lòng nhập số trong khoảng [1,100]")
        else:
            if n<r:
                print("Vui lòng nhập số lớn hơn")
            elif n>r:
                print("Vui lòng nhập số nhỏ hơn")
            elif n==r:
                print("Correct")
                break
    except ValueError: 
        print("Vui lòng nhập số nguyên")
kq="Bạn đã Thắng" if n==r else "Bạn đã thua"
print(f"Số cần đoán: {r}.{kq} với số lần đoán {count} lịch sử đoán: {ls}")


#!HOẶC
import random
def ktra(user_input,so_bi_mat):
    try:
        n=int(user_input)
        if n<=0 or n>100:
            return False, "Vui lòng nhập số trong khoảng [1,100]",None
        elif n>so_bi_mat:
            return True, "Vui lòng nhập số bé hơn", n
        elif n<so_bi_mat:
            return True, "Vui lòng nhập số lớn hơn", n
        return True,"Correct",n
    except ValueError:
        return False,"Vui lòng nhập số nguyên dương",None
def play_game():
    count=0
    r=random.randint(1,100)
    ls=[]
    win=False
    print("Bạn có tối đa 7 lần đoán")
    while count<7:
        count+=1
        user_input=input(f"Nhập số lần thứ {count}: ")
        ls.append(user_input)
        hop_le,thong_bao,so_hop_le=ktra(user_input, r) #!trả về so_hop_le để có thể phục vụ những tính toán cần thiết như không nhập lại số cũ,...
        print(thong_bao) #!In ra thông báo
        if thong_bao=="Correct":
            win=True
            break
    kq="Bạn đã thắng " if win else "Bạn đã thua"
    print(f"số bí mật: {r}.{kq} với số lần đoán {count} và lịch sử đoán {ls}")
play_game()

















"""Project 7: Trình Nén & Giải nén dữ liệu văn bản (Text Compress & Decompress Engine)
Yêu cầu hệ thống:
Xây dựng một công cụ có 2 hàm độc lập hoạt động trên bảng mã ký tự:
Hàm compress(văn_bản): Nhận vào chuỗi thô và nén lại bằng cách đếm số lần xuất hiện liên tiếp của ký tự. Ví dụ: "AAABBC" sẽ thành "A3B2C1".
Hàm decompress(chuỗi_nén): Nhận vào chuỗi đã nén ở hàm trên và phục hồi nguyên vẹn về chuỗi gốc ban đầu. Ví dụ: Nhập "X2Y4Z1" phải trả về "XXYYYYZ".
Điều kiện biên: Hàm giải nén phải xử lý được trường hợp số lần lặp lại là số có nhiều chữ số (Ví dụ: "A12B2" phải giải nén ra 12 chữ A và 2 chữ B)."""
def decompress(text):
    num=''
    i=0
    giaima=[]
    while i<len(text) and text[i].isalpha(): #!Lưu ý để điều kiện i<len(text) trước nếu không sẽ lỗi index out of range
        char=text[i]
        i+=1
        num=''
        while i<len(text) and text[i].isdigit():
            num+=text[i]
            i+=1
        giaima.append(f"{char*int(num)}" if num!='' else f"{char}")
    return "".join(giaima)

def compress(text):
    count=1
    mahoa=[]
    current_char=text[0]
    for char in text[1:]:
        if current_char==char:
            count+=1
        else:
            mahoa.append(f"{current_char}{count}" if count!=1 else f"{current_char}")
            count=1
            current_char=char   
    mahoa.append(f"{current_char}{count}" if count!=1 else f"{current_char}")
    return "".join(mahoa)

def doing(text):
    if len(text)<=1:
        return text
    n = input("1.Giải nén | 2.Mã hoá : ").strip()
    if n == "1":
        return decompress(text)
    elif n == "2":
        return compress(text)
    else:
        return "Lựa chọn không hợp lệ! Vui lòng chỉ chọn 1 hoặc 2."


















""" Project 4: Hệ thống Quản lý công việc và Tiến độ (To-Do List Manager)
Yêu cầu hệ thống:
Khởi tạo một trình quản lý chạy liên tục hiển thị Menu gồm 5 tùy chọn: 1. Xem danh sách, 2. Thêm công việc, 3. Đánh dấu hoàn thành, 4. Xóa công việc, 5. Thoát.
Quy trình hoạt động:
Khi xem danh sách: Hiển thị rõ số thứ tự, tên công việc, và trạng thái (Ví dụ: [Chưa xong] hoặc [Đã xong]).
Khi thêm: Cho phép nhập tên công việc mới (mặc định trạng thái ban đầu là chưa xong).
Khi đánh dấu hoàn thành: Người dùng nhập số thứ tự của công việc. Hệ thống phải chuyển trạng thái công việc đó thành [Đã xong]. Nếu số thứ tự không tồn tại, báo lỗi.
Khi xóa: Người dùng nhập số thứ tự để xóa hẳn công việc ra khỏi hệ thống. Các công việc còn lại phải tự động cập nhật lại số thứ tự hiển thị cho chính xác.
"""
todo_list = [
    {"task_name": "Học Python nâng cao về Ma trận", "status": "Chưa làm"},
    {"task_name": "Làm bài tập nén chuỗi Project 7", "status": "Đã xong"},
    {"task_name": "Làm bài tập nén chuỗi Project 8", "status": "Đang làm"}]

def ds():
    for index,work in enumerate(todo_list,1):
        print(f"{index}.{work["task_name"]:<33}-{work["status"]:>9}")

while True:
    print("1. Xem danh sách\n2. Thêm công việc\n3. Đánh dấu trạng thái\n4. Xóa công việc\n5. Thoát.")
    choice=input("Nhập lựa chọn: ").strip()
    if choice=="1":
        ds()
    elif choice=="2":
        name=input("Tên công việc mới: ")
        if name:
            todo_list.append({"task_name":name,"status":"Chưa làm"})
    elif choice=="3":
        ds()
        try:
            stt=int(input("Nhập số thứ tự muốn đổi trạng thái: "))
            index=stt-1
            if index<0 or index>=len(todo_list):
                print("Số thứ tự không tồn tại.")
                continue
            status=input("Nhập trạng thái muốn thay đổi: 1.Đang làm | 2.Đã xong: ").strip()
            todo_list[index]["status"]="Đang làm" if status=="1" else "Đã xong"
        except ValueError:
            print("Lỗi. Vui lòng chỉ nhập số nguyên. ")
    elif choice=="4":
        ds()
        try:
            stt=int(input("Nhập stt muốn xoá: "))
            index=stt-1
            if index<0 or index>=len(todo_list):
                print("Số thứ tự không tồn tại.")
                continue
            cv_xoa=todo_list.pop(index)
        except ValueError:
            print("Lỗi. Vui lòng chỉ nhập số nguyên. ")
    elif choice=="5":
        break
    else:
        print("Không có lựa chọn hợp lệ")


















"""Project 1: Hệ thống Đăng ký & Xác thực tài khoản (Account Validator)
Yêu cầu hệ thống:
Nhận đầu vào từ bàn phím gồm username, email, và password.
Trả về thông báo lỗi cụ thể cho người dùng và bắt nhập lại nếu vi phạm các điều kiện sau:
username: Phải dài từ 5 đến 15 ký tự, không chứa ký tự đặc biệt (chỉ chứa chữ và số).
email: Phải có đúng một ký tự @, phải có ít nhất một dấu chấm . xuất hiện sau ký tự @, và không được có khoảng trắng.
password: Phải dài tối thiểu 8 ký tự, phải có ít nhất 1 chữ cái viết hoa, 1 chữ cái viết thường, 1 chữ số, và 1 ký tự đặc biệt trong tập hợp [!@#$%^&*].
Hệ thống chỉ dừng lại và in ra "Đăng ký tài khoản thành công!" khi tất cả các trường đều hợp lệ cùng một lúc."""
from collections import Counter

# 1. Hàm kiểm tra Username (Giữ nguyên - Rất tốt)
def ktra_username(username):
    if 5 <= len(username) <= 15 and username.isalnum():
        return True
    return False
    
# 2. Hàm kiểm tra Email (Sửa lỗi typo biến dic)
def ktra_email(email):
    dic_email = dict(Counter(email))
    
    # Chặn lỗi nếu email không có ký tự '@' hoặc ' ' để tránh nổ lỗi KeyError
    if "@" not in dic_email or " " in dic_email:
        return False
        
    if dic_email["@"] != 1 or "@gmail.com" not in email:
        return False
    return True
    
# 3. Hàm kiểm tra Mật khẩu (Sửa lỗi typo biến digti và cú pháp hàm all)
def ktra_mk(mk):
    if len(mk) < 8:
        return False
    upper, lower, digit, special = False, False, False, False
    for char in mk:
        if char.isupper():
            upper = True
        if char.islower():
            lower = True
        if char.isdigit():
            digit = True
        if char in '!@#$%^&*':
            special = True
    # Hàm all() cần nhận vào một iterable
    return all([upper, lower, digit, special])

# --- LUỒNG CHƯƠNG TRÌNH CHÍNH (Sửa lỗi thụt lề và gọi hàm) ---
while True:
    username = input("Nhập user_name (5-15 ký tự, chỉ gồm chữ và số): ").strip()
    if not ktra_username(username):
        print("❌ Vui lòng nhập lại username hợp lệ!")
        continue
    
    while True:
        email = input("Nhập email đầy đủ (ví dụ: abc@gmail.com): ").strip()
        if not ktra_email(email): # Sửa từ 'if' thành 'if not'
            print("❌ Vui lòng nhập lại email đúng định dạng .......@gmail.com và không chứa khoảng trắng!")
            continue
            
        while True:
            print("\n🔒 Lưu ý mật khẩu: Dài tối thiểu 8 ký tự, có ít nhất 1 chữ HOA, 1 chữ thường, 1 số, và 1 ký tự [!@#$%^&*]")
            mk = input("Nhập mật khẩu: ").strip()
            if not ktra_mk(mk): # Bổ sung truyền tham số (mk)
                print("❌ Vui lòng nhập lại mật khẩu đúng quy định!")
                continue
            break # Thoát vòng lặp mật khẩu
        break # Thoát vòng lặp email
    break # Thoát vòng lặp username



















"""Project 3: Máy mã hóa văn bản bảo mật (Caesar Cipher Processor)
Yêu cầu hệ thống:
Chương trình yêu cầu người dùng chọn 1 trong 2 chế độ: 1 - Mã hóa, 2 - Giải mã, sau đó nhập một chuỗi văn bản và một số nguyên k (khóa dịch chuyển).
Quy tắc xử lý văn bản:
Nếu chọn Mã hóa: Dịch chuyển mỗi ký tự chữ cái trong văn bản tiến về phía sau k vị trí trong bảng chữ cái (vòng tròn từ z lại quay về a, từ Z lại quay về A).
Nếu chọn Giải mã: Dịch chuyển ngược lại phía trước k vị trí.
Điều kiện bắt buộc: Giữ nguyên toàn bộ các ký tự không phải chữ cái (khoảng trắng, số, dấu câu) ở đúng vị trí cũ, không được biến đổi chúng.
In ra chuỗi văn bản kết quả cuối cùng sau khi biến đổi."""
def mahoa_giaima(strg,k,choice):
    if len(strg)==0:
        return strg
    new=[]
    m=k if choice=='1' else -k
    for char in strg:
        if char.isalpha():
            #!Tự viết mã nhưng không giải thích được tại sao đúng ?????
            ma=ord(char)+m%26-26 if (ord(char)<=90 and ord(char)+m%26 > 90) or ord(char)+m%26>122 else ord(char)+m%26
            new.append(chr(ma))
        else:
            new.append(char)
    
    return "".join(new)
choice=input("1. Mã hoá | 2.Giải mã: ")
print(mahoa_giaima("ABZzyk,. ?",10,choice))


#!HOẶC
def mahoa_giaima(strg,k,choice):
    if len(strg)==0:
        return strg
    new=[]
    m=k if choice=='1' else -k
    for char in strg:
        if char.isupper():
            ma=(ord(char)-ord("A")+m)%26+ord("A")
            new.append(chr(ma))
        elif char.islower():
            ma=(ord(char)-ord("a")+m)%26+ord("a")
            new.append(chr(ma))
        else:
            new.append(char)
    
    return "".join(new)
choice=input("1. Mã hoá | 2.Giải mã: ")
print(mahoa_giaima("ABZzyk,. ?",10,choice))




















"""Project 6: Hệ thống Bỏ phiếu bầu cử chống gian lận (Secure Voting System)
Yêu cầu hệ thống:
Chương trình giả lập một phòng bỏ phiếu điện tử. Người vào bỏ phiếu phải nhập Mã cử tri và Tên ứng cử viên mà họ muốn bầu.
Quy tắc kiểm soát dữ liệu:
Mỗi  Mã cử tri  chỉ được phép bỏ phiếu đúng 1 lần duy nhất trong toàn bộ chương trình. Nếu một Mã cử tri đã tồn tại trong hệ thống mà cố tình nhập lại, chương trình phải từ chối ghi nhận phiếu, in ra cảnh báo "Cử tri này đã bỏ phiếu, hành vi gian lận!" và tiếp tục cho người tiếp theo bỏ phiếu.
Nếu ứng cử viên được nhập chưa từng có ai bầu trước đó, hệ thống phải tự động thêm ứng cử viên này vào danh sách theo dõi.
Khi nhập mã lệnh kết thúc cuộc bầu cử, chương trình phải in ra: Tổng số phiếu hợp lệ, số phiếu cụ thể của từng ứng cử viên, và tuyên bố người trúng cử (người có nhiều phiếu nhất).
"""
voters = {"V101", "V102", "V105", "V110", "V123"}
# Cấu trúc: { "Tên ứng cử viên": Số phiếu hiện tại }
candidates = {
    "Nguyen Van A": 14,
    "Tran Thi B": 15,
    "Le Quang C": 9
}
def ds():
    for index,ten_ung_cu in enumerate(candidates,1):
        print(f"{index}.{ten_ung_cu}")
voted=set()
while True:
    choice=input("1.Bầu cử | 2.Kết thúc bầu cử: ").strip()
    if choice=='1':
        print("Nhập mã cử tri và Tên ứng cử viên")
        ma_cu_tri="V"+ input("Nhập mã cử tri (V***):V")
        if ma_cu_tri not in voters:
            print("Mã cử tri không tồn tại")
            continue
        elif ma_cu_tri in voted:
            print("Cử tri đã bầu cử")
            continue
        ds()
        ten_ung_cu=input("Nhập tên ứng cử viên: ").strip().title()
        if ten_ung_cu:
            voted.add(ma_cu_tri)
            candidates[ten_ung_cu]=candidates.get(ten_ung_cu,0)+1
    elif choice=='2':
        break
phieu_bau_max=max(candidates.values())
trung_cu=[per for per,phieu in candidates.items() if phieu==phieu_bau_max]
print(trung_cu)

















'''Project 8: Trình theo dõi và Phân bổ tài chính cá nhân (Finance Ledger)
Yêu cầu hệ thống:
Chương trình quản lý một danh sách các lịch sử giao dịch. Mỗi giao dịch gồm các thông tin bắt buộc: Ngày tháng, Số tiền (Số dương là tiền thu vào, Số âm là tiền chi ra), và Hạng mục mục đích (Ví dụ: "Ăn uống", "Lương", "Mua sắm").
Hệ thống phải thực hiện các chức năng báo cáo sau:
Tính tổng số tiền đã thu vào, tổng số tiền đã chi ra, và số dư hiện tại trong tài khoản.
Thống kê xem hạng mục chi tiêu nào đang tiêu tốn nhiều tiền nhất của người dùng và chiếm bao nhiêu phần trăm tổng số tiền đã chi ra.
In ra lịch sử các giao dịch được lọc riêng theo một Hạng mục cụ thể do người dùng yêu cầu.'''
finance_ledger = [
    {"date": "2026-05-01", "amount": 15000000, "category": "Lương"},
    {"date": "2026-05-02", "amount": -120000,   "category": "Ăn uống"},
    {"date": "2026-05-03", "amount": -3500000,  "category": "Mua sắm"},
    {"date": "2026-05-04", "amount": 500000,    "category": "Freelance"},
    {"date": "2026-05-05", "amount": -450000,   "category": "Ăn uống"}
]

def thong_tin():
    thu,chi=0,0
    thu_ds,chi_ds={},{}
    hang_muc=[]

    for ls in finance_ledger:
        cat=ls["category"]
        
        if ls["amount"]>0:
            thu+=ls["amount"]
            thu_ds[cat]=thu_ds.get(cat,0)+ls["amount"]
        else:
            hang_muc.append(cat)
            tien_chi=abs(ls["amount"])
            chi+=tien_chi
            chi_ds[cat]=chi_ds.get(cat,0)+tien_chi
            
    if thu_ds:
        thu_max=max(thu_ds.values())
        cat_thu_max=[{cat:f"{amt:,}"} for cat,amt in thu_ds.items() if amt==thu_max]
        
    if chi_ds:
        chi_max=max(chi_ds.values())
        cat_chi_max=[{cat:f"{amt:,}"} for cat,amt in chi_ds.items() if amt==chi_max]
        
    return thu, chi, thu-chi, cat_thu_max, cat_chi_max, hang_muc, chi_ds
    
while True:
    print(finance_ledger)
    thu,chi, tong, cat_thu_max, cat_chi_max, hang_muc, chi_ds = thong_tin()

    while True:
        choice=input("1.Số dư | 2.Tiền thu | 3.Tiền chi | 4.Thêm giao dịch | 5.Thu/chi theo hạng mục: ")

        if choice=='1':
            print(f"Số dư hiện tại: {tong:,}")

        elif choice=='2':
            if cat_thu_max:
                print(f"Tổng thu nhập: {thu:,} VNĐ")
                print(cat_thu_max)
            else:
                print("Chưa có thu nhập")

        elif choice=='3':
            if cat_chi_max:
                print(f"Tổng chi tiêu: {chi:,} VNĐ")
                print(cat_chi_max)

            else:
                print("Chưa có chi tiêu")

        elif choice=='4':
            ngay=input("Nhập ngày: ")
            thang=input("Nhập tháng: ")
            nam=input("Nhập năm: ")
            date=f"{nam}-{thang.zfill(2)}-{ngay.zfill(2)}"
            thu_chi=input("1.Thu nhập | 2.Chi tiêu: ")
            amount=int(input("Nhập tiền chi tiêu: "))
            category=input("category: ")
            if thu_chi=="2":
                amount=-amount
            finance_ledger.append({"date":date,"amount":amount,"category":category.capitalize()})
            break

        elif choice=='5':
            print(hang_muc)
            cat=input("Nhập hạng mục chi: ").strip().capitalize()
            print(f"{chi_ds[cat]:,}")
        else:
            print('không có lựa chọn.')

















"""Project 10: Hệ thống Đặt chỗ & Quản lý phòng vé (Cinema Seat Booking System)
Yêu cầu hệ thống:
Quản lý một sơ đồ phòng chiếu phim được mô tả bằng một ma trận kích thước 5×6 (5 hàng, 6 cột). Vị trí ghế trống hiển thị ký tự 0, ghế đã được đặt hiển thị ký tự X.
Hệ thống cung cấp các chức năng cốt lõi:
Hiển thị sơ đồ phòng chiếu phim hiện tại ra màn hình theo cấu trúc hàng - cột rõ ràng.
Tính năng đặt ghế: Người dùng nhập vị trí ghế (Ví dụ: hàng 3, ghế 4). Nếu ghế trống (0), hệ thống chuyển trạng thái thành đã đặt (X) và thông báo đặt thành công kèm giá vé. Nếu ghế đã là X, thông báo ghế đã có người ngồi và từ chối giao dịch.
Tính năng thống kê: In ra tổng số ghế còn trống, tổng số vé đã bán được, và tổng doanh thu phòng vé hiện tại thu được là bao nhiêu.
"""
matrix = [[0 for _ in range(11)] for _ in range(11)]

def hien_thi():
    # In tiêu đề số ghế (1 đến 9)
    print("\nSTT|  " + " ".join([f"{i:<3}" for i in range(1, len(matrix[0]) + 1)]))

    # In từng hàng ghế kèm chữ cái đại diện
    for index, hang in enumerate(matrix):
        chu_cai = chr(index + ord("A"))
        # Biến đổi các số 0, 1 thành ký tự [0], [1] nhìn cho đẹp mắt
        hang_hien_thi = [f"[{status}]" for status in hang]
        print(f" {chu_cai} | {' '.join(hang_hien_thi)}")
    print("\n[1]: Ghế đã đặt | [0]: Ghế còn trống")

while True:
    hien_thi()
    
    # 1. Chọn hàng và kiểm tra hợp lệ
    hang_nhap = input("Chọn hàng (A-K) hoặc gõ 'EXIT' để thoát: ").strip().upper()
    if hang_nhap == 'EXIT':
        break
        
    if len(hang_nhap) != 1 or not ("A" <= hang_nhap <= "K"):
        print("❌ Hàng không hợp lệ! Vui lòng chọn từ A đến K.")
        continue
        
    index_hang = ord(hang_nhap) - ord("A")
    
    # Kiểm tra xem hàng đó đã hết sạch ghế chưa
    if all(ghe == 1 for ghe in matrix[index_hang]):
        print(f"❌ Hàng {hang_nhap} đã hết sạch ghế trống!")
        continue

    # 2. Nhập danh sách ghế muốn đặt
    print(f"--- Bạn đang chọn hàng {hang_nhap} ---")
    ghe_input = input("Nhập các số ghế muốn chọn (ví dụ: 1, 2, 3): ").strip()
    
    try:
        # Cắt chuỗi bằng dấu phẩy và chuyển thẳng thành list số nguyên
        # Cách này xử lý được cả số có nhiều chữ số như 10, 11 và tự động bỏ khoảng trắng
        danh_sach_ghe = [int(g.strip()) for g in ghe_input.split(",") if g.strip().isdigit()]
        
        if not danh_sach_ghe:
            print("❌ Vui lòng nhập số ghế hợp lệ!")
            continue
            
        # Kiểm tra điều kiện: Số ghế phải từ 1 đến 9
        if any(g < 1 or g > len(matrix[index_hang]) for g in danh_sach_ghe):
            print(f"❌ Số ghế không tồn tại! (Chỉ chọn từ 1 đến {len(matrix[index_hang])})")
            continue
            
        # Kiểm tra xem có ghế nào trong danh sách trúng vị trí đã đặt (số 1) chưa
        if any(matrix[index_hang][g - 1] == 1 for g in danh_sach_ghe):
            print("❌ Gian lận hoặc trùng lặp! Có ghế trong danh sách bạn chọn đã có người đặt.")
            continue
            
        # 3. Tiến hành đặt ghế (Cập nhật ma trận)
        
        print("Ghế bạn đã chọn:")
        print("\nSTT|  " + " ".join([f"{i:<3}" for i in range(1, len(matrix[0]) + 1)]))
        hang_hien_thi=["[x]" if i+1 in danh_sach_ghe else '[0]' for i in range(len(matrix[index_hang]))]
        print(f" {hang_nhap} | {' '.join(hang_hien_thi)}")
        thanh_toan=input("1.Thanh toán | 2.Quay lại: ")
        if thanh_toan=='2':
            continue
        for g in danh_sach_ghe:
            matrix[index_hang][g - 1] = 1
            
        #print(f"🎉 Đặt thành công các ghế: {danh_sach_ghe} tại hàng {hang_nhap}!")
        
    except ValueError:
        print("❌ Lỗi: Vui lòng chỉ nhập số nguyên phân tách bằng dấu phẩy!")


















"""Project 9: Trò chơi Cờ Caro thu nhỏ trên Terminal (Console Tic-Tac-Toe Game)
Yêu cầu hệ thống:
Giả lập bàn cờ 3×3 hiển thị trực quan trên màn hình. Hai người chơi X và O luân phiên nhập tọa độ (dòng, cột) từ bàn phím để đi nước cờ của mình.
Quy tắc xử lý ma trận bàn cờ:
Hệ thống phải từ chối và bắt nhập lại nếu tọa độ nằm ngoài phạm vi bàn cờ, hoặc ô đó đã được đánh trước đó.
Ngay sau mỗi nước đi, hệ thống phải rà soát toàn bộ ma trận bàn cờ để kiểm tra điều kiện thắng: Có 3 ký tự giống nhau nằm liên tiếp trên cùng một hàng ngang, cùng một cột dọc, hoặc trên hai đường chéo (chính và phụ).
Kết thúc trò chơi và tuyên bố người thắng cuộc ngay lập tức khi điều kiện thắng được thỏa mãn, hoặc tuyên bố Hòa khi tất cả 9 ô đều đã bị lấp đầy mà không có ai thắng.
"""
matrix = [["" for _ in range(10)] for _ in range(10)]
x_choice=[f"{x}" for x in range(1,len(matrix[0])+1)]
y_choice=[f"{y}" for y in range(1,len(matrix)+1)]

def hien_thi():
    print(f"     {"   ".join(x_choice)}")
    print(f"   +{"---+"*len(matrix[0])}")
    for index,hang in enumerate(matrix):
        char=chr(ord("A")+index)
        print(f"{char}  |{"   |"*len(matrix[0])}")
        print(f"   +{"---+"*len(matrix[0])}")

def win(y,x,quan_co):
    huong=[(0,1),(1,0),(1,1),(1,-1)]
    for dy,dx in huong:
        chuoi_lien_tiep=1
        for i in range(1,5):
            ny,nx=y+dy*i,x+dx*i
            if 0<=ny<=len(matrix)-1 and 0<=nx<=len(matrix[0]) and matrix[ny][nx]==quan_co:
                chuoi_lien_tiep+=1
            else:
                break
        for i in range(1,5):
            ny,nx=y-dy*i,x-dx*i
            if 0<=ny<=len(matrix)-1 and 0<=nx<=len(matrix[0]) and matrix[ny][nx]==quan_co:
                chuoi_lien_tiep+=1
            else:
                break
    if chuoi_lien_tiep>=5:
        return True

luot_choi="X"
lan_danh=0
lan_danh_max=len(matrix)*len(matrix[0])

while lan_danh<=lan_danh_max:
    hien_thi()
    y=input(f"Nhập {luot_choi} toạ độ tung độ (A,B,..,Y): ").strip().upper()
    if not y or not("A"<=y<=chr(ord("A")+len(matrix)-1)):
        print("Hàng nhập không hợp lệ. Vui lòng nhập lại")
        toa_do_y=ord(y)-ord("A")
    try:
        x=int(input(f"Nhập {luot_choi} toạ độ hoành độ (1,2,..,25): ").strip())
        if not(len(matrix[0])>=x>0):
            print(f"Chỉ nhập số trong khoảng (1,{len(matrix[0])})")
        toa_do_x=x-1
        if matrix[toa_do_y][toa_do_x]!="":
            print("Ô chọn đã có cờ")
            continue
        matrix[toa_do_y][toa_do_x]=luot_choi
        lan_danh+=1

    except ValueError:
        print("Lỗi! Vui lòng nhập số nguyên. ")
        continue


    #Kiểm tra chiến thắng
    if win(toa_do_y,toa_do_x,luot_choi):
        hien_thi()
        print(f"Người chơi {luot_choi} chiến thắng.")

    #Kiểm tra hoà cờ
    if lan_danh==lan_danh_max:
        print("Hoà cờ")

    #Đổi cờ
    luot_choi="O" if luot_choi=="X" else "X"
