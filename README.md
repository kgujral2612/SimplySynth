# SimpleSynth

Implementation of a simplistic synthesizer in Python

## Libraries
Please install these libraries using the following bash command:
 ```bash
 pip install numpy
 pip install soundaudio
 pip install MIDIfile
 ````

## Vision

Implement a synthesizer program that plays a song fed from a file containing MIDI values. Given a MIDI value, the synthesizer should evaluate the note and the corresponding frequency.

* **Phase 1**: In the past homework assignments, we have learned how to create sine waves. Using this knowledge, we plan to create sine, square, triangle, and sawteeth wave oscillators. We will combine these waves to create complex waveforms (sounds like musical instruments such as the trumpet) using Fourier series coefficients. 

* **Phase 2**: Next, we plan to implement a suitable modulator like the ADSR Envelope[2] that would allow us to smooth out transitions between the notes. Our goal is to play an arrangement of MIDI notes (song) provided in the form of an array such as: [A4 0 1, G4 1 1, F4 2 1,...]

* **Phase 3**: Further, we will implement some filters such as the low-pass filter and the high-pass, etc in order to sculpt the complex waveforms created in the previous phases.

* **Phase 4**: Assuming everything has gone well so far our final goal is to be able to read the input from a MIDI file using a python library.

## Authors
- Harmandeep Singh
- Kaushambi Gujral