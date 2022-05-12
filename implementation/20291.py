n = int(input())
list = []
for i in range(n):
    file = input()
    list.append(file)

dic = {}
cnt = 0
for i in list:
    a,b = i.split(".")
    if b in dic:
        dic[b] += 1
    else:
        dic[b] = 1
dic = sorted(dic.items(), key=lambda x: x[0])

for i in dic:
    print(i[0],i[1])
