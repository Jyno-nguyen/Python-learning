
#* Input: A3B4CD11E
#* Output:AAABBBBCDD..DE
#*C1
m="A3B4CD11E"
i=0
new=[]
while i<len(m) and m[i].isalpha():
    char=m[i]
    num=''
    while i+1<len(m) and m[i+1].isdigit():
        num+=m[i+1]
        i+=1
    new.append(f"{char*int(num)}" if num!='' else char)
    i+=1
print(''.join(new))

#*
mahoa="A5BCD11"
processed=''
for char in mahoa:
    processed+=" "+ char if char.isalpha() else char #!Tách ra thành "A5 B C D11"
new=[]
for st in processed.split():
    num=int(st[1:]) if st[1:]!='' else 1
    new.append(st[0]*num)
print(''.join(new))

#!Cách dùng biến cờ



#* Input: AAABBBBCDD..DDE
#* Output:A3B4CD11E
inp="AAABBBBCDDDDDDDDDDDE"
count=1
new=[]
for i in range(len(inp)):
    char=inp[i]
    if i+1<len(inp) and inp[i]==inp[i+1]:
        count+=1
    else:
        new.append(f"{char}{count}" if count>1 else char)
print("".join(new))
print(new)

#!zip(text,text[1:])
n="ABBCCCDDDDE"
num=1
new=[]
if not n:
    print("None")
for a,b in zip(n,n[1:]):
    if a==b:
        num+=1
    else:
        new.append(f"{a}{num}" if num>1 else a)
        num=1
new.append(f"{a}{num}" if num>1 else n[-1])
print("".join(new))

#!Cách dùng biến cờ, dùng zip





