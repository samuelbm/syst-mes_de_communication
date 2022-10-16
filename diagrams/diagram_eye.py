# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def get_eye_diagram_figure(ax: Axes, signal:np.array, title:str, xlabel:str, ylabel:str, fontsize:int=20):
    I = np.real(signal)
    Q = np.imag(signal)
    maximum_value = 1.1*np.max([np.max(np.abs(I)), np.max(np.abs(Q))])
    ax.scatter(I, Q, color='b')
    ax.axis('equal')
    ax.set_title(title, fontsize=fontsize)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_xlim([-maximum_value, maximum_value])
    ax.set_ylim([-maximum_value, maximum_value])
    ax.axhline(0, color='k', linewidth=2)
    ax.axvline(0, color='k', linewidth=2)
    #ax.tick_params(axis='both', which='major', labelsize=fontsize)

if __name__ == "__main__":
    I = np.array([1,0,0,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,0,1])
    Q = np.array([0,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0])
    signal = np.array([np.exp(1j*2*np.pi*i/4) for i in range(4)])

    fig = plt.figure(figsize=(15,12), dpi=80)
    ax1 = fig.add_subplot(421)
    get_eye_diagram_figure(ax1, signal, 'title', 'xlabel', 'ylabel')

    # plt.tight_layout()
    # plt.savefig('../images/eye_diagram.png')
    plt.show()