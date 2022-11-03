# -*- coding: utf-8 -*-
from __future__ import print_function
from gilded_rose import Item, GildedRose 
from tabulate import tabulate

if __name__ == "__main__":

    dex = "+5 Dexterity Vest"
    age = "Aged Brie"
    elixir = "Elixir of the Mongoose"
    sulf = "Sulfuras, Hand of Ragnaros"
    back_stage = "Backstage passes to a TAFKAL80ETC concert"
    conj_mana = "Conjured Mana Cake"

    print ("OMGHAI!")
    items = [
            Item(name=dex, sell_in=10, quality=20),
            Item(name=age, sell_in=2, quality=0),
            Item(name=elixir, sell_in=5, quality=7),
            Item(name=sulf, sell_in=0, quality=80),
            Item(name=sulf, sell_in=-1, quality=80),
            Item(name=back_stage, sell_in=15, quality=20),
            Item(name=back_stage, sell_in=10, quality=49),
            Item(name=back_stage, sell_in=5, quality=49),
            Item(name=conj_mana, sell_in=3, quality=6),  
    ]

    days = 2
    import sys

    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
        
    for day in range(days):
        print("-------- day %s --------" % day)
        print(tabulate(
            [(i.name, i.sell_in, i.quality) for i in items], 
            headers=['name', 'sell_in', 'quality']
        ))
        
        print("")
        GildedRose(items).update_quality()