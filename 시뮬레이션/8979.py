n,k=map(int,input().split())

country=[list(map(int,input().split())) for i in range(n)]
country.sort(key=lambda x:(-x[1],-x[2],-x[3]))


for i in range(n):
    if country[i][0] == k:
        number=i

for i in range(n):
    if country[number][1:]==country[i][1:]:
        print(i+1)
        break


