import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_item_quality_never_more_than_fifty(self):
        # Creating an item with quality at 50
        items = [Item("Aged Brie", 4, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # Assert that the quality is never more than 50  after updating
        self.assertEqual(items[0].quality, 50, "Item quality is never more than 50.")

    def test_item_sulfuras_never_sold(self):
        # Creating an item with quality at 50
        items = [Item("Sulfuras, Hand of Ragnaros", 2, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # Assert that the item sulfuras is never sold.
        self.assertEqual(items[0].quality, 2, "Sulfuras is never sold .")

    def test_conjured_items_degrade_twice_as_fast(self):
        # Setting up a normal item and a conjured item with the same initial quality and sell_in values
        items = [
            Item("bread", 10, 20),
            Item("Conjured", 10, 20)  # Assuming we identify "Conjured" items by their name
        ]
        gilded_rose = GildedRose(items)
        # Update quality for 1 day
        gilded_rose.update_quality()
        # Calculate the quality degradation for both items
        bread_degradation = 20 - items[0].quality
        conjured_degradation = 20 - items[1].quality

        # Assert that the Conjured item's quality degrades twice as much as the normal item's quality
        self.assertEqual(conjured_degradation, 2 * bread_degradation,
                         "Conjured item did not degrade twice as fast as normal item.")

if __name__ == '__main__':
    unittest.main()
