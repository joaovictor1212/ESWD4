# -*- coding: utf-8 -*-

import pytest
from gilded_rose import AgedBrie, Conjured, Sulfuras, Tickets
from collections import namedtuple
import sys


ItemValues = namedtuple("ItemValues", ["sell_in", "quality"])


@pytest.mark.parametrize(
    "item, expected_values",
    [
        [
            Sulfuras(), 
            [
                ItemValues(sell_in=0, quality= 80),
                ItemValues(sell_in=0, quality= 80),
                ItemValues(sell_in=0, quality= 80),
                ItemValues(sell_in=0, quality= 80)
            ],
        ],
        [
            AgedBrie(sell_in=2, quality=0), 
            [
                ItemValues(sell_in=2, quality= 0),
                ItemValues(sell_in=1, quality= 1),
                ItemValues(sell_in=0, quality= 2),
                ItemValues(sell_in=-1, quality= 4),
                ItemValues(sell_in=-2, quality= 6),
            ],
        ],
        [
            Tickets(
                "Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20
            ),
            [
                ItemValues(sell_in=15, quality= 20),
                ItemValues(sell_in=14, quality= 21),
                ItemValues(sell_in=13, quality= 22),
                ItemValues(sell_in=12, quality= 23),
                ItemValues(sell_in=11, quality= 24),
                ItemValues(sell_in=10, quality= 25),
                ItemValues(sell_in=9, quality= 27),
                ItemValues(sell_in=8, quality= 29),
                ItemValues(sell_in=7, quality= 31),
                ItemValues(sell_in=6, quality= 33),
                ItemValues(sell_in=5, quality= 35),
                ItemValues(sell_in=4, quality= 38),
                ItemValues(sell_in=3, quality= 41),
                ItemValues(sell_in=2, quality= 44),
                ItemValues(sell_in=1, quality= 47),
                ItemValues(sell_in=0, quality= 50),
                ItemValues(sell_in=-1, quality= 0)
            ],
        ],
        [
            Conjured("Conjured Mana Potion", sell_in=2, quality=20), 
            [
                ItemValues(sell_in=2, quality= 20),
                ItemValues(sell_in=1, quality= 18),
                ItemValues(sell_in=0, quality= 16),
                ItemValues(sell_in=-1, quality= 12),
                ItemValues(sell_in=-2, quality= 8)
            ],
    ],
    ],
)
def test_items(item, expected_values):
    for values in expected_values:
        item.quality == values.quality
        item.sell_in == values.sell_in
        item.next_day()