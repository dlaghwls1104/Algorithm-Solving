A=int(input())

array=[list(map(int,input().split(" "))) for i in range(A)]

for i in array:
    i.sort(reverse=True)
    result=i[2]
    print(result)