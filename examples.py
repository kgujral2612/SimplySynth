""" This module contains some examples displaying the features by the project

***** Options *****
Wave Type:  Sine (1), Square (2), Sawtooth (3), Triangle (4),
             Oboe (5), Flute(6), Bell (7), Violin (8)
Envelopes:  Trapezoidal (1), ADSR (2)
Effects:    White Noise (1), Environmental Noise (2), Time Stretch (3),
            Pitch Scaling (4), Inverse Polarity (5), Random Gain (6)
Filters:    Low-Pass (1)
============================================================================================
"""
from interface_handler import play_notes, play_midi


def mode_a_example():
    """ A sample code that runs in mode-a. 
        The user must input a set of notes and beats,
        and the program plays those notes.
    """
    print("\nEg-1: Playing silent night on an oboe")
    notes = ["A4", "B4", "A4", "F#4", "A4", "B4", "A4", "F#4",
             "E5", "E5", "C#5", "D5", "D5", "A4",
             "B4", "B4", "D5", "C#5", "B4", "A4", "B4", "A4", "F#4",
             "B4", "B4", "D5", "C#5", "B4", "A4", "B4", "A4", "F#4",
             "E5", "E5", "G5", "E5", "C#5", "D5", "F#5",
             "D5", "A4", "F#4", "A4", "G4", "E4", "D4"
             ]

    beats = [1, 1, 1, 3, 1, 1, 1, 3,
             1, 2, 3, 1, 2, 3,
             2, 1, 1, 1, 1, 1.5, 0.5, 1, 3,
             2, 1, 1, 1, 1, 1.5, 0.5, 1, 3,
             2, 1, 1.5, 0.5, 1, 3, 3,
             1, 1, 1, 2, 0.5, 1, 4
             ]
    bpm = 120
    play_notes(notes=notes, beats=beats, bpm=bpm, wave_type=5)


def effects_example():
    """ A sample code that demonstrates pitch scaling 
        and time stretch effects
    """
    print("\nEg-2: Playing the bell")
    notes = ["C5", "D5", "C5"]
    beats = [1, 2, 1]
    bpm = 120
    play_notes(notes=notes, beats=beats, bpm=bpm, wave_type=7)

    print("Playing the same example with pitch scaling")
    play_notes(notes=notes, beats=beats, bpm=bpm, wave_type=7, effect=4)

    print("Time stretch")
    play_notes(notes=notes, beats=beats, bpm=bpm, wave_type=7, effect=3)


# Mode-B
def sawtooth_example():
    """ A sample code that demonstrates Sawtooth Wave
        created by the program
    """
    print("\nEg-3: Playing Viva La Vida with Sawtooth Wave")
    path = "Files/viva_la_vida.mid"
    play_midi(path, wave_type=3)


def violin_example():
    """ A sample code that demonstrates Violin sound
        created by the program
    """
    print("\nEg-4: Playing Harry Potter Theme Song on a violin")
    path = "Files/harry_potter.mid"
    play_midi(path, wave_type=8)


def flute_example():
    """ A sample code that demonstrates flute sound
        created by the program 
    """
    print("\nEg-5: Playing notes on a flute")
    notes = ["G4", "E4", "E4", "D4", "C4", "D4", "E4", "G4", "D5", "D5", "C5", "D5", "D5", "E5"
             ]
    beats = [1, 1, 1, 3, 1, 1, 2,
             1, 1, 1, 3, 1, 1, 2]
    play_notes(notes=notes, beats=beats, wave_type=6)


def triangle_example():
    """ A sample code that demonstrates triangle wave
        created by the program 
    """
    print("Playing Wii Mii Channel Song on a triangle wave")
    path = "Files/wii_mii.mid"
    play_midi(path, wave_type=4)


if __name__ == "__main__":
    mode_a_example()
    effects_example()
    sawtooth_example()
    violin_example()
    flute_example()
    triangle_example()
