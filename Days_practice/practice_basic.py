
#*TASK1: Tìm trong list file chuyển file .png thành .imag
lst = ["anh.png", "doc.txt", "bai_tap.py", "ha.png", "jino.png"]
new=[f.rsplit('.',1)[0]+".imag" for f in lst if f.endswith(".png")] #!Cắt từ bên phải sang(rsplit) lấy phần tử trước dấu chấm[0]




#*TASK2 Lấy ra phần tử chung của 2 list
lst1=[1,2,3,4,5,1,1]
lst2=[1,1,2]
lst3=list(set(lst1) & set(lst2)) #Nhanh nhất

phantuchung=set(lst1).intersection(set(lst2))



#*TASK3: Tạo ra ma trận vuông nxn với số nguyên tăng dần từ 1
n=int(input())
matrix=[i+n*m for i in range(1,n+1) for m in range(0,n)]
#[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


#*TASK4: Kiểm tra số nguyên
n=int(input())
if n<=1:
    print(False)
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print(False)
        break
else:
    print(True)


#* TASK5: Ma trận đơn vị. Nhập vào số nguyên N. Tạo ra một ma trận vuông N×N có các phần tử trên đường chéo chính bằng 1, các phần tử còn lại bằng 0.
n=int(input())
matrix=[[1 if i==m else 0 for i in range(n) ] for m in range(n)]
print(matrix)


#* TASK6:  Cho một danh sách 2 chiều chứa các danh sách con
#* Ví dụ: [[1, 2], [3, 4], [5, 6]]. Hãy biến nó thành danh sách 1 chiều phẳng: [1, 2, 3, 4, 5, 6].
lst1= [[1, 2], [3, 4], [5, 6]]
lst2=[n for m in lst1 for n in m]

#! sum có thể cộng các list con với nhau tạo thành 1 list
lst3=sum(lst1,[])



#* TASK7: nhập n in ra số nguyên tố từ 2<n
n=int(input())
ds_songuyen=([2] if n>=2 else [])+[m for m in range(3,n+1,2) if all(m%i!=0 for i in range(2,int(m**0.5)+1))]


#* TASK8: in ra n phần tử của dãy fibonacci
n=int(input())
fibonacci=[]
a,b=0,1
for _ in range(n):
    fibonacci.append(a)
    a,b=b,a+b
print(fibonacci)

#!BIẾN RÁC: _
lay_thong_tin_khach_hang=("hà",18,0335749274,2005)
ten, _, sdt, _ = lay_thong_tin_khach_hang()
print(ten, sdt) # Code cực sạch, không sinh ra các biến thừa như tuoi, dia_chi

x, *_, y = [1, 2, 3, 4, 5, 6, 7]
print(x) # 1
print(y) # 7
# Toàn bộ đống [2, 3, 4, 5, 6] bị gom vào *_ và ném vào sọt rác!

so_tien = 1_000_000_000  # Nhìn tường minh hơn hẳn 1000000000
print(so_tien)           # Máy vẫn hiểu và in ra: 1000000000


#* TASK9: kiểm tra số Armstrong a1a2a3a4..an=(a1)**n + (a2)**n + (a3)**n + .... + (an)**n
n=input()
tong=0
for so in n:
    tong+=int(so)**len(n)
print(tong==int(n))

#!Hoặc
n=input()
print(int(n)== sum(int(so)**len(n) for so in n))
    


#* TASK10: đến số lần xuất hiện của từ rồi lưu dict
cau="Python là một ngôn ngữ lập trình tuyệt vời. Học Python không chỉ vui mà Python còn giúp bạn tư duy tốt hơn, một ngôn ngữ rất đơn giản!"
dic={}
for tu in cau.lower().split():
    tu_sach=tu.strip(".,;:?!") #!Những dấu lạ sẽ không loại được ví dụ như 'Python'
    dic[tu_sach]=dic.get(tu_sach,0)+1
print(dic)

#!
import string as s
daucau=s.punctuation #!Tất cả các dấu câu
for tu in cau.lower().split():
    tu_sach=tu.strip(daucau) 
    dic[tu_sach]=dic.get(tu_sach,0)+1
print(dic)


#* TASK11: Mã hoá "AAABBCEDDDDD" thành A3B2C1E1D5
mahoa="AAABBCEDDDDD"
num=1
new=[]
for i in range(len(mahoa)):
    char=mahoa[i]
    if i+1<len(mahoa) and char==mahoa[i+1]:
        num+=1
    else:
        new.append(f"{char}{num}")
        num=1
print("".join(new))



#*TASK12:
a="Tìm từ dài nhất. Cho một câu văn bản. Hãy tìm từ có độ dài lớn nhất trong câu đó. Nếu có nhiều từ dài bằng nhau, lấy từ xuất hiện đầu tiên."
max=0
word=''
for tu in a.split():
    tu_sach=tu.strip(",.:;!?")
    if len(tu_sach)>=max:
        max=len(tu_sach)
        word=tu_sach

#!HOẶC:
import string as s
ds_tu=[tu.strip(s.punctuation) for tu in a.split()]
tu_max=max(ds_tu,key=len)



#*TASK 13:
from collections import Counter
d1 = {"a": 1, "b": 2, "c": 1}
d2 = {"b": 1, "c": 2}
# Biến dict thành Counter rồi cộng lại như cộng số bình thường
ket_qua = Counter(d1) + Counter(d2)
# Ép ngược lại thành dict truyền thống nếu muốn
print(dict(ket_qua))  # Kết quả: {'a': 1, 'b': 3, 'c': 3}



