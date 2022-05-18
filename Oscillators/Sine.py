import math
import itertools
import numpy as np


class Sine_Oscillator:

    def __init__(self, freq, amp=1, phase=0, sample_rate=44100, duration=1):
        self.freq = freq
        self.amp = amp
        self.phase = phase
        self.sample_rate = sample_rate
        self.samples = round(sample_rate * duration)

    def sin_osc(self):
        self.phase = (self.phase / 360) * 2 * math.pi
        increment = (2 * math.pi * self.freq) / self.sample_rate
        return (math.sin(self.phase + v) * self.amp for v in itertools.count(start=0, step=increment))

    def get_iterator(self, iterator):
        return [next(iterator) for i in range(self.samples)]

    def get_wave(self):
        osc = self.sin_osc()
        y = np.array(self.get_iterator(osc), dtype=np.float32)
        audio = y * (2 ** 15 // 2) / np.max(np.abs(y))  # ensuring the correct range for the amplitude
        return audio.astype(np.int16)


