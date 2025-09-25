# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import List

class Item:
    """Class representing an item in the inventory."""
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return f"{self.name}, {self.sell_in}, {self.quality}"

class UpdatableItem(ABC):
    """Abstract base class for items that can be updated."""
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, item: 'Item'):
        self.item = item

    @abstractmethod
    def update(self) -> None:
        pass

    def _increase_quality(self, amount: int = 1) -> None:
        self.item.quality = min(self.MAX_QUALITY, self.item.quality + amount)

    def _decrease_quality(self, amount: int = 1) -> None:
        self.item.quality = max(self.MIN_QUALITY, self.item.quality - amount)

class AgedBrie(UpdatableItem):
    """Aged Brie increases in quality as it ages.
        Quality increases by 1 each day and by 2 after sell date.
        """
    def update(self) -> None:
        self.item.sell_in -= 1
        self._increase_quality()
        if self.item.sell_in < 0:
            self._increase_quality()

class BackstagePass(UpdatableItem):
    """Backstage passes increase in quality as concert approaches.
    Quality increases by 1 when there are more than 10 days,
    by 2 when there are 5-10 days, and by 3 when there are 0-5 days. After the concert, quality drops to 0.
    """
    def update(self) -> None:
        self.item.sell_in -= 1
        if self.item.sell_in > 10:
            self._increase_quality(1)
        elif self.item.sell_in > 5:
            self._increase_quality(2)
        elif self.item.sell_in > 0:
            self._increase_quality(3)
        
        # After concert, quality drops to 0
        if self.item.sell_in < 0:
            self.item.quality = self.MIN_QUALITY
    

class ConjuredItem(UpdatableItem):
    """Conjured items degrade in quality twice as fast as normal items.
    """
    def update(self) -> None:
        self.item.sell_in -= 1
        self._decrease_quality(2)
        if self.item.sell_in < 0:
            self._decrease_quality(2)

class NormalItem(UpdatableItem):
    """Normal items decrease in quality over time.
    Quality degrades twice as fast after sell date.
    """
    def update(self) -> None:
        self.item.sell_in -= 1
        self._decrease_quality()
        if self.item.sell_in < 0:
            self._decrease_quality()

class LegendaryItem(UpdatableItem):
    """Legendary items do not change in quality or sell_in.
    """
    def update(self) -> None:
        pass  # Legendary items do not change

    
class GildedRose:
    def __init__(self, items: List['Item']):
        self.items = [self.get_updatable_item(item) for item in items]

    def get_updatable_item(self, item: 'Item') -> UpdatableItem:
        if "Aged Brie" in item.name:
            return AgedBrie(item)
        elif "Backstage passes" in item.name:
            return BackstagePass(item)
        elif "Conjured" in item.name:
            return ConjuredItem(item)
        elif "Sulfuras" in item.name:
            return LegendaryItem(item)
        else:
            return NormalItem(item)

    def update_quality(self) -> None:
        for item in self.items:
            item.update()



