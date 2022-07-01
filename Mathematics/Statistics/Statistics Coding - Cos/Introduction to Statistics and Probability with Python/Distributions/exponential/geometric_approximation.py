import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import binom
import ipywidgets as widgets

import warnings
warnings.filterwarnings("ignore")

def exponential_approx(n, p):
    '''
    Approximate the PMF of the geometric distribution with the 
    PDF of the exponential distribution.
    '''
    x = np.arange(1, n+1)
    y = [((1-p)**(z-1))*p for z in x]
    λ = p
    x0 = np.arange(1, n+1, n/1000)
    y0 = λ*np.exp(-λ*x0)
    plt.plot(x0, y0, label = 'Exponential(%0.2f)' %λ)
    plt.plot(x, y, 'r', label = 'Geometric(%0.2f)' %p)
    plt.legend(fontsize = 20)
    plt.title("Exponential Approximation of Geometric(%.2f)" %p, fontsize = 20)
    plt.gcf().set_size_inches(20,10)
    axes = plt.gca().set_xlim([1,n])
    plt.xlabel('x', fontsize = 20)
    plt.ylabel('y', fontsize = 20)
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.show()
    x0 = np.arange(1, n+1)
    y0 = λ*np.exp(-λ*x0)
    print("")
    print('|| P_Exponential - P_Geometric ||\u2081 = ',sum(abs(y-y0)))
    print("")
    print("")
    
widgets.interact(
            exponential_approx, 
            p = widgets.FloatSlider(min=0, max=1, step=0.01, value=0.5), 
            n = widgets.IntSlider(min=2, max=1000, step=1, value=10))
