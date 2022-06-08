n = int(input())
array=[0 for _ in range(n+1)]
array[0]=0
array[1]=1
for i in range(1,n):
    array[i+1]=array[i]+array[i-1]
        
print(array[-1])
        