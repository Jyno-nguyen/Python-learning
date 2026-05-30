
#* TASK1: TÌM CHUỖI CON ĐỐI XỨNG DÀI NHẤT
s = "hRACECARef"
chuoi_max = ""
# Vòng lặp i chọn điểm bắt đầu, j chọn điểm kết thúc
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1): #!Lặp quá nhiều chuỗi quá dài dẫn đến treo máy
        dao = s[i:j]
        # Kiểm tra đối xứng bằng cách đảo ngược chuỗi [::-1]
        if dao == dao[::-1]:
            # Nếu chuỗi con này dài hơn kỷ lục cũ thì ghi nhận
            if len(dao) > len(chuoi_max):
                chuoi_max = dao
print(chuoi_max) 


#!CÁCH TỐI ƯU HƠN
s = "hRACECARef"
chuoi_max = ""
for i in range(len(s)):
    trai,phai=i,i #!Duyệt từng chữ 
    while trai>=0 and phai<len(s) and s[trai]==s[phai]:
        #!Vòng lặp duyệt qua từng chữ, rồi mở rộng sang 2 bên nếu chuỗi đối xứng có tâm là khoảng trắng thì sẽ bị sai
        if len(s[trai:phai+1])>len(chuoi_max):
            chuoi_max=s[trai:phai+1]
        trai-=1
        phai+=1
    trai,phai=i,i+1 #!Duyệt qua từng cặp chữ rồi mới mở rộng ra, tâm là khoảng tắng ở giữa
    while trai>=0 and phai<len(s) and s[trai]==s[phai]:
        #!Xét xem cặp chữ giống nhau thì mới mở rộng sang 2 bên
        if len(s[trai:phai+1])>len(chuoi_max):
            chuoi_max=s[trai:phai+1]
        trai-=1
        phai+=1


#* TASK2: LẬP MA TRẬN VUÔNG NxN VỚI SỐ TĂNG DẦN TỪ NGOÀI VÀO TRONG THEO CHIỀU KIM ĐỒNG HỒ
n=int(input("Nhập ma trận vuông nxn: "))
matrix=[[0 for _ in range(n)] for _ in range(n)] 
top,bottom=0,n-1
left,right=0,n-1
current_num=0
while top<=bottom and left<=right: #*Cần phải có dấu bằng nếu trường hợp ma trận lẻ thì số chính giữa xảy ra khi top=bottom=left=right=(n-1)/2
    for i in range(left,right+1): 
        matrix[top][i]=current_num 
        current_num+=1
    top+=1
    for i in range(top,bottom+1): 
        matrix[i][right]=current_num 
        current_num+=1
    right-=1
    if top<=bottom:
        for i in range(right,left-1,-1):  #![right, left -1 - (-1)]
            matrix[bottom][i]=current_num
            current_num+=1
        bottom-=1
    if left<=right:
        for i in range(bottom,top-1,-1):   #![bottom, top -1 - (-1)]
            matrix[i][left]=current_num
            current_num+=1
        left+=1
print("\nKết quả của Matrix")
for row in matrix:
    final_row=[f"{num:0>2d}" for num in row]
    print(" ".join(final_row))

#!f-string:
          #*{num:02d}: 0 là ký tự lấp đầy, 2 là độ rộng tối thiểu, d là định dạng số nguyên Demacial 
          #!n=1.234{n:08.5f} => 01.23400 (. cũng tính là 1 ký tự)
          #!n=1.234{n:0<8.2f} => 1.230000 (. cũng tính là 1 ký tự)
          #!{1243143:,} =>1,243,143
          #!{1234.456:0<13,.4f} "1,234.4600000"
n = int(input('Enter size of matrix: '))
dx, dy = 0,1
x, y = 0,0
spiral_matrix = [[None] * n for j in range(n)]
for i in range(n ** 2):
    spiral_matrix[x][y] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and spiral_matrix[nx][ny] == None:
        x, y = nx, ny
    else:
        dx, dy = dy, -dx
        x,y = x + dx, y + dy
