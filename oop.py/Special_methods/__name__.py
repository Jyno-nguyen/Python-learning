
#? __name__ là 1 biến ẩn(special variable) - Python sẽ tự gán cho mỗi file.py khi file đó hoạt động
#? Giá trị của biến __name__ không cố định. Nó thay đổi tùy thuộc vào việc file đó tự chạy hay bị file khác gọi ké.

# __main__ là chuỗi đặc biệt do Python quy ước sẵn
# có nghĩa là luồng chính. file nào TRỰC TIẾP BẤM RUN thì __main__ sẽ đóng mác vào biến __name__

# File: toan_hoc.py
def tinh_tong(a, b):
    return a + b
# Phép so sánh bằng ở cuối file
if __name__ == "__main__": #!chạy trực tiếp 
    print("Test thử hàm: ", tinh_tong(5, 5))

# File: thuvien_game.py
# In thử xem giá trị __name__ của file này hiện tại là gì
print(f"[Bên trong thuvien_game.py] Biến __name__ đang có giá trị là: '{__name__}'")
if __name__ == "__main__": #!nếu chạy trong file khác được import thì __name__ sẽ khác __main__ nên dòng này sẽ không chạy
    print("Lệnh này CHỈ CHẠY khi bạn bấm nút RUN trực tiếp tại file thuvien_game.py!")

# File: __name__.py
import thuvien_game  
print(f"[Bên trong main.py] Biến __name__ đang có giá trị là: '{__name__}'")

#!Khi bấm run ở file __name__.py, VÌ IMPORT FILE CON NÊN NHỮNG GÌ CHẠY ĐƯỢC TRONG FILE CON SẼ CHẠY HẾT 
#-> [Bên trong thuvien_game.py] Biến __name__ đang có giá trị là: 'thuvien_game'
#-> [Bên trong main.py] Biến __name__ đang có giá trị là: '__main__'

#* Chức năng chính, tối cao và duy nhất của "công tắc" if __name__ == "__main__": là:
#* CHẶN không cho những đoạn code chạy thử (hoặc code vãng lai) tự động kích hoạt ngoài ý muốn khi file đó bị một file khác import vào.






#? import file.py


