from AdditiveSynthesis import WaveAdder
from Oscillators import Sine, Triangle

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
    return WaveAdder.Wave_Adder(sine_list, duration=duration).mixer()


# flute
def flute(frequency, duration, components=2):
    sine_list = []
    f = frequency
    a = 1.0
    for i in range(components):
        sine_list.append(Triangle.Triangle_Oscillator(freq=f, amp=a, duration=duration))
        f += frequency
        a /= 2.0
    return WaveAdder.Wave_Adder(sine_list, duration=duration).mixer()


# bell
# reference: http://www.themillatju.online/music-tech/
def bell(frequency, duration, components=9):
    sine_list = []
    a = 1.0
    freq_coeffs = [0.56, 0.92, 1.19, 1.71, 2, 2.74, 3, 3.76, 4.07]
    for i in range(components):
        sine_list.append(Sine.Sine_Oscillator(freq=(frequency * freq_coeffs[i]), amp=a, duration=duration))
        a /= 2.0
    return WaveAdder.Wave_Adder(sine_list, duration=duration).mixer()

