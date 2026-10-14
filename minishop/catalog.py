"""Каталог товаров."""
from dataclasses import dataclass


@dataclass
class Product:
    sku: str
    name: str
    price: str  # строка с десятичной ценой, например "12.50"


class Catalog:
    def __init__(self):
        self._items = {}

    def add(self, product: Product):
        if product.sku in self._items:
            raise KeyError(f"duplicate sku {product.sku}")
        self._items[product.sku] = product

    def get(self, sku: str) -> Product:
        return self._items[sku]

    def all(self):
        return sorted(self._items.values(), key=lambda p: p.sku)
