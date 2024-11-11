# pylint: disable=locally-disabled, missing-module-docstring, missing-class-docstring, missing-function-docstring

import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_palauttaa_oikean_pelaajan(self):
        pelaaja = self.stats.search("Kurri")
        self.assertEqual(pelaaja.name, "Kurri")

    def test_search_palauttaa_none_jos_pelaajaa_ei_ole(self):
        pelaaja = self.stats.search("aaaaaa")
        self.assertIsNone(pelaaja)

    def test_team_haku_palauttaa_joukkueen_pelaajat(self):
        pelaajat = self.stats.team("EDM")
        self.assertEqual(len(pelaajat), 3)

    def test_team_haettua_joukkuetta_ei_ole(self):
        pelaajat = self.stats.team("AAA")
        self.assertEqual(len(pelaajat), 0)

    def test_top_palauttaa_oikean_maaran_pelaajia(self):
        pelaajat = self.stats.top(2)
        self.assertEqual(len(pelaajat), 3)
