# SimplySynth

Implementation of a simplistic synthesizer in Python
<br />
<img src="Files/Images/homescreen.JPG" alt="main-page" width="550"/>
<br />
<img src="Files/Images/mode1screen.JPG" alt="model-screen" width="550"/>


## Libraries
Please install these libraries using the following bash command:
 ```bash
 pip install mido
 pip install numpy
 pip install soundaudio
 pip install scipy
 pip install pygame
 pip install pygame-gui
 pip install librosa
 ````

## Features
### Modes
<ol>
<li>Mode A: Input notes and corresponding duration in form of text files</li>
<li>Mode B: MIDI input file</li>
<li>Mode C: Aleatoric</li>
</ol>

### Options
#### Wave Type
Sine, Square, Sawtooth, Triangle
Oboe, Flute, Bell

#### Envelopes
Trapezoidal, ADSR

#### Effects
<ol>
  <li>White noise: random signal</li>
  <li>Environmental noise: a soothing background sound of forest at night</li>
  <li>Time Stretch: increases the duration of each note</li>
  <li>Pitch Scaling: changes the pitch of the audio</li>
  <li>Inverse Polarity: reverses the amplitude of the signal</li>
  <li>Random Gain: increases the amplitude by some random value</li>
</ol>

### Filters
Low-pass band, High-pass band

## Known Issues
- Unable to play midi files that don't consistently contain a "note-off" message for every "note-on"

## Extensions
<ol>
<li>Simulate the sound of complex instruments such as the piano, guitar, etc</li>
<li>Simulate percussion instruments</li>
</ol>

## Authors
- Harmandeep Singh
- Kaushambi Gujral
