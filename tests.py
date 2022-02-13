import unittest
from functions import bernulli_test, create_samples
import numpy as np

# TDD version 1

def test_bernulli_aa(p_value=0.05):
    a_dist, b_dist = create_samples(same=1, distribution = 'bernoulli')
    result = bernulli_test(a_dist, b_dist, p_value)  # p-value
    # проверить логику
    if result > p_value:
        return 'test_passed'
    else:
        return 'test_failed'


def test_bernulli_ab( p_value=0.05):
    a_dist, b_dist = create_samples(same=0, distribution = 'bernoulli')
    result = bernulli_test(a_dist, b_dist, p_value)  # p-value
    # проверить логику
    if result <= p_value:
        return 'test_passed'
    else:
        return 'test_failed'


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
