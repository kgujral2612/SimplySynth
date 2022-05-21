import numpy as np
from Oscillators import Sine


class WaveTable:

    def __init__(self, midi_dict, midi_length, t_count, sample_rate=44100):
        self.midi_dict = midi_dict
        self.rate = sample_rate
        self.l = round(midi_length * sample_rate)
        self.song = np.zeros(self.l)
        self.t_count = t_count

    def tabulate(self):
        overlay_list = []
        for start_time, notes in self.midi_dict.items():
            for note in notes:
                overlay_list.append(self.process(Sine.Sine_Oscillator(freq=note[0], duration=note[1]).get_wave(), start_time))
            self.overlay(overlay_list)
        return self.song.astype(np.int16)

    def overlay(self, wave_list):
        self.song = np.sum(wave_list, axis=0) // (2 * self.t_count)

    def process(self, snippet, start_pos):
        i = round(start_pos * self.rate)
        a = np.zeros(self.l)
        for s in snippet:
            if i >= self.l:
                return a
            a[i] += s
            i += 1
        return a

    def tabulatefunc(self):
        for start_time, notes in self.midi_dict.items():
            for note in notes:
                self.overlayfunc(Sine.Sine_Oscillator(freq=note[0], duration=note[1]).get_wave(), start_time)
        self.song = self.song // (2 * self.t_count)
        return self.song.astype(np.int16)

    def overlayfunc(self, snippet, start_time):
        i = round(start_time * self.rate)
        c = self.song[i:i + len(snippet)]
        d = self.song[i + len(snippet) + 1:]
        e = self.song[:i]
        c = np.add(c, snippet)

        if len(e) == 0:
            if len(d) == 0:
                self.song = c
            else:
                self.song = c+d
        elif len(d) == 0:
            self.song = e + c
        else:
            self.song = e+c+d








