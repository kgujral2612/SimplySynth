# Synthesizer
#
# Everything below is for the synth interface
# and has no relation to any of the core functionality
#
#

import simpleaudio as sa
from Helpers import MidiHelper, PitchHelper
from Oscillators import Sine, Square, SawTooth

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
amplitude, rate = so.get_wave(freq)
play_obj = sa.play_buffer(amplitude, 1, 2, rate)
play_obj.wait_done()


sqo = Square.Square_Oscillator()
amplitude, rate = sqo.get_wave(freq)
play_obj = sa.play_buffer(amplitude, 1, 2, rate)
play_obj.wait_done()


sqo = SawTooth.SawTooth_Oscillator()
amplitude, rate = sqo.get_wave(freq)
play_obj = sa.play_buffer(amplitude, 1, 2, rate)
play_obj.wait_done()
