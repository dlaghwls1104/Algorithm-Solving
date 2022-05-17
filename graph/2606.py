com = int(input())
n=int(input())

graph = [[] for i in range(com+1)]
for _ in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visitied = []
need_visited=[]
cnt=0
def dfs(graph,start):
    global cnt
    need_visited.append(start)
    while need_visited:
        node= need_visited.pop(0)
        if node not in visitied:
            visitied.append(node)
            cnt+=1
            need_visited.extend(graph[node])    
    return cnt-1

print(dfs(graph,1))


