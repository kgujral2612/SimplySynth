from abc import ABC, abstractmethod


class WaveOscillator(ABC):

    @abstractmethod
    def get_wave(self, frequency, duration=1, phase=0, sample_rate=44100):
        pass