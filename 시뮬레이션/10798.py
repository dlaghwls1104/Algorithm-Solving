'''
A A B C D D
a f z z 
0 9 1 2 1
a 8 E W g 6
P 5 h 3 k x
'''
word= [input() for i in range(5)]

for i in range(15):
    for j in range(5):
        if i < len(word[j]):
            print(word[j][i],end="")
