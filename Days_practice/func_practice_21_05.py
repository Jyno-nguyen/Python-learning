
#*Tìm số lớn nhất và nhỏ nhất trong 1 list
#!Dùng reduce
from functools import reduce
def find_max_min(lst):
    return reduce(lambda a,b :(max(a[0],b),min(a[1],b)),lst,(lst[0],lst[0]))
                 #truyền vào a=(,) và b là số tiếp theo trong list
                 #ban đầu a=(1,1) b=2 rồi sau đó 
                 # a=(max(),min()) b=3 .....
print(find_max_min([1,2,3,4,5,6,7,8,9,0,-1,-2,-7,-9]))

#!Dùng đệ quy chia đôi list rồi tìm max(), min() trong mỗi nửa list đó
def find_max_min(lst):
    if len(lst)==1:
        return lst[0],lst[0]
    if len(lst)==2:
        return (lst[0],lst[1]) if lst[0]>lst[1] else (lst[1],lst[0])
    mid=len(lst)//2
    maxl,minl=find_max_min(lst[:mid])
    maxr,minr=find_max_min(lst[mid:]) 
    return max(maxl,maxr),min(minl,minr)
print(find_max_min([7,2,1,12,9,8,3,4,10,6,5,11]))






#* remove_duplicates(lst): Hàm loại bỏ các phần tử trùng lặp trong một list và giữ nguyên thứ tự xuất hiện ban đầu.
def remove_duplicates(lst):
    new=[]
    for i in lst:
        if i not in new: #!Toán tử not in trong vòng list là một vòng lặp ẩn và không hiệu quả đối với chuỗi dài
            new.append(i)
    return new

#!TOÁN TỬ NOT IN TRONG SET THÌ VÔ CÙNG HIỆU QUẢ
def remove_duplicates(lst):
    new=[]
    seen=set()
    for i in lst:
        if i not in seen:
            seen.add(i)
            new.append(i)
    return new
#!HOẶC
def remove_duplicates(lst):
    seen=set()
    return [i for i in lst if not(i in seen or seen.add(i))]

#!Kiểm tra bằng fromkeys()
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))









#* is_sorted(lst): Hàm kiểm tra xem một danh sách số có đang được sắp xếp tăng dần hay không. Trả về True/False.
def is_sorted(lst):
    if len(lst)<=1: #! ARR [] hoặc 1 phần tử thì coi là có sắp xếp vì không có cặp nào lệch nhau cả
        return True
    if len(lst)==2:
        return a<b
    a,b,*c=lst
    return a<=b and is_sorted(lst[1:])
print(is_sorted([1,2,3,4,5,6,7,8,9]))

#! all(),any(): nếu gặp false(all()) hoặc true(any()) thì lập tức ngắt mạch sớm
def is_sorted(lst):
    return not any(lst[i]>lst[i+1] for i in range(len(lst)-1))

def is_sorted(lst):
    return all(lst[i]<=lst[i+1] for i in range(len(lst)-1))

#!zip()
def is_sorted(lst):
    results=(map(lambda x: x[0]<=x[1] ,zip(lst,lst[1:]))) 
    #LƯU Ý: zip tạo thành các cặp tuple ()()() => khi so sánh để x[0]<=x[1] (vì mỗi lần lambda lấy 1 tuple vào để so sánh)
    return all(results)
print(is_sorted([1,2,3,4,5,6,7,8,9]))








#*average_list(lst): Hàm tính điểm trung bình của một list số, loại bỏ số lớn nhất và số nhỏ nhất trước khi tính.
from collections import Counter
def average_list(lst):
    if len(lst)<=1:
        return 0
    lst_count=Counter(lst)
    max_=max(lst_count)
    min_=min(lst_count)
    #!Xoá phần tử khỏi dict
    del lst_count[max_]
    del lst_count[min_]
    lis_tinh=list(lst_count.elements())
    if not lis_tinh:
        return 0
    return sum(lis_tinh)/len(lis_tinh)
print(average_list([1, 1, 5, 5]))






#*Kiểm tra mật khẩu 
def validate_password(password):
    if len(password)<8:
        return "Mật khẩu quá ngắn"
    upper=any(char.isupper() for char in password)
    lower=any(char.islower() for char in password)
    digit=any(char.isdigit() for char in password)
    return upper and lower and digit
print(validate_password("pss324Dword"))

#!Công nhiệp
import re

def validate_password_v3(password):
    # Giải thích bùa chú:
    # (?=.*[A-Z]) : Phải có ít nhất 1 chữ hoa
    # (?=.*[a-z]) : Phải có ít nhất 1 chữ thường
    # (?=.*\d)    : Phải có ít nhất 1 chữ số (\d viết tắt của digit)
    # .{8,}       : Độ dài phải từ 8 ký tự trở lên
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
    
    # Kiểm tra xem password có khớp hoàn toàn với pattern không
    if re.match(pattern, password):
        return True
    return False

print(validate_password_v3("Python2026!")) # True







#*mask_credit_card(card_number): Hàm nhận vào chuỗi số thẻ tín dụng và che các số đầu, chỉ hiển thị 4 số cuối (Ví dụ: "************1234").
def mask_credit_card(card_number):
    if len(card_number)<=4:
        return "Số thẻ không hợp lệ"
    return f"{(len(card_number)-4)*'*'}{card_number[-4:]}"
print(mask_credit_card(input().replace(" ","")))






#*leap_year_range(start, end): Hàm nhận vào năm bắt đầu và năm kết thúc, trả về danh sách tất cả các năm nhuận trong khoảng đó.
def leap_year_range(start, end):
    # Tìm bệ phóng (năm chia hết cho 4 đầu tiên và là năm nhuận)
    for i in range(8):
        current_year = start + i
        if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
            start = current_year
            break
    return [i for i in range(start, end + 1, 4) if i % 100 != 0 or i % 400 == 0]

print(leap_year_range(90, 1000))

#!HOẶC
def leap_year_range(start, end):
    return(y for y in range(start,end+1) if (y%4==0 and y%100!=0) or y%400==0)

#!HOẶC
def leap_year_range(start, end):
    start=start + 4- start%4
    if start%100==0 and start%400!=0:
        start+=4
    return [y for y in range(start,end+1,4) if y%100!=0 or y%400==0]


#!Thư viện calender
import calendar
def leap_year_range_calendar(start, end):
    # Trông là quét từng năm nhưng chạy ngầm bằng ngôn ngữ C nên nhanh xé gió
    return [year for year in range(start, end + 1) if calendar.isleap(year)]#!trả về True nếu là năm nhuận
print(leap_year_range_calendar(90, 1000))








#*Tìm idex của số xuất hiện trong lst
def linear_search_fast(lst, target):
    try:
        return lst.index(target) # Hàm .index() sẽ tìm và trả về vị trí đầu tiên của target
    except ValueError:
        return -1
mang_khong_lo = [1] * 10000 + [4]+[1] * 1000 +[4,4,4]
print(linear_search_fast(mang_khong_lo, 4)) # Kết quả: 10000

#!Tìm kiếm nhị phân ( nếu list đã được xếp theo thứ tự tăng dần hoặc giảm dần)
def binary_search(lst, target):
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2
        if lst[mid]==target:
            return mid
        elif lst[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
mang_da_xep = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(mang_da_xep, 70)) # Kết quả: 6


#!dùng dict siêu nhanh
dic={}
lst=[10,40,40,40,50]
for index,num in enumerate(lst):
    if num not in dic:
        dic[num]=index
def super_fast_search(target):
    return dic.get(target,-1)







    