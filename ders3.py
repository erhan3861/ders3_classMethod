
class Kurs():
    kurslar = []

    def __init__(self, kurs_adi, kurs_fiyati, kontenjan):
        self.kurs_adi = kurs_adi
        self.kurs_fiyati = kurs_fiyati
        self.kontenjan = kontenjan
        self.ogrenciler = []

    @classmethod
    def kurs_ekle(cls, kurs_adi, kurs_fiyati, kontenjan):
        yeni_kurs = cls(kurs_adi, kurs_fiyati, kontenjan)
        cls.kurslar.append(yeni_kurs)
        print(f"{kurs_adi} kursu eklendi.")

    def kayit_ol(self, ogr_adi):
        if self.kontenjan > 0:
            self.ogrenciler.append(ogr_adi) 
            print(f"{ogr_adi} isimli öğrenci, {self.kurs_adi} kursuna kayıt oldu.")
            self.kontenjan -= 1
        else:
            print(f"{self.kurs_adi} kursu dolu. Kayıt yapılamadı.")


# ana bölüm
Kurs.kurs_ekle("Python Programlama", 500, 1)
Kurs.kurs_ekle("Veri Bilimi", 800, 8)
Kurs.kurs_ekle("Web Geliştirme", 600, 12)

# Kayıt Ol
kurs1 = Kurs.kurslar[0] 
kurs2 = Kurs.kurslar[1]
kurs3 = Kurs.kurslar[2]

kurs1.kayit_ol("Ahmet")
kurs1.kayit_ol("Çağlar")

