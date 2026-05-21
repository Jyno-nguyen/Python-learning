
#* Lambda: hàm nặc danh (anonymous) trả về một hàm
#! lambda argument_1, argument_2, …, argument_n : expression
#* là một dòng expression duy nhất
#* ưu tiên tạo ra các khối lệnh đơn giản

ave=lambda a,b,c:(a+b+c)/3
ave(1,2,3)

tich=lambda x,a=2: x**a
print(tich(2))   #4
print(tich(2,3)) #8

def member():
    mem=lambda x: x+' is member of team'
    return mem
call_mem=member()
print(call_mem("jyno")) #Jyno is member of team
print(call_mem("ha"))   #ha is member of team


lst=[lambda x:x**2,lambda x:x**3]
print(lst) #[<function <lambda> at 0x7f42bf5e8180>, <function <lambda> at 0x7f42bf5e8220>]
print(lst[0]) #<function <lambda> at 0x78e29991c180>
print(lst[0](2)) #2**2=4
#*Câu trên nếu muốn dùng def
def f1(x):
    return x**2
def f2(x):
    return x**3
lst=[f1,f2]
print(lst[0](2)) #4
print(lst[-1](2))#8
#!Hoặc 
for func in lst:
    print(func(3)) #9 27


#*Cũng có thể sử dụng với dict
k='so1'
dic={"so1":lambda:1,"so2":lambda:2,"so3":lambda:3}
print(dic[k]()) #1
                 #!Phần agr để trống () là đúng cú pháp vì là optional không bắt buộc
#*Nếu muốn dùng def cho hàm trên
def f1():
    return 1
def f2():
    return 2
def f3():
    return 3
k="so1"
dic={"so1":f1,"so2":f2,"so3":f3}
print(dic[k]())




#*Câu điều kiện cho lambda
so_lon=lambda x,y: x if x>y else y
print(so_lon(3,4))

#!Kiểm tra xem có cùng ước là 2 và 3 không nếu có trả về 1 , else 0
ktra=lambda x: (1 if x%2==0 else 0) if x%3==0 else 0 #chạy điều kiện bên ngoài trước rồi mới chạy điều kiện bên trong
ktra=lambda x: 1 if (x%2==0 and x%3==0) else 0
ktra=lambda x: (1 if not x%2 else 0) if not x%3 else 0

def ktra(x):
    if x%3==0:
        if x%2==0:
            return 1
        else:
            return 0
    else:
        return 0
    



#*Lambda chồng lambda
def member(mem1):
    return lambda mem2: mem1+' '+mem2
member1=member("Jyno")
print(member1("Viet Ha"))


ds=lambda so1: (lambda so2 : so1+so2)
ds1=ds(5)
print(ds1(4)) #9