for row in spiral_matrix:
    final= [f"{num:0>2d}" for num in row ]
    print(" ".join(final))





#* TASK3: XOAY MA TRẬN THEO CHIỀU KIM ĐỒNG HỒ 
matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix_=[[matrix[k][i] for k in range(len(matrix)-1,-1,-1)] for i in range(len(matrix[0]))]
print(matrix_)
#!Cách này tạo ra một ma trận mới sẽ làm tốn dung lượng

#!Tìm cách thay đổi luôn trên ma trận cũ nhưng chỉ áp dụng với ma trận vuông
import copy as c
matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix_goc=c.deepcopy(matrix) #!vẫn tốn do tạo thêm 1 cái ma trận copy
for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[i][j]=matrix_goc[len(matrix)-j-1][i]
print(matrix)
#! Tạo ma trận hoán vị rồi sau đó đảo ngược
for i in range(len(matrix)):
    for j in range(i+1,len(matrix)):
        #!Tạo ma trận hoán vị
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
for i in range(len(matrix)):
    matrix[i]=matrix[i][::-1]




#* TASK4: TÍNH RA SỐ TIỀN TỐI THIỂU THEO CÁC MỆNH GIÁ KHI NHẬP SỐ TIỀN
#!Thuật toán tham lam, luôn xét từ số tiền lớn nhất trước
#!Chỉ thoả mãn khi mà mệnh giá tờ[i] luôn lớn hơn ít nhất 2 lần tờ[i+1]
#!Ví dụ [400,300,100] khi đổi 600 thì sẽ lấy [400:1 và 100:2] nhưng [300:2] thì mới thoả mãn lấy ra ít nhất
ds=[500000, 200000, 100000, 50000, 20000, 10000, 5000,1000]
tien=int(input())
for gia in ds:
    if tien>=gia:
        so=tien//gia
        tien%=gia
        print(f"{gia}:{so}")

ds_te=[400,300,100]
tien=int(input())
so_to_tien_min=99999
to_4k = 0
to_3k = 0
to_1k = 0
for to_400 in range((tien//400)+1):
    for to_300 in range((tien//300)+1):
        for to_100 in range((tien//100)+1):
            tong_tien=400*to_400+300*to_300+100*to_100
            if tien==tong_tien:
                so_to_tien=to_400+to_300+to_100
                if so_to_tien<so_to_tien_min:
                    so_to_tien_min=so_to_tien
                    to_4k = to_400
                    to_3k = to_300
                    to_1k = to_100



#* TASK5: CHO DANH SÁCH SỐ NGUYÊN CÓ N-1 PHẦN TỬ, THIẾU 1 PHẦN TỬ TRONG SỐ TỪ 1 ĐẾN N
#* TÌM PHẦN TỬ ĐÓ
ds = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 
n = len(ds) + 1
tong_ly_thuyet = int(n * (n + 1) / 2)
sobithieu = tong_ly_thuyet - sum(ds)




#* TASK6: Khôi phục mảng từ khoảng cách: Tìm tất cả các đoạn danh sách con liên tiếp (subarray) trong một mảng số nguyên có tổng các phần tử đúng bằng số mục tiêu K.
ds = [ 4, 5, 6, 7, 8, 13, 20, 15, 8, 9, 10, 16] 
K=43
trai=0
tong_hien_tai=0
for phai in range(len(ds)):
    tong_hien_tai+=ds[phai]
    while trai<=phai and tong_hien_tai>K:
        tong_hien_tai-=ds[trai]
        trai+=1
    if tong_hien_tai==K:
        print(ds[trai:phai+1])
#!Cách trên CHỈ ĐÚNG VỚI SỐ DƯƠNG, GẶP SỐ ÂM LÀ SAI

#!
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


                





    


