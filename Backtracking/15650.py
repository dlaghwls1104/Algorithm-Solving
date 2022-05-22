

n,m =map(int,input().split())

s=[]
def dfs(start):
    if m == len(s):
        num=' '.join(map(str,s))
        print(num)
        return 
    for i in range(start+1,n+1):
        if i not in s:
            s.append(i)
            dfs(i)
            s.pop()

dfs(0)
