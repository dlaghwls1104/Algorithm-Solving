'''
7
35 

49 26 27 28 29 30 31
48 25 10 11 12 13 32
47 24 9 2 3 14 33
46 23 8 1 4 15 34
45 22 7 6 5 16 35
44 21 20 19 18 17 36
43 42 41 40 39 38 37
5 7
'''

def makesnail(n):
    global a,b
    snail = [[0]*n for i in range(n)]

    start = n**2
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]

    direction = 0
    x,y=0,0
    snail[x][y]=start
    start -=1

    while start>0:
        nx = x+dx[direction]
        ny = y+dy[direction]
        if  0 <= nx < n and 0 <= ny < n and  snail[nx][ny] == 0 :
            snail[nx][ny]=start
            if m == start:
                a,b=nx+1,ny+1
            x,y=nx,ny
            start -=1
        else:
            direction = (direction + 1)%4
    return snail
n = int(input())
m= int(input())
snail =makesnail(n)

for row in snail:
    print(*row)
print(a,b)
    
