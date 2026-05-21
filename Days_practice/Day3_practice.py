    #Bài 1: Đảo vị trí đầu/cuối INPUT: python/OUTPUT: nythop
nhap1=input()
print(nhap1[-1]+nhap1[1:-1]+nhap1[0])

    #Bài 2._1: Kiểm tra chuỗi đối xứng(tính khoảng trắng ở giữa, không tính khoảng trắng 2 bên, không phân biệt hoa thường)
nhap2_1=input().strip().lower()
print(nhap2_1[::-1]==nhap2_1)
    #Bài 2_2: Kiểm tra chuối đối xứng (...), không tính khoảng trắng ở giữa
nhap2_2=input().strip().lower()
xoa_khoang_cach=nhap2_2.replace(' ','')
print(xoa_khoang_cach[::-1]==xoa_khoang_cach)
    #!Bài 3: Kiểm tra email hợp lệ
    #Bài 4: Mã hoá caeser đơn giản - Dịch mỗi chữ sang phải 1 đơn 
a='jasjfhasf ZAHzH'
result=''
for c in a:
    if c.isalpha(): #? có thể dùng isspace(): kiểm tra: '',\n,\t (điều kiện ít nhất 1 ký tự và chỉ chứa khoảng trắng)
        if c=='z': result+='a' #! nếu có "z" quay trở về "a"
        elif c=='Z': result+='A' #! nếu có "Z" quay trở về "A"
        else:
            result+=chr(ord(c)+1)
    else:
        result+=c
print(result)


    #Bài 5: tìm ký tự xuất hiện nhiều nhất

    #Bài 6: Kiểm tra anagram (là cùng ký tự nhưng cách sắp xếp khác nhau)
s1=input().replace(' ','').lower()
s2=input().replace(' ','').lower()
if sorted(s1)==sorted(s2):
    print("Anagram")
else:
    print("khong phai Anagram")
    #Bài 7: Tạo bảng bằng format
""" + ------+ --------------- + ---------- +
    | 123   |      VietHa     |       0262 |
    | Đchi  |      VPhuc      |       1502 |
    | abc   |       xyz       |        mnq |
    + ------+ --------------- + ---------- +  """
row1=f'+{'':-<6}+{'':-^15}+{'':->10}+\n' #!Dùng f-string
row2=f'|{123:<6}|{456:^15}|{789:>10}|\n'
row3='|{:<6}|{:^15}|{:>10}|\n'.format('abc','def','ijk') #!Dùng format
row4='|{:<6}|{:^15}|{:>10}|\n'.format('xyz','mnq','wvl')
row5='+{:-<6}+{:-^15}+{:->10}+\n'.format('','','')
print(row1+row2+row3+row4+row5)

