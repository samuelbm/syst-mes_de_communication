import numpy as np
import matplotlib.pyplot as plt


n = 1024
f = 60
fs = 200
t_start = -(n/(2*fs))
t_stop =((n-1)/(2*fs))
print(t_start, t_stop)

t = np.linspace(t_start, t_stop, n, False)
wave = np.array([np.sinc(2*f*tk) if np.abs(tk) < 1/(4*f) else 0 for tk in t])
#print(t.size)
#wave = np.sinc(2*f*t)
fft_wave = np.fft.fft(wave)
fft_freq = np.fft.fftfreq(n=wave.size, d=1/fs)
plt.plot(np.fft.fftshift(fft_freq), np.fft.fftshift(np.abs(fft_wave)))
#plt.plot(t, wave)
plt.show()