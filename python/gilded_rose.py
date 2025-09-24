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
    CONJURED = "Conjured Mana Cake"

    def __init__(self, items: list['Item']):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            # Skip legendary items (they don't change)
            if item.name == self.SULFURAS:
                continue
                
            # Decrease sell_in for all non-legendary items
            item.sell_in -= 1
            
            # Update quality based on item type
            if item.name == self.AGED_BRIE:
                self._update_aged_brie_quality(item)
            elif item.name == self.BACKSTAGE_PASSES:
                self._update_backstage_pass_quality(item)
            elif item.name == self.CONJURED:
                self._update_conjured_item_quality(item)
            else:
                self._update_normal_item_quality(item)

    def _update_aged_brie_quality(self, item: 'Item') -> None:
        """Aged Brie increases in quality as it ages.
        Quality increases by 1 each day and by 2 after sell date.
        """
        if item.quality < self.MAX_QUALITY:
            item.quality += 1
        
            if item.sell_in < 0 and item.quality < self.MAX_QUALITY:
                item.quality += 1


    def _update_backstage_pass_quality(self, item: 'Item') -> None:
        """Backstage passes increase in quality as concert approaches."""
        if item.sell_in < 0:
            # Concert has passed, worthless
            item.quality = 0
        elif item.quality < self.MAX_QUALITY:
            item.quality += 1
            # Additional increases as concert approaches
            if item.sell_in < 10 and item.quality < self.MAX_QUALITY:
                item.quality += 1
            if item.sell_in < 5 and item.quality < self.MAX_QUALITY:
                item.quality += 1

    def _update_normal_item_quality(self, item: 'Item') -> None:
        """Normal items decrease in quality over time.
        Quality degrades twice as fast after sell date.
        """
        if item.quality > self.MIN_QUALITY:
            item.quality -= 1
            # Double decrease after sell date
            if item.sell_in < 0 and item.quality > self.MIN_QUALITY:
                item.quality -= 1

    def _update_conjured_item_quality(self, item: 'Item') -> None:
        """Conjured items degrade in quality twice as fast as normal items."""
        if item.quality > self.MIN_QUALITY:
            item.quality -= 2
            if item.sell_in < 0 and item.quality > self.MIN_QUALITY:
                item.quality -= 2
class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
