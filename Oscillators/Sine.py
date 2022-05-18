import math
import itertools
import numpy as np


class Sine_Oscillator:

    def sin_osc(self, freq, amp, phase, sample_rate):
        phase = (phase / 360) * 2 * math.pi
        increment = (2 * math.pi * freq) / sample_rate
        return (math.sin(phase + v) * amp for v in itertools.count(start=0, step=increment))

    def get_iterator(self, iterator, n):
        return [next(iterator) for i in range(n)]

    def get_wave(self, freq, amp=1, phase=0, sample_rate=44100):
        osc = self.sin_osc(freq, amp, phase, sample_rate)
        y = np.array(self.get_iterator(osc, sample_rate), dtype=np.float32)
        audio = y * (2 ** 15 // 2) / np.max(np.abs(y))  # ensuring the correct range for the amplitude
        return audio.astype(np.int16)


