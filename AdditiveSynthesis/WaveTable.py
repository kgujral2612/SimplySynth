import numpy as np
from Oscillators import Sine


class WaveTable:

    def __init__(self, midi_dict, midi_length, t_count, sample_rate=48000):
        self.midi_dict = midi_dict
        self.rate = sample_rate
        self.l = round(midi_length * sample_rate)
        self.song = np.zeros(self.l)
        self.t_count = t_count


    def tabulate(self):
        for start_time, notes in self.midi_dict.items():
            for note in notes:
                self.overlay(Sine.Sine_Oscillator(freq=note[0], duration=note[1]).get_wave(), start_time)
        self.song = self.song * (2 ** 15 // 2) / np.max(np.abs(self.song))
        return self.song.astype(np.int16)

    def overlay(self, snippet, start_time):
        i = round(start_time * self.rate)
        c = self.song[i:i + len(snippet)]
        d = self.song[i + len(snippet) + 1:]
        e = self.song[:i]
        if len(c)<len(snippet):
            c= np.add(c,snippet[0:len(c)])
        else:
            c = np.add(c, snippet)
        self.song = np.concatenate((e,c,d),axis=None)








