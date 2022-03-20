from functions import *
from tests import *
from statsmodels import stats

import numpy as np
# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    print('Same samples: bernoulli')
    a_dist, b_dist = create_samples(1, 'bernoulli')
    result = bernulli_test(a_dist, b_dist)
    print(result)

    print('Different samples: bernoulli')
    a_dist, b_dist = create_samples(0, 'bernoulli')
    result = bernulli_test(a_dist, b_dist)
    print(result)

    print('Quality check')
    print(test_bernulli_aa(0.05))
    print(test_bernulli_ab(0.05))
    print(test_bernulli_info(p_value=0.05, additional_information=True))