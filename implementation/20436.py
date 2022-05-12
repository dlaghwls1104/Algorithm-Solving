l,r = input().split()
letter = input()
dic = {}
a=['q','w','e','r','t','y','u','i','o','p']
b=['a','s','d','f','g','h','j','k','l','none']
c=['z','x','c','v','b','n','m','none','none','none']

list=[a,b,c]
time = 0

for i in range(3):
    for j in range(10):
        dic[list[i][j]]=(i,j)
x,y = dic[l]
n,m = dic[r]
 #자음
ja=['q','w','e','r','t','a','s','d','f','g','z','x','c','v']
for i in letter:
    if i in ja:
        time +=1
        a,b=dic[i]
        time += abs(x-a)+abs(y-b)
        x,y = a,b
    else:
        time+=1
        a,b=dic[i]
        time += abs(n-a)+abs(m-b)
        n,m = a,b

print(time)
#모음  zoac
#mo=['y','u','i','o','p','h','j','k','l','b','n','m']

