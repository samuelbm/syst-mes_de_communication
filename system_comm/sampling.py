import numpy as np
import matplotlib.pyplot as plt

def sample_signal(signal:np.array, start:int, fs, Rb)->np.array:
    samples_per_bit = int(fs/Rb)
    index = np.array([index for index in range(start, signal.size,samples_per_bit)])
    t = index / fs
    sampled_signal = np.array(signal[index], dtype=np.complex128)
    return t, sampled_signal

if __name__ == "__main__":
    pass
