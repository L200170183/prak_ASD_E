class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'

    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2

class SiswaSMA(Manusia):
    def __init__(self, nama, NIS, umur, sangu):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nisn = NISN
        self.umur = umur
        self.sangu = sangu

    def __str__(self):
        s = self.nama +', NIS '+str(self.nis)\
            +'. Berumur '+ str(self.umur) \
            +'. Uang saku Rp. '+ str(self.sangu)\
            +' tiap harinya.'
        return s

    def tahunlahir(self):
        thnskr = date.today().year
        tl = thnskrng - self.umur
        return tl
