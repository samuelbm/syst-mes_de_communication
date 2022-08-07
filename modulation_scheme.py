import numpy as np
import matplotlib.pyplot as plt


def compute_I_Q_line_code(m, pulse):
    even_indices = np.array([i for i in range(np.size(m)) if not i%2])
    odd_indicies = np.array([i for i in range(np.size(m)) if i%2])
    Im = m[even_indices]
    Qm = m[odd_indicies]
    half_period_samples = int(pulse.size/2)
    in_phase_line_code = np.zeros(Im.size * pulse.size + half_period_samples)
    in_quadrature_line_code = np.zeros(Qm.size * pulse.size + half_period_samples)
    for index in range(Im.size):
        in_phase_line_code[index * pulse.size + half_period_samples - 1] = 2*Im[index]-1
        in_quadrature_line_code[index * pulse.size + 2*half_period_samples - 1] = 2*Qm[index]-1
    I = np.convolve(in_phase_line_code, pulse, 'same')
    Q = np.convolve(in_quadrature_line_code, pulse, 'same')
    return (I, Q)

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


m = np.array([0,0,0,1,1,0,1,1])
Fs = 20
Rb = 1
samples_per_bit = int(Fs/Rb)
d_phase = np.pi/6
d_freq = 0
start = int(d_phase * samples_per_bit/np.pi) - 1
t = np.linspace(0, np.pi, samples_per_bit, False)
pulse = np.sin(t)
I, Q = compute_I_Q_line_code(m, pulse)
I_rotated, Q_rotated = rotate(I, Q, d_phase, d_freq, Fs)
Im, Qm = sample_message(I_rotated, Q_rotated, samples_per_bit, start)



fig = plt.figure()
ax1 = fig.add_subplot(211)
circle2 = plt.Circle((0, 0), np.sqrt(2), color='k', fill=False, zorder = 0)
ax1.add_patch(circle2)
ax1.axis('equal')
plt.scatter(Im, Qm)

ax2 = fig.add_subplot(212)
t = np.linspace(0, I_rotated.size / Fs, I_rotated.size, False)
ax2.plot(t, I_rotated, t, Q_rotated)
plt.show()
