
#*Generator: là một iterator một dạng của iterable nhưng không thể tái sử dụng
#* nó không lưu trữ toàn bộ ở bộ nhớ mà sinh ra lần lượt
gene=(i for i in range(3))
for g in gene:
    print(g)


#* yield: trả về một generator
#yield (Generator) giống như một "Cuộn phim quay chậm" (bạn bấm Pause ở đâu thì lần sau bấm Play nó sẽ chạy tiếp từ đúng giây đó).
def cuon_phim_hanh_dong():
    print("[TẬP 1] - Trận chiến bắt đầu!")
    yield "Kết quả tập 1: Anh hùng thắng"  # <--- BẤM PAUSE LẦN 1 TẠI ĐÂY

    print("[TẬP 2] - Kẻ thù quay trở lại trả thù!")
    yield "Kết quả tập 2: Quái vật thắng"  # <--- BẤM PAUSE LẦN 2 TẠI ĐÂY
    
    print("[TẬP 3] - Trận chiến sinh tử cuối cùng!")
    yield "Kết quả tập 3: Hòa bình lập lại" # <--- BẤM PAUSE LẦN 3 TẠI ĐÂY

# Bước 1: Gọi hàm. Đúng như lý thuyết nói: "Những dòng lệnh sẽ không chạy ngay".
# Máy chỉ tạo ra một đối tượng generator (đĩa phim) nằm chờ.
dia_phim = cuon_phim_hanh_dong() 

# LẦN 1: Gọi next() -> Máy bắt đầu chạy vào trong hàm từ ĐẦU HÀM.
tap_1 = next(dia_phim)
print("-> Khách nhận được:", tap_1)
'''--- BẮT ĐẦU XEM PHIM ---
[TẬP 1] - Trận chiến bắt đầu!
-> Khách nhận được: Kết quả tập 1: Anh hùng thắng'''

# LẦN 2: Gọi next() tiếp
tap_2 = next(dia_phim)
print("-> Khách nhận được:", tap_2)
'''[TẬP 2] - Kẻ thù quay trở lại trả thù!
-> Khách nhận được: Kết quả tập 2: Quái vật thắng'''

#!Bạn cũng cần lưu ý thêm, nếu không có giá trị yield khi được gọi tiếp thì sẽ yield sẽ không  trả về bất cứ thứ gì
#!có nghĩa là None object cũng không được trả về






#* SEND:gửi giá trị vào trong generator
#* Cú pháp: generator.send(value)
def gen():
    for i in range(4):
        x = yield i
        print('value sent from you', x)
g = gen() # gán generator này cho biến g
next(g) # gọi hàm next để chạy lệnh yield "x = yield i"
        # 0
g.send('Kteam') # x vừa nãy khi gán cho biến yield giờ sẽ được gửi giá trị
                # value sent from you Kteam
g.send('Free education') # value sent from you Free education
next(g) # lần này ta không dùng send, mặc định giá trị gửi vào là None
        # value sent from you None

