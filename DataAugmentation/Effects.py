#
# reference: https://www.youtube.com/watch?v=umAXGVzVvwQ
#
import random
from scipy.io import wavfile
import numpy as np
import librosa


# white noise
def white_noise(signal, noise_factor=0.1):
    noise = np.multiply(np.random.normal(0, signal.std(), signal.size), noise_factor)
    augmented_signal = np.add(signal, noise)
    augmented_signal = augmented_signal * (2 ** 15 // 2) / np.max(np.abs(augmented_signal))
    return augmented_signal.astype(np.int16)


# add environmental noise
def env_noise(signal, noise_factor=0.1):
    sampling_rate, env_signal = wavfile.read("Files/env_noise/forest-night.wav")
    env_noise = np.multiply(env_signal, noise_factor)
    diff = len(signal) - len(env_noise)
    if diff == 0:
        augmented_signal = np.add(env_noise, signal)
    elif diff < 0:
        augmented_signal = np.add(env_noise[: len(signal)], signal)
    else:
        patch = np.zeros(diff)
        temp = np.concatenate(env_noise, patch, axis=0)
        augmented_signal = np.add(signal, temp)
    augmented_signal = augmented_signal * (2 ** 15 // 2) / np.max(np.abs(augmented_signal))
    return augmented_signal.astype(np.int16)


# time stretch
def time_stretch(signal, stretch_rate=0.1):
    return librosa.effects.time_stretch(signal, stretch_rate)


# pitch scaling
def pitch_scaling(signal, sample_rate=48000, num_semitones=1):
    return librosa.effects.pitch_shift(signal, sample_rate, num_semitones)


# inverse polarity
def inverse_pol(signal):
    return np.multiply(signal, -1)


# random gain
def random_gain(signal, min_gain_factor=0, max_gain_factor=1):
    gain_factor = random.uniform(min_gain_factor, max_gain_factor)
    return np.multiply(signal, gain_factor)
