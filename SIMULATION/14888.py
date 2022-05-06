n = int(input())
num=list(map(int,input().split()))
oper=list(map(int,input().split()))
# + - x /

i=0
result=0

if oper[0] != 0:
    result = num[i]+num[i+1]
    oper[0] -= 1
    i+=1
    if i < len(num):
        i=0
elif oper[1] != 0:
    result -= num[i]
    oper[1] -= 1
    i+=1
elif oper[2] != 0:
    result *= num[i]
    oper[2] -= 1
    i+=1
    if i < len(num):
        i=0
elif oper[3]!= 0:
    result /= num[i]
    oper[3] -= 1
    i+=1

print(result)