
#? all(): tất cả phải đúng
#? any(): chỉ cần một người đúng

#! Giá trị Falsy (Coi là Sai): Số 0, chuỗi rỗng "", danh sách rỗng [], từ điển rỗng {}, và giá trị None.
#! Giá trị Truthy (Coi là Đúng): Tất cả các giá trị còn lại (số khác 0, chuỗi có chữ, list có phần tử...).

print(all([1, 2, "Hello", [1, 2]])) # Kết quả: True (Vì không có cái nào trống/bằng 0)
print(any([0, "", [], 5]))          # Kết quả: True (Vì có số 5 gánh team)
print(all([1, 2, 0, 4]))            # Kết quả: False (Vì có số 0 là Falsy)

danh_ba = ["0912", "0988", "0345", "1234"]
tat_ca_hop_le = all(sdt.startswith("0") for sdt in danh_ba)# Đọc là: Kiểm tra xem TẤT CẢ các sdt có bắt đầu bằng "0" không
print(tat_ca_hop_le) # Kết quả: False (vì dính ông "1234")


diem = [7.5, 8.0, 9.5, 10.0, 6.0]
co_thu_khoa = any(d == 10.0 for d in diem)
print(co_thu_khoa) # Kết quả: True

#! all(): chỉ trả về false nếu tìm được 1 phần tử sai nhưng vì ds rỗng nên không tìm được phần tử nào sai
print(any([]))  # Kết quả: False
print(all([]))  # Kết quả: True  <-- Ơ KÌA?!


#* Tìm số nguyên tố
n=int(input())
songuyen=n>1 and not any(n%i==0 for i in range(2,int(n**0.5)+1))
songuyen=n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))
