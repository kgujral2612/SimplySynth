from Oscillators import Sine
from AdditiveSynthesis import WaveAdder


class Flute:
    def __init__(self, freq):
        self.freq = freq
        self.coeff = 1
        self.n = 10
        self.amp = 1.0

    def play(self):
        sine_list = []
        for i in range(self.n):
            sine_list.append(Sine.Sine_Oscillator(freq=self.freq * self.coeff, amp=self.amp))
            self.coeff += 1
            self.amp /= 2.0
        return WaveAdder.Wave_Adder(sine_list).mixer()

