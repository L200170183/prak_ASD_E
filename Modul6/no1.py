from no2sub import Mahasiswa
from a import urut

c0 = Mahasiswa('ika',10,'sukoharjo',240000)
c1 = Mahasiswa('budi',51,'sragen',230000)
c2 = Mahasiswa('ahmad',2,'surakarta',250000)
c3 = Mahasiswa('chandra',18,'surakarta',234000)
c4 = Mahasiswa('eka',4,'boyolali',240000)
c5 = Mahasiswa('fandi',31,'salatiga',250000)
c6 = Mahasiswa('deni',13,'klaten',245000)
c7 = Mahasiswa('galuh',5,'wonogiri',245000)
c8 = Mahasiswa('janto',23,'klaten',245000)
c9 = Mahasiswa('hasan',64,'karanganyar',270000)
c10 = Mahasiswa('khalid',29,'purwodadi',265000)

NIMmhs = [c0.NIM,c1.NIM,c2.NIM,c3.NIM,c4.NIM,c5.NIM,c6.NIM,c7.NIM,c8.NIM,c9.NIM,c10.NIM]
USmhs = [c0.uangSaku,c1.uangSaku,c2.uangSaku,c3.uangSaku,c4.uangSaku,c5.uangSaku,c6.uangSaku,
         c7.uangSaku,c8.uangSaku,c9.uangSaku,c10.uangSaku]

a1 = urut(NIMmhs)
b2 = urut(USmhs)

a1.printMerge(NIMmhs)
b2.printMerge(USmhs)

a1.printQuick(NIMmhs)
b2.printQuick(USmhs)
