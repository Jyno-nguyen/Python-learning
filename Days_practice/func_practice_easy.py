
#* is_prime(n): kiểm tra số nguyên
def is_prime(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1)) 
    # True nếu cả 2 đúng còn False

#! Hoặc
ktra=lambda x: x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1)) 

#!HOẶC
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True








#* perfect_numb(): kiểm tra số hoàn hảo: SỐ=1+....(BẰNG TỔNG CÁC ƯỚC CỦA NÓ CỘNG LẠI)
def perfect_numb(n):
    if 1>=n:
        return False
    return n==sum(i for i in range(1,n//2+1) if n%i==0) #không nên dùng sum([list comprehension]) vì sẽ phải tạo ra một list trong bộ nhớ RAM
                                                        #!dùng ngoặc tròn tạo generator expression dùng xong sẽ không còn lưu trữ thừa
#! Tại sao lệnh if lại đứng sau vòng for vì vòng for diễn ra như sau
n=int(input())
for i in range(1,n//2+1):
    if n%i==0:
        #yield i
        break

#!Dùng filter
def perfect_num():
    if n<=1:
        return False
    ds_uoc=filter(lambda i: n%i==0,range(1,n//2+1))
    return sum(ds_uoc)==n

#!Dùng cho những số lớn
def perfect_num():
    if n<=1:
        return False
    tong=1
    for i in range(2,int(n**0.5)+1): #!Vì chỉ duyện đến n**0.5 nên với số lớn sẽ có lợi hơn nhiều
        if n%i==0:
            tong+=i
            if i!=n//i:
                tong+=n//i
    return tong==n








#* tính tổng các chữ số sum_of_digits(n):
def sum_of_digits_v1(n):
    if not n:
        return 0
    return n%10 + sum_of_digits_v1(n//10)
#!HOẶC NGẮN GỌN HƠN NHƯNG CÙNG BẢN CHẤT
def sum_of_digits_v2(n):
    return 0 if not n else n%10+sum_of_digits_v2(n//10)

#*Chuyển thành chuỗi và lấy từng số của chuỗi
def sum_of_digits_v3(n):
    return sum(int(char) for char in str(n)) #tạo generator expression chữ không tạo list tốn RAM


#* while ( toán học thuần tuý ) => chạy nhanh nhất
def sum_of_digits_v4(n):
    total=0
    while n:
        tong+=n%10
        n//=10
    return total









#*Tìm ước chung lớn nhất của hai số gcd(c,d)
def gcd_v1(c,d):
    return c if d==0 else gcd_v1(d,c%d)

def gcd_v2(c,d):
    while d!=0:
        c,d=d,c%d
    return c

def gcd_v3(c,d):
    if c==0 or d==0:
        return c+d
    while c!=d:
        if c>d:
            c-=d
        else:
            d-=c
    return c







#*Tìm bội chung nhỏ nhất lcm(a,b)
def lcm_v1(a,b):
    max_=max(a,b)
    step=max_
    while True:
        if step%a==0 and step%b==0:
            return step
        step+=max_


def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
def lcm_v2(a,b):
    return a*b//gcd(a,b)







#* Đếm số lượng nguyên âm (a,e,i,o,u) không phân biệt hoa thường trong một chuỗi
#!Đếm tổng số lượng nguyên âm
def vowel_counts(s):
    vowels='aeiou'
    count=0
    for char in s.lower():
        if char in vowels:
            count+=1

#!Kỹ thuật đệ quy
def vowel_counts_v2(s):
    if not s:
        return 0
    dem=1 if s[0].lower() in 'aeuio' else 0
    return dem+vowel_counts_v2(s[1:])

#!list comprehension
def vowel_counts_v3(s):
    lst=[char for char in s if char.lower() in 'auioe']
    return len(lst)
#!generator expression
def vowel_counts_v4(s):
    return sum(1 if char.lower() in 'auioe' else 0 for char in s)

#*Đếm số lượng của từng chữ cái:
def vowel_counts(s):
    dic_vowel=dict.fromkeys("aoeui",0) #{'a': 0, 'o': 0, 'e': 0, 'u': 0, 'i': 0}
    for char in s.lower():
        if char in dic_vowel:
            dic_vowel[char]+=1
    return dic_vowel
print(vowel_counts("jksajfakjfKDAOFFQIF"))


#!DUNG COUNT KẾT HỢP VỚI COMPREHENSION
def vowel_counts(s):
    return {v:s.lower().count(v) for v in 'aoiue'} #!Nhưng vỡi mỗi một ký tự count phải chạy 1 vòng 

#!Counter trong thư viện collections
from collections import Counter
def vowel_counts(s):
    all_count=Counter(s.lower())
    return {v:all_count[v] for v in 'aeoiu'}









#*Kiểm tra đối xứng
def is_palindrome(s):
    lam_sach="".join(s.lower().split())
    return lam_sach==lam_sach[::-1]

#*viết hoa chữ cái đầu mỗi chữ mà không dùng title()
def is_cap(s):
    return " ".join(f"{i[:1].upper()}{i[1:]}" for i in s.lower().split(" "))#Nếu vì lý do nào đó có khoảng trắng ở trước chữ cái muốn viết hoa 
                                                                            #sẽ báo lỗi nếu dùng i[0].upper() vì tồn tại khoảng trắng ở trước
                                                                            #dùng slicing: i[:1].upper() sẽ không bị lỗi
print(is_cap("  nguyen viet ah dep trai"))

def is_cap(s):
    return " ".join(char.capitalize() for char in s.split())
print(is_cap("  nguyen viet ah dep trai"))

#*Xoá nguyên âm của chuỗi
def remove_vowels(s):
    v='aeuoi'
    return "".join(char for char in s if char.lower() not in v)
print(remove_vowels("  nguyen viet ah dep trai"))

#!Dùng bộ đôi str.maketrans() and translate()
"""Hàm xóa toàn bộ nguyên âm trong chuỗi bằng bộ đôi maketrans và translate (Lõi C).
    - Hai tham số đầu '' và '' nghĩa là KHÔNG thay thế chữ này bằng chữ khác và phải có độ dài bằng nhau.
    - Tham số thứ ba 'aeiouAEIOU' nghĩa là XÓA SẠCH các ký tự này khi bắt gặp."""

def remove_vowels_fast(s):
    bang_dich = str.maketrans('', '', 'aeiouAEIOU')
    
    # Áp bảng dịch vào chuỗi s để trả về chuỗi mới đã sạch nguyên âm
    return s.translate(bang_dich)
print(remove_vowels_fast("   NGUYEN viet ah DEP TRAI")) # "   NGYN vt h DP TR"


#*find_longest_word(s): Hàm tìm và trả về từ có độ dài lớn nhất trong một câu.
def find_longest_word(s):
    if not s:
        return ""
    smax=''
    for word in s.split():
        if len(word)>len(smax):
            smax=word
    return smax

#!HOẶC
def find_longest_word(s):
    return max(s.split(),key=len) if s.split() else ""

#!OR
def find_longest_word(s):
    current_word=''
    smax=""
    s+=" "
    for char in s:
        if char!=' ':
            current_word+=char #!cộng dồn ký tự gặp ' ' thì dừng
        else:
            if len(current_word)>len(smax):
                smax=current_word
            current_word=""
    return smax
print(find_longest_word("nguyen viet ha dep trai"))












