"""Tests for the cart pricing module. Run with: python3 -m unittest"""

import unittest

from cart import apply_discount, bulk_discount, checkout, subtotal, with_tax


class TestSubtotal(unittest.TestCase):
    def test_empty_cart(self):
        self.assertEqual(subtotal([]), 0.0)

    def test_single_item(self):
        self.assertEqual(subtotal([{"price": 10.0, "qty": 3}]), 30.0)

    def test_multiple_items(self):
        items = [{"price": 10.0, "qty": 2}, {"price": 5.0, "qty": 4}]
        self.assertEqual(subtotal(items), 40.0)


class TestDiscount(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(apply_discount(100.0, 0), 100.0)

    def test_ten_percent(self):
        self.assertEqual(apply_discount(100.0, 10), 90.0)

    def test_full_discount(self):
        self.assertEqual(apply_discount(100.0, 100), 0.0)

    def test_invalid_percent(self):
        with self.assertRaises(ValueError):
            apply_discount(100.0, 101)


class TestCheckout(unittest.TestCase):
    def test_with_tax(self):
        self.assertAlmostEqual(with_tax(100.0), 107.5)

    def test_checkout_end_to_end(self):
        items = [{"price": 50.0, "qty": 2}]
        self.assertEqual(checkout(items, discount_percent=10), 96.75)


class TestBulkDiscount(unittest.TestCase):
    def test_small_order_no_discount(self):
        self.assertEqual(bulk_discount(100.0, 3), 100.0)

    def test_ten_items_gets_discount(self):
        self.assertEqual(bulk_discount(100.0, 10), 90.0)

    def test_large_order_gets_discount(self):
        self.assertEqual(bulk_discount(100.0, 25), 90.0)


if __name__ == "__main__":
    unittest.main()
