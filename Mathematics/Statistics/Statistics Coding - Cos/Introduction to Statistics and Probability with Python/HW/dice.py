import matplotlib.pyplot as plt
import numpy as np
import random
import math
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
count = 0
D = []
random.seed(0)
P_one = []
P_one_cond2 = []
P_one_cond3 = []
P_one_cond4 = []
P_one_cond5 = []
P_one_cond6 = []
import warnings
warnings.filterwarnings("ignore")
for i in range(1, 10001):
    d = random.choice(np.arange(1, 7))
    D.append(d)

    #if d == 1:
#   redx.append(d)
#  greent.append(d)
#else:
#   if d == 2:
#      redx.append(-10)
#     greent.append(d)
#else:
#   redx.append(-10)
#  greent.append(-10)
for i in range(1, 10001):
    D_trunc = D[0:i]
    index1 = [j for j in range(0, i) if D_trunc[j] == 1]
    indexc2 = [j for j in range(0, i) if D_trunc[j] <= 2]
    indexc3 = [j for j in range(0, i) if D_trunc[j] <= 3]
    indexc4 = [j for j in range(0, i) if D_trunc[j] <= 4]
    indexc5 = [j for j in range(0, i) if D_trunc[j] <= 5]
    indexc6 = [j for j in range(0, i) if D_trunc[j] <= 6]
    #one = [x for x in D_trunc if x == 1]
    #onetwo = [x for x in D_trunc if x == 1 or x == 2]
    P_one.append(len(index1) / i)
    if len(index1) == 0:
        P_one_cond2.append(0)
        P_one_cond3.append(0)
        P_one_cond4.append(0)
        P_one_cond5.append(0)
        P_one_cond6.append(0)
    else:
        P_one_cond2.append(len(index1) / len(indexc2))
        P_one_cond3.append(len(index1) / len(indexc3))
        P_one_cond4.append(len(index1) / len(indexc4))
        P_one_cond5.append(len(index1) / len(indexc5))
        P_one_cond6.append(len(index1) / len(indexc6))
plt.xlabel('x', fontsize=24)
plt.ylabel('y', fontsize=24)


def f(n, conditional, u):
    D_n = D[0:n]
    index1_n = [z for z in index1 if z < n]
    s = [u'x'] * len(index1_n)
    col = ['r'] * len(index1_n)
    S = [160] * len(index1_n)
    #for i in index1_n:
    #   s[i] = u'x'
    #  S[i] = 80
    # col[i] = 'r'
    # y = D_n
    # x = np.arange(1,n+1)
    y = [1] * len(index1_n)
    x = np.array(index1_n) + np.array([1] * len(index1_n))
    for _s, c, _x, _y, _S in zip(s, col, x, y, S):
        plt.scatter(_x, _y, marker=_s, c=c, s=_S)

    if conditional:
        if u == 2:
            indexc = indexc2
        if u == 3:
            indexc = indexc3
        if u == 4:
            indexc = indexc4
        if u == 5:
            indexc = indexc5
        if u == 6:
            indexc = indexc6
        indexc_n = [z for z in indexc if z < n]
        s = [u'o'] * len(indexc_n)
        col = ['g'] * len(indexc_n)
        S = [40] * len(indexc_n)
        y = [D_n[i] for i in indexc_n]
        x = np.array(indexc_n) + np.array([1] * len(indexc_n))
        for _s, c, _x, _y, _S in zip(s, col, x, y, S):
            plt.scatter(_x, _y, marker=_s, c=c, s=_S)

    plt.plot(range(1, n + 1), D_n, 'k.')

    #plt.plot(range(1,n+1), redx[0:n], 'rx', markersize = 10.0, mew = 3)
    #plt.plot(range(1,n+1), greent[0:n], 'go')
    axes = plt.gca()
    fig = plt.gcf()
    fig.set_size_inches(20, 10)
    axes.set_xlim([1, n])
    axes.set_ylim([0, 7])
    plt.show()
    axes = plt.gca()
    fig = plt.gcf()
    fig.set_size_inches(20, 10)
    plt.plot(range(0, 10000), [1 / 6] * 10000, 'b', linewidth=5.0)
    #plt.plot(range(0,10000),[1]*10000, 'k', linewidth = 3.0)
    axes.set_xlim([0, n + 1])
    #axes.set_ylim([min(P_one), max(P_one)])
    plt.plot(np.arange(1, n + 1), P_one[0:n], 'k-', linewidth=3.0)
    plt.xticks(np.arange(1, n + 1), fontsize=20)
    #axes.set_xticklabels(x_ax)
    plt.yticks(fontsize=20)
    axes = plt.gca()
    fig = plt.gcf()
    fig.set_size_inches(20, 10)
    axes.set_xlim([1, n])
    axes.set_ylim([min(P_one), 1])
    if conditional:
        if u == 2:
            plt.plot(range(0, 10000), [1 / 2] * 10000, 'b', linewidth=5.0)
            plt.plot(
                np.arange(1, n + 1), P_one_cond2[0:n], 'g-', linewidth=3.0)
        if u == 3:
            plt.plot(range(0, 10000), [1 / 3] * 10000, 'b', linewidth=5.0)
            plt.plot(
                np.arange(1, n + 1), P_one_cond3[0:n], 'g-', linewidth=3.0)
        if u == 4:
            plt.plot(range(0, 10000), [1 / 4] * 10000, 'b', linewidth=5.0)
            plt.plot(
                np.arange(1, n + 1), P_one_cond4[0:n], 'g-', linewidth=3.0)
        if u == 5:
            plt.plot(range(0, 10000), [1 / 5] * 10000, 'b', linewidth=5.0)
            plt.plot(
                np.arange(1, n + 1), P_one_cond5[0:n], 'g-', linewidth=3.0)
        if u == 6:
            plt.plot(range(0, 10000), [1 / 6] * 10000, 'b', linewidth=5.0)
            plt.plot(
                np.arange(1, n + 1), P_one_cond6[0:n], 'g-', linewidth=3.0)
    plt.xticks(np.arange(1, n + 1), fontsize=20)
    #axes.set_xticklabels(x_ax)
    plt.yticks(fontsize=20)
    plt.show()


interact(
    f,
    n=widgets.IntSlider(min=1, max=10000),
    continuous_update=False,
    conditional=widgets.ToggleButton(
        value=False, description="Conditional Probability"),
    u=widgets.IntSlider(min=2, max=6))
