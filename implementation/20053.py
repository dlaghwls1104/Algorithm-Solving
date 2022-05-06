n = int(input())

for i in range(n):
    m=int(input())
    s = list(map(int,input().split()))
    s.sort()
    min=s[0]
    max=s[len(s)-1]
    print(min,max)