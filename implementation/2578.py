# 빙고판
'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18

'''
# 빙고 부르는 순서
'''
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''
cnt = 0
board=[]
board=[list(map(int,input().split())) for i in range(5)]
check=[[0]*5 for i in range(5)]

dic={}
for i in range(5):
    for j in range(5):
        dic[board[i][j]] = (i,j) 

bingo = [list(map(int,input().split())) for i in range(5)]

for k in range(5):
    for l in range(5):
        result = dic[bingo[k][l]] 
        check[result[0]][result[1]] = 1

        for z in range(5):
            if sum(check[z]) == 5:
                cnt +=1
            if sum([j[z] for j in check]) == 5:
                cnt+=1
        if check[0][4]+check[1][3]+check[2][2]+check[3][1]+check[4][0] == 5:
            cnt+=1
        if check[0][0]+check[1][1]+check[2][2]+check[3][3]+check[4][4] == 5:
            cnt+=1

if cnt >= 3:
    print(bingo[k][l])
            
            

            

        

