"""
This file handles user input
*****  Modes  *****
A) Notes + Tempo, B) Midi Path, C) Aleatoric
###########################################################################
***** Options *****
Wave Type:  Sine (1), Square (2), Sawtooth (3), 
            Triangle (4), Oboe (5), Flute(6), Bell (7), Violin (8)
Envelopes:  Trapezoidal (1), ADSR (2)
Effects:    White Noise (1), Environmental Noise (2), Time Stretch (3),
            Pitch Scaling (4), Inverse Polarity (5), Random Gain (6)
Filters:    Low-Pass (1)
###########################################################################
"""
import random
import numpy as np
import simpleaudio as sa
from scipy.io import wavfile
from helpers import midi_helper
from helpers.pitch_helper import get_freq_from_name, get_num_from_name, get_freq_from_num
from additive_synthesis import wave_table
from data_augmentation.filters import low_pass_filter
from data_augmentation.effects import white_noise, env_noise
from data_augmentation.effects import time_stretch, pitch_scaling, inverse_pol, random_gain


def create_synth_file_path(path, wave_type, envelope, effect, filter_type):
    """ a utility method to create a file path where the output is saved """
    synth_wave_path = "Files/wav files/" + \
        path[6: len(path)-4] + "-" + str(wave_type)
    synth_wave_path += ("-" + str(envelope)) if envelope is not None else ""
    synth_wave_path += ("-" + str(effect)) if effect is not None else ""
    synth_wave_path += ("-" + str(filter_type)
                        ) if filter_type is not None else ""
    synth_wave_path += "-synth.wav"
    return synth_wave_path


def apply_filter(audio, filter_type):
    """ applies filter to the given audio
        currently, there is only 1 filter, i.e low-pass
    """
    if filter_type == 1:  # low-pass
        return low_pass_filter(audio)
    return audio


def apply_effect(audio, effect_type):
    """ applies effects to the given audio
        white noise (1), environmental noise (2),
        time stretch (3), pitch scaling (4) ,
        inverse_pol (5), random gain (6)
    """
    if effect_type == 1:
        return white_noise(audio)
    if effect_type == 2:
        return env_noise(audio)
    if effect_type == 3:
        return time_stretch(audio)
    if effect_type == 4:
        return pitch_scaling(audio)
    if effect_type == 5:
        return inverse_pol(audio)
    if effect_type == 6:
        return random_gain(audio)


def play_notes(notes, beats=None, bpm=120, wave_type=1, 
               envelope=None, effect=None, filter_type=None):
    """ plays a given set of notes and beats (mode-a)"""
    if not notes or len(notes) == 0:
        return None
    if not wave_type:
        wave_type = 1

    # Step-1: Calculate frequencies from notes
    beat_duration = 60 / bpm
    if not beats:
        beats = np.ones(len(notes))
    beats = np.multiply(beats, beat_duration)

    curr = 0
    duration_freq_dict = {}

    for i, beat in enumerate(beats):
        val = [(get_freq_from_name(notes[i]), beat)]
        duration_freq_dict[curr] = val
        curr += beat

    duration = curr

    # Step-2: create the audio
    rate = 48000
    synth_wave_path = create_synth_file_path(
        "Files/play_notes.mid", wave_type, envelope, effect, filter_type)
    audio = wave_table.WaveTable(
        duration_freq_dict, duration, wave_type, envelope, rate).tabulate()
    if not wave_type:
        wave_type = 1

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


def play_midi(path=None, wave_type=1, envelope=None, effect=None, filter_type=None):
    """ reads and plays notes from a midi file """
    if path is None:
        return None
    if not wave_type:
        wave_type = 1

    # Step-1: read midi file
    result = midi_helper.Midi_Helper.input_midifile(path)
    if result.length > 0:
        midi_info_list = midi_helper.Midi_Helper.midi_info(result)
        rate = 48000  # default rate
        val = 0
        key = 0
        for m_key, m_val in midi_info_list.items():
            key = m_key
            val = m_val
        part_dur = val[-1]
        duration = key + part_dur[1]

        # Step-2: create the audio
        synth_wave_path = create_synth_file_path(
            path, wave_type, envelope, effect, filter_type)
        audio = wave_table.WaveTable(
            midi_info_list, duration, wave_type, envelope, rate).tabulate()

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


def play_aleatoric(root_note, bpm, beats,  wave_type=1, envelope=None):
    """ plays given notes in an aleatoric mode """
    duration = 60/bpm
    rate = 48000
    root = get_num_from_name(root_note)
    key_arr = [root+2, root+4, root+5, root+7, root+9, root+11, root+12]
    root_freq = get_freq_from_name(root_note)
    duration_freq_dict = {}
    duration_freq_dict[0] = [(root_freq, duration)]
    final = []
    while True:
        root_data = wave_table.WaveTable(
            duration_freq_dict, duration, wave_type, envelope, rate).tabulate()
        final = root_data
        for i in range(beats-1):
            note = random.choice(key_arr)
            note_freq = get_freq_from_num(note)
            duration_freq_dict[0] = [(note_freq, duration)]
            note_data = wave_table.WaveTable(
                duration_freq_dict, duration, wave_type, envelope, rate).tabulate()
            final = np.concatenate((final, note_data), axis=None)
        play_obj = sa.play_buffer(final, 1, 2, 48000)
        play_obj.wait_done()
    return None
