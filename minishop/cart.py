"""Корзина."""
from .catalog import Catalog
from .pricing import compute_total


class Cart:
    def __init__(self, catalog: Catalog):
        self.catalog = catalog
        self.lines = {}  # sku -> qty

    def add(self, sku: str, qty: int = 1):
        self.catalog.get(sku)
        self.lines[sku] = self.lines.get(sku, 0) + qty

    def items(self):
        return [(self.catalog.get(sku).price, qty) for sku, qty in sorted(self.lines.items())]

    def total(self, discount_code=None):
        return compute_total(self.items(), discount_code)
