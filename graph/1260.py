n,m,v=map(int,input().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(len(graph)):
    graph[i].sort()    
    

def dfs(graph,start):
    need_visit =[]
    visited = []
    need_visit.append(start)
    while need_visit:
        node= need_visit.pop()
        if node not in visited:
            visited.append(node)
            a= list(reversed(graph[node]))
            need_visit.extend(a)
    print(*visited)
    
def bfs(graph,start):
    need_visit =[]
    visited = []
    need_visit.append(start)
    while need_visit:
        node= need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    print(*visited)




dfs(graph,v)
bfs(graph,v)
