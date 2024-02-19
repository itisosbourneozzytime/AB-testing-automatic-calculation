import pandas as pd, scipy as sc, numpy as np, math
import statsmodels.stats.api as sms
#import statsmodels.stats.power as smp
#from statsmodels.stats.power import zt_ind_solve_power
#import statsmodels.stats.proportion as proportion
import pandas as pd
import random


def create_samples(number_of_samples, is_same=1, distribution = 'bernoulli', len = 10000):
    """
    :number_of_samples: int. 10> number_of_samples > 0. Number of samples for AB testing.
    :is_same: binary. 1 = create same distributions, 0 = create different distributions
    :distribution distribution: bernoulli, arpu, etc.
    :return: a_dist, b_dist. 2 samples of needed distribution
    """
    if isinstance(number_of_samples, int):
        if number_of_samples < 10 and number_of_samples > 0:
            if number_of_samples == 2:
                if is_same == 1 and distribution == 'bernoulli':
                    n, p = 10, .5
                    a_dist = np.random.binomial(1, p, 10000)
                    b_dist = np.random.binomial(1, p, 10000)
                elif is_same == 0 and distribution == 'bernoulli':
                    n1, p1, n2, p2 = 10, .5, 5, 0.2
                    a_dist = np.random.binomial(1, p1, 10000)
                    b_dist = np.random.binomial(1, p2, 10000)
                else:
                    a_dist, b_dist = [], []
                return a_dist, b_dist
            else:
                if distribution == 'bernoulli':
                    if is_same == 0:
                        result_ndarray = []
                        for i in range(number_of_samples - 1):
                            n = random.randrange(0, 50)
                            p = random.random()
                            globals()[f'{i}_dist'] = np.random.binomial(1, p, 10000)
                            result_ndarray.append(globals()[f'{i}_dist'])
                        n = random.randrange(0, 50)
                        p = random.random()
                        cg_dist = np.random.binomial(1, p, 10000)
                        result_ndarray.append(cg_dist)
                    else:
                        result_ndarray = []
                        n = random.randrange(0, 50)
                        p = random.random()
                        for i in range(number_of_samples - 1):
                            globals()[f'{i}_dist'] = np.random.binomial(1, p, 10000)
                            result_ndarray.append(globals()[f'{i}_dist'])
                        cg_dist = np.random.binomial(1, p, 10000)
                        result_ndarray.append(cg_dist)
                    return result_ndarray
                else:
                    return 'There is no such distribution yet.'
        else:
            return 'Error: Number_of_samples should be between 10 and 0.'
    else:
        return 'Error: Wrong type of number_of_samples. Should be integer between 10 and 0.'

def bernoulli_test(a_dist, b_dist, p_value=0.05, additional_information = False):

    A_nobs = len(a_dist)
    B_nobs = len(b_dist)
    A_counts = sum(a_dist == 0)
    B_counts= sum(b_dist == 0)

    A_prop = A_counts / A_nobs
    B_prop = B_counts / B_nobs
    A_B_uplift_abs = B_prop - A_prop
    if A_prop != 0:
        A_B_uplift_rel = (B_prop - A_prop) / A_prop
    else:
        A_B_uplift_rel = 0

    dataframe = pd.DataFrame([[A_counts, B_counts], [A_nobs, B_nobs]])

    p_value_binom_test = sms.binom_test(count=[A_counts, B_counts], nobs=[A_nobs, B_nobs])
    z_score, ztest_pvalue = sms.proportions_ztest(count=[A_counts, B_counts], nobs=[A_nobs, B_nobs])

    if additional_information == True:
        print('CONCLUSIONS')
        print('------')
        print('A group proportion = ', round(A_prop, 5))
        print('B group proportion = ', round(B_prop, 5))
        print('ABS Proportions uplift = ', round(A_B_uplift_abs, 5))
        print('Relative Proportions uplift = ', round(A_B_uplift_rel, 5))
        print()
        print('p_value for binom test = ', p_value_binom_test)
        print('p_value for z test = ', ztest_pvalue)

    return ztest_pvalue

def multiple_test(ndarray, p_value = 0.05, method = 'holm-bonferroni'):
    # calculate p_vals
    number_of_samples = len(ndarray)
    pvals = {}
    for i in range(0, number_of_samples-1):
        # Test group compared to control group
        p_val = bernoulli_test(ndarray[i], ndarray[number_of_samples-1])
        pvals.update({i: p_val})
    # sort pvals
    pvals = dict(sorted(pvals.items(), key = lambda item: item[1]))
    # calculate p value correction
    alpha_corrected = p_value / (number_of_samples-1)
    # return rejected hypothesis
    rejected = {}
    for key, value in pvals.items():
        if value < alpha_corrected:
            rejected.update({key: value})
        else:
            break
    return rejected