k=5 
while k>0:
    print("k = ",k)
    k-=1


s="nguyen viet ha dep trai"
idx=0
while idx<len(s):
    print(idx, "stand for", s[idx])
    idx+=1


#Break: kết thúc vòng lặp
nums=[]
k=1
while True:
    if k%2==0:
        nums.append(k)
        if len(nums)>=5:
            break
    k+=1
print(k)
print(nums)


#Continue: tiếp tục vòng lặp
k=0
while k<10:
    k+=1
    if k%2==0:
        continue #bỏ qua code bên dưới nó và quay lại vòng lặp whilr
    print(k,"là số lẻ")


#while else: kết thúc vòng lặp while thì chạy else
k=0
while k<10:
    print("số này nhỏ hơn 10",k)
    k+=1
else: print("không có số nào lớn hơn 10")



#Thay chữ đứng trước chữ 'Kteam' bằng chữ 'How'
a="an so dfn Kteam odsa in fasfna Kteam pzcvqp Kteam dfaojf kteam dfna Kteam dfaodf afdna Kteam adfoasdf ncxvo aern Kteam dfad"
b=a.split()
m=0
while m<len(b)-1:
    if b[m+1]=="Kteam": #vì m+1 <= len-1 nên phía trên phải để m< len(b)-1
        b[m]="How"
    m+=1
print(' '.join(b))




#Tính tổng chữ số: Cho một số nguyên dương (ví dụ: n = 12345). 
#Dùng while để tính tổng các chữ số của nó (1+2+3+4+5). Gợi ý: Dùng % 10 để lấy số cuối và // 10 để bỏ số cuối.
a=int(input("nhap so nguyen duong: ")) #! CHÚ Ý INPUT SẼ TRẢ VỀ STR PHẢI ÉP KIỂU 
tongchuso=0
while a>0:
    tongchuso+=a%10
    a//=10
print(tongchuso)



#In ra n chữ số của dãy Fibonacci(0,1,1,2,3,5,8,13,....)
n=int(input())
count=0
a,b=0,1
while count<n:   #đến số thứ n-1 là dừng
    #Nếu in như này    print(a)    thì sẽ mỗi số 1 dòng, thay vào đó có thể dùng: end (để in trên cùng 1 dòng)
    print(a,end=' ') #in số thứ 0 
    a,b=b,a+b
    count+=1

#? Cách 2
n=int(input())
count=0
a,b=0,1
c=[]
while count<n:
    c.append(a)
    a,b=b,a+b
    count+=1
print(c)





#Đảo ngược số 
n=int(input())
daonguoc=0
while n:
    daonguoc=daonguoc*10+n%10
    n//=10
print(daonguoc)






#Trò chơi nhập số ngẫu nhiên đến khi nào đúng thì thôi [1;100]
bimat=42
count=1
while True:
    n=int(input(f"lần {count}, Nhap so: "))
    if n>bimat:
        print("nhỏ hơn")
    elif n<bimat:
        print("lớn hơn")
    else:
        print("correct")
        break
    count+=1

import random
so=random.randint(1,1000)
count=0
while True:
    count+=1
    n=int(input(f"nhap so lan thu {count}:"))
    if n>so:
        print("vui long nhap so be hon")
    elif n<so:
        print("vui long nhap so lon hon")
    else:
        print('correct')
        break



#giải chức năng của thuật toán gcd(a,b): tìm UCLN của a,b
a=input()
b=input()
while b!=0:
    a,b=b,a%b
    print(f"UCLN: {a}")

#?Cách khác
a_bandau,b_bandau=a,b
while a!=b:
    if a>b:
        a=a-b
    elif b>a:
        b=b-a
    print(f"ƯCLN của hai số {a_bandau} và {b_bandau} la: {a}")




#Loại bỏ phần tử trùng với nhau trong 1 list bằng while mà không tạo list mới (với trường hợp cùng kiểu dữ liệu trong 1 list )
nums=[1,2,3,4,5,3,4,2,4,1,1]
i=0
nums.sort()
while i<len(nums)-1:
    if nums[i]==nums[i+1]:
        nums.pop(i+1)
        i-=1 #nếu loại bỏ số rồi thì phải dùng i-1 để giảm thứ tự số tiếp theo vì -1 phần tử list thì len(list) cũng giảm đi 1
    i+=1
