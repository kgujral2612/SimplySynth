# Synthesizer
#
# Everything below is for the synth interface
# and has no relation to any of the core functionality
#
#

import simpleaudio as sa
from scipy.io import wavfile
from Oscillators import Sine, Square, SawTooth, Triangle
from mido import MidiFile
from collections import defaultdict
from Helpers import MidiHelper
import argparse

cmd = argparse.ArgumentParser(prog='Tuner',
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
# create a sine wave at that note
so = Sine.Sine_Oscillator()
rate = 44100
audio = so.get_wave(freq=freq, sample_rate=rate)
wavfile.write('sine2.wav', rate, audio)  # writing on to the wav file
# play the wave
play_obj = sa.play_buffer(audio, 1, 2, rate)
play_obj.wait_done()

'''