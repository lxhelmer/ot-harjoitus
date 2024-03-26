import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
    
    def test_luotu_kassapaate_raha_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_luotu_kassapaate_myydyt_oikein(self):
        self.assertEqual(self.kassa.edulliset + self.kassa.maukkaat, 0)


    def test_kateisosto_edullisesti_vaihtoraha_oikein(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(250), 10)

    def test_kateisosto_edulliseseti_kasvattaa_kassaa_oikein(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1002.4)
    
    def test_kateisosto_edullisesti_kasvattaa_myytyja(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kateisosto_edullisesti_raha_ei_riita_kassa_ei_muutu(self):
        self.kassa.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_kateisosto_edullisesti_raha_ei_riita_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(230), 230)

    def test_kateisosto_edullisesti_raha_ei_riita_myydyt_ei_muutu(self):
        self.kassa.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassa.edulliset, 0)



    def test_kateisosto_maukkaasti_vaihtoraha_oikein(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(410), 10)

    def test_kateisosto_maukkaasti_kasvattaa_kassaa_oikein(self):
        self.kassa.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1004.0)
    
    def test_kateisosto_maukkaasti_kasvattaa_myytyja(self):
        self.kassa.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kateisosto_maukkaasti_raha_ei_riita_kassa_ei_muutu(self):
        self.kassa.syo_maukkaasti_kateisella(390)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_kateisosto_maukkaasti_raha_ei_riita_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(230), 230)

    def test_kateisosto_maukkaasti_raha_ei_riita_myydyt_ei_muutu(self):
        self.kassa.syo_maukkaasti_kateisella(230)
        self.assertEqual(self.kassa.maukkaat, 0)


    def test_kortilla_edullisesti_tarpeeksi_rahaa_true(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), True)

    def test_kortilla_edullisesti_kasvattaa_myytyja(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kortilla_edullisesti_raha_ei_riita_false(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), False)

    def test_kortilla_edullisesti_raha_ei_riita_myydyt_ei_muutu(self):
        kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 0)


    def test_kortilla_maukkaasti_tarpeeksi_rahaa_true(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti), True)

    def test_kortilla_maukkaasti_kasvattaa_myytyja(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kortilla_maukkaasti_raha_ei_riita_false(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti), False)

    def test_kortilla_maukkaasti_raha_ei_riita_myydyt_ei_muutu(self):
        kortti = Maksukortti(200)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kassa_ei_muutu_kortilla_maukkaat(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_kassa_ei_muutu_kortilla_edulliset(self):
        kortti = Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_kortin_saldo_muuttuu_ladatessa(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, 200)
        self.assertEqual(kortti.saldo_euroina(), 12.0)

    def test_kassa_muuttuu_ladatessa(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, 200)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1002.0)

    def test_ei_positiivinen_lataus_ei_muuta_kortin_saldoa(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, -10)
        self.assertEqual(kortti.saldo_euroina(), 10.0)

    def test_ei_positiivinen_lataus_ei_muuta_kassaa(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, -10)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

