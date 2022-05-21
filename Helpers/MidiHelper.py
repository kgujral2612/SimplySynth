import time
import numpy as np
from mido import MidiFile, tick2second
from collections import defaultdict


class Midi_Helper:

    def input_midifile(wave_path):
        midi_file = MidiFile(wave_path)
        return midi_file

    def note_to_freq(note, concert_A=440.0):
        return (2.0 ** ((note - 69) / 12.0)) * concert_A
    
    def tempo_calc(time, tempo_info):
        for i in range(len(tempo_info)):
            if time<=tempo_info[0][1]:
                return tempo_info[0][0]
            elif time>tempo_info[i][1]:
                if i==0:
                    return tempo_info[i][0]
                else:
                    return tempo_info[i-1][0]
            
    def midi_info(midifile):
        count=0

        for tracks in midifile.tracks:
            count+=1

        track_info=np.empty((count,0)).tolist()
        count=0
        tempo=500000
        tempo_info=[]
        time_tempo=0.0

        for track in midifile.tracks:
            time_elapsed = 0.0
            notes_dict = defaultdict(dict)

            for msg in track:                
                time_elapsed += tick2second(msg.time, midifile.ticks_per_beat, tempo) 

                if msg.type == 'note_on': 
                    tempo=Midi_Helper.tempo_calc(time_elapsed, tempo_info)                  
                    notes_dict[msg.channel][msg.note] = (time_elapsed) 

                if msg.type == 'note_off': 
                    tempo=Midi_Helper.tempo_calc(time_elapsed, tempo_info)                  
                    start_pos = notes_dict[msg.channel].pop(msg.note)            
                    duration = (time_elapsed - start_pos)
                    track_info[count].append((Midi_Helper.note_to_freq(msg.note),duration, start_pos))

                if msg.type == 'set_tempo':
                    time_tempo+=msg.time
                    tempo_info.append((msg.tempo,time_tempo))
        
            count+=1
        return track_info

