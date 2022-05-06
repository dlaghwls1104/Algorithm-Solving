n=int(input())
prime=list(map(int,input().split(" ")))
result=0
for i in prime:
    not_prime=0
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                not_prime+=1           
        if not_prime == 0:
            result+=1

print(result)

