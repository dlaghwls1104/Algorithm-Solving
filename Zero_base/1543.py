n=input()
word=input()

index=0
result=0

while len(n)- index >= len(word):
    if n[index:index+len(word)]==word:
        result += 1
        index+=len(word)
    else:
        index += 1

print(result)