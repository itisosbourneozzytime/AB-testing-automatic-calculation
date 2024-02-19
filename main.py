from functions import *
from tests import *
from statsmodels import stats

import numpy as np

if __name__ == '__main__':


    print('Same samples: bernoulli')
    a_dist, b_dist = create_samples(number_of_samples=2, is_same=1, distribution='bernoulli')
    result = bernoulli_test(a_dist, b_dist)
    print(result)

    print('Different samples: bernoulli')
    a_dist, b_dist = create_samples(number_of_samples=2, is_same=0, distribution='bernoulli')
    result = bernoulli_test(a_dist, b_dist)
    print(result)

    print('Different samples: multitest bernoulli')
    ndarray = create_samples(number_of_samples = 4, is_same = 0, distribution= 'bernoulli')
    result = multiple_test(ndarray, p_value = 0.05, method = 'holm-bonferroni')
    print(result)

    print('Quality check')
    print(test_bernoulli_aa(0.05))
    print(test_bernoulli_ab(0.05))
    print(test_bernoulli_info(p_value=0.05, additional_information=True))
    print(test_multiple_comparison_abc(p_value=0.05, method = 'holm-bonferroni'))
    print(test_multiple_comparison_aaa(p_value=0.05, method = 'holm-bonferroni'))