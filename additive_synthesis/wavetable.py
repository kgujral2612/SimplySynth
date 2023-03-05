from oscillators import sawtooth, square
from instruments.sounds import *
from envelopes.envelope import *


class WaveTable:

    def __init__(self, midi_dict, midi_length, wave_type=1, envelope=None, sample_rate=48000):
        self.midi_dict = midi_dict
        self.rate = sample_rate
        self.l = round(midi_length * sample_rate)
        self.song = np.zeros(self.l)
        self.wave_type = wave_type
        self.envelope = envelope

    # Wave Type: Sine (1), Square (2), Sawtooth (3), Triangle (4), Oboe (5)
    def get_type_wave(self, f, d):
        if self.wave_type == 1:
            return sine.Sine_Oscillator(freq=f, duration=d).get_wave()
        elif self.wave_type == 2:
            return square.Square_Oscillator(freq=f, duration=d).get_wave()
        elif self.wave_type == 3:
            return sawtooth.SawTooth_Oscillator(freq=f, duration=d).get_wave()
        elif self.wave_type == 4:
            return triangle.Triangle_Oscillator(freq=f, duration=d).get_wave()
        elif self.wave_type == 5:
            self.envelope = 2
            return oboe(frequency=f, duration=d)
        elif self.wave_type == 6:
            self.envelope = 1
            return flute(frequency=f, duration=d)
        elif self.wave_type == 7:
            return bell(frequency=f, duration=d)
        elif self.wave_type == 8:
            self.envelope = 2
            return violin(frequency=f,duration=d)

    def get_envelope(self, audio):
        if self.envelope is None:
            return audio
        if self.envelope == 1:
            return trap_ar(audio)
        if self.envelope == 3:
            return lfo_amp(audio, freq=5)
        return adsr(audio)

    def tabulate(self):
        for start_time, notes in self.midi_dict.items():

            for note in notes:
                
                if self.wave_type==6:
                    wave = self.get_type_wave(f=note[0], d=note[1])                   
                    wave = lfo_amp(wave, freq=4)
                    wave = self.get_envelope(wave)
                    wave = flute_noise(wave)
                elif self.wave_type==8:
                    wave = self.get_type_wave(f=note[0], d=note[1]) 
                    wave = lfo_amp(wave, freq=4)                 
                    wave = self.get_envelope(wave)
                else:
                    wave = self.get_envelope(self.get_type_wave(f=note[0], d=note[1]))
                
                self.overlay(wave, start_time)
        self.song = self.song * (2 ** 15 // 2) / np.max(np.abs(self.song))
        return self.song.astype(np.int16)

    def overlay(self, snippet, start_time):
        i = round(start_time * self.rate)
        pre = self.song[:i]
        post = self.song[i + len(snippet) + 1:]
        overlay_snip = self.song[i:i + len(snippet)]

        if len(overlay_snip) < len(snippet):
            overlay_snip = np.add(overlay_snip, snippet[0:len(overlay_snip)])
        else:
            overlay_snip = np.add(overlay_snip, snippet)
        self.song = np.concatenate((pre, overlay_snip, post), axis=None)








