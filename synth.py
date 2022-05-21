# Synthesizer
#
# Everything below is for the synth interface
# and has no relation to any of the core functionality
#
#

import simpleaudio as sa
from scipy.io import wavfile
from Helpers import MidiHelper
from Oscillators import Sine
from AdditiveSynthesis import WaveAdder, WaveTable
from mido import tick2second
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
t_count = len(result.tracks) - 1
if t_count==0:
    t_count=1
if result.length > 0:
    midi_info_list = MidiHelper.Midi_Helper.midi_info(result)
    val = 0
    key = 0
    for k, v in midi_info_list.items():
        key = k
        val = v

    rate = 48000
    x = key
    y = val[-1]
    duration = x + y[1]

    audio = WaveTable.WaveTable(midi_info_list, duration, t_count, rate).tabulate()
    wavfile.write('Files/wav files/twinkle_triangle.wav', rate, audio)  # writing on to the wav file
    #play_obj = sa.play_buffer(audio, 1, 2, rate)
    #play_obj.wait_done()



