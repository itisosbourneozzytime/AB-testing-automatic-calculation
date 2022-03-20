import pandas as pd, scipy as sc, numpy as np, math
import statsmodels.stats.api as sms
import statsmodels.stats.power as smp
from statsmodels.stats.power import zt_ind_solve_power
import statsmodels.stats.proportion as proportion
import pandas as pd


def create_samples(same=1, distribution = 'bernoulli'):
    """
    :param same: binary. 1 = create same distributions, 0 = create different distributions
    :param distribution: bernoulli, arpu, etc.
    :return: a_dist, b_dist. 2 samples of needed distribution
    """

    if same == 1 and distribution == 'bernoulli':
        n, p = 10, .5
        a_dist = np.random.binomial(n, p, 10000)
        b_dist = np.random.binomial(n, p, 10000)
    elif same == 0 and distribution == 'bernoulli':
        n1, p1, n2, p2 = 10, .5, 5, 0.2
        a_dist = np.random.binomial(n1, p1, 10000)
        b_dist = np.random.binomial(n2, p2, 10000)
    else:
        a_dist, b_dist = [], []
    return a_dist, b_dist

def bernulli_test(a_dist, b_dist, p_value=0.05, additional_information = False):
    # Считаем результаты теста

    A_nobs = len(a_dist)
    B_nobs = len(b_dist)
    A_counts = sum(a_dist == 0)
    B_counts= sum(b_dist == 0)

    A_prop = A_counts / A_nobs
    B_prop = B_counts / B_nobs
    A_B_uplift = B_prop - A_prop
    A_B_uplift_abs = B_prop - A_prop
    A_B_uplift_rel = (B_prop - A_prop) / A_prop

    dataframe = pd.DataFrame([[A_counts, B_counts], [A_nobs, B_nobs]])

    p_value_binom_test = sms.binom_test(count=[A_counts, B_counts], nobs=[A_nobs, B_nobs])
    chi2, chi2_p, df, arr = sc.stats.chi2_contingency(dataframe, correction=True)  # для таблиц 2х2 нужно делать коррекцию в хи-квадрат критерии
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
        print('p_value for chisq test = ', chi2_p)
        print('p_value for z test = ', ztest_pvalue)


    return ztest_pvalue

