# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Sulfuras, GildedRose

dex = "+5 Dexterity Vest"
age = "Aged Brie"
elixir = "Elixir of the Mongoose"
sulf = "Sulfuras, Hand of Ragnaros"
back_stage = "Backstage passes to a TAFKAL80ETC concert"
conj_mana = "Conjured Mana Cake"


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras(self):
        items = Sulfuras()
        assert items.name == "Sulfuras, Hand of Ragnaros"
        assert items.quality == 80
        assert items.sell_in == 0

        items.next_day()

        
if __name__ == '__main__':
    unittest.main()