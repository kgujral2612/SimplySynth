# Synthesizer
#
# Everything below is for the synth interface
# and has no relation to any of the core functionality
#
#

import simpleaudio as sa
from scipy.io import wavfile
from Helpers import PygameHelper
import pygame
import pygame_gui
#result = MidiHelper.Midi_Helper.input_midifile(wave_path)


pygame.init()
pygame.display.set_caption('SimplySynth')

Interface = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

background = pygame.Surface((1000, 800))
background.fill(pygame.Color('#B2DFEE'))

manager = pygame_gui.UIManager((1000, 800), 'Files/themes.json')

#hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
#                                             text='Say Hello',
#                                             manager=manager)


button_layout_rect1 = pygame.Rect(00, 250, 300, 300)
button_layout_rect2 = pygame.Rect(350, 250, 300, 300)
button_layout_rect3 = pygame.Rect(699, 250, 300, 300)

mode_1=pygame_gui.elements.UIButton(relative_rect=button_layout_rect1,
        text='MODE 1',
        manager=manager)
mode_2=pygame_gui.elements.UIButton(relative_rect=button_layout_rect2,
        text='MODE 2',
        manager=manager)
mode_3=pygame_gui.elements.UIButton(relative_rect=button_layout_rect3,
        text='MODE 3',
        manager=manager)

is_running = True
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == mode_1:
                PygameHelper.mode_1_window()
                print('Play a note or series of notes')
                print('Enter botes and tempo')
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == mode_2:               
                PygameHelper.mode_2_window()
                print('Midi File player')
                print('Enter midifile path')
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == mode_3:
                PygameHelper.mode_3_window()
                print('Aleatoric Player')
                print('Enter root note, tempo and number of beats')        
        manager.process_events(event)
    manager.update(time_delta)
    Interface.blit(background, (0, 0))
    manager.draw_ui(Interface)
    pygame.display.update()











