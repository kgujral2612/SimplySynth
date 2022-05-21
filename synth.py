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
from AdditiveSynthesis import WaveAdder
from AdditiveSynthesis.Instruments import Flute, Oboe, Piano

import argparse

'''cmd = argparse.ArgumentParser(prog='Tuner',
                              usage='%(prog)s [options] path',
                              description='Displaying the frequency of either a live microphone or a given wavefile.')
cmd.add_argument('wav_path',
                 metavar='Input WAV file',
                 nargs='?',
                 default='',
                 type=str,
                 help='Enter the path of the WAV file that needs to be tuned.')
args = cmd.parse_args()
wave_path = args.wav_path


result = MidiHelper.Midi_Helper.input_midifile(wave_path)
midi_info_list = MidiHelper.Midi_Helper.midi_info(result)
for tracks in midi_info_list:
    for info in tracks:
        print(info)

'''
# create a note
n = PitchHelper.Note("A", 4)
nf = PitchHelper.PitchToFreq()
freq = nf.get_freq(n)


freq_a2 = nf.get_freq(PitchHelper.Note("A", 2))
freq_e5 = nf.get_freq(PitchHelper.Note("E", 5))

'''
osc = WaveAdder.Wave_Adder([
    Square.Square_Oscillator(27.5, amp=0.1),
    Triangle.Triangle_Oscillator(55, amp=0.5),
    Sine.Sine_Oscillator(110),
    Square.Square_Oscillator(220, amp=0.1),
    Sine.Sine_Oscillator(440,amp=0.3),
    Triangle.Triangle_Oscillator(880,amp=0.05)]
)'''

osc = WaveAdder.Wave_Adder([
    Sine.Sine_Oscillator(freq_a2),
    Sine.Sine_Oscillator(freq_a2+3),
    Triangle.Triangle_Oscillator(freq, amp=0.6),
    Triangle.Triangle_Oscillator(freq_e5, amp=0.8)]
)

final = osc.mixer()
rate = 44100
wavfile.write('added.wav', rate, final)
play_obj = sa.play_buffer(final, 1, 2, rate)
play_obj.wait_done()

