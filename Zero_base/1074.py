array =[[0]*2 for _  in range(2)]


def recursive(x):
    k=0
    j=0
    for i in range(x):
        if k <2:
            array[0][k] = i
            k += 1
        else:
            array[1][j] =i
            j+=1
    print(array)

recursive(4)