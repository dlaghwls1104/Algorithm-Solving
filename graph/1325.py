n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


result=[]
def bfs(graph,start):
    visited=[]
    need_visited=[]
    cnt = 0
    need_visited.append(start)
    while need_visited:
        node = need_visited.pop(0)
        if node not in visited:
            visited.append(node)
            cnt += 1
            need_visited.extend(graph[node])
    return cnt
for i in range(1,n+1):
    result.append(bfs(graph,i))

max = max(result)
for i in range(0,n):
    if result[i] == max:
        print(i+1,end=" ")