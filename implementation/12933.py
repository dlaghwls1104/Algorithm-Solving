# quqacukqauackck
# 2
duck =input()
cnt =0
visited = [False]*len(duck)

if len(duck) % 5 != 0:
    print(-1)
    exit()

def solve(n):
    global cnt
    first = True
    quack = 'quack'
    j = 0
    for i in range(n,len(duck)):
        if duck[i] == quack[j] and not visited[i]:
            visited[i] = True
            if duck[i] == 'k':
                if first:
                    cnt += 1
                    first = False
                j=0
    
            j+=1




for i in range(len(duck)):
    if duck[i] == 'q' and not visited[i]:
        solve(i)

if not all(visited) or cnt == 0:
    print(-1)
else:
    print(cnt)
