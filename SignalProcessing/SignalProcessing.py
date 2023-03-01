# Практична робота 3; варіант 10
import numpy
import scipy
import matplotlib.pyplot as plt
from scipy import signal, fft

n = 500
Fs = 1000
F_max = 21
F_filter = 28

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

discrete_signals = []
discrete_spectrums = []
w2 = F_filter/(Fs/2)
discrete_signals_filter = []
dispersion_differ = []
sign_noise = []
# Дискретизація сигналу
for Dt in [2, 4, 8, 16]:
    discrete_signal = numpy.zeros(n)
    for i in range(0, round(n/Dt)):
        discrete_signal[i * Dt] = filtration_signal[i * Dt]
    discrete_signals += [list(discrete_signal)]
# Розрахунок спектрy сигналів
    discrete_spectr = scipy.fft.fft(discrete_signal)
    discrete_mod_val = numpy.abs(scipy.fft.fftshift(discrete_spectr))
    discrete_spectrums += [list(discrete_mod_val)]
# Відновлення аналогового сигналу з дискретного
    discrete_parameters = scipy.signal.butter(3, w2, 'low', output='sos')
    discrete_filter = scipy.signal.sosfiltfilt(discrete_parameters, discrete_signal)
    discrete_signals_filter += [list(discrete_filter)]
# Дисперсія та співвідношення сигнал-шум
    E1 = discrete_signals_filter - rand_signal
    dispersion1 = numpy.var(rand_signal)
    dispersion2 = numpy.var(E1)
    dispersion_differ += [dispersion2]
    sign_noise += [numpy.var(rand_signal)/numpy.var(E1)]

# figure 3
fig, ax = plt.subplots(2, 2, figsize=(21 / 2.54, 14 / 2.54))
s = 0
for i in range(0, 2):
    for j in range(0, 2):
        ax[i][j].plot(time_ox, discrete_signals[s], linewidth=1)
        s += 1
fig.supxlabel('Час (секунди)', fontsize=14)
fig.supylabel('Амплітуда сигналу', fontsize=14)
fig.suptitle('Сигнал з кроком дискретизації Dt = (2, 4, 8, 16)', fontsize=14)
fig.savefig('./figures/' + 'Сигнал з кроком дискретизації Dt = (2, 4, 8, 16)' + '.png', dpi=600)

# figure 4
fig, ax = plt.subplots(2, 2, figsize=(21 / 2.54, 14 / 2.54))
s4 = 0
for i in range(0, 2):
    for j in range(0, 2):
        ax[i][j].plot(symmetry, discrete_spectrums[s4], linewidth=1)
        s4 += 1
fig.supxlabel('Частота (Гц)', fontsize=14)
fig.supylabel('Амплітуда спектру', fontsize=14)
fig.suptitle('Спектри сигналів з кроком дискретизації Dt = (2, 4, 8, 16)', fontsize=14)
fig.savefig('./figures/' + 'Спектри сигналів з кроком дискретизації Dt = (2, 4, 8, 16)' + '.png', dpi=600)

# figure 5
fig, ax = plt.subplots(2, 2, figsize=(21 / 2.54, 14 / 2.54))
s5 = 0
for i in range(0, 2):
    for j in range(0, 2):
        ax[i][j].plot(time_ox, discrete_signals_filter[s5], linewidth=1)
        s5 += 1
fig.supxlabel('Частота (Гц)', fontsize=14)
fig.supylabel('Амплітуда спектру', fontsize=14)
fig.suptitle('Відновлені аналогові сигнали з кроком дискретизації Dt = (2, 4, 8, 16)', fontsize=14)
fig.savefig('./figures/' + 'Відновлені аналогові сигнали з кроком дискретизації Dt = (2, 4, 8, 16)' + '.png', dpi=600)

X = [2, 4, 8, 16]
# figure 6
fig, ax = plt.subplots(figsize=(21 / 2.54, 14 / 2.54))
ax.plot(X, dispersion_differ, linewidth=1)
ax.set_xlabel("Крок дискретизації", fontsize=14)
ax.set_ylabel("Дисперсія", fontsize=14)
plt.title("Сигнал з максимальною частотою F_max = 17", fontsize=14)
fig.savefig("./figures/" + "Залежність дисперсії від кроку дискретизації" + ".png", dpi=600)

# figure 7
fig, ax = plt.subplots(figsize=(21 / 2.54, 14 / 2.54))
ax.plot(X, sign_noise, linewidth=1)
ax.set_xlabel("Крок дискретизації", fontsize=14)
ax.set_ylabel("ССШ", fontsize=14)
plt.title("Сигнал з максимальною частотою F_max = 17", fontsize=14)
fig.savefig("./figures/" + "Залежність співвідношення сигнал-шум від кроку дискретизації" + ".png", dpi=600)
