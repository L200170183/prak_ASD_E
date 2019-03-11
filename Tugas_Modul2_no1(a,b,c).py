class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object
    """

    def __init__(self,sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku Mempunyai', len(self.teks),'karakter.')
    def perbarui(self,stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self,bro):
        if bro in self.teks():
            return True
        else:
            return False
    def hitungKonsonan(self):
        kon = "bcdfghjklmnpqrstvwxyzBCDFGHKLMNPQRSTVWXYZ"
        jum = 0
        for i in self.teks:
            if i in kon:
                jum += 1
        return jum
    def hitungVokal(self):
        vok = "aiueAIUEO"
        jum = 0
        for i in self.teks:
            if i in vok:
                jum += 1
        return jum
    
p9 = Pesan('Indonesia adalah negeri yang indah')
p10 = Pesan('Surakarta')
