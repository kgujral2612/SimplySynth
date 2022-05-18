import math
import itertools
import numpy as np


class SawTooth_Oscillator:

    def __init__(self, freq=440, amp=1, phase=0, sample_rate=44_100, duration=1):
        self.freq = freq
        self.amp = amp
        self.phase = phase
        self.sample_rate = sample_rate
        self.samples = round(sample_rate * duration)

    def sw_osc(self):
        period = self.sample_rate/self.freq
        self.phase = ((self.phase + 90) / 360) * period
        increment = 1
        return (2*((v + self.phase)/period - math.floor(0.5 + (v + self.phase)/period)) * self.amp for v in itertools.count(start=0, step=increment))

    def get_iterator(self, iterator):
        return [next(iterator) for i in range(self.samples)]

    def get_wave(self):
        osc = self.sw_osc()
        y = np.array(self.get_iterator(osc), dtype=np.float32)
        audio = y * (2 ** 15 // 2) / np.max(np.abs(y))  # ensuring the correct range for the amplitude
        return audio.astype(np.int16)

