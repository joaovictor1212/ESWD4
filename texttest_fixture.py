from __future__ import print_function
from tabulate import tabulate
from gilded_rose import Item, AgedBrie, GildedRose, Sulfuras, Tickets


dex = "+5 Dexterity Vest"
age = "Aged Brie"
elixir = "Elixir of the Mongoose"
sulf = "Sulfuras, Hand of Ragnaros"
back_stage = "Backstage passes to a TAFKAL80ETC concert"
conj_mana = "Conjured Mana Cake"



if __name__ == "__main__":
    items = [
             Item(name=dex, sell_in=10, quality=20),
             AgedBrie(sell_in=2, quality=0),
             Item(name=elixir, sell_in=5, quality=7),
             Sulfuras(),
             Tickets (name=back_stage,sell_in=15, quality=20
             ),
             Tickets (
                name=back_stage, sell_in=10, quality=49
                ),
             Tickets(
                name=back_stage, sell_in=5, quality=49
                ),
             Item(name=conj_mana, sell_in=3, quality=6)
        ]
  
    days = 2
    import sys

    gilded_rose = GildedRose(items)

    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print(
            tabulate(
            [(i.name, i.sell_in, i.quality) for i in items], 
            headers=["name", "sell_in", "quality"],
            )
        )
        print("")
        gilded_rose.update_quality()