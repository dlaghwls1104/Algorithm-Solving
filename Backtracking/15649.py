n,m = map(int,input().split())

word=[]
def dfs():
    if m == len(word):
        print(' '.join(map(str,word)))
        return
    for i in range(1,n+1):
        if i not in word:
            word.append(i)
            dfs()
            word.pop()
dfs()