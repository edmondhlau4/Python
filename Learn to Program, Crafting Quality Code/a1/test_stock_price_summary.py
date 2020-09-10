import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.

    def test_stock_price_summary_none(self):
        """Test the stock price summary where there are no stocks, to
            an empty set"""
        
        price_changes = []
        actual = a1.stock_price_summary(price_changes)
        expected = (0.00,-0.00)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_0(self):
        """Test the stock price summary where there is only 1 stock, to check
            the value after adding 0"""

        price_changes = [0.00]
        actual = a1.stock_price_summary(price_changes)
        expected = (0.00, -0.00)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_1_positive(self):
        """Test the stock price summary where there is only 1 stock, to check
            the addition of sum"""
        
        
        price_changes = [0.01]
        actual = a1.stock_price_summary(price_changes)
        expected = (0.01, -0.00)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_1_negative(self):
        """Test the stock price summary where there is only 1 stock, to check
            the addition of losses"""

        price_changes = [-0.01]
        actual = a1.stock_price_summary(price_changes)
        expected = (0.00, -0.01)
        self.assertEqual(expected, actual)


    def test_stock_price_summary_2_positive(self):
        """Test the stock price summary where there are only 2 stocks, to check
            the correct addition of the gains in price_changes"""

        price_changes = [0.01, 0.02]
        actual = a1.stock_price_summary(price_changes)
        expected = (0.03, -0.00)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_2_negative(self):
        """Test the stock price summary where there are only 3 stocks, to check
            the correct addition of the losses in price_changes"""

        price_changes = [0.01, -0.02, -0.01]
        actual = a1.stock_price_summary(price_changes)
        expected = (0.01, -0.03)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_random_mix(self):
        """Test the stock price summary where there are only 6 stocks, to check
            a random sampled mix of positive and negative
            numbers, some with double digits"""

        price_changes = [-0.12, 0.14, 0.00, 0.05, -0.16, - 0.04]
        actual = a1.stock_price_summary(price_changes)
        expected = (0.19, -0.32)
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main(exit=False)
