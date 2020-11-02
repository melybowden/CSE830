import numpy as np # zeros, array, load, save
import random # seed, randint
import matplotlib.pyplot as plt # plotting
from sorting_algorithms import merge_sort, insertion_sort, tim_sort
from time import time # time


def exp1(path, st=0, n=1000, sp=1, n2=1, do_sort=False, do_reverse=False, k=150):
    times = np.zeros((n,3))
    for i in range(st, n, sp):
        print('Round i:{}'.format(i))
        t1 = time()
        for j in range(n2):
            random.seed(9876)
            unsorted = [random.randint(0, n) for _ in range(i)]
            if do_sort:
                unsorted = sorted(unsorted, reverse=do_reverse)
            # print(unsorted)
            sort = insertion_sort(unsorted) # sort list of 10 randomly selected numbers
            # print('Insertion Sort:{}'.format(sort))
            assert sort == sorted(unsorted)
        times[i, 0] = time() - t1

        # random.seed(9876)
        # unsorted = (1000)*[random.randint(0, N) for _ in range(i)]
        t1 = time()
        for j in range(n2):
            random.seed(9876)
            unsorted = [random.randint(0, n) for _ in range(i)]
            if do_sort:
                unsorted = sorted(unsorted, reverse=do_reverse)
            # print(unsorted)
            sort = merge_sort(unsorted) # sort list of 10 randomly selected numbers
            # print('Merge Sort:{}'.format(sort))
            assert sort == sorted(unsorted)
        times[i, 1] = time() - t1

        t1 = time()
        for j in range(n2):
            random.seed(9876)
            unsorted = [random.randint(0, n) for _ in range(i)]
            if do_sort:
                unsorted = sorted(unsorted, reverse=do_reverse)
            # print(unsorted)
            sort = tim_sort(unsorted, k) # sort list of 10 randomly selected numbers
            # print('Merge Sort:{}'.format(sort))
            assert sort == sorted(unsorted)
        times[i, 2] = time() - t1
    np.save(path, times)

def plot_exp(fname, st=0, n=1000, sp=1, fig_title='Time for sorting N elements with insertion and merge sort', fldr='q2/imgs/unsorted/', k=150):
    res = np.load(fname)
    res = np.array([res[_] for _ in range(st, n, sp)])
    intervals = [_ for _ in range(st, n, sp)]
    fig, ax = plt.subplots()
    ax.plot(intervals, res[:n,0], 'bo', label='Insertion Sort')
    ax.plot(intervals, res[:n,1], 'ro', label='Merge Sort')
    ax.plot(intervals, res[:n,2], 'go', label='Tim Sort, k={}'.format(str(k)))
    ax.legend()
    ax.set(xlabel='N Inputs', ylabel='Time (s)',
            title=fig_title)
    ax.grid()
    fname = fname.split('/')[-1]
    plt.savefig(fldr+fname.split('.')[0]+'.png')
    # plt.show()

def ins_wins(fname):
    f, ext = fname.split('.')
    f = f.split('/')[-1]
    params = f.split('_')
    n = int(params[0][:-1])
    st = int(params[1][:-2])
    sp = int(params[2][:-2])
    n2 = int(params[3][:-2])
    res = np.load(fname)
    res = np.array([res[_] for _ in range(st, n, sp)])
    print(np.where(res[:,0] < res[:,1]))


####################### Q1 ##############################
# exp1(PATH)
# plot_exp(PATH, N, STEP)
# ins_wins(PATH) # for reverse sorted N<=100, N2=1000, crossover at N=40
# ins_wins('200N_0ST_1SP_5000N2.npy') # avg case N = 128
# ins_wins(PATH) # N = 87 for 10000N2 from 80-200 for reverse sorted
# ins_wins('200N_80ST_1SP_10000N2_FalseSORT_TrueR.npy') # avg case N=87 -> N=167 (80+87)
# ins_wins('400N_0ST_1SP_100N2_TrueSORT_TrueR.npy') # ins worst case -> N=53
# ins_wins('res/500N_0ST_1SP_100N2_TrueSORT_FalseR.npy')
####################### Q2 ##############################
