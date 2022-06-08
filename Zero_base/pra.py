array=[0 for _ in range(11)]
array[0]=0
array[1]=1
for i in range(1,10):
    array[i+1]=array[i]+array[i-1]

print(array)