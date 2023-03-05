#
# reference: https://en.wikipedia.org/wiki/Additive_synthesis
#

import numpy as np


#
# Adds 2 waves of equal sample rate and duration
#
class wave_adder:

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

    def instr_mixer(self):
        audio = np.zeros(self.samples)
        for osc in self.oscillators:
            new_audio = osc.get_instr_wave()
            if len(new_audio) == len(audio)+1:
                new_audio = new_audio[0:len(new_audio)-1]
            audio = np.add(audio, new_audio)
        audio = audio // len(self.oscillators)
        return audio.astype(np.int16)
