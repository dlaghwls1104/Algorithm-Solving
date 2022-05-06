import sys
 
input = sys.stdin.readline
n,m = map(int,input().split())
light = list(map(int,input().split()))
a=[]
for i in range(m):
    a.append(list(map(int,input().split())))

for j in range(m):
    if a[j][0] == 1:
        light[a[j][1]-1] = a[j][2]

    elif a[j][0] == 2:
        for i in range(a[j][1]-1,a[j][2]+1):
            if light[i] == 0:
                light[i] = 1
            else:
                light[i] = 0
    elif a[j][0] == 3:
        for i in range(a[j][1]-1,a[j][2]):
            light[i] = 0
    else:
        for i in range(a[j][1]-1,a[j][2]):
            light[i] = 1

print(light)
print(a)

# [0, 1, 0, 1, 0, 0, 0, 0]
# a[j][0]