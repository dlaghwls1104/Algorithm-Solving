number_list=[]
for _ in range(7):
    number=int(input())
    number_list.append(number)

sum=0
result=[]
for i in number_list:
    if i % 2 != 0:
        result.append(i)
        sum+=i
if result : 
    print(sum)
    print(min(result))

else:
    print(-1)