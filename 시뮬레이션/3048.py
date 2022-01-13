n,m=map(int,input().split())
first=input()
second=input()
t=int(input())
list=[]
for i in range(n,0,-1):
    list.append(first[i-1])
for j in range(m):
    list.append(second[j])
if t == 0:
    result="".join(list)
    print(result)
elif t==1 :
    for i in range(t):
        list[n-1-i],list[n-i]=list[n-i],list[n-1-i]
    result="".join(list)
    print(result)

else:
    for i in range(t):
        list[n-1-i],list[n-i]=list[n-i],list[n-1-i]
        list[m-1],list[m-1+i]=list[m-1+i],list[m-1]
    result="".join(list)
    print(result)