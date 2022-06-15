n=int(input())

best = [input() for i in range(n)]

book=dict()

result=1
for i in best:
    if i in book:
        book[i]=book[i]+1
    else:
        book[i] = result
target= max(book.values())
array=[]

for book,number in book.items():
    if number==target:
        array.append(book)
print(sorted(array)[0])