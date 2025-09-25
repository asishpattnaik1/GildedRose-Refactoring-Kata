# -*- coding: utf-8 -*-
import pytest
from gilded_rose import GildedRose, Item


class TestGildedRose:
    """Comprehensive Unit testing suite for GildedRose functionality."""
    #1
    def test_normal_item_quality_decreases(self):
        """Normal items decrease in quality by 1 each day."""
        item = Item("Normal Item", 10, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        
        assert item.quality == 19
        assert item.sell_in == 9
    #2
    def test_normal_item_quality_decreases_twice_after_sell_date(self):
        """Normal items decrease in quality by 2 after sell date."""
        item = Item("Normal Item", 0, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        
        assert item.quality == 18  # Decreased by 2
        assert item.sell_in == -1
    #3
    def test_quality_never_negative(self):
        """Quality never goes below 0."""
        item = Item("Normal Item", 5, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        
        assert item.quality == 0
    #4
    def test_aged_brie_increases_quality(self):
        """Aged Brie increases in quality over time."""
        item = Item("Aged Brie", 10, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        
        assert item.quality == 21
        assert item.sell_in == 9
    #5
    def test_aged_brie_increases_twice_after_sell_date(self):
        """Aged Brie increases by 2 after sell date."""
        item = Item("Aged Brie", 0, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        
        assert item.quality == 22
        assert item.sell_in == -1
    #6
    def test_quality_never_exceeds_50(self):
        """Quality never exceeds 50 (except Sulfuras)."""
        item = Item("Aged Brie", 5, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        
        assert item.quality == 50
    #7
    def test_sulfuras_never_changes(self):
        """Sulfuras never changes in quality or sell_in."""
        item = Item("Sulfuras, Hand of Ragnaros", 10, 80)
        original_quality = item.quality
        original_sell_in = item.sell_in
        
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        
        assert item.quality == original_quality
        assert item.sell_in == original_sell_in
    #8
    def test_backstage_pass_increases_quality(self):
        """Backstage passes increase in quality as concert approaches."""
        item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        
        assert item.quality == 21  # +1
        assert item.sell_in == 14
    #9
    def test_backstage_pass_increases_by_2_when_10_days_or_less(self):
        """Backstage passes increase by 2 when 10 days or less."""
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        
        assert item.quality == 22  # +2
        assert item.sell_in == 9
    #10
    def test_backstage_pass_increases_by_3_when_5_days_or_less(self):
        """Backstage passes increase by 3 when 5 days or less."""
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        
        assert item.quality == 23  # +3
        assert item.sell_in == 4
    #11
    def test_backstage_pass_worthless_after_concert(self):
        """Backstage passes become worthless after concert."""
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        
        assert item.quality == 0
        assert item.sell_in == -1

    #12
    def test_backstage_pass_quality_does_not_exceed_50(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 50

    #13
    def test_conjured_item_degrades_twice_as_fast(self):
        """Conjured items degrade in quality twice as fast as normal items."""
        item = Item("Conjured Mana Cake", 10, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        
        assert item.quality == 18  # Decreased by 2
        assert item.sell_in == 9
    #14
    def test_conjured_item_degrades_twice_as_fast_after_sell_date(self):
        """Conjured items degrade in quality twice as fast as normal items."""
        item = Item("Conjured Mana Cake", 0, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()

        assert item.quality == 16  # Decreased by 4
        assert item.sell_in == -1
    #15
    def test_item_name_case_insensitivity(self):
        """Item name checks are case-sensitive.
        Should behave like a normal item since name doesn't match exactly"""
        item = Item("garlic", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        
        assert item.quality == 9


    #16
    def test_quality_exactly_at_max_does_not_increase(self):
        """Aged Brie quality does not increase beyond 50."""
        item = Item("Aged Brie", 5, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 50
    #17
    def test_quality_exactly_at_min_does_not_decrease(self):
        """Normal item quality does not decrease below 0."""
        item = Item("Normal Item", 5, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 0
    #18
    def test_multiple_items_update_correctly(self):
        """Test multiple items updating in a single day."""
        items = [
            Item("Normal Item", 10, 20),
            Item("Aged Brie", 2, 0),
            Item("Sulfuras, Hand of Ragnaros", 0, 80),
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Conjured Mana Cake", 3, 6),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        assert items[0].quality == 19
        assert items[1].quality == 1
        assert items[2].quality == 80
        assert items[3].quality == 21
        assert items[4].quality == 4
    #19
    @pytest.mark.parametrize("days", [1, 5, 10, 30])
    def test_extended_simulation(self, days):
        """Test extended simulation to ensure no crashes"""
        items = [
            Item("Normal Item", 10, 20),
            Item("Aged Brie", 5, 10),
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Sulfuras, Hand of Ragnaros", 0, 80),
            Item("Conjured Mana Cake", 3, 6),
        ]
        
        gilded_rose = GildedRose(items)
        
        for _ in range(days):
            gilded_rose.update_quality()
            
            # Ensure quality constraints are maintained
            for item in items:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    assert 0 <= item.quality <= 50
                else:
                    assert item.quality == 80

if __name__ == '__main__':
    pytest.main([__file__])