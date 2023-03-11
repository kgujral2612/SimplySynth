"""This module provides a class and functions to create a wave table"""
import numpy as np
from oscillators import sine, sawtooth, square, triangle
from instruments.sounds import oboe, bell, flute, violin
from envelopes.envelope import lfo_amp, trap_ar, adsr
from data_augmentation.effects import flute_noise


class WaveTable:
    """Another comment """

    def __init__(self, midi_dict, midi_length, wave_type=1, envelope=None, sample_rate=48000):
        self.midi_dict = midi_dict
        self.rate = sample_rate
        length = round(midi_length * sample_rate)
        self.song = np.zeros(length)
        self.wave_type = wave_type
        self.envelope = envelope

    def get_type_wave(self, freq, duration):
        """ Returns the wave of a certain type.
            Wave Type: Sine (1), Square (2), Sawtooth (3), Triangle (4), Oboe (5)"""
        if self.wave_type == 1:
            return sine.SineOscillator(freq=freq, duration=duration).get_wave()
        if self.wave_type == 2:
            return square.SquareOscillator(freq=freq, duration=duration).get_wave()
        if self.wave_type == 3:
            return sawtooth.SawToothOscillator(freq=freq, duration=duration).get_wave()
        if self.wave_type == 4:
            return triangle.TriangleOscillator(freq=freq, duration=duration).get_wave()
        if self.wave_type == 5:
            self.envelope = 2
            return oboe(frequency=freq, duration=duration)
        if self.wave_type == 6:
            self.envelope = 1
            return flute(frequency=freq, duration=duration)
        if self.wave_type == 7:
            return bell(frequency=freq, duration=duration)
        if self.wave_type == 8:
            self.envelope = 2
            return violin(frequency=freq, duration=duration)

    def get_envelope(self, audio):
        """Returns the type of envelope.
            Envelope Types: Trapezoidal (1), ADSR (2), LFO (3)"""
        if self.envelope is None:
            return audio
        if self.envelope == 1:
            return trap_ar(audio)
        if self.envelope == 3:
            return lfo_amp(audio, freq=5)
        return adsr(audio)

    def tabulate(self):
        """Creates a table and returns it"""
        for start_time, notes in self.midi_dict.items():
            for note in notes:
                if self.wave_type == 6:
                    wave = self.get_type_wave(freq=note[0], duration=note[1])
                    wave = lfo_amp(wave, freq=4)
                    wave = self.get_envelope(wave)
                    wave = flute_noise(wave)
                elif self.wave_type == 8:
                    wave = self.get_type_wave(freq=note[0], duration=note[1])
                    wave = lfo_amp(wave, freq=4)
                    wave = self.get_envelope(wave)
                else:
                    wave = self.get_envelope(
                        self.get_type_wave(freq=note[0], duration=note[1]))
                self.overlay(wave, start_time)
        self.song = self.song * (2 ** 15 // 2) / np.max(np.abs(self.song))
        return self.song.astype(np.int16)

    def overlay(self, snippet, start_time):
        """OVerlay the waves with the envelopes"""
        i = round(start_time * self.rate)
        pre = self.song[:i]
        post = self.song[i + len(snippet) + 1:]
        overlay_snip = self.song[i:i + len(snippet)]

        if len(overlay_snip) < len(snippet):
            overlay_snip = np.add(overlay_snip, snippet[0:len(overlay_snip)])
        else:
            overlay_snip = np.add(overlay_snip, snippet)
        self.song = np.concatenate((pre, overlay_snip, post), axis=None)
