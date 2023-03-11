""" This module provides the functionality to 
    add envelopes on a given audio"""

import numpy as np
from oscillators import sine


def adsr(samples, attack=0.2, decay=0.1, sustain=0.8, release=0.2):
    """ applies adsr envelope to samples """
    ramp_data = adsr_ramp_calc(
        len(samples), attack=attack, decay=decay, sustain=sustain, release=release)
    final_data = (np.multiply(samples, ramp_data)).astype(np.int16)
    return final_data


def lfo_amp(samples, freq=4):
    """ applies LFO envelope to samples """
    duration = len(samples)/48000
    lfo_wave = sine.SineOscillator(
        freq=freq, duration=duration).get_lfo_wave()
    final_data = (np.multiply(samples, lfo_wave)).astype(np.int16)
    return final_data


def trap_ar(samples, ramp=0.5):
    """ applies trapezoidal envelope to samples """
    ramp_data = trap_ar_ramp_calc(len(samples), ramp)
    final_data = (np.multiply(samples, ramp_data)).astype(np.int16)
    return final_data


def noise_ar(samples, ramp=0.25):
    """ applies noise ar envelope to samples """
    ramp_data = noise_ar_ramp_calc(len(samples), ramp)
    final_data = (np.multiply(samples, ramp_data)).astype(np.int16)
    return final_data


def adsr_ramp_calc(data_len, attack, decay, sustain, release):
    """ utility method for adsr envelope ramp calculation """
    ramp_data = np.ones(data_len)
    attack_step = 1 / (data_len * attack)
    decay_step = (1 - sustain) / (data_len * decay)
    release_step = sustain / (data_len * release)
    decay_count = decay * data_len
    release_count = release * data_len
    for i in range(data_len):
        if i <= attack * data_len:
            ramp_data[i] = i * attack_step
        elif i <= (decay * data_len):
            ramp_data[i] = decay_count * decay_step
            decay_count -= 1
        elif i <= (data_len - (release * data_len)):
            ramp_data[i] = sustain
        else:
            ramp_data[i] = release_count * release_step
    return ramp_data


def trap_ar_ramp_calc(data_len, ramp):
    """ utility method for trapezoidal envelope ramp calculation """
    ramp_data = np.ones(data_len)
    step = 1 / (data_len * ramp)
    for i in range(data_len):
        if i <= ramp * data_len:
            ramp_data[i] = i * step
        elif i >= (data_len - (ramp * data_len)):
            ramp_data[i] = (data_len - i - 1) * step
    return ramp_data


def noise_ar_ramp_calc(data_len, ramp):
    """ utility method for noise ar envelope ramp calculation """
    ramp_data = np.ones(data_len)
    step1 = 1 / (data_len * ramp)
    for i in range(data_len):
        if i <= ramp * data_len:
            ramp_data[i] = i * step1
        elif i <= 2*ramp * data_len:
            ramp_data[i] = (data_len - i - 1) * step1
        else:
            ramp_data[i] = 0
    return ramp_data
