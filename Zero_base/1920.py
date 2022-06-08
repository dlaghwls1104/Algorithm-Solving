n= int(input())
m = set(map(int,input().split()))

k= int(input())
l = list(map(int,input().split()))

for i in l:
    if i not in m:
        print(0)
    else:
        print(1)