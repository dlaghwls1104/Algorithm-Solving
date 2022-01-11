game=[list(map(int,input().split(" "))) for i in range(3)]

for i in range(3):
    if game[i].count(0)==4:
        print("D")
    elif game[i].count(0)==1:
        print("A")
    elif game[i].count(0)==2:
        print("B")
    elif game[i].count(0)==3:
        print("C")
    else:
        print("E")