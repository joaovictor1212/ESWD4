# -*- coding: utf-8 -*-

from abc import  abstractmethod

from numpy import quantile



dex = "+5 Dexterity Vest"
age = "Aged Brie"
elixir = "Elixir of the Mongoose"
sulf = "Sulfuras, Hand of Ragnaros"
back_stage = "Backstage passes to a TAFKAL80ETC concert"
conj_mana = "Conjured Mana Cake"




class Item:
    name = ""
    discount = 1
    quality_min = 0
    quality_max = 50


    def __init__(self, sell_in, quality):
        
        assert quality >= self.quality_min
        assert quality <= self.quality_max

        self.sell_in = sell_in
        self.quality = quality

    
    def next_day(self):
        self.sell_in = self.sell_in - 1

        diff = self.discount
        if self.sell_in < 0:
            diff *= 2
        
        self.quality = self.quality - diff
        self.quality = max(self.quality_min, self.quality)
        self.quality = min(self.quality_min, self.quality)
            

 

class Tickets(Item):
    name = "Backstage passes to a TAFKAL80ETC concert"

    def next_day(self):
        for record in self:
            if record.sell_in < 0:
                record.quality = 0
                return

            if record.sell_in < 5:
                record.discount = 3

            elif record.sell_in < 10:
                record.discount = 2

            else:
                record.discount = 1


        super().next_day()



class GildedRose(object):
    items = Item
    def __init__(self, items):
        self.items = items


    def update_quality(self):
        for item in self.items:
            item.next_day()



# class OGGildedRose(object):

#     def __init__(self, items):
#         self.items = items

#     def update_quality(self):
#         for item in self.items:
#             if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
#                 if item.quality > 0:
#                     if item.name != "Sulfuras, Hand of Ragnaros":
#                         item.quality = item.quality - 1
#             else:
#                 if item.quality < 50:
#                     item.quality = item.quality + 1
#                     if item.name == "Backstage passes to a TAFKAL80ETC concert":
#                         if item.sell_in < 11:
#                             if item.quality < 50:
#                                 item.quality = item.quality + 1
#                         if item.sell_in < 6:
#                             if item.quality < 50:
#                                 item.quality = item.quality + 1
#             if item.name != "Sulfuras, Hand of Ragnaros":
#                 item.sell_in = item.sell_in - 1
#             if item.sell_in < 0:
#                 if item.name != "Aged Brie":
#                     if item.name != "Backstage passes to a TAFKAL80ETC concert":
#                         if item.quality > 0:
#                             if item.name != "Sulfuras, Hand of Ragnaros":
#                                 item.quality = item.quality - 1
#                     else:
#                         item.quality = item.quality - item.quality
#                 else:
#                     if item.quality < 50:
#                         item.quality = item.quality + 1


# class OGItem:
#     def __init__(self, name, sell_in, quality):
#         self.name = name
#         self.sell_in = sell_in
#         self.quality = quality

#     def __repr__(self):
#         return "%s, %s, %s" % (self.name, self.sell_in, self.quality)