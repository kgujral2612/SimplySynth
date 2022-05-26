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
import numpy as np
#result = MidiHelper.Midi_Helper.input_midifile(wave_path)


pygame.init()
pygame.display.set_caption('SimplySynth')

Interface = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Futura', 75)
sub_heading_font = pygame.font.SysFont('arial', 30)
heading_font = pygame.font.SysFont('Futura', 100)
background = pygame.Surface((1000, 800))
background.fill(pygame.Color('#B2DFEE'))

heading_rect = pygame.Rect(300, 100, 250, 100)
sub_heading_rect = pygame.Rect(130, 570, 500, 150)
button_layout_rect1 = pygame.Rect(80, 300, 250, 250)
button_layout_rect2 = pygame.Rect(380, 300, 250, 250)
button_layout_rect3 = pygame.Rect(680, 300, 250, 250)
box_color = np.zeros(3)

is_running = True
while is_running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEMOTION:
            if button_layout_rect1.collidepoint(event.pos):
                box_color=np.zeros(3)
                box_color[0]=1
            elif button_layout_rect2.collidepoint(event.pos):
                box_color=np.zeros(3)
                box_color[1]=1
            elif button_layout_rect3.collidepoint(event.pos):
                box_color=np.zeros(3)
                box_color[2]=1
            else:
                box_color=np.zeros(3)
        if event.type == pygame.MOUSEBUTTONDOWN:
                if button_layout_rect1.collidepoint(event.pos):
                    PygameHelper.mode_1_window()
                if button_layout_rect2.collidepoint(event.pos):
                    PygameHelper.mode_2_window()
                if button_layout_rect3.collidepoint(event.pos):
                    PygameHelper.mode_3_window()        
   

    button_text1 = font.render('Mode 1', True,'#FAF0E6')
    button_text2 = font.render('Mode 2', True,'#FAF0E6')
    button_text3 = font.render('Mode 3', True,'#FAF0E6')
    heading_text = heading_font.render('SimplySynth', True,'#4D4D4D')
    sub_heading_text1 = sub_heading_font.render('Note Player', True,'#4D4D4D')
    sub_heading_text2 = sub_heading_font.render('Midifile Player', True,'#4D4D4D')
    sub_heading_text3 = sub_heading_font.render('Aleatoric Player', True,'#4D4D4D')

    Interface.blit(background, (0, 0))
    pygame.draw.rect(Interface,('#FFA07A' if box_color[0] else '#4D4D4D'), button_layout_rect1)
    pygame.draw.rect(Interface,('#FFA07A' if box_color[1] else '#4D4D4D') , button_layout_rect2)
    pygame.draw.rect(Interface,('#FFA07A' if box_color[2] else '#4D4D4D'), button_layout_rect3)

    Interface.blit(button_text1, (button_layout_rect1.x+35, button_layout_rect1.y+100))
    Interface.blit(button_text2, (button_layout_rect2.x+35, button_layout_rect2.y+100))
    Interface.blit(button_text3, (button_layout_rect3.x+35, button_layout_rect3.y+100))
    Interface.blit(heading_text, (heading_rect.x, heading_rect.y))
    Interface.blit(sub_heading_text1, (sub_heading_rect.x+10, sub_heading_rect.y))
    Interface.blit(sub_heading_text2, (sub_heading_rect.x+300, sub_heading_rect.y))
    Interface.blit(sub_heading_text3, (sub_heading_rect.x+600, sub_heading_rect.y))


    pygame.display.update()











