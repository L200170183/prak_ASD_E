class mhsTIF():
    def __init__(self, nama, asal, uang):
        self.nama = nama
        self.asal = asal
        self.uang = uang

c0 = mhsTIF('aaa','Sukoharjo',240000)
c1 = mhsTIF('bbb','Klaten', 260000)
c2 = mhsTIF('ccc','Salatiga',280000)
c3 = mhsTIF('ddd','Klaten',200000)
c4 = mhsTIF('eee','Surakarta',200000)
c5 = mhsTIF('fff','Salatiga',290000)
c6 = mhsTIF('ggg','Surakarta',230000)

daftar = [c0,c1,c2,c3,c4,c5,c6]

#NOMOR 1
def cari(n):
    baru = []
    for i in range(len(n)):
        if(n[i].asal.lower() == 'Klaten'):
            baru.append(i)
    return baru


#NOMOR 2
def uangKcl(n):
    baru = n[0].uang
    for i in range(len(n)):
        if(n[i].uang<baru):
            baru = n[i].uang
    return baru

#NOMOR 3
def uangKcl2(n):
    baru = n[0].uang
    list = []
    for i in range(len(n)):
        if(n[i].uang==baru):
            list.append(n[i].nama)
        elif(n[i].uang<baru):
            baru = n[i].uang
            list = []
            list.append(n[i].nama)
    return list

#NOMOR 4
def uangKrg(n):
    batas = 250000
    list = []
    for i in range(len(n)):
        if(n[i].uang < batas):
            list.append(n[i].nama)
    return list
print(cari(daftar))
print(uangKcl(daftar))
print(uangKcl2(daftar))
print(uangKrg(daftar))
