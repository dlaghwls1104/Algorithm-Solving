n = int(input())

online=[]
for i in range(n):
    a,b = input().split(" ")
    online.append((int(a),b))

online = sorted(online, key=lambda x:x[0])

for i,j in online:
    print(i,j)
    