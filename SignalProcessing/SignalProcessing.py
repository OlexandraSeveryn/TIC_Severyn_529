# Практична робота 2; варіант 10
import numpy
import scipy
import matplotlib.pyplot as plt
from scipy import signal, fft

n = 500
Fs = 1000
F_max = 21

rand_signal = numpy.random.normal(0, 10, n)
time_ox = numpy.arange(n) / Fs
w = F_max / (Fs / 2)
lp_filter = scipy.signal.butter(3, w, 'low', output='sos')
filtration_signal = scipy.signal.sosfiltfilt(lp_filter, rand_signal)

fig, ax = plt.subplots(figsize=(21 / 2.54, 14 / 2.54))
ax.plot(time_ox, filtration_signal, linewidth=1)
ax.set_xlabel("Час (секунди)", fontsize=14)
ax.set_ylabel("Амплітуда сигналу", fontsize=14)
plt.title("Сигнал з максимальною частотою F_max = 21 Гц", fontsize=14)
fig.savefig('./figures/' + 'fig1 (signal)' + '.png', dpi=600)

spectr = scipy.fft.fft(filtration_signal)
mod_val = numpy.abs(scipy.fft.fftshift(spectr))
times_frequency = scipy.fft.fftfreq(n, 1 / n)
symmetry = scipy.fft.fftshift(times_frequency)

fig, ax = plt.subplots(figsize=(21 / 2.54, 14 / 2.54))
ax.plot(symmetry, mod_val, linewidth=1)
ax.set_xlabel("Частота (Гц)", fontsize=14)
ax.set_ylabel("Амплітуда сигналу", fontsize=14)
plt.title("Спектр сигналу з максимальною частотою F_max = 21 Гц", fontsize=14)
fig.savefig('./figures/' + 'fig2 (signal)' + '.png', dpi=600)
