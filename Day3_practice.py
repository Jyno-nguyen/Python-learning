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
    #Bài 3: Kiểm tra email hợp lệ
    #Bài 4: Mã hoá caeser đơn giản - Dịch mỗi chữ sang phải 1 đơn vị
    #Bài 5: tìm ký tự xuất hiện nhiều nhất
    #Bài 6: Kiểm tra anagram (là cùng ký tự nhưng cách sắp xếp khác nhau)
s1=input().replace(' ','').lower()
s2=input().replace(' ','').lower()
if s1.sorted()==s2.sorted():
    print("Anagram")
else:
    print("khong phai Anagram")
    #Bài 7: Tạo bảng bằng format
""" + ------+ --------------- + ---------- +
    | 123   |      VietHa     |       0262 |
    | Đchi  |      VPhuc      |       1502 |
    | abc   |       xyz       |        mnq |
    + ------+ --------------- + ---------- +  """
row1='+{:-<6}+{:-^15}+{:->10}+\n'.format('','','')
row2='|{:<6}|{:^15}|{:>10}|\n'.format('123','456','789')
row3='|{:<6}|{:^15}|{:>10}|\n'.format('abc','def','ijk')
row4='|{:<6}|{:^15}|{:>10}|\n'.format('xyz','mnq','wvl')
row5='+{:-<6}+{:-^15}+{:->10}+\n'.format('','','')
print(row1+row2+row3+row4+row5)

