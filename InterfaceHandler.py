#
# This file handles user input
# *****  Modes  *****
# A) Notes + Tempo, B) Midi Path, C) Aleatoric
###########################################################################
# ***** Options *****
# Wave Type: Sine (1), Square (2), Sawtooth (3), Triangle (4), Oboe (5)

# Envelopes: Trapezoidal (1), ADSR (2)

# Effects: White Noise (1), Environmental Noise (2), Time Stretch (3),
# Pitch Scaling (4), Inverse Polarity (5), Random Gain (6)

# Filters: Low-Pass (1)
###########################################################################
import numpy as np

from Helpers import MidiHelper
from Helpers.PitchHelper import *
from AdditiveSynthesis import WaveTable
from DataAugmentation.Filters import *
from DataAugmentation.Effects import *
import simpleaudio as sa
from scipy.io import wavfile


def create_synth_file_path(path, wave_type, envelope, effect, filter_type):
    synth_wave_path = "Files/wav files/" + path[6: len(path)-4] + "-" + str(wave_type)
    synth_wave_path += ("-" + str(envelope)) if envelope is not None else ""
    synth_wave_path += ("-" + str(effect)) if effect is not None else ""
    synth_wave_path += ("-" + str(filter_type)) if filter_type is not None else ""
    synth_wave_path += "-synth.wav"
    return synth_wave_path


def apply_filter(audio, filter_type):
    if filter_type == 1:  # low-pass
        return low_pass_filter(audio)
    return audio


def apply_effect(audio, effect_type):
    if effect_type == 1:
        return white_noise(audio)
    elif effect_type == 2:
        return env_noise(audio)
    elif effect_type == 3:
        return pitch_scaling(audio)
    elif effect_type == 4:
        return inverse_pol(audio)
    else:
        return random_gain(audio)


# Mode-A: Notes
def play_notes(notes, beats=None, bpm=120, wave_type=1, envelope=None, effect=None, filter_type=None):
    if not notes or len(notes) == 0:
        return None

    # Step-1: Calculate frequencies from notes
    beat_duration = 60 / bpm
    if not beats:
        beats = np.ones(len(notes))
    beats = np.multiply(beats, beat_duration)

    curr = 0
    duration_freq_dict = {}
    for i in range(len(beats)):
        val = [(get_freq_from_name(notes[i]), beats[i])]
        duration_freq_dict[curr] = val
        curr += beats[i]

    duration = curr

    # Step-2: create the audio
    rate = 48000
    synth_wave_path = create_synth_file_path("Files/play_notes.mid", wave_type, envelope, effect, filter_type)
    audio = WaveTable.WaveTable(duration_freq_dict, duration, wave_type, envelope, rate).tabulate()

    # Step-3: apply filters
    if filter_type:
        audio = apply_filter(audio, filter_type)

    # Step-4: apply effects
    if effect:
        audio = apply_effect(audio, effect)

    # Step-5: play the audio
    play_obj = sa.play_buffer(audio, 1, 2, rate)
    play_obj.wait_done()

    # Step-6: saving generated audio as a wav file
    wavfile.write(synth_wave_path, rate, audio)


# Mode-B: Midi File
def play_midi(path=None, wave_type=1, envelope=None, effect=None, filter_type=None):
    if path is None:
        return None

    # Step-1: read midi file
    result = MidiHelper.Midi_Helper.input_midifile(path)
    if result.length > 0:
        midi_info_list = MidiHelper.Midi_Helper.midi_info(result)
        rate = 48000  # default rate
        val = 0
        key = 0
        for k, v in midi_info_list.items():
            key = k
            val = v
        x = key
        y = val[-1]
        duration = x + y[1]

        # Step-2: create the audio
        synth_wave_path = create_synth_file_path(path, wave_type, envelope, effect, filter_type)
        audio = WaveTable.WaveTable(midi_info_list, duration, wave_type, envelope, rate).tabulate()

        # Step-3: apply filters
        if filter_type:
            audio = apply_filter(audio, filter_type)

        # Step-4: apply effects
        if effect:
            audio = apply_effect(audio, effect)

        # Step-5: play the audio
        play_obj = sa.play_buffer(audio, 1, 2, rate)
        play_obj.wait_done()

        # Step-6: saving generated audio as a wav file
        wavfile.write(synth_wave_path, rate, audio)


# Mode-C: Aleatoric
def play_aleatoric(root_note, bpm, beats,  wave_type=1, envelope=None, effect=None, filter_type=None):
    return None












