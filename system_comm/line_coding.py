import numpy as np
import matplotlib.pyplot as plt

def binary_message_to_symbol_message(binary_message: np.array, bits_per_symbol: int)->np.array:
    nb_symbols = int(binary_message.size/bits_per_symbol)
    symbol_message = np.zeros(nb_symbols)
    weight = np.array([2**(bits_per_symbol-bit-1) for bit in range(bits_per_symbol)])
    for index in range(nb_symbols):
        symbol_message[index] = np.sum(weight * binary_message[index*bits_per_symbol: (index+1)*bits_per_symbol])
    return symbol_message

def binary_message_to_I_and_Q_message(binary_message:np.array):
    I_message = binary_message[np.array([2*i for i in range(int(binary_message.size/2))])]
    Q_message = binary_message[np.array([(2 * i) + 1 for i in range(int(binary_message.size / 2))])]
    return I_message, Q_message

def NRZ_line_coding(symbol_message: np.array, fs:float, rb:float, bits_per_symbol:int, pulse=np.array([1])):
    nb_symbols = symbol_message.size
    samples_per_bit = int(fs/rb)
    signal = np.zeros(nb_symbols * samples_per_bit)
    for index in range(nb_symbols):
        signal[index*samples_per_bit] = (2/(2**bits_per_symbol-1))*symbol_message[index]-1
    return np.convolve(signal, pulse)[0:-pulse.size+1]

if __name__ == "__main__":
   pass

