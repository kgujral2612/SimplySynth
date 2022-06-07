from AdditiveSynthesis import WaveAdder
from Oscillators import Sine, Triangle
from DataAugmentation.Effects import *
from Envelopes import Envelope
#
# reference: https://www.projectrhea.org/rhea/index.php/Fourier_analysis_in_Music
#


# oboe
def oboe(frequency, duration, components=10):
    sine_list = []
    f = frequency
    coeffs = [1.0, 0.9, 2.1, 0.2, 0.22, 0.25, 0.55, 0.3, 0.25, 0, 0.01, 0.001, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(components):
        a = coeffs[i]
        sine_list.append(Sine.Sine_Oscillator(freq=f, amp=a, duration=duration))
        f = f + frequency
    return white_noise(WaveAdder.Wave_Adder(sine_list, duration=duration).mixer())


# flute
def flute(frequency, duration, components=10):
    sine_list = []
    f = 52.49
    coeffs = [2.6275144, 1971.9965, 773.3403, 416.96512, 920.1261, 184.70355, 78.39568, 88.53661, 25.209017, 4.08456]
    for i in range(components):
        a = coeffs[i]
        sine_list.append(Sine.Sine_Oscillator(freq=f, amp=a, duration=duration))
        if i==0:
            f=0
        f = f + frequency
    return WaveAdder.Wave_Adder(sine_list, duration=duration).instr_mixer()


# bell
# reference: http://www.themillatju.online/music-tech/
def bell(frequency, duration, components=9):
    sine_list = []
    a = 1.0
    freq_coeffs = [0.56, 0.92, 1.19, 1.71, 2, 2.74, 3, 3.76, 4.07]
    for i in range(components):
        sine_list.append(Sine.Sine_Oscillator(freq=(frequency * freq_coeffs[i]), amp=a, duration=duration))
        a /= 2.0
    return  white_noise(WaveAdder.Wave_Adder(sine_list, duration=duration).mixer())

def violin(frequency, duration, components=20):
    sine_list = []
    f = frequency
    coeffs = [565.67645, 1480.7347, 949.55945, 321.98218, 317.2813, 172.26096, 136.12212, 121.8747, 208.8552, 67.335846, 172.15009, 32.675083, 93.15583, 19.948515, 27.01039, 16.36757, 38.366905, 23.404427, 20.308054, 18.097034]
    for i in range(components):
        a = coeffs[i]
        sine_list.append(Sine.Sine_Oscillator(freq=f, amp=a, duration=duration))
        f = f + frequency
    return WaveAdder.Wave_Adder(sine_list, duration=duration).instr_mixer()