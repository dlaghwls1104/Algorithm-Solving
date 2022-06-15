bird=int(input())

result=0
i=1
while bird != 0:
    if bird < i:
        i=1
        bird -= i
        i+=1
        result += 1

    else:
        bird -= i
        i+=1
        result += 1

print(result)
