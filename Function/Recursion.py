
#*Đệ quy: Gọi một hàm trong chính nó
def cal_sum(lst):
    if not len(lst): #Nếu không còn phần tử nào trả về 0
        return 0 #!Vì return 0 nên không cộng được list chuỗi và [[][][][]]
    else:
        return lst[0]+cal_sum(lst[1:]) #Lần lượt sự thay đổi: #!Chiều đi xuống (Bóc tách và đứng đợi)
                                       # 1+[2,3,4,5]
                                       # + 2 + [3,4,5] #!Vì mỗi lần chạy đều + cal_sum(lst[1:]): TỨC CÁI MỚI TẠO RA LUÔN ĐƯỢC CỘNG VÀO CÁI CŨ
                                       # + 3 + [4,5]
                                       # + 4 + [5]
                                       # + 5 + []
                                       # 0 
                                       #!Chiều đi lên: vì mỗi lần tạo ra một số (1,2,3,4,5,0) các số phải đứng đợi đến khi hoàn thành cal_sum rồi mới tiền hành cộng
                                       #0+5=5+4=9+3=12+2=14+1=15 
print(cal_sum([1,2,3,4,5]))

#!HOẶC
def call_sum(lst):
    return 0 if not lst else lst[0]+call_sum(lst[1:])
call_sum([1,2,3,4])

#!List n phần tử thì có (n+1) lần return ta có thể giảm xuống n bằng cách: KHÔNG ÁP DỤNG CHO LIST RỖNG
def call_sum(lst):
    return lst[0] if len(lst)==1 else lst[0]+call_sum(lst[1:])
call_sum([1,2,3,4])
call_sum([[1,2],[3,4]]) # lần 1: lst[0]=[1,2]+[[3,4]]
                        # lần 2: len([[3,4]])=1 => lst[0]=[3,4] và kết thúc chiều đi xuống
                        # [1,2]+[3,4]=[1,2,3,4]
                        #! Tương tự với list các chuỗi

#!PACKING LIST: CŨNG KHÔNG ĐƯỢC DÙNG CONTAINER RỖNG
def call_sum(lst):
    idx0, *r=lst #idx0,*r cần tối thiểu 1 phần tử gán cho idx0
    return idx0 if not r else idx0+call_sum(r)
call_sum([[1,2],[4,5]]) # lần 1: idx0=[1,2], *r=[[4,5]]
                        # lần 2: idx0=[4,5], *r=0 => kết thúc chiều đi xuống
                        # [1,2]+[3,4]=[1,2,3,4]
                        #! Tương tự với list các chuỗi

#!MỖI BÀI TOÁN TRÊN ĐỀU CÓ 1 TRONG 2 NHƯỢC ĐIỂM: LIST RỖNG LỖI, LIST KÝ TỰ, LIST CÁC LIST CON LỖI
#*THÊM ĐIỀU KIỆN ĐẦU VÀO
def call_sum(lst):
    if not lst:
        return 0
    return lst[0] if len(lst)==1 else lst[0]+call_sum(lst[1:])







#*HOẶC DÙNG SUM() ĐỂ CỘNG LIST CÁC LIST: sum(iterable,start)
def my_sum(iterable,start):
    total=start #! total mang kiểu dữ liệu của start
    for element in iterable:
        total+=element
    return total

sum([[3,4],[5,6],[1,2]],[]) #[3, 4, 5, 6, 1, 2]
                            #! Nhớ phải bắt đầu bằng 1 list rỗng
sum([],[])




