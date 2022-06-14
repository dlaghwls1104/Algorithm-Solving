import copy
operators=[]
def recur(arr,m):
    if len(arr)==m:
        operators.append(copy.deepcopy(arr))
        return

    arr.append(' ')
    recur(arr, m)
    print(arr)
    arr.pop()

    arr.append('+')
    recur(arr, m)
    print(arr)
    arr.pop()

    arr.append('-')
    recur(arr, m)
    print(arr)
    arr.pop()
    
recur([],2)