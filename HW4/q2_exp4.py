import numpy as np
from code import *
# with REVERSE SORTED INPUTS TEST K values from 0-200 by 10s
START, N, STEP, N2, SORT, REVERSE = 0, 200, 1, 100, True, True
for K in range(0, 200, 10):
    PATH = 'q2/res/{}N_{}ST_{}SP_{}N2_{}SORT_{}R_{}K.npy'.format(N, START, STEP, N2, SORT, REVERSE, K)
    exp1(PATH, st=START, n=N, sp=STEP, n2=N2, do_sort=SORT, do_reverse=REVERSE, k=K)
    plot_exp(PATH, START, N, STEP, 'Algorithm comparison for sorting N reverse sorted ints', 'q2/imgs/reverse/', K)
