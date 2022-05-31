n= int(input())
for _ in range(n):
    word = input()

    word_stack=[]
    word_pop=[]
    for i in word:
        if i !='<' and i !='>' and i != '-':
            word_stack.append(i)
        elif i == '<':
            if word_stack:  
                word_pop.append(word_stack.pop())
        elif i == '>':
            if word_pop:
                word_stack.append(word_pop.pop())
        elif i == '-':
            if word_stack: 
                word_stack.pop()

    answer = "".join(word_stack)+"".join(reversed(word_pop))
    print(answer)
