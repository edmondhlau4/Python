import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """
    # Add your test methods for a1.num_buses here.

    def test_num_buses_nobody(self):
        """Test num_buses with 0 amount of people to check
            how many buses would be needed for no capacity"""

        n = 0
        actual = a1.num_buses(n)
        expected = 0
        self.assertEqual(expected, actual)

    def test_num_buses_minimum(self):
        """Test num_buses with 1 amount of people to check
            how many buses would be needed for minimum capacity"""

        n = 1
        actual = a1.num_buses(n)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_middle(self):
        """Test num_buses with 25 amount of people to check
            how many buses would be needed for middle capacity"""

        n = 25
        actual = a1.num_buses(n)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_max(self):
        """Test num_buses with 50 amount of people to check
            how many buses would be needed for max capacity"""

        n = 50
        actual = a1.num_buses(n)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_max_and_extra(self):
        """Test num_buses with 51 amount of people to check
            how many buses would be needed for max capacity and extra"""

        n = 51
        actual = a1.num_buses(n)
        expected = 2
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
