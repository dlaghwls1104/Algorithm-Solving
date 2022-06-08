array = input()

for j in range(9,-1,-1):
    for i in array:
        if int(i) == j:
            print(int(i),end="")