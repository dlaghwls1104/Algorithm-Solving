n = int(input())
aslist = []
for _ in range(n):
    i = int(input())
    aslist.append(i)

a=sorted(aslist)

for i in a:
    print(i)