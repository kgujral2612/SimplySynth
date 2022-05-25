#
# reference: https://en.wikipedia.org/wiki/Additive_synthesis
#

import numpy as np


#
# Adds 2 waves of equal sample rate and duration
#
class Wave_Adder:

    def __init__(self, oscillators, duration=1, sample_rate=48000):
        self.oscillators = oscillators
        self.samples = round(duration * sample_rate)

    def mixer(self):
        audio = np.zeros(self.samples)
        for osc in self.oscillators:
            audio = np.add(audio, osc.get_wave())
        audio = audio // len(self.oscillators)
        res = audio * (2 ** 15 // 2) / max(0.001, np.max(np.abs(audio)))  # ensuring the correct range for the amplitude
        return res.astype(np.int16)
