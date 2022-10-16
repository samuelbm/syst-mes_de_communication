import numpy as np

def modulation(complex_signal:np.array)->np.array:
    pass

def demodulation(I:np.array, Q:np.array)->np.array:
    pass


def rotate(complex_signal: np.array, phase_error: float, frequency_error: float, fs: float)-> np.array:
    t = fs*np.linspace(0, complex_signal.size, complex_signal.size, False)
    theta = phase_error + t*frequency_error
    rotation = np.exp(1j*theta)
    rotated_signal = np.zeros(complex_signal.size, dtype=complex_signal.dtype)
    np.multiply(complex_signal, rotation, rotated_signal)
    return rotated_signal


if __name__ == "__main__":
    pass

