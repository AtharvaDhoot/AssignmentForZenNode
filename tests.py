import unittest
from unittest.mock import patch
from task1 import (
    calculate_flat_10_discount,
    calculate_bulk_5_discount,
    calculate_bulk_10_discount,
    calculate_tiered_50_discount,
    calculate_gift_wrap_fee,
    calculate_shipping_fee,
    get_max_discount,
    calculate_final_price,
    take_order,
)

class TestEaziShopping(unittest.TestCase):
    def test_calculate_flat_10_discount(self):
        self.assertEqual(calculate_flat_10_discount(250), 10)
        self.assertEqual(calculate_flat_10_discount(100), 0)

    def test_calculate_bulk_5_discount(self):
        quantities = [15, 20, 5]
        prices = [10, 5, 8]
        self.assertEqual(calculate_bulk_5_discount(quantities, prices), 12.5)

    def test_calculate_bulk_10_discount(self):
        self.assertEqual(calculate_bulk_10_discount(25, 300), 30)
        self.assertEqual(calculate_bulk_10_discount(15, 100), 0)

    def test_calculate_tiered_50_discount(self):
        quantities = [20, 10, 25]
        prices = [10, 5, 8]
        self.assertEqual(calculate_tiered_50_discount(quantities, prices), 65)

    def test_calculate_gift_wrap_fee(self):
        self.assertEqual(calculate_gift_wrap_fee(True, 5), 5)
        self.assertEqual(calculate_gift_wrap_fee(False, 10), 0)

    def test_calculate_shipping_fee(self):
        self.assertEqual(calculate_shipping_fee(20), 10)
        self.assertEqual(calculate_shipping_fee(25), 15)

    def test_get_max_discount(self):
        total_sum, total_quantity, prices, quantities = 300, 25, [20, 10, 15], [10, 5, 10]
        result = get_max_discount(total_sum, total_quantity, prices, quantities)
        discount_name = result[0]
        discount_value = result[1]
        self.assertEqual(discount_name, "Bulk 10")
        self.assertEqual(discount_value, 30)

    def test_calculate_final_price(self):
        self.assertEqual(calculate_final_price(200, 20, 10, 5), 195)
        self.assertEqual(calculate_final_price(100, 0, 5, 0), 105)

    @patch('builtins.input', side_effect=['5', 'N', '10', 'Y', '8', 'n'])
    def test_take_order(self, mock_input):
        products = [
            {"name": "Headphones", "price": 20},
            {"name": "Bulb", "price": 40},
            {"name": "Pepsico", "price": 50},
        ]
        expected_order = [
            {"name": "Headphones", "price": 20, "quantity": 5, "is_wrapped": False},
            {"name": "Bulb", "price": 40, "quantity": 10, "is_wrapped": True},
            {"name": "Pepsico", "price": 50, "quantity": 8, "is_wrapped": False},
        ]
        with patch('task1.PRODUCTS_STORE', products):
            self.assertEqual(take_order(products), expected_order)

if __name__ == '__main__':
    unittest.main()
