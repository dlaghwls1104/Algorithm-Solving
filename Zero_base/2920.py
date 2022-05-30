song = list(map(int,input().split(" ")))
ascending = False
decending = False

for i in range(7):
    if song[i] > song[i+1]:
        decending = True
    else:
        ascending = True


if decending and ascending:
    print('mixed')
elif decending:
    print('descending')
elif ascending:
    print('ascending')
