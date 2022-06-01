from InterfaceHandler import *


# Mode-A
# Playing silent night on an obo with some background noise
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
play_notes(notes=notes, beats=beats, bpm=bpm, wave_type=5, effect=1, envelope=2)

# Mode-B
path = "Files/test_midi1.mid"
play_midi(path, wave_type=3)

