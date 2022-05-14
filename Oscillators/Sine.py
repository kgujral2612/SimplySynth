import numpy as np
from Oscillators import Oscillator


class Sine_Oscillator(Oscillator.WaveOscillator):

    def get_wave(self, frequency, duration, phase, sample_rate=44100):
        sample_count = int(sample_rate * duration)
        x = np.linspace(0, duration, num=sample_count, endpoint=False)
        y = np.sin((2 * np.pi * frequency * x) + phase)
        audio_sin = y * (2 ** 15 // 4) / np.max(np.abs(y))
        audio_sin = audio_sin.astype(np.int16)
        return audio_sin, sample_rate

