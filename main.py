import numpy as np
import matplotlib.pyplot as plt

# Channel: perfect, gaussian noise, linear distorsion, pass band frequency, ISI
# Demodulation: synchrone perfect, syncrhone with phase shift, synchrone with frequency shift, asynchrone
# line coding: polar-NRZ, polar-RZ
# pulse-shaping: sin, rect, sinc, raised-cosine, squared-root-raised-cosine


def sinc(start, finish, n, f, h):
    t = np.linspace(start, finish, n+1, True)
    y = np.sinc(2*f*(t-h))
    return t, y


f = 100
minimum = -100
maximum = 100
a = -1000
b = 0
n = 1000
y_total = np.zeros(n+1)
for i in range(a, b + 1):
    t, y = sinc(minimum, maximum, n, 0.5, i)
    if (i%2)^(i<0):
        y = -y
    y_total = y_total + y
    plt.plot(t, y)
plt.plot(t, y_total)
plt.plot([0, 0], [-2, 2], color='k', linestyle='-', linewidth=2)
plt.plot([0.1, 0.1], [-2, 2], color='k', linestyle='-', linewidth=2)
plt.plot([minimum, maximum], [0, 0], color='k', linestyle='-', linewidth=2)
#plt.xlim([-1, 1])
plt.show()
