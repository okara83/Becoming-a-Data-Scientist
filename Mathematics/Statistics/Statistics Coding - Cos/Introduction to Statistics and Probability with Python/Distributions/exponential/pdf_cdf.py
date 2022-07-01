import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import binom
import ipywidgets as widgets

def plot_pdf_cdf(λ, x_max, y_max, CDF):
    '''
    Plot the PDF and the CDF of the exponential distribution.
    '''
    x = np.arange(0, x_max, x_max/1000)
    y = λ*np.exp(-λ*x)
    z = 1 - np.exp(-λ*x)
    plt.plot(x, y, linewidth = 3.0, label = 'PDF')
    if CDF == True:
        plt.plot(x, z, 'r', linewidth = 3.0, label = 'CDF')
    plt.title("Exponential(%.2f)" %λ, fontsize = 20)
    plt.gcf().set_size_inches(20,10)
    plt.xlabel('x', fontsize = 20)
    plt.ylabel('y', fontsize = 20)
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.gca().set_xlim([0,x_max])
    plt.gca().set_ylim([0,y_max])
    plt.legend(fontsize = 18)
    plt.show()
widgets.interact(
            plot_pdf_cdf, 
            λ=widgets.FloatSlider(description = '$\lambda$', min=0.01, max=10, step=0.01, value=0.5), 
            x_max=widgets.FloatSlider(description = '$x_{\max}$', min=1, max=1000, step=1, value=10), 
            y_max=widgets.FloatSlider(description = '$y_{\max}$', min=0.1, max=10, step=0.1, value=1), 
            CDF = widgets.ToggleButton(value = False))
