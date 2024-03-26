import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_saldon_lataus_toimii(self):
        self.maksukortti.lataa_rahaa(1050)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.50)

    def test_saldo_muuttuu_jos_on(self):
        self.maksukortti.ota_rahaa(900)

        self.assertEqual(self.maksukortti.saldo_euroina(), 1.0)

    def test_saldo_ei_muutu_jos_ei_ole(self):
        self.maksukortti.ota_rahaa(1001)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_saldo_muutto_palaittaa_true_jos_rahaa_on(self):
        
        self.assertEqual(self.maksukortti.ota_rahaa(900), True)

    def test_saldo_muutto_palaittaa_false_jos_rahaa_ei_ole(self):
        
        self.assertEqual(self.maksukortti.ota_rahaa(1001), False)

    def test_saldon_tulostus(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")


