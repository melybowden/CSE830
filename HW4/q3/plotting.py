import numpy as np
import matplotlib.pyplot as plt

st, n, sp = 0, 10000000, 1000000
fig_title = 'Insert/Erase times for {:,}-{:,} inputs mapped from int:int with -O2'.format(st,n)
path = 'imgs/{:,}_to_{:,}_by_{:,}_ijj_O2_INS_DEL.png'.format(st,n,sp)
res = [float(_) for _ in input().split()] # input file name
# d_res = [float(_) for _ in input().split()]
half = len(res)//2
res, d_res = res[:half], res[half:]
half = len(res)//2
mm = np.array(res[:half])
umm = np.array(res[half:])
d_mm = np.array(d_res[:half])
d_umm = np.array(d_res[half:])

# # For bad file
# mm = res[:n//sp]
# print(len(mm))
# umm = [res[_] for _ in range(n//sp, len(res), 2)]
# print(len(umm))

intervals = np.array([_ for _ in range(st, n, sp)])
print(intervals.shape)
print(mm.shape)
print(umm.shape)
print(d_mm.shape)
print(d_umm.shape)
m1, b1 = np.polyfit(np.array(intervals), np.array(mm), 1) # find linear fit using least squares
m2, b2 = np.polyfit(np.array(intervals), np.array(umm), 1) # find linear fit using least squares
m3, b3 = np.polyfit(np.array(intervals), np.array(d_mm), 1) # find linear fit using least squares
m4, b4 = np.polyfit(np.array(intervals), np.array(d_umm), 1) # find linear fit using least squares

fig, ax = plt.subplots()
ax.plot(intervals, mm, 'co', label='BBT Insert (std::multimap)')
ax.plot(intervals, m1*intervals + b1, color='c', label='BBT Insert: y={:+.4e}x{:+.4e}'.format(m1,b1))
ax.plot(intervals, d_mm, 'bo', label='BBT Erase (std::multimap)')
ax.plot(intervals, m3*intervals + b3, color='b', label='BBT Erase: y={:+.4e}x{:+.4e}'.format(m3,b3))
ax.plot(intervals, umm, 'mo', label='Hash Table Insert (std::unordered_multimap)')
ax.plot(intervals, m2*intervals + b2, color='m', label='Hash Insert: y={:+.4e}x{:+.4e}'.format(m2,b2))
ax.plot(intervals, d_umm, 'ro', label='Hash Table Erase (std::unordered_multimap)')
ax.plot(intervals, m4*intervals + b4, color='r', label='Hash Erase: y={:+.4e}x{:+.4e}'.format(m4,b4))
ax.legend()
ax.set(xlabel='N Inputs', ylabel='Time (s)',
        title=fig_title)
ax.grid()
plt.savefig(path)
plt.show()
