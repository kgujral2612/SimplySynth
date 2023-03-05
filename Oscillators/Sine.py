""" An oscillator that produces sine waves
    reference: https://python.plainenglish.io/making-a-synth-with-python-oscillators-2cb8e68e9c3b
"""

import math
import itertools
import numpy as np


class SineOscillator:
    """ Class to produce a sine wave """

    def __init__(self, freq, amp=1, phase=0, sample_rate=48000, duration=1):
        self.freq = freq
        self.amp = amp
        self.phase = phase
        self.sample_rate = sample_rate
        self.duration = duration
        self.samples = round(sample_rate * duration)

    def sin_osc(self):
        """ oscillation """
        increment = (2 * math.pi * self.freq) / self.sample_rate
        return (math.sin(v) * self.amp for v in itertools.count(start=0, step=increment))

    def sin_lfo_osc(self):
        """ oscillation for sine lfo wave"""
        self.phase = (self.phase / 360) * 2 * math.pi
        increment = (2 * math.pi * self.freq) / self.sample_rate
        return (math.sin(0.45+self.phase)*self.amp if math.sin(self.phase + v) < 0.45
                else math.sin(0.55+self.phase)*self.amp if math.sin(self.phase + v) > 0.55
                else math.sin(self.phase + v) * self.amp
                for v in itertools.count(start=0, step=increment))

    def get_iterator(self, iterator):
        """ returns an iterator for the oscillation """
        return [next(iterator) for i in range(self.samples)]

    def get_wave(self):
        """ returns a sine wave """
        osc = self.sin_osc()
        y = np.array(self.get_iterator(osc), dtype=np.float32)
        # ensuring the correct range for the amplitude
        audio = y * (2 ** 15 // 2) / max(0.001, np.max(np.abs(y)))
        return audio.astype(np.int16)

    def get_lfo_wave(self):
        """ returns sine wave for lfo"""
        osc = self.sin_lfo_osc()
        y = np.array(self.get_iterator(osc), dtype=np.float32)
        return y

    def get_instr_wave(self):
        """ returns instr wave """
        return np.sin(np.arange(0, self.duration, 1 / 48000) * self.freq * 2 * np.pi)*self.amp
