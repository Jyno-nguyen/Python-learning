    #Những gì ghi trong ' ', " ", """ """, ''' ''' được gọi là chuỗi
    #escape sequence
""" \a: phát ra tiếng bíp
    \b: lùi con trỏ về và xoá ký tự trước đó, \b ở vị trí đầu và cuối bị bỏ qua
    \t: tab có độ dài là 8
    \n: xuống dòng
    \': in ký tự '
    \": in ký tự "
    \\: in ký tự \
"""


    #XỬ LÝ CHUỖI
print(r'nguyen viet \nha') #bỏ qua escape sequence, in ra toàn bộ

    #Toán tử cộng chuỗi
stra="nguyenvietha"
strb="deptrai"
strc= stra+ "\n" +strb
print(strc)

    #Toán tử nhân
strd="nguyenvietha\n"
stre=strd*5 
#!Toán tử nhân với số <=0 thì trả về chuỗi rỗng: VÀ NÓ VẪN LÀ 1 CHUỖI('') CHỨ KHÔNG GIỐNG NHƯ None: ĐẠI DIỆN CHO VIỆC KHÔNG CÓ GIÁ TRỊ

    #Toán tử in: trả về TRUE OR FALSE
strf="i"
strg= strf in stra #kết quả trả về True ( chữ i có nằm trong nguyenvietha )

    #Toán tử so sánh
so1= 'ă' < 'â' # vì ‘ă’ đứng sau ‘â’ trong bảng mã Unicode >>> False
so2= 'a' > 'b' # vì ‘b’ đứng sau ‘a’ trong bảng mã Unicode >>> False
so3= 'ac' > 'abc' # Ở kí tự thứ hai (có chỉ số index là 1) thì ‘c’ > ‘b’ >>> True
so4= 'z' > 'abcdefz' # Kí tự đầu tiên: ‘z’ > ‘a’ >>> True
so5= 'ab' < 'abc' # Đã xét hết 2 cặp kí tự, nhưng không tìm thấy sự khác nhau, chương trình so sánh độ dài của 2 chuỗi >>> True



    #Đánh số các ký tự trong chuỗi: Từ 0/(-n) - (n-1)/(-1) theo thứ tự trừ trái sang phải (với n là số ký tự trong chuỗi )
stra="nguyenvietha"
strk=stra[3]     #lấy ra chữ y
print(len(stra)) #lấy ra độ dài chuỗi = n

    #Cắt chuỗi
strk1=stra[1:len(stra)] #lấy từ vị trí 1 đến n=> [1;n)=[1;n-1] => guyenvietha
strk2=stra[1:None]      #None là vị trí bắt đầu hoặc kết thúc => guyenvietha
strk3=stra[None:5]      #nguye = [0;4]=[0;5)
strk4=stra[None:None]   #nguyenvietha = [:] = [None:] = [:None] (bỏ trống tự hiểu là None )
#s[-4: -1]  # cắt từng kí tự có vị trí từ -4 đến -2 >>> ‘ xy’
#s[1: -1]  # cắt từng kí tự có vị trí từ 1(-6) đến 5(-2) vì vị trí dừng là 6(-1) >>> ‘bc xy’

    #Nếu <vị trí bắt đầu> hoặc <vị trí dừng> là một giá trị vượt ngoài phạm vi của chuỗi, thì python cũng sẽ cho chúng ta cắt chuỗi một cách tối ưu nhất:
#a[1: 100] // lấy từ kí tự a[0] đến cuối chuỗi >>> '23456'
#a[-1000: 1000] // lấy toàn bộ chuỗi >>> '123456'
#a[-10:-3] // lấy từ a[-6] đến a[-4] >>> '123'

strk5=stra[None:None:2] #cắt chuỗi bước nhảy ( cũng tương tự các trường hợp như trên, nếu muốn cắt ngược lại thì để bước nhảy âm)
    #Có thể cắt chuỗi liên tiếp 
s = "Jyno_AI_Engineer_2026"
s[0:10][0:5:1] #cắt được chuỗi lần 1 rồi coi là chuỗi mới có số thứ tự mới rồi cắt tiếp


s = "Jyno_AI_Engineer_2026"

# Cú pháp: s[start:stop:step]
# Index dương: 0,1,2...20
# Index âm:  -21,-20,...-1

# 1. Ký tự đầu
s[0] / s[-21]

# 2. Ký tự cuối
s[-1] / s[20]

# 3. "Jyno"
s[:4] / s[:-17]

