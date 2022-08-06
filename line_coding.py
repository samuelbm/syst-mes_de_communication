import numpy as np



def line_coding(binary_message:np.array, nb_bits_per_symbol:int)->np.array:
    nb_symbols = int(binary_message.size / nb_bits_per_symbol)
    symbols = np.zeros(nb_symbols)
    for index in range(nb_symbols):
        start_index = index*nb_bits_per_symbol
        symbol_bits = binary_message[start_index: start_index + nb_bits_per_symbol]
        symbols[index] = binary_message_to_symbols(symbol_bits)
    return symbols

def binary_message_to_symbols(symbol_bits: np.array)->int:
    length = symbol_bits.size
    weight = [2**(length-i-1) for i in range(length)]
    return np.sum(symbol_bits * weight)

