n = int(input())
array=[]
for i in range(n):
    a,b=map(int,input().split(" "))
    array.append((a,b))

array = sorted(array)


for i,j in array:
    print(i,j)