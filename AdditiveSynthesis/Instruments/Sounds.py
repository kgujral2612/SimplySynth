from AdditiveSynthesis import WaveAdder
from Oscillators import Sine


# oboe
def oboe(frequency, components):
    sine_list = []
    f = frequency
    coeffs = [1.0, 0.9, 2.1, 0.2, 0.22, 0.25, 0.55, 0.3, 0.25, 0, 0.01, 0.001, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(components):
        a = coeffs[i]
        sine_list.append(Sine.Sine_Oscillator(freq=f, amp=a))
        f = f + frequency
    return WaveAdder.Wave_Adder(sine_list).mixer()


def flute(frequency, components):
    sine_list = []
    f = frequency
    a = 1.0
    for i in range(components):
        sine_list.append(Sine.Sine_Oscillator(freq=f, amp=a))
        f += frequency
        a /= 2.0
    return WaveAdder.Wave_Adder(sine_list).mixer()
