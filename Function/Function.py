
#*def <function_name>(parameter_1 , parameter_2 , .., parameter_n ):

#    function-block

#!TƯỜNG MINH
#!MODULE HOÁ
#!KIỂM SOÁT TỐT
#!DỄ CHỈNH SỦA

def kteam():
    pass #!(Placeholder statement) giúp cho khối lệnh block không bị thiếu trong trường hợp bạn chưa biết viết gì cho phù hợp


def pri():
    print("Nguyen Viet Ha")
pri() # Nguyen Viet Ha


def func1(text): #!Kiểu tự do hoàn toàn bạn có thể truyền vào bất kể kiểu dữ liệu gì mà bạn muốn
    print(text)
func1([1,2,3,4])
func1({"coca":14})


def P(SomeThing: str) -> None: #!Type hints: gợi ý kiểu dữ liệu không nhập đúng cũng không sao
                               #!None: Hàm này chỉ làm nhiệm vụ in ấn, không trả về bất kỳ một giá trị nào(bình thường không cần ghi làm gì)
                               #!Mặc định hàm không có return sẽ trả về giá trị None
    print(SomeThing)
t=P
t is P #! True: chỉ là đặt thêm một cái tên rồi cùng trỏ vào hàm def
t(89)  # 89


def kteam(name, greating='Hi'): #!Defaule argument: phải để ở hàng sau cùng
    print(greating, name + '!')
kteam("Nguyen Viet Ha") #Hi Nguyen Viet Ha! 
                        #! Nếu không truyền giá trị sẽ trả về default
kteam("Nguyen Viet Ha","Hello") #Hello Nguyen Viet Ha!

#!Defaule argument là một unhashable container và nó không được refresh
def f(kteam=[]):
    kteam.append('F')
    print(kteam)
f() #['F']
f() #['F', 'F']
f() #['F', 'F', 'F']
f([1, 2, 3]) #[1, 2, 3, 'F'] #!Nếu truyền vào giá trị thì nó hoạt động bình thường và bỏ qua default
f() #['F', 'F', 'F', 'F']

iter1=[]
def f(kteam=iter1):
    kteam.append('F')
    print(kteam)
f() #['F']
f() #['F', 'F']
f() #['F', 'F', 'F']
f([1, 2, 3]) #[1, 2, 3, 'F']
f() #['F', 'F', 


#* sort()
def compare(value: str) -> int:
    return len(value)
a = ['abb', 'z', 'tt', 'ryu']
a.sort(key=compare) # ['z', 'tt', 'abb', 'ryu']


def compare(value: list) -> int:
    return sum(value)
a = [[3, 4, 2], [1, 2, 4], [3, 2, -3], [-1, 4, 3]]
a.sort(key=compare, reverse=True) # Sắp xếp một ma trận gồm nhiều list dựa vào tổng các phần tử trong các list đó
print(a) #[[3, 4, 2], [1, 2, 4], [-1, 4, 3], [3, 2, -3]]

