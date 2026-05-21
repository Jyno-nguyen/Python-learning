"""TASK6: Khôi phục mảng từ khoảng cách
Tìm tất cả các đoạn danh sách con liên tiếp (subarray) trong một mảng số nguyên có tổng các phần tử đúng bằng số mục tiêu K """
ds = [3, 4, 7, 2, -3, 1, 4, 2]
k=7
tong_hien_tai=0
ky_uc_vi_tri={0:[-1]}
for i in range(len(ds)):
    tong_hien_tai+=ds[i]
    tong_can_tim=tong_hien_tai-k
    if tong_can_tim in ky_uc_vi_tri:
        cac_vi_tri=ky_uc_vi_tri[tong_can_tim]
        for vi_tri in cac_vi_tri:
            print(ds[vi_tri+1:i+1])
    if tong_hien_tai in ky_uc_vi_tri:
        ky_uc_vi_tri[tong_hien_tai].append(i)
    else:
        ky_uc_vi_tri[tong_hien_tai]=[i]
"""Giải thích
    Bước 1: phai = 0 (Số 3)
Tổng tích lũy hiện tại: tong_hien_tai = 3. (Bạn đang ở cách gốc 3 mét).
Bạn tìm vạch: 3-7=-4.
Tra sổ xem có vạch -4 không? → Không có.
Ghi vào sổ: Vạch 3 mét nằm ở vị trí 0.
Sổ hiện tại: {0: [-1], 3: [0]}

    Bước 2: phai = 1 (Số 4)
Tổng tích lũy tăng lên: 3+4= 7. (Bạn đang cách gốc 7 mét).
Bạn tìm vạch: 7-7= 0.
Tra sổ xem có vạch 0 không? → CÓ! Vạch 0 nằm ở vị trí -1.
Bạn bốc mảng con từ vị trí (-1 + 1) đến 1, tức là arr[0:2] → [3, 4]. (Tìm được mảng thứ nhất!)
Ghi vào sổ: Vạch 7 mét nằm ở vị trí 1.
Sổ hiện tại: {0: [-1], 3: [0], 7: [1]}

    Bước 3: phai = 2 (Số 7)
Tổng tích lũy tăng lên: 7+7= 14. (Bạn đang cách gốc 14 mét).
Bạn tìm vạch: 14-7= 7.
Tra sổ xem có vạch 7 không? → CÓ! Vạch 7 nằm ở vị trí 1 (do bước trước vừa ghi).
Bạn bốc mảng con từ vị trí (1 + 1) đến 2, tức là arr[2:3] → [7]. (Tìm được mảng thứ hai!)
Ghi vào sổ: Vạch 14 mét nằm ở vị trí 2.
Sổ hiện tại: {0: [-1], 3: [0], 7: [1], 14: [2]}

    Bước 4: phai = 3 (Số 2)
Tổng tăng lên: 14+2= 16.
Tìm vạch: 16-7=9→ Sổ không có vạch 9.
Ghi vào sổ: Vạch 16 mét ở vị trí 3.

    Bước 5: phai = 4 (Số -3) → KHÚC ẢO DIỆU ĐÂY
Bạn gặp số âm, tổng tích lũy bị giảm xuống: 16+(-3)= 13.
Tìm vạch: 13-7=6→ Sổ không có vạch 6.
Ghi vào sổ: Vạch 13 mét ở vị trí 4.

    Bước 6: phai = 5 (Số 1)
Tổng tăng lên: 13+1= 14. (Ô kìa, tổng lại quay về số 14 giống bước 3!).
Bạn tìm vạch: 14-7= 7.
Tra sổ xem có vạch 7 không? → CÓ! Sổ báo vạch 7 nằm ở vị trí 1.
Bạn bốc mảng con từ vị trí (1 + 1) đến 5, tức là arr[2:6] → [7, 2, -3, 1]. (Tìm được mảng thứ ba! Có chứa số âm ngon lành)."""




"""Cộng hai số lớn dạng chuỗi
Vì bộ nhớ máy tính có giới hạn, hãy nhập vào 2 số nguyên cực kỳ lớn dưới dạng Chuỗi (Ví dụ số có 50 chữ số)
Hãy dùng vòng lặp mô phỏng lại phép toán đặt tính cộng tiểu học (cộng từng hàng đơn vị và nhớ sang hàng kế tiếp) để trả về chuỗi tổng chính xác. 
"""
so1='123456789123456789123456789123456789123456789123456789'
so2='23174351284567123452354'
kq=[]
biennho=0
if len(so1)>len(so2):
    so2=f"{so2:0>{len(so1)}}"
elif len(so1)<len(so2):
    so1=f"{so1:0>{len(so2)}}"
for i,j in zip(so1[::-1],so2[::-1]):
    tong=int(i)+int(j)+biennho
    kq.append(str(tong%10))
    biennho=tong//10
if biennho>0:
    kq.append(str(biennho))
print(''.join(kq)[::-1])


#! import thư viện itertools để không phải thêm số 0 cho số ngắn hơn
from itertools import zip_longest
so1 = '999999999999999999999999' # Số ngắn
so2 = '1111'                   # Số dài lệch hẳn
kq = []
biennho = 0
# Dùng zip_longest để chuỗi ngắn hơn được tự động bù số '0' vào bên trái (sau khi đảo ngược)
for i, j in zip_longest(so1[::-1], so2[::-1], fillvalue='0'):
    tong = int(i) + int(j) + biennho
    kq.append(str(tong % 10))
    biennho = tong // 10
if biennho > 0:
    kq.append(str(biennho))
print(''.join(kq)[::-1])