from mido import MidiFile
from collections import defaultdict
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


def input_midifile(path):
    midi_file = MidiFile(path, clip=True)
    return midi_file


result = input_midifile(wave_path)
tempo = 100

'''
  from wikipedia: http://en.wikipedia.org/wiki/MIDI_Tuning_Standard#Frequency_values
'''
def note_to_freq(note, concert_A=440.0):
    return (2.0 ** ((note - 69) / 12.0)) * concert_A


def ticks_to_ms(ticks):
    tick_ms = (60000.0 / tempo) / result.ticks_per_beat
    return ticks * tick_ms


for track in result.tracks:
    # position of rendering in ms
    current_pos = 0.0

    current_notes = defaultdict(dict)

    for msg in track:
        current_pos += ticks_to_ms(msg.time)

        if msg.type == 'note_on':
            current_notes[msg.channel][msg.note] = (current_pos, msg)

        if msg.type == 'note_off':
            start_pos, start_msg = current_notes[msg.channel].pop(msg.note)

            duration = current_pos - start_pos
            print(note_to_freq(msg.note))
            # signal_generator = Sine(note_to_freq(msg.note))
            # rendered = signal_generator.to_audio_segment(duration=duration-50, volume=-20).fade_out(100).fade_in(30)

            # output = output.overlay(rendered, start_pos)

# output.export("animal.wav", format="wav")


'''class WaveOscillatorMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """
    def __instancecheck__(class_name, instance):
        return class_name.__subclasscheck__(type(instance))

    def __subclasscheck__(class_name, subclass_name):
        return (hasattr(subclass_name, 'updated_freq_setter') and 
                callable(subclass_name.updated_freq_setter) and 
                hasattr(subclass_name, 'updated_phase_setter') and 
                callable(subclass_name.updated_phase_setter) and
                hasattr(subclass_name, 'updated_period_setter') and 
                callable(subclass_name.updated_period_setter) and
                hasattr(subclass_name, 'osc_initialization') and 
                callable(subclass_name.osc_initialization) and
                hasattr(subclass_name, 'next') and 
                callable(subclass_name.next)) 

class WaveOscillatorInterface(metaclass=WaveOscillatorMeta):
    pass

class WaveOscillator():
    def __init__(self, frequency, phase, amp, sampling_rate, wave_range):
        self._freq = frequency
        self._amp = amp
        self._phase = phase
        self._sampling_rate = sampling_rate
        self._wave_range = wave_range
        
    def updated_freq_setter(self):
        pass
    def updated_phase_setter(self):
        pass
    def updated_period(self):
        pass
    def osc_initialization(self):
        pass
    def next(self):
        pass
    def squish_val(val, min_val=0, max_val=1):
        return (((val + 1) / 2 ) * (max_val - min_val)) + min_val'''
