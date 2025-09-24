# -*- coding: utf-8 -*-
from typing import List

class GildedRose(object):

    #quality constants
    MAX_QUALITY = 50
    MIN_QUALITY = 0
    SULFURAS_QUALITY = 80

    #item constants
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"



    def __init__(self, items: list['Item']):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            if item.name != self.AGED_BRIE and item.name != self.BACKSTAGE_PASSES:
                if item.quality > self.MIN_QUALITY:
                    if item.name != self.SULFURAS:
                        item.quality = item.quality - 1
            else:
                if item.quality < self.MAX_QUALITY:
                    item.quality = item.quality + 1
                    if item.name == self.BACKSTAGE_PASSES:
                        if item.sell_in < 11:
                            if item.quality < self.MAX_QUALITY:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < self.MAX_QUALITY:
                                item.quality = item.quality + 1
            if item.name != self.SULFURAS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != self.AGED_BRIE:
                    if item.name != self.BACKSTAGE_PASSES:
                        if item.quality > self.MIN_QUALITY:
                            if item.name != self.SULFURAS:
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < self.MAX_QUALITY:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