#*TASK 14: Tìm phần tử độc nhất (Unique): Cho một danh sách có nhiều phần tử trùng lặp. Tìm các phần tử chỉ xuất hiện đúng 1 lần duy nhất trong danh sách
l=[1,1,1,1,2,3,4,5,6,7,9,5,8,9]
l2={}
for i in l:
    l2[i]=l2.get(i,0)+1
l3=[k for k,v in l2.items() if v==1]

l4=[i for i in l if l.count(i)==1] #!count không hiệu quả vì mỗi lần số mới là đếm hết list 
print(l3)
print(l4)


#!HOẶC
da_thay, trung_lap= set(), set()
for i in l:
    if i in da_thay:
        trung_lap.add(i)
    else:
        da_thay.add(i)
l_final=list(da_thay-trung_lap)



#* TASK15: Ma trận chuyển vị
matrix=[[1,2],[3,4],[5,6]]
matrix_chuyen_vi=[[matrix[k][i] for k in range(len(matrix))] for i in range(matrix[0])]
print(matrix_chuyen_vi) #[[1,3,5],[2,4,6]]


#* TASK16: Tìm số lớn nhất của matrix
matrix=[[1,2,5,6],[3,4,1,2],[5,6,9,5],[1,2,3,4]]
lon_nhat=max(matrix[k][i] for i in range(len(matrix[0])) for k in range(len(matrix)))
print(lon_nhat)

#!HOẶC
matrix = [[1,2,5,6],[3,4,1,2],[5,6,9,5],[1,2,3,4]]
# 'dong' là từng list nhỏ, 'so' là từng con số nằm trong 'dong' đó
lon_nhat = max(so for dong in matrix for so in dong)

#*Tìm list chỉ có số chẵn
matrix=[[2,2,4,6],[3,4,1,2],[5,6,9,5],[1,2,3,4]]
chan=[dong for dong in matrix if all(so%2==0 for so in dong)]
print(chan)





#* TASK18: Thuật toán sắp xếp nổi bọt Bubble sort
l = [1, 2, 3, 7, 6, 5, 4, 9, 10, 11, 1, 1, 1, 3, 4, 5]
# Duyệt qua từng phần tử của list gốc
for i in range(len(l)):
    # len(l) - i - 1 giúp giới hạn không nhìn lại những thằng lớn nhất đã trôi về cuối mảng
    for m in range(len(l) - i - 1):
        if l[m] > l[m + 1]:
            # Đổi chỗ nếu thằng đứng trước lớn hơn thằng đứng sau
            l[m], l[m + 1] = l[m + 1], l[m]
print(l)



#* TASK19: check xem list có theo tứ tự tăng dần không
l=[1,2,3,4,5,6,7,8,9,10]

tangdan=all(l[i]<=l[i+1] for i in range(len(l)-1)) #! cơ chế tạo generator expresstion 
                                                   #!all() phải gọi cái máy phát này để lấy số i, rồi dùng số i đó đi dò vị trí l[i] và l[i+1] trong bộ nhớ (gọi là cơ chế tạo Generator Expression).

#!HOẶC : tối ưu hơn cách trên
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        print(False)
        break
else: 
    print(True)

#!HOẶC:
tangdan=all(a<=b for a,b in zip(l,l[1:]))



#* TASK20: Tìm cặp số có tổng bằng K : 
#* Cho danh sách số và số mục tiêu K. Dùng vòng lặp (hoặc kết hợp Set) để tìm ra cặp số đầu tiên có tổng bằng K.
l = [3, 5, 1, 4, 2, 6]
k=6
for i in range(len(l)): #!Chạy 1 vòng nếu số cần tìm ở tít cuối
    if k-l[i] in l and l[i]!=k-l[i]: #!Chạy vòng thứ 2
        print(l[i],k-l[i])
        break #!=> Hiệu suất không tối ưu


#!HOẶC
l = [3, 5, 4, 1, 2, 6]
da_thay=set()
k=7
for x in l:
    so_con_thieu=k-x #2: Tìm hiệu của (k với số xét tiếp theo) xem có nằm trong da_thay không
    if so_con_thieu in da_thay:
        print(so_con_thieu,x) #3: in số cũ đã add vào da_thay trước, rồi mới in x
    else:
        da_thay.add(x) #1: Add từng số x xét lần lượt trong l
# x=3 hiệu 7-3=4 không nằm trong da_thay nên da_thay={3}
# x=5 hiệu 7-5=2 không nằm trong da_thay nên da_thay={3,5}
# x=4 hiệu 7-4=3 nằm trong da_thay={3,5}
# in ra (3,4)

#!Kỹ thuật 2 con trỏ
l = [3, 5, 4, 1, 2, 6]
trai=0
phai=len(l)-1
l.sort() #! Bắt buộc phải sắp xếp mảng trước và cặp đầu tiên lấy ra sẽ theo thứ tự của sớm nhất của mảng mới
while trai<phai:
    tong=l[trai]+l[phai]
    if tong==k:
        print(l[trai],l[phai])
        break
    elif tong<k:
        trai+=1
    else:
        phai-=1


#* TASK21: In hình tam giác cân (Kim tự tháp): Nhập vào chiều cao H, in ra hình kim tự tháp bằng dấu sao cân đối ở giữa màn hình 
n=int(input())
tgiac=[f"{" "*(n-i)}{(2*i-1)*'*'}" for i in range(1,n+1)]
print("\n".join(tgiac))

#!HOẶC
n=int(input())
tgiac=[f"{(2*i-1)*'*':^{2*n-1}}" for i in range(1,n+1)]
#! :^(2*n-1)}:LỖI VÌ Python bắt buộc phải dùng dấu ngoặc nhọn { } để bao bọc một biến số hoặc một phép tính
print("\n".join(tgiac))















