from MhsTIF import MhsTIF
import sys

mhs1 = MhsTIF('1',123,'Surakarta',240000)
mhs2 = MhsTIF('2',234,'Surakarta',240000)
mhs3 = MhsTIF('3',345,'Surakarta',240000)
mhs4 = MhsTIF('4',456,'Surakarta',240000)
mhs5 = MhsTIF('5',567,'Surakarta',240000)
mhs6 = MhsTIF('6',678,'Surakarta',240000)
mhs7 = MhsTIF('7',789,'Surakarta',240000)
mhs8 = MhsTIF('8',890,'Surakarta',240000)
mhs9 = MhsTIF('9',198,'Surakarta',240000)
mhs10 = MhsTIF('10',987,'Surakarta',240000)

Daftar = [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6, mhs7, mhs8, mhs9, mhs10]

def urutkan(A):
    baru = {}
    
    for i in range(len(A)):
        baru[A[i].nama] = A[i].NIM
    listofTuples = sorted(baru.items(), key = lambda x: x[1])
    for elem in listofTuples :
        print(elem[0] , ":" , elem[1])

urutkan(Daftar)
