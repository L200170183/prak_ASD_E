def rata(b=[]):
    x=0
    n=0
    if b != []:
        for i in b:
            x+=i
            n+=1
        return x/n
    return "illegal"
print(rata([2,2]))
