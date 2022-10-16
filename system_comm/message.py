import numpy as np
import random
def get_same_random_message(message_length_in_bits:int) -> np.array:
    random.seed(10)
    return np.array([random.randint(0,1) for bit in range(message_length_in_bits)])

if __name__ == "__main__":
    pass