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
from WaveAdders import WaveAdder

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
# create a note
n = PitchHelper.Note("C#", 4)
nf = PitchHelper.PitchToFreq()
freq = nf.get_freq(n)
print(freq)


# create a sine wave at that note
so = Sine.Sine_Oscillator(freq=freq, duration=1.5)
rate = 44100
audio = so.get_wave()
wavfile.write('sine.wav', rate, audio)  # writing on to the wav file
# play the wave
play_obj = sa.play_buffer(audio, 1, 2, rate)
play_obj.wait_done()


so = Sine.Sine_Oscillator(freq=440)
so2 = Sine.Sine_Oscillator(freq=440)
sq = Square.Square_Oscillator(freq=440)
st = SawTooth.SawTooth_Oscillator(freq=440)
t = Triangle.Triangle_Oscillator(freq=440)
osc = [so, so2, sq, st, t]
wv = WaveAdder.Wave_Adder(osc)
final = wv.mixer()
wavfile.write('added.wav', rate, final)
play_obj = sa.play_buffer(final, 1, 2, rate)
play_obj.wait_done()

'''