# 4. "2026"
s[-4:] / s[17:]

# 5. "Engineer"
s[8:16] / s[-13:-6]

# 6. Đảo ngược
s[::-1] / s[-1::-1]

# 7. Index chẵn
s[::2] / s[-21::2]

# 8. "AI" bằng index âm
s[-16:-14]

    # LƯU Ý QUAN TRỌNG:
# - stop không bao gồm index đó (lấy đến stop-1)
# - index vượt quá không báo lỗi khi slice: s[17:9999] OK
# - index vượt quá báo lỗi khi truy cập đơn: s[100] → IndexError
# - step âm = đi ngược

    #!Định dạng bằng toán tử %
per="i'm %s %s %s years old" %('15','16','17') # i'm 15 years old 
per2='%s %s'
print(per2 %('D','16')) # >>> D 16
    # Số nguyên
print("%d" % 3.9)      # 3 — chỉ lấy phần nguyên
print("%i" % 3.9)      # 3 — giống %d

    # !Số thực
print("%f" % 3.14)     # 3.140000 — mặc định 6 chữ số thập phân
print("%.2f" % 3.14)   # 3.14 — giới hạn 2 chữ số
print("%e" % 3.14)     # 3.140000e+00 — dạng khoa học

    #!Chuỗi
print("%s" % "Jyno")   # Jyno
print("%r" % "Jyno")   # 'Jyno'
print("%10s" % "Jyno") #       Jyno — căn phải 10 ký tự
print("%-10s" % "Jyno")# Jyno       — căn trái 10 ký tự

    # Nhiều giá trị cùng lúc
print("%s is %d years old" % ("Jyno", 21))  # Jyno is 21 years old





    #?ĐỊNH DẠNG BẰNG CHUỖI F-STRING
name= 'Nguyen Viet Ha'
address="772 Kim Giang"
Phone="0348597151"
print(f"Name:{name}\nAddress:{address}\nPhone:{Phone}")
""" Name:Nguyen Viet Ha
    Address:772 Kim Giang
    Phone:0348597151
"""
    #Nếu chưa có thông tin thì thêm 1 ngoặc nhọn bên ngoài ( về sau muốn làm những chương trình lớn mà không bị lỗi thì nên để, sau khi hoàn thiện bộ khung thì điền thông tin sau)
print(f"Name:{{name}}\nAddress:{{address}}\nPhone:{{Phone}}")
""" Name:{name}
    Address:{address}
    Phone:{Phone}
"""
    #F-string cho phép thực hiện phép toán bên trong dấu ngoặc nhọn
m=10;n=20
print('s=m+n ='f"{m+n}") # 30 
print(f'{n+m=}') # kết quả sẽ in ra n+m=30 ( cho phép thực hiện phép tính bên trong dấu ngoặc và in ra phép tính)

    #Lấy số thập phân
import math
print(f"{math.pi:.2f}") #3.14

    #?ĐỊNH DẠNG BẰNG PHƯƠNG THỨC FORMAT
s='a:{},b:{},c:{}'.format(2,4,5) #Trong ngoặc có thể điền nhiều số hơn nhưng không được thiếu, và số thứ tự đánh từ (0 đến n-1)
print(s) # a:2,b:4,c:5
s='a:%s,b:%s,c:%s' %(2,4,5) #a:2,b:4,c:5

s1='a:{2},b:{0},c:{1}'.format('one','two','three')
s2='only one value:{1}'.format(0,3,5,6) # only one value: 3
s3='two same value:{1},{1}'.format(0,3,5,6) #two same value: 1,1
s4='a:{two},b:{one},c:{}'.format(one=111,two=222) #a:222,b:111

#Căn lề bằng format: Căn vè bên nào tức là để ký tự/chuỗi về bên đấy trước xong điền vào chỗ trống

'{:(c)^10}'.format('aaaa') #Căn lề giữa, chừa 10 đơn vị căn 'aaaa' vào giữa và chỗ trống bù đắp bằng (c)(nếu không điền thì sẽ tự động để trống)
'{:(c)>10}'.format('aaaa') #Căn lề phải, tương tự
'{:(c)<10}'.format('aaaa') #Căn lề trái
r='nguyen viet {:*^10} dep trai'.format("ha")
print(r) #nguyen viet ****ha**** dep trai
print("{:#>10.2f}".format(12.3)) #có thể kết hợp nếu muốn lấy số phần tập phân khi dùng format

