# -*- coding: utf-8 -*-



from gilded_rose import Item


class Sulfuras(Item):

    name = "Sulfuras, Hand of Ragnaros"
    discount = 0
    quality_min = 80
    quality_max = 80


    def next_day(self):
        self.sell_in = 0