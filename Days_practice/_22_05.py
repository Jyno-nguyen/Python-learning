
#*anagram_check(s1, s2):
from collections import Counter
def anagram_check(s1,s2):
    return Counter(s1.replace(" ","").lower())==Counter(s2.replace(" ","").lower())
print(anagram_check(input(),input()))

#!So sánh 2 dict bằng nhau
from collections import Counter
def anagram_check(s1,s2):
    s1_,s2_={},{}
    for i in s1.replace(" ","").lower():
        s1_[i]=s1_.get(i,0)+1
    for i in s2.replace(" ","").lower():
        s2_[i]=s2_.get(i,0)+1
    return s1_==s2_
print(anagram_check(input(),input()))

#!Dùng sorted(str): sẽ tạo ra một list 
from collections import Counter
def anagram_check(s1,s2):
    str1=s1.replace(" ","").lower()
    str2=s2.replace(" ","").lower()
    return sorted(s1)==sorted(s2)
print(anagram_check(input(),input()))

#!Dùng ord
def anagram_check(s1,s2):
    #!Tạo 1 list ord tương đương với 26 chữ cái từ a-z
    if len(s1.replace(" ","").lower())!=len(s2.replace(" ","").lower()):
        return False
    list_ord=[0]*26 #*Cách tạo nhanh 1 list
    for char1,char2 in zip(s1.replace(" ","").lower(),s2.replace(" ","").lower()):
        list_ord[ord(char1)-ord("a")]+=1
        list_ord[ord(char2)-ord("a")]-=1
    return all(count==0 for count in list_ord)







#*calculate_stats(*args): Hàm nhận vào một số lượng tham số không giới hạn là các con số
#*Trả về một Dictionary chứa: Tổng, Trung bình cộng, và số lượng số dương.
def calculate_stats(*args):
    dic={}
    if not args:
        return None
    dic["Tong"]=sum(args)
    dic["tbc"]=sum(args)/len(args)
    dic["soluong"]=len(list(filter(lambda x:x>1,args)))
    dic["soluong"]=sum(x>0 for x in args)
    #!
    from functools import reduce
    dic["soluong"] = reduce(lambda count, x: count + 1 if x > 0 else count, args, 0)
    return dic
print(calculate_stats(*[1,2,3,4,5,6,7,8,9,-1]))








#*matrix_transpose(matrix): Hàm nhận vào một ma trận 2 chiều (list của các list) và trả về ma trận chuyển vị của nó (dòng biến thành cột).
def matrix_transpose(matrix):
    #!Cách này tạo ra một ma trận mới làm tốn RAM
    return [[matrix[i][k] for i in range(len(matrix))] for k in range(len(matrix[0]))]
print(matrix_transpose([[1,2],[3,4],[5,6]]))

#!Dùng vòng lặp:nhưng phải ma trận vuông
def matrix_transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix[0])):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix
print(matrix_transpose([[1,2,10],[3,4,11],[5,6,12]]))

#!Hoặc
def matrix_transpose(matrix):
    #!Cách này tạo ra một ma trận mới làm tốn RAM
    return [list(row) for row in zip(*matrix)]






#*merge_sorted_lists(lst1, lst2): Hàm nhận vào 2 list đã được sắp xếp tăng dần. Hãy gộp chúng lại thành 1 list duy nhất cũng được sắp xếp tăng dần mà không dùng hàm sort().
def merge_sorted_lists(lst1, lst2):
    lstt=lst1+lst2
    if len(lstt)<=1:
        return lstt
    check=len(lstt)-1
    while check:
        i=0
        while i<check:
            if lstt[i]>lstt[i+1]:
                lstt[i],lstt[i+1]=lstt[i+1],lstt[i]
            i+=1
        check-=1
    return lstt
print(merge_sorted_lists([1,3,7],[2,4,6]))

