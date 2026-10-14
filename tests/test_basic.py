import unittest
from decimal import Decimal

from minishop.catalog import Catalog, Product
from minishop.cart import Cart
from minishop.pricing import compute_total


class BasicTest(unittest.TestCase):
    def test_total_no_discount(self):
        self.assertEqual(compute_total([("10.00", 2)]), Decimal("24.00"))

    def test_cart(self):
        c = Catalog(); c.add(Product("A1", "Apple", "1.50"))
        cart = Cart(c); cart.add("A1", 4)
        self.assertEqual(cart.total(), Decimal("7.20"))


if __name__ == "__main__":
    unittest.main()
