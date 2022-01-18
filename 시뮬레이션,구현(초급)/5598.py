after=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
before =["D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C"]



word=input()
result=[]
for i in word:
    for j in range(len(before)):
        if before[j] == i:
            result.append(after[j])

result="".join(result)
print(result)
