""" This module simulates sounds of actual instruments
    reference: https://www.projectrhea.org/rhea/index.php/Fourier_analysis_in_Music
"""
from additive_synthesis.wave_adder import WaveAdder
from oscillators.sine import SineOscillator
from data_augmentation.effects import white_noise


def oboe(frequency, duration, components=10):
    """ creates the sound of an oboe 
        for a given frequency and duration
    """
    sine_list = []
    freq = frequency
    coeffs = [1.0, 0.9, 2.1, 0.2, 0.22, 0.25, 0.55, 0.3, 0.25,
              0, 0.01, 0.001, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(components):
        sine_list.append(SineOscillator(
            freq=freq, amp=coeffs[i], duration=duration))
        freq = freq + frequency
    return white_noise(WaveAdder(sine_list, duration=duration).mixer())


def flute(frequency, duration, components=10):
    """ creates the sound of a flute 
        for a given frequency and duration
    """
    sine_list = []
    freq = 52.49
    coeffs = [2.6275144, 1971.9965, 773.3403, 416.96512,
              920.1261, 184.70355, 78.39568, 88.53661, 25.209017, 4.08456]
    for i in range(components):
        sine_list.append(SineOscillator(
            freq=freq, amp=coeffs[i], duration=duration))
        if i == 0:
            freq = 0
        freq = freq + frequency
    return WaveAdder(sine_list, duration=duration).instr_mixer()


def bell(frequency, duration, components=9):
    """ creates the sound of a bell 
        for a given frequency and duration
        reference: http://www.themillatju.online/music-tech/
    """
    sine_list = []
    amp = 1.0
    freq_coeffs = [0.56, 0.92, 1.19, 1.71, 2, 2.74, 3, 3.76, 4.07]
    for i in range(components):
        sine_list.append(SineOscillator(freq=(frequency * freq_coeffs[i]),
                                              amp=amp, duration=duration))
        amp /= 2.0
    return white_noise(WaveAdder(sine_list, duration=duration).mixer())


def violin(frequency, duration, components=20):
    """ creates the sound of a violin 
        for a given frequency and duration
    """
    sine_list = []
    freq = frequency
    coeffs = [565.67645, 1480.7347, 949.55945, 321.98218, 317.2813, 172.26096,
              136.12212, 121.8747, 208.8552, 67.335846, 172.15009, 32.675083, 93.15583,
              19.948515, 27.01039, 16.36757, 38.366905, 23.404427, 20.308054, 18.097034]
    for i in range(components):
        sine_list.append(SineOscillator(
            freq=freq, amp=coeffs[i], duration=duration))
        freq = freq + frequency
    return WaveAdder(sine_list, duration=duration).instr_mixer()