print(nums)

#Cách code sạch sẽ an toàn hơn
nums=[1,2,3,4,5,3,4,2,4,1,1]
i=0
nums.sort()
while i<len(nums)-1:
    if nums[i]==nums[i+1]:
        nums.pop(i+1) #pop(): bỏ số đó khỏi chuỗi và có thể in ra màn hình nếu muốn
    else: i+=1 
print(nums)




#sắp xếp các số theo trình tự các số từ thấp đến cao
nums=[5,3,4,5,7,8,1,2]
n=len(nums)
so_lan_duyet=1
while so_lan_duyet<n: #sẽ duyệt từng cặp 1 rồi cuối cùng sau mỗi lần duyệt sẽ tìm được số lớn nhất đặt ở cuối
    i=0
    while i< n-so_lan_duyet: #sau mỗi lần duyệt vì tìm được 1 số lớn nhất ở ngoài cùng nên i sẽ chỉ xét đến n-1-lần duyệt
        if nums[i]>nums[i+1]: #so sánh từng cặp số liền kề 
            nums[i],nums[i+1]=nums[i+1],nums[i]
        i+=1
    so_lan_duyet+=1
print(nums)






#Xác định xem có phải số nguyên tố hay không
import math
n=int(input())
i=1
count=0
while i<=math.sqrt(n):
    if n%i==0:
        count+=1
        if count==2:
            print("không phải là số nguyên tố")
    i+=1
#! theo như trên thì số 1 vẫn là số nguyên tố
#! chưa in ra được nếu đúng là số nguyên tố

#Code khắc phục lỗi 
import math
n=int(input())
i=1
count=0
is_prime=True
if n==1:
    is_prime=False
else:
    while i<=math.sqrt(n):
        if n%i==0:
            count+=1
            if count==2:
                is_prime=False
        i+=1
if is_prime:
    print("là số nguyên tố")
else: print("không là số nguyên tố")
#!Nhưng vẫn hơi thừa thãi và có rủi ro

#? Code chuẩn nhất
import math
n=int(input())
is_prime=True
if n<2:
    is_prime=False
else:
    i=2
    while i<=math.sqrt(n): #khi n=4 thì while mới bắt đầu chạy 
        if n%i==0:
            is_prime=False
            break
        i+=1
if is_prime:
    print("n là số nguyên tố")
else:
    print("n không phải là số nguyên tố")
    



#Tìm ƯCLN của 1 list
nums=[12,18,24,30]
ucln=nums[0]
i=1
while i<len(nums):
    a=ucln
    b=nums[i]
    while b!=0:
        a,b=b,a%b
    ucln=a
    i+=1
print(ucln)



#nhập n rồi in ra dãy số Fibonacci sao cho tổng của các số nhỏ hơn bằng n
n=int(input())
a,b=0,1
sum=0
k=[]
while sum+a<=n:
    sum+=a
    k.append(a)
    a,b=b,a+b
print(k)



#Phân tích thừa số nguyên tố
#Yêu cầu: Nhập một số nguyên n (ví dụ n = 60). In ra các thừa số nguyên tố của nó: 2*2*2*3...
#!có vấn đề xuất hiện, số nguyên tố đang bị giới hạn bởi những số đã nhập nên sẽ để máy tính tự tính
n=int(input())
uoc=2
k=[]
while n>1:
    if n%uoc==0:
        k.append(uoc)
        n//=uoc #vì sẽ chia hết nên dùng // để ép kiểu int
    else: uoc+=1
print("*".join(map(str, k)))





#kiểm tra số đối xứng
so_ban_dau=int(input())
so_doi_xung=0
n=so_ban_dau
while n:
    m=n%10
    so_doi_xung=so_doi_xung*10+m
    n//=10
if so_ban_dau==so_doi_xung:
    print("n là số đối xứng")
else: 
    print("n không phải là số đối xứng")
        




    






