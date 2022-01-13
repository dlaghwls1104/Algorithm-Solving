n,m=map(int,input().split())
first=input()
second=input()
t=int(input())
list=[]
for i in range(n,0,-1):
    list.append(first[i-1])
for j in range(m):
    list.append(second[j])
result="".join(list)
if t == 0:
    print(result)
else:
    temp=result[n-1]
    result[n-1]=result[m]
    result[m]=temp
    print(temp)