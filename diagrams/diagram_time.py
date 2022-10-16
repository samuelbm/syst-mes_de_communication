# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def plot_time_diagram(ax: Axes, t:np.array, signal:np.array, title:str, xlabel:str, ylabel:str, label:str, color:str, fontsize:int=20):
    maximum_value = 1.2*np.max(np.abs(signal))
    ax.plot(t, signal, color=color, label=label)
    #ax.axis('equal')
    ax.set_title(title, fontsize=fontsize)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    #ax.set_xlim([-maximum_value, maximum_value])
    ax.set_ylim([-maximum_value, maximum_value])
    ax.axhline(0, color='k', linewidth=2)
    ax.axvline(0, color='k', linewidth=2)
    #ax.tick_params(axis='both', which='major', labelsize=fontsize)
    if label is not '':
        ax.legend(fontsize=fontsize)

def scatter_time_diagram(ax: Axes, t:np.array, signal:np.array, title:str, xlabel:str, ylabel:str, label:str, color:str, fontsize:int=20):
    #maximum_value = 1.1*np.max(np.abs(signal))
    ax.scatter(t, signal, color=color, label=label)
    #ax.axis('equal')
    ax.set_title(title, fontsize=fontsize)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    #ax.set_xlim([-maximum_value, maximum_value])
    #ax.set_ylim([-maximum_value, maximum_value])
    ax.axhline(0, color='k', linewidth=2)
    ax.axvline(0, color='k', linewidth=2)
    #ax.tick_params(axis='both', which='major', labelsize=fontsize)
    if label is not '':
        ax.legend(fontsize=fontsize)

if __name__ == "__main__":
    pass