def hitung(x):
    vokal='aiueoAIUEO'
    bb=0
    for i in x:
        if i not in vokal:
            bb+=1
    return (len(x), bb)

print(hitung('surakarta'))
