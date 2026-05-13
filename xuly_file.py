#XỬ LÝ FILE TRONG PYTHON
#? Cấu trúc cơ bản
with open("test.txt", encoding="utf-8") as f:# as f:(ĐỊNH DẠNG) đặt tên biến để làm việc với file
                                            #! as: chỉ có tác dụng bên trong khối lệnh


    with open("nguon.txt", "r") as f_in, open("dich.txt", "w") as f_out:
        data = f_in.read()
        f_out.write(data)


#! with: tự động đóng file khi ra khỏi khối lệnh with, không phải đóng thủ công f.close()
#!Nếu không đóng file có thể không ghi được dữ liệu muốn thay đổi, file có thể bị khoá khi chạy trên chương trình khác, RÒ RỈ BỘ NHỚ, CHIẾM TÀI NGUYÊN LÀM CHƯƠNG TRÌNH CHẠY CHẬM
    d1=f.read()        # đọc toàn bộ file → 1 chuỗi 
    d2=f.readline()    # đọc 1 dòng
    d3=f.readlines()   # đọc tất cả dòng → trả về list 
    # File 10GB → readlines() load hết vào RAM → chết máy!
    # for line in f → chỉ load 1 dòng tại 1 thời điểm → an toàn!

with open("file_lon.txt", encoding="utf-8") as f: 
    for line in f:
        print(line)  # xử lý từng dòng, không tốn RAM, in ra từng dòng 1

print(d3)
#!Mode:
    #"r"   # read — chỉ đọc (mặc định)
    #"w"   # write — ghi mới (xóa hết nội dung cũ!)
    #"a"   # append — thêm vào cuối file
    #"r+"  # đọc và ghi
    #"rb"  # read binary — đọc file nhị phân (ảnh, video)
    #"wb"  # write binary — ghi file nhị phân

d1=f.read()     #!Khi đọc hết file con trỏ ở cuối
d2=f.readline() #!=> Rỗng
f.seek(0)       #!Reset con trỏ về đầy file rồi mới có thể đọc được tiếp
#! f.tell() trả về vị trí hiện tại của con trỏ



#! Luôn dùng encoding="utf-8" với tiếng Việt
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# "w" sẽ XÓA hết nội dung cũ!
with open("file.txt", "w") as f:
    f.write("abc")  # nội dung cũ mất hết!

# Dùng "a" nếu muốn giữ nội dung cũ
with open("file.txt", "a") as f:
    f.write("them vao cuoi")

# File không tồn tại + mode "r" → FileNotFoundError!
with open("khong_co.txt", "r") as f:  # lỗi ngay!
    pass

# File không tồn tại + mode "w"/"a" → tự tạo file mới ✅
with open("moi.txt", "w") as f:
    f.write("tao moi")

# r+ → con trỏ ở đầu file
with open("file.txt", "r+") as f:
    f.read()    # đọc được
    f.write("abc")  # ghi được

# a+ → con trỏ ở CUỐI file
with open("file.txt", "a+") as f:
    f.write("abc")   # thêm vào cuối
    f.seek(0)        # phải seek(0) mới đọc từ đầu được!
    f.read()         # đọc được


#!Xử lý file không tồn tại
try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File khong ton tai!")

#!Kiểm tra file trước khi mở:
import os
if os.path.exists("file.txt"):
    with open("file.txt", "r") as f:
        content = f.read()




#? write() và writelines()
# write() — ghi 1 chuỗi
with open("file.txt", "w") as f:
    f.write("Hello Jyno")      # ghi 1 chuỗi
    f.write("dong 2")          # ghi tiếp, không xuống dòng

# writelines() — ghi list các chuỗi
with open("file.txt", "w") as f:
    f.writelines(["Hello\n", "Jyno\n", "AI\n"])  # ghi cả list

# write() — nhận 1 chuỗi
f.write("Hello")        # ✅
f.write(["Hello"])      # ❌ TypeError — không nhận list!

# writelines() — nhận list/tuple các chuỗi
f.writelines(["Hello\n", "Jyno\n"])  # ✅
f.writelines("Hello")                # ✅ nhưng ghi từng ký tự!



#!MỞ FILE Ở THƯ MỤC KHÁC
# Cách 1: đường dẫn tuyệt đối (full path)
with open("/Users/nguyenvietha/Documents/test.txt", encoding="utf-8") as f:
    content = f.read()

# Cách 2: đường dẫn tương đối (relative path)
with open("../Jyno-code/test.txt", encoding="utf-8") as f:
    content = f.read()
# .. = lùi ra folder cha


 
