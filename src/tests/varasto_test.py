import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_pienentaa_saldoa(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.ota_varastosta(4)
        self.assertAlmostEqual(self.varasto.saldo, 6)

    def test_ei_voi_lisata_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus+20)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ei_voi_ottaa_liikaa_tavaraa(self):
        self.varasto.ota_varastosta(self.varasto.tilavuus+20)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_paljonko_mahtuu_palauttaa_oikean_tuloksen(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(self.varasto.saldo, 3)

    def test_str_palauttaa_oikein(self):
        self.varasto.lisaa_varastoon(7)
        self.assertEqual(f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}", str(self.varasto))

    def test_uudella_varastolla_oikea_saldo(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ei_voi_olla_negatiivinen_tilavuus(self):
        self.varasto=Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_alku_saldo_positiivinen(self):
        self.varasto=Varasto(10, -10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_alku_saldo_suurempi_kuin_tilavuus(self):
         self.varasto = Varasto(10, 20)
         self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ei_voi_ottaa_negatiivista_maaraa(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-10), 0)
    def test_ei_voi_lisata_negatiivista_maaraa(self):
        self.assertEqual(self.varasto.lisaa_varastoon(-10), None)


