from Oscillators import Sine
from AdditiveSynthesis import WaveAdder


class Oboe:
    def __init__(self, freq):
        self.freq = freq
        self.coeffs = [1.0, 0.9, 2.1, 0.2, 0.22, 0.25, 0.55, 0.3, 0.25, 0, 0.01, 0.001, 0, 0, 0, 0, 0, 0, 0, 0]
        self.increment = 1
        self.n = 20

    def play(self):
        sine_list = []
        for i in range(self.n):
            if self.coeffs[i] == 0:
                continue
            sine_list.append(Sine.Sine_Oscillator(freq=self.freq * self.increment, amp=self.coeffs[i]))
            self.increment += 1
        return WaveAdder.Wave_Adder(sine_list).mixer()
