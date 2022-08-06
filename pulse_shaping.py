import numpy as np


def pulse_shaping(signal:np.array, pulse:np.array)->np.array:
    interpolated_signal = zero_interpolation(signal, pulse.size)
    return np.convolve(interpolated_signal, pulse)[0:interpolated_signal.size]



def zero_interpolation(signal:np.array, samples_per_symbol:int)->np.array:
    interpolated_signal = np.zeros(signal.size * samples_per_symbol).reshape((samples_per_symbol, signal.size))
    interpolated_signal[0, :] = signal
    return interpolated_signal.transpose().flatten()



