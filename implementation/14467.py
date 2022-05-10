n = int(input())
cnt = 0
dic={}
for i in range(n):
    a,b = map(int,input().split())
    if a in dic.keys() and dic[a] != b:
        cnt+=1
    dic[a] = b

print(cnt)