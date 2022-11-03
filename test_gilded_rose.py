# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item
from sulfuras import Sulfuras
from aged_brie import AgedBrie



dex = "+5 Dexterity Vest"
age = "Aged Brie"
elixir = "Elixir of the Mongoose"
sulf = "Sulfuras, Hand of Ragnaros"
back_stage = "Backstage passes to a TAFKAL80ETC concert"
conj_mana = "Conjured Mana Cake"


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras(self):
        item = Sulfuras(0, 80)
        assert item.name == sulf
        assert item.quality == 80
        assert item.sell_in == 0

        item.next_day()
        assert item.quality == 80
        assert item.sell_in == 0


    def test_agedbrie(self):
        item = AgedBrie(sell_in=2, quality=0)

        assert item.name == age
        assert item.quality == 0
        assert item.sell_in == 2

        item.next_day()
        assert item.quality == 1
        assert item.sell_in == 1

        item.next_day()
        assert item.quality == 2
        assert item.sell_in == 0

        item.next_day()
        assert item.quality == 4
        assert item.sell_in == -1




        
if __name__ == '__main__':
    unittest.main()