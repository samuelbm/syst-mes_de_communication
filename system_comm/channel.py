import random

import numpy as np
import matplotlib.pyplot as plt

def generate_noise(samples):
    random.seed(10)
    return 2*np.array([np.random.normal() for sample in range(samples)])-1

if __name__ == "__main__":
    pass