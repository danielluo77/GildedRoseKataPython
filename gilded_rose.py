class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._get_item_strategy(item).update(item)

    def _get_item_strategy(self, item: Item):
        if item.name == "Aged Brie":
            return AgedBrieStrategy()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasStrategy()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassesStrategy()
        elif item.name.startswith("Conjured"):
            return ConjuredItemStrategy()
        else:
            return NormalItemStrategy()


class ItemStrategy:
    def update(self, item: Item):
        raise NotImplementedError("Update method should be implemented by subclasses")


class NormalItemStrategy(ItemStrategy):
    def update(self, item: Item):
        self._decrease_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._decrease_quality(item)

    def _decrease_quality(self, item: Item):
        if item.quality > 0:
            item.quality -= 1


class AgedBrieStrategy(ItemStrategy):
    def update(self, item: Item):
        self._increase_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._increase_quality(item)

    def _increase_quality(self, item: Item):
        if item.quality < 50:
            item.quality += 1


class SulfurasStrategy(ItemStrategy):
    def update(self, item: Item):
        # "Sulfuras" does not change in quality or sell_in
        pass


class BackstagePassesStrategy(ItemStrategy):
    def update(self, item: Item):
        if item.sell_in > 0:
            self._increase_quality(item)
            if item.sell_in <= 10:
                self._increase_quality(item)
            if item.sell_in <= 5:
                self._increase_quality(item)
        else:
            item.quality = 0  # After the concert, quality drops to 0

        item.sell_in -= 1

    def _increase_quality(self, item: Item):
        if item.quality < 50:
            item.quality += 1


class ConjuredItemStrategy(ItemStrategy):
    def update(self, item: Item):
        self._decrease_quality(item)
        self._decrease_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._decrease_quality(item)
            self._decrease_quality(item)

    def _decrease_quality(self, item: Item):
        if item.quality > 0:
            item.quality -= 1

