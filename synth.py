# Synthesizer
#
# Everything below is for the synth interface
# and has no relation to any of the core functionality
#
#

import simpleaudio as sa
from scipy.io import wavfile
from Helpers import MidiHelper, PitchHelper
from Oscillators import Sine, Square, SawTooth, Triangle

#path = "Files/mario.mid"
#helper = MidiHelper.Midi_Helper()
#midi_obj = helper.midi_file_reader(path)

# create a note
n = PitchHelper.Note("C#", 4)
nf = PitchHelper.PitchToFreq()
freq = nf.get_freq(n)
print(freq)

# create a sine wave at that note
so = Sine.Sine_Oscillator()
rate = 44100
audio = so.get_wave(freq=freq, sample_rate=rate)
wavfile.write('sine.wav', rate, audio)  # writing on to the wav file
# play the wave
play_obj = sa.play_buffer(audio, 1, 2, rate)
play_obj.wait_done()

# create a square wave at that note
sq = Square.Square_Oscillator()
rate = 44100
audio = sq.get_wave(freq=freq, sample_rate=rate)
wavfile.write('square.wav', rate, audio)  # writing on to the wav file
# play the wave
play_obj = sa.play_buffer(audio, 1, 2, rate)
play_obj.wait_done()

# create a sawtooth wave at that note
sw = SawTooth.SawTooth_Oscillator()
rate = 44100
audio = sw.get_wave(freq=freq, sample_rate=rate)
wavfile.write('sawtooth.wav', rate, audio)  # writing on to the wav file
# play the wave
play_obj = sa.play_buffer(audio, 1, 2, rate)
play_obj.wait_done()


# create a triangle wave at that note
t = Triangle.Triangle_Oscillator()
rate = 44100
audio = t.get_wave(freq=freq, sample_rate=rate)
wavfile.write('triangle.wav', rate, audio)  # writing on to the wav file
# play the wave
play_obj = sa.play_buffer(audio, 1, 2, rate)
play_obj.wait_done()



