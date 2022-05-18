import numpy as np
from mido import MidiFile, tick2second
from collections import defaultdict


class Midi_Helper:

    def input_midifile(wave_path):
        midi_file = MidiFile(wave_path)
        return midi_file

    def note_to_freq(note, concert_A=440.0):
        return (2.0 ** ((note - 69) / 12.0)) * concert_A

    def ticks_to_s(ticks,tick_per_beat):
        #tempo is 100
        tick_ms = (60000.0 / 100) / tick_per_beat
        return (ticks * tick_ms)/1000

    def midi_info(midifile):
        count=0
        for tracks in midifile.tracks:
            count+=1
        track_info=np.empty((count,0)).tolist()
        count=0
        for track in midifile.tracks:
            duration=0
            for msg in track:
                if msg.type == 'note_off':
                    duration=Midi_Helper.ticks_to_s(msg.time-duration, midifile.ticks_per_beat)
                    frequency = Midi_Helper.note_to_freq(msg.note)           
                    track_info[count].append((frequency,duration))
                if msg.type == 'note_on':
                    duration=msg.time
            count+=1
        
        return track_info