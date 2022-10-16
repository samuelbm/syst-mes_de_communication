import numpy as np
import matplotlib.pyplot as plt

def OQPSK(I:np.array, Q:np.array, samples_per_bit)->np.array:
    signal = np.zeros(I.size + int(samples_per_bit/2), dtype=np.complex128)
    signal[0:I.size] = I
    signal[int(samples_per_bit/2):signal.size] += 1j*Q
    return signal

def sample_message(I, Q, samples_per_bit, start):
    nb_bit = int((I.size - start)/samples_per_bit)
    half_period_samples = int(samples_per_bit/2)
    I_sample = np.zeros(nb_bit)
    Q_sample = np.zeros(nb_bit)
    for index in range(nb_bit):
        I_sample[index] = I[start + index*samples_per_bit + half_period_samples]
        Q_sample[index] = Q[start + index*samples_per_bit + 2*half_period_samples]
    return (I_sample, Q_sample)

def rotate(I, Q, d_phase, d_freq, fs):
    theta = np.linspace(d_phase, d_phase + 2*np.pi*d_freq*I.size/fs, I.size, False)
    I_rotated = I*np.cos(theta) - Q*np.sin(theta)
    Q_rotated = I*np.sin(theta) + Q*np.cos(theta)
    return (I_rotated, Q_rotated)



if __name__ == "__main__":
    pass