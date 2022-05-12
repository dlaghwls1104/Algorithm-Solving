'''
8
0 1 0 1 0 0 0 1
2
1 3
2 3
'''

'''
1 0 0 0 1 1 0 1

'''

import sys
 
input = sys.stdin.readline

def switching(n):
    if n==0:
        return 1
    else :
        return 0

n = int(input())
light = list(map(int,input().split()))

switch = int(input())
for _ in range(switch):
    a,b = map(int,input().split())
    if a == 1:
        for i in range(b,len(light),b):
            if light[i-1] == 0:
                light[i-1] = 1
            else:
                light[i-1] = 0
    if a == 2:
        light[b-1] = switching(light[b-1])
        for i in range(1,b):
            if light[b-1-i] == light[b-1+i]:
                light[b-1-i] = switching(light[b-1-i])
                light[b-1+i] =switching(light[b-1+i])
            else:
                break
print(*light)
            

#한번만 [0, 1, 1, 1, 0, 1, 0, 1]
#[1, 0, 1, 0, 1, 1, 0, 1]
#[0, 0, 0, 0, 0, 1, 0, 1]