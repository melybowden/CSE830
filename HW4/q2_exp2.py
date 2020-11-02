import numpy as np
from code import *
# OVERALL TIMSORT GROWTH WITH THRESHOLD=100 (FROM UNSORTED EXP)
START, N, STEP, N2, SORT, REVERSE, K = 0, 10000, 50, 1, False, False, 100
PATH = 'q2/res/{}N_{}ST_{}SP_{}N2_{}SORT_{}R_{}K.npy'.format(N, START, STEP, N2, SORT, REVERSE, K)
exp1(PATH, st=START, n=N, sp=STEP, n2=N2, do_sort=SORT, do_reverse=REVERSE, k=K)
plot_exp(PATH, START, N, STEP, 'Algorithm comparison for sorting N random ints', 'q2/imgs/unsorted/', K)
# ins_wins(PATH)