#? Nhanh nhất, trường hợp xấu thì vẫn chưa tốt nhất
def quick_sort(lst):
    if len(lst)<=1:
        return lst
    mid=lst[len(lst)//2]
    left=[x for x in lst if x<mid]
    middle=[x for x in lst if x==mid]
    right=[x for x in lst if x>mid]
    return quick_sort(left)+ middle+ quick_sort(right) 

#? Merge_sort: thuật toán chia nửa
def merge_sort(lst): #!Chia nửa đến khi còn 1 số
    if len(lst)<=1:
        return lst
    mid=len(lst)//2
    left=merge_sort(lst[:mid])
    right=merge_sort(lst[mid:])
    return merge(left,right)
def merge(left,right):
    lst_final=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            lst_final.append(left[i])
            i+=1
        else:
            lst_final.append(right[j])
            j+=1
    lst_final.extend(left[i:])
    lst_final.extend(right[j:])
    return lst_final








#*Mã hoá: AAAABBBBBBCEE
def compress_string(s):
    if not s: return ""
    count=1
    i=0
    new=[]
    while i<len(s):
        char=s[i]
        i+=1
        while i<len(s) and char==s[i]:
            count+=1
            i+=1
        new.append(f"{char}{count}" if count>1 else char)
        count=1
    return "".join(new)
print(compress_string("AAAABBBBBBCEE"))

def compress_string(s):
    count=1
    new=[]
    for a,b in zip(s,s[1:]):#!Nếu chuỗi có 1 triệu ký tự zip sẽ tạo thêm 1 chuỗi s[1:] có sấp xỉ 1 triệu ký tự nữa làm tốn RAM
        if a==b:
            count+=1
        else:
            new.append(f"{a}{count}" if count>1 else a)
            count=1
    new.append(f"{s[-1]}{count}" if count >1 else s[-1])
    return "".join(new)
print(compress_string("AAAABBBBBBCEE"))


from itertools import groupby
def compress_string_ultimate(s):
    if not s: return ""
    new = []
    # groupby sẽ tự động gom các ký tự giống nhau liên tiếp lại
    for char, group in groupby(s):
        # group là một iterator chứa các ký tự lặp lại, ta dùng len(list(...)) để đếm số lượng
        count = len(list(group))
        new.append(f"{char}{count}")    
    return "".join(new)
print(compress_string_ultimate("aabcccccaaa")) # Kết quả: a2b1c5a3







#*find_pairs(lst, target): Hàm tìm tất cả các cặp gồm 2 số trong lst có tổng bằng target.
def find_pairs(lst, target):
    seen_pairs=set()
    set1=set()
    for i in lst:
        hieu=target-i
        if hieu in set1:
            seen_pairs.add(min(i,hieu)max(i,hieu))
        set1.add(i)
    return seen_pairs
print(find_pairs([1,2,3,4,5,6,7,8,8,8,8,8,8,8,8,9,10],12))

#!Dùng 2 con trỏ
def find_pairs(lst,target):
    left=0
    right=len(lst)-1
    sx=sorted(lst)
    seen_pairs=set()
    while left<=right:
        if sx[left]+sx[right]==target:
            seen_pairs.add((sx[left],sx[right]))
            left+=1
            right-=1
        elif sx[left]+sx[right]<target:
            left+=1
        else:
            right-=1
    return seen_pairs

#!LẤY RA INDEX CHỨ KHÔNG LẤY RA SỐ ĐÓ
def find_pairs(lst,target):
    dic={}
    seen_pairs=[]
    for index,value in enumerate(lst):
        hieu=target-value
        if hieu in dic:
            seen_pairs.append((dic[hieu],index))
        dic[value]=index
    return seen_pairs
print(find_pairs([1,2,3,4,5,6,7,8,8,8,8,8,8,8,8,9,10],12))
"""
Bị rác (Quá nhiều cặp trùng): Nó sẽ bắt cặp liên tục tạo ra hàng loạt index trùng lặp giá trị (6, 6).#!Nhưng vẫn chưa lấy hết được 
Bị ghi đè mất dấu: Dòng code dic[value] = index sẽ liên tục ghi đè vị trí của số 6 sau lên số 6 trước. Kết quả là máy tính sẽ bị "mất trí nhớ", không biết các số 6 xuất hiện đầu tiên nằm ở đâu nữa.
"""

#!LẤY TẤT CẢ CÁC CẶP INDEX KỂ CẢ TRÙNG VALUE
def find_pairs(lst,target):
    dic={}
    seen_pairs=[]
    for current_index,value in enumerate(lst):
        hieu=target-value
        if hieu in dic[hieu]:
            for past_index in dic[hieu]:
                seen_pairs.append((past_index,current_index))
        if value not in dic:
            dic[value]=[] #!Biến đổi dic[value]=[] thì sẽ lưu hết những giá trị index đã đi qua
        dic[value].append(current_index)
    return seen_pairs
print(find_pairs([1,2,3,4,5,6,7,8,8,8,8,8,8,8,8,9,10],16))


#!CHỈ LẤY MỘT CẶP TRÙNG LẶP 
def find_pairs(lst,target):
    dic={}
    seen_pairs=set()
    pairs=[]
    for index,value in enumerate(lst):
        hieu=target-value
        if hieu in dic and (min(value,hieu),max(value,hieu)) not in seen_pairs:
            pairs.append((dic[hieu],index))
            seen_pairs.add((min(value,hieu),max(value,hieu)))
        dic[value]=index
    return pairs
print(find_pairs([1,2,3,4,5,6,7,7,7,7,7,8,8,8,8,8,8,8,8,9,10],15))

