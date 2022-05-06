result = list(range(1,31))


for i in range(28):
    n=int(input())
    if n in result:
        result.remove(n)

print(result[0])
print(result[1])