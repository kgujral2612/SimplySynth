#
# reference: https://www.youtube.com/watch?v=umAXGVzVvwQ
#
import random
from scipy.io import wavfile
import numpy as np
import librosa
from envelopes import envelope
from oscillators import sine

def flute_noise(signal, noise_factor=0.0014):
    noise = np.multiply(np.random.normal(0, signal.std(), signal.size), noise_factor)
    noise = envelope.noise_ar(noise)
    augmented_signal = np.add(signal, noise)
    return augmented_signal.astype(np.int16)

# white noise
def white_noise(signal, noise_factor=0.05):
    noise = np.multiply(np.random.normal(0, signal.std(), signal.size), noise_factor)
    augmented_signal = np.add(signal, noise)
    augmented_signal = augmented_signal * (2 ** 15 // 2) / np.max(np.abs(augmented_signal))
    return augmented_signal.astype(np.int16)


# add environmental noise
def env_noise(signal, noise_factor=0.025):
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
def time_stretch(signal, stretch_rate=0.8):
    signal = signal.astype(np.float32)
    augmented_signal = librosa.effects.time_stretch(signal, rate=stretch_rate)
    augmented_signal = augmented_signal * (2 ** 15 // 2) / np.max(np.abs(augmented_signal))
    return augmented_signal.astype(np.int16)


# pitch scaling
def pitch_scaling(signal, sample_rate=48000, num_semitones=1):
    signal = signal.astype(np.float32)
    augmented_signal = librosa.effects.pitch_shift(signal, sr=sample_rate, n_steps=num_semitones)
    augmented_signal = augmented_signal * (2 ** 15 // 2) / np.max(np.abs(augmented_signal))
    return augmented_signal.astype(np.int16)


# inverse polarity
def inverse_pol(signal):
    augmented_signal = np.multiply(signal, -1)
    augmented_signal = augmented_signal * (2 ** 15 // 2) / np.max(np.abs(augmented_signal))
    return augmented_signal.astype(np.int16)


# random gain
def random_gain(signal, min_gain_factor=0, max_gain_factor=1):
    gain_factor = random.uniform(min_gain_factor, max_gain_factor)
    augmented_signal = np.multiply(signal, gain_factor)
    augmented_signal = augmented_signal * (2 ** 15 // 2) / np.max(np.abs(augmented_signal))
    return augmented_signal.astype(np.int16)
