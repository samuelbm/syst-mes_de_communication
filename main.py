import numpy as np
import matplotlib.pyplot as plt

from diagrams.diagram_constellation import get_constellation_diagram
from diagrams.diagram_time import plot_time_diagram, scatter_time_diagram
from system_comm.channel import generate_noise
from system_comm.message import*
from system_comm.line_coding import*
from system_comm.modulation_demodulation import rotate
from system_comm.modulation_scheme import OQPSK
from system_comm.pulse_shaping import*
from system_comm.sampling import*
from diagrams.diagram_eye import*


# Channel: perfect, gaussian noise, linear distorsion, pass band frequency, ISI
# Demodulation: synchrone perfect, syncrhone with phase shift, synchrone with frequency shift, asynchrone
# line coding: polar-NRZ, polar-RZ
# pulse-shaping: sin, rect, sinc, raised-cosine, squared-root-raised-cosine


#
# plt.plot(t, y_total)
# plt.plot([0, 0], [-2, 2], color='k', linestyle='-', linewidth=2)
# plt.plot([0.1, 0.1], [-2, 2], color='k', linestyle='-', linewidth=2)
# plt.plot([minimum, maximum], [0, 0], color='k', linestyle='-', linewidth=2)
# #plt.xlim([-1, 1])
# plt.show()

if __name__ == "__main__":
    rb = 1
    fs = 100
    samples_per_bit = int(fs/rb)
    message_length = 50
    bits_per_symbol = 1

    # message
    binary_message = get_same_random_message(message_length)
    I_binary, Q_binary = binary_message_to_I_and_Q_message(binary_message)

    # line coding and pulse shaping
    sin_pulse = get_sin_pulse(rb, fs)
    I_signal = NRZ_line_coding(I_binary, fs, rb, bits_per_symbol, sin_pulse)
    Q_signal = NRZ_line_coding(Q_binary, fs, rb, bits_per_symbol, sin_pulse)
    complex_signal = OQPSK(I_signal, Q_signal, samples_per_bit)
    t_I_perfect, I_perfect = sample_signal(complex_signal.real, int(samples_per_bit/2), fs, rb)
    t_Q_perfect, Q_perfect = sample_signal(complex_signal.imag, samples_per_bit, fs, rb)
    phase_error_samples = rotate(I_perfect + 1j*Q_perfect, np.pi/6, 0, fs)
    frequency_error_samples = rotate(I_perfect + 1j*Q_perfect, np.pi/6, 0.01, fs)
    I_noise = I_perfect + 0.02*generate_noise(I_perfect.size)
    Q_noise = Q_perfect + 0.02*generate_noise(Q_perfect.size)
    t_signal = np.linspace(0, complex_signal.size, complex_signal.size, False)/fs

    fig = plt.figure(figsize=(16,12), dpi=80)
    ax1a = fig.add_subplot(6,2,1)
    plot_time_diagram(ax1a, t_signal, complex_signal.real, 'O-QPSK signal in phase (I)', 'Time [s]', 'Amplitude [V]', '', 'b', 20)
    scatter_time_diagram(ax1a, t_I_perfect, I_perfect, 'O-QPSK signal in phase (I)', 'Time [s]', 'Amplitude [V]', '', 'b', 20)

    ax1b = fig.add_subplot(6,2,3)
    plot_time_diagram(ax1b, t_signal, complex_signal.imag, 'O_QPSK in quadrature (Q)', 'Time [s]', 'Amplitude [V]', '', 'orange', 20)
    scatter_time_diagram(ax1b, t_Q_perfect, Q_perfect, 'O_QPSK in quadrature (Q)', 'Time [s]', 'Amplitude [V]', '', 'orange', 20)

    ax2 = fig.add_subplot(6,2,(2,4))
    get_constellation_diagram(ax2, complex_signal, 'Constellation diagram of complete signal', 'I', 'Q', '', 20)

    ax3 = fig.add_subplot(6,2,(5,7))
    get_constellation_diagram(ax3, I_perfect + 1j * Q_perfect, 'Constellation diagram of sampled signal', 'I', 'Q', '', 20)

    ax4 = fig.add_subplot(6,2,(6,8))
    get_constellation_diagram(ax4, phase_error_samples, 'Constellation diagram of signal with phase error', 'I', 'Q', '', 20)

    ax5 = fig.add_subplot(6, 2, (9, 11))
    get_constellation_diagram(ax5, frequency_error_samples, 'Constellation diagram of signal with drifting clock', 'I', 'Q', '', 20)

    ax6 = fig.add_subplot(6, 2, (10, 12))
    get_constellation_diagram(ax6, I_noise + 1j * Q_noise, 'Constellation diagram of signal with noise', 'I', 'Q', '', 20)

    plt.tight_layout()
    plt.savefig('./images/OQPSK.png')
    plt.show()

