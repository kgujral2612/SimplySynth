
from mido import MidiFile, tick2second
from collections import defaultdict


class Midi_Helper:

    def midi_file_reader(self, path):
        midi_file = MidiFile(path, clip=True)
        return midi_file

    def ticks_to_ms(self, tempo, ticks, ticks_per_beat):
        tick_ms = (60000.0 / tempo) / ticks_per_beat
        return ticks * tick_ms

    def midi_file_interpreter(self, result):
        tempo = 500000
        current_notes = defaultdict(dict)
        current_pos = 0.0

        for i in range(len(result.tracks)):
            track = result.tracks[i]

            for event in track:
                current_pos += self.ticks_to_ms(event.time)
                if event.type == 'note_on':
                    current_notes[event.channel][event.note] = (current_pos, event)
                elif event.type == 'set_tempo':
                    tempo = event.tempo

