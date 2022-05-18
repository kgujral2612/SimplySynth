import math
import itertools
import numpy as np


class Square_Oscillator:

    def sq_osc(self, freq, amp, phase, sample_rate, wave_range, threshold):
        phase = (phase / 360) * 2 * math.pi
        increment = (2 * math.pi * freq) / sample_rate
        return ((wave_range[0] if math.sin(phase + v) < threshold else wave_range[1]) * amp for v in itertools.count(start=0, step=increment))

    def get_iterator(self, iterator, n):
        return [next(iterator) for i in range(n)]

    def get_wave(self, freq=440, amp=1, phase=0, sample_rate=44_100, wave_range=(-1, 1), threshold=0):
        osc = self.sq_osc(freq, amp, phase, sample_rate, wave_range, threshold)
        y = np.array(self.get_iterator(osc, sample_rate), dtype=np.float32)
        audio = y * (2 ** 15 // 2) / np.max(np.abs(y))  # ensuring the correct range for the amplitude
        return audio.astype(np.int16)


