import unittest
from functions import *
import numpy as np

# TDD version 1

def test_bernoulli_aa(p_value=0.05):
    a_dist, b_dist = create_samples(number_of_samples= 2, is_same=1, distribution = 'bernoulli')
    result = bernoulli_test(a_dist, b_dist, p_value)  # p-value
    if result > p_value:
        return 'test_passed'
    else:
        return 'test_failed'


def test_bernoulli_ab(p_value=0.05):
    a_dist, b_dist = create_samples(number_of_samples= 2, is_same=0, distribution = 'bernoulli')
    result = bernoulli_test(a_dist, b_dist, p_value)  # p-value
    if result <= p_value:
        return 'test_passed'
    else:
        return 'test_failed'

def test_bernoulli_info(p_value=0.05, additional_information = True):
    a_dist, b_dist = create_samples(number_of_samples= 2, is_same=0, distribution = 'bernoulli')
    result = bernoulli_test(a_dist, b_dist, p_value, additional_information = additional_information)  # p-value
    if result <= p_value:
        return 'test_passed'
    else:
        return 'test_failed'

def test_multiple_comparison_abc(p_value=0.05, method = 'holm-bonferroni'):
    ndarray = create_samples(number_of_samples = 3, is_same=0, distribution='bernoulli')
    rejected = multiple_test(ndarray, p_value = p_value, method = method)
    if len(rejected) == 2:
        return 'test_passed'
    else:
        return 'test_failed'

def test_multiple_comparison_aaa(p_value=0.05, method = 'holm-bonferroni'):
    ndarray = create_samples(number_of_samples = 3, is_same=1, distribution='bernoulli')
    rejected = multiple_test(ndarray, p_value = p_value, method = method)
    print("test :", rejected)
    if len(rejected) == 0:
        return 'test_passed'
    else:
        return 'test_failed'


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
