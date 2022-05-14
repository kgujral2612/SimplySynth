import numpy as np
from scipy import signal
from Oscillators import Oscillator


class Square_Oscillator(Oscillator.WaveOscillator):

    def get_wave(self, frequency, duration=1, phase=0, sample_rate=44100):
        sample_count = int(sample_rate * duration)
        x = np.linspace(0, duration, num=sample_count, endpoint=False)
        y = signal.square((2 * np.pi * frequency * x) + phase)
        return y, sample_rate

