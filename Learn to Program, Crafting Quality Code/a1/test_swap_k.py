import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k."""

    # Add your test methods for a1.swap_k here.

    def test_swap_k_0_values(self):
        """Test to swap no items of L where L has no values, this checks
            to see if nothing is swapped at all in an empty set
            
            Precondition: 0 <= k <= len(L) // 2
        """
        
        L = []
        k = 0
        a1.swap_k(L,k)
        actual = L
        expected = []
        self.assertEqual(expected, actual)

    def test_swap_k_1_values(self):
        """Test to swap no items of L where L has 1 value, this checks
            to see if nothing is swapped at all with at least 1 value
            
            Precondition: 0 <= k <= len(L) // 2
        """
        
        L = [1]
        k = 0
        a1.swap_k(L,k)
        actual = L
        expected = [1]
        self.assertEqual(expected, actual)
        

    def test_swap_k_2_values(self):
        """Test to swap first item of L with last item of L, where
            L has 2 values, this checks to see if both values can be swapped
            
            Precondition: 0 <= k <= len(L) // 2
        """

        L = [1, 2]
        k = 1
        a1.swap_k(L,k)
        actual = L
        expected = [2, 1]
        self.assertEqual(expected, actual)

    def test_swap_k_odd_length(self):
        """Test to swap first 2 items of L with last 2 items of L, where
            L has 5 values, this checks to see if multiple values are swapped
            at an odd length
            
            Precondition: 0 <= k <= len(L) // 2
        """

        L = [1, 2, 3, 4, 5]
        k = 2
        a1.swap_k(L,k)
        actual = L
        expected = [4, 5, 3, 1, 2]
        self.assertEqual(expected, actual)

    def test_swap_k_entire_length(self):
        """Test to swap first 3 items of L with last 3 items of L, where
            L has 6 values, this checks to see if all values are swapped
            in the entire length
            
            Precondition: 0 <= k <= len(L) // 2
        """

        L = [1, 2, 3, 4, 5, 6]
        k = 3
        a1.swap_k(L,k)
        actual = L
        expected = [4, 5, 6, 1, 2, 3]
        self.assertEqual(expected, actual)
        


if __name__ == '__main__':
    unittest.main(exit=False)
