""" An oscillator that produces square waves
"""

import math
import itertools
import numpy as np


class SquareOscillator:
    """ Class to produce a square wave """

    def __init__(self, freq=440, amp=1, phase=0, sample_rate=48000, wave_range=(-1, 1), threshold=0, duration=1):
        self.freq = freq
        self.amp = amp
        self.phase = phase
        self.sample_rate = sample_rate
        self.wave_range = wave_range
        self.threshold = threshold
        self.samples = round(sample_rate * duration)

    def sq_osc(self):
        """ oscillation """
        phase = (self.phase / 360) * 2 * math.pi
        increment = (2 * math.pi * self.freq) / self.sample_rate
        return ((self.wave_range[0] if math.sin(phase + v) < self.threshold
                  else self.wave_range[1]) * self.amp 
                  for v in itertools.count(start=0, step=increment))

    def get_iterator(self, iterator):
        """ returns an iterator for the oscillation """
        return [next(iterator) for i in range(self.samples)]

    def get_wave(self):
        """ returns a square wave """
        osc = self.sq_osc()
        y = np.array(self.get_iterator(osc), dtype=np.float32)
        # ensuring the correct range for the amplitude
        audio = y * (2 ** 15 // 2) / np.max(np.abs(y))
        return audio.astype(np.int16)
