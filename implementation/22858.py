N,K = map(int,input().split())

s = list(map(int,input().split()))
d = list(map(int,input().split()))
p = [0]*N



for j in range(K):
    for i in range(N):
        p[d[i]-1]=s[i]
    if j == K-1:
        break
    else:
        s = p
        p= [0]*N
print(*p)