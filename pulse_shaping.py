import numpy as np
import matplotlib.pyplot as plt

def pulse_shaping(signal:np.array, pulse:np.array)->np.array:
    interpolated_signal = zero_interpolation(signal, pulse.size)
    return np.convolve(interpolated_signal, pulse)[0:interpolated_signal.size]



def zero_interpolation(signal:np.array, samples_per_symbol:int)->np.array:
    interpolated_signal = np.zeros(signal.size * samples_per_symbol).reshape((samples_per_symbol, signal.size))
    interpolated_signal[0, :] = signal
    return interpolated_signal.transpose().flatten()


def get_pulse_filter(pulse_name, line_code_name, nb_bits_per_symbol):
    if line_code_name == "NRZ":
        pulse_width = nb_bits_per_symbol
    elif line_code_name == "RZ":
        pulse_width = int(nb_bits_per_symbol/2)
    else:
        print("line code name has no match found")

    if pulse_name == "rect":
        print("rect")
    elif pulse_name == "sine":
        print("sine")
    elif pulse_name == "sinc":
        print("sinc")
    elif pulse_name == "RC":
        print("RC")
    elif pulse_name == "RRC":
        print("RRC")
    else:
        print("pulse name has no match found")

def get_sinc_pulse(Rb, fs, symbol_period):
    t = np.linspace(-symbol_period, symbol_period, int(symbol_period*fs/Rb))
    return np.sinc(t)

def get_rect_pulse(Rb, fs, symbol_period):
    t = np.linspace(-symbol_period, symbol_period, int(symbol_period * fs / Rb))
    return np.array([1 if np.abs(tk) <= Rb else 0 for tk in t])

def get_sin_pulse(Rb, fs, symbol_period):
    t = np.linspace(-symbol_period, symbol_period, int(symbol_period * fs / Rb))
    return np.array([np.cos(np.pi*tk/2) if np.abs(tk) <= Rb else 0 for tk in t])

def get_raised_cosine_pulse(Rb, fs, symbol_period):
    return 1

def get_root_raised_cosine_pulse(Rb, fs, symbol_period):
    return 1

plt.plot(get_sinc_pulse(1, 100, 5))
plt.plot(get_rect_pulse(1,100,5))
plt.plot(get_sin_pulse(1, 100, 5))
plt.show()