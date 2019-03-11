class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'

    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku', self.nama)
    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2


class Mahasiswa(Manusia):
    """Class yang dibangun dari class Manusia"""

    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kota = kota
        self.us = us

    def __str__(self):
        s = self.nama +', NIM '+str(self.NIM)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s

    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.us
    def tambahUangSaku(self, tambahUang):
        self.us += tambahUang
    def ambilKotaTinggal(self):
        return self.kota
    def perbaruiKotaTinggal(self, kotabaru):
        self.kota = kotabaru
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa jika sambil belajar ."""
        print("Saya baru saja makan",s,"sambil menonton tv")
        self.keadaan = 'kenyang'


a = input("Masukkan nama: ")
b = input("Masukkan nim: ")
c = input("Masukkan kota tinggal: ")
d = input("Masukkan uang saku: ")

x = Mahasiswa(a,b,c,d)
print (x)
