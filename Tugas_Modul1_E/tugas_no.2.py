def persegi_panjang(x,y):
    for i in range (x):
        if i == 0 or i == x-1:
            print ('@'*y)
        else:
            print ('@'+' '*(y-2)+'@')
            
persegi_panjang(4,5)
