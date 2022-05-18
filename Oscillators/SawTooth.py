import math
import itertools
import numpy as np


class SawTooth_Oscillator:

    def sw_osc(self, freq, amp, phase, sample_rate):
        period = sample_rate/freq
        phase = ((phase + 90) / 360) * period
        increment = 1
        return (2*((v + phase)/period - math.floor(0.5 + (v + phase)/period)) * amp for v in itertools.count(start=0, step=increment))

    def get_iterator(self, iterator, n):
        return [next(iterator) for i in range(n)]

    def get_wave(self, freq=440, amp=1, phase=0, sample_rate=44_100):
        osc = self.sw_osc(freq, amp, phase, sample_rate)
        y = np.array(self.get_iterator(osc, sample_rate), dtype=np.float32)
        audio = y * (2 ** 15 // 2) / np.max(np.abs(y))  # ensuring the correct range for the amplitude
        return audio.astype(np.int16)

