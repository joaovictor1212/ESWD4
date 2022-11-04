# -*- coding: utf-8 -*-


from typing import List
import sys
from importlib import reload


class Item:
    name: str 
    degradation: int = 1
    quality_min: int = 0
    quality_max: int = 50

    def __init__(self,name: str, sell_in: int, quality: int):
        assert quality >= self.quality_min
        assert quality <= self.quality_max

        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def next_day(self):
        self.sell_in -= 1
        
        diff = self.degradation
        if self.sell_in < 0:
            diff *= 2

            self.quality = self.quality - diff
            self.quality = max(self.quality_min, self.quality)
            self.quality = min(self.quality_max, self.quality)


class AgedBrie(Item):
    degradation = -1

    def __init__(self, sell_in: int, quality: int):
        super().__init__("Aged Brie", sell_in, quality)


class Conjured(Item):
    degradation = -2


class Sulfuras(Item):
    degradation = 0
    quality_min = 80
    quality_max = 80

    def __init__(self):
        super().__init__("Sulfuras, Hand of Ragnaros", sell_in=0,quality=80)

    def next_day(self):
        super().next_day()
        self.sell_in == 0


class Tickets(Item):
    def next_day(self):
        if self.sell_in < 0:
            self.quality = 0
            self.sell_in -= 1
            return

        if self.sell_in <= 5:
            self.degradation = -3
        elif self.sell_in <= 10:
            self.degradation = -2
        else:
            self.degradation = -1

        super().next_day()


class GildedRose(object):
    items: List[Item]

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.next_day()    