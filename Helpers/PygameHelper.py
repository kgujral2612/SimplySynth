import numpy as np
import pygame
import pygame_gui
import InterfaceHandler


#def attributes():

def mode_1_window():
    pygame.init()
    pygame.display.set_caption('SimplySynth/ Mode 2')
    Interface = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()

    note_path=None
    note_arr=[]
    beat_path=None
    beat_arr=[]
    wavetype = None
    effects = None
    filters = None
    envelopes = None
    
    path1_input_rect = pygame.Rect(330, 600, 240, 50)
    path2_input_rect = pygame.Rect(330, 660, 240, 50)

    text_rect = pygame.Rect(30, 600, 300, 50)
    heading_rect1 = pygame.Rect(30, 50, 150, 40)
    play_button_rect = pygame.Rect(450, 730, 150, 60)

    wave_rect1 = pygame.Rect(30, 100, 120, 40)
    wave_rect2 = pygame.Rect(170, 100, 120, 40)
    wave_rect3 = pygame.Rect(310, 100, 120, 40)
    wave_rect4 = pygame.Rect(450, 100, 120, 40)
    wave_rect5 = pygame.Rect(590, 100, 120, 40)
    wave_rect6 = pygame.Rect(730, 100, 120, 40)
    wave_rect7 = pygame.Rect(870, 100, 100, 40)
    filter_rect1 = pygame.Rect(30, 230, 200, 40)
    effect_rect1 = pygame.Rect(30, 360, 250, 40)
    effect_rect2 = pygame.Rect(380, 360, 250, 40)
    effect_rect3 = pygame.Rect(720, 360, 250, 40)
    effect_rect4 = pygame.Rect(30, 420, 250, 40)
    effect_rect5 = pygame.Rect(380, 420, 250, 40)
    effect_rect6 = pygame.Rect(720, 420, 250, 40)
    envelope_rect1 = pygame.Rect(30, 520, 250, 40)
    envelope_rect2 = pygame.Rect(380, 520, 250, 40)
    envelope_rect3 = pygame.Rect(720, 520, 250, 40)
    
    base_font = pygame.font.SysFont('Futura', 48)
    heading_font = pygame.font.SysFont('Futura', 30)

    user_text1 = '<filename>.txt'
    user_text2 = '<filename>.txt'

    active_1=False
    active_2=False

    color_1='#4D4D4D'
    color_2='#4D4D4D'
    colorw = np.zeros(7)
    colore = np.zeros(6)
    colorf = np.zeros(1)
    coloren = np.zeros(3)

    is_running = True
    while is_running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False                
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if wave_rect1.collidepoint(event.pos):
                    wavetype=1
                    colorw=np.zeros(7)
                    colorw[0]=1
                if wave_rect2.collidepoint(event.pos):
                    wavetype=2
                    colorw=np.zeros(7)
                    colorw[1]=1
                if wave_rect3.collidepoint(event.pos):
                    wavetype=3
                    colorw=np.zeros(7)
                    colorw[2]=1
                if wave_rect4.collidepoint(event.pos):
                    wavetype=4
                    colorw=np.zeros(7)
                    colorw[3]=1
                if wave_rect5.collidepoint(event.pos):
                    wavetype=5
                    colorw=np.zeros(7)
                    colorw[4]=1
                if wave_rect6.collidepoint(event.pos):
                    wavetype=6
                    colorw=np.zeros(7)
                    colorw[5]=1
                if wave_rect7.collidepoint(event.pos):
                    wavetype=7
                    colorw=np.zeros(7)
                    colorw[6]=1
                if filter_rect1.collidepoint(event.pos):
                    filters=1
                    colorf=np.zeros(1)
                    colorf[0]=1
                if effect_rect1.collidepoint(event.pos):
                    effects=1
                    colore=np.zeros(6)
                    colore[0]=1
                if effect_rect2.collidepoint(event.pos):
                    effects=2
                    colore=np.zeros(6)
                    colore[1]=1
                if effect_rect3.collidepoint(event.pos):
                    effects=3
                    colore=np.zeros(6)
                    colore[2]=1
                if effect_rect4.collidepoint(event.pos):
                    effects=4
                    colore=np.zeros(6)
                    colore[3]=1
                if effect_rect5.collidepoint(event.pos):
                    effects=5
                    colore=np.zeros(6)
                    colore[4]=1
                if effect_rect6.collidepoint(event.pos):
                    effects=6
                    colore=np.zeros(6)
                    colore[5]=1
                if envelope_rect1.collidepoint(event.pos):
                    envelopes=1
                    coloren=np.zeros(3)
                    coloren[0]=1
                if envelope_rect2.collidepoint(event.pos):
                    envelopes=2
                    coloren=np.zeros(3)
                    coloren[1]=1
                if envelope_rect3.collidepoint(event.pos):
                    envelopes=3
                    coloren=np.zeros(3)
                    coloren[2]=1
                if play_button_rect.collidepoint(event.pos):
                    with open(note_path) as n:
                        lines = n.readlines()
                        for line in lines:
                            line = line.strip()
                            note_arr.append(line.replace('""',''))
                        n.close()
                    if beat_path != None:
                        with open(beat_path) as b:
                            lines = b.readlines()
                            for line in lines:
                                beat_arr.append(float(line))
                            b.close()

                    InterfaceHandler.play_notes(notes = note_arr, beats = beat_arr, bpm=90 ,wave_type=wavetype, effect=effects, filter_type=filters, envelope=envelopes)
                if path1_input_rect.collidepoint(event.pos):
                    # Toggle the active_1 variable.
                    active_1 = not active_1
                    user_text1 = ''
                else:
                    active_1 = False
                if path2_input_rect.collidepoint(event.pos):
                    # Toggle the active_1 variable.
                    active_2 = not active_2
                    user_text2=''
                else:
                    active_2 = False
                
                # Change the current color of the input box.
                color_1 = '#FFA07A' if active_1 else '#4D4D4D'
                color_2 = '#FFA07A' if active_2 else '#4D4D4D'
            if event.type == pygame.KEYDOWN:
                if active_1:
                    if event.key == pygame.K_RETURN:
                        note_path = user_text1
                    elif event.key == pygame.K_BACKSPACE:
                        user_text1 = user_text1[:-1]
                    else:
                        user_text1 += event.unicode
                if active_2:
                    if event.key == pygame.K_RETURN:
                        beat_path = user_text2
                    elif event.key == pygame.K_BACKSPACE:
                        user_text2 = user_text2[:-1]
                    else:
                        user_text2 += event.unicode
        

        Interface.fill('#B2DFEE')
        pygame.draw.rect(Interface,'#4D4D4D' , play_button_rect)
        pygame.draw.rect(Interface,color_1 , path1_input_rect)
        pygame.draw.rect(Interface,color_2 , path2_input_rect)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[0] else '#4D4D4D') , wave_rect1)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[1] else '#4D4D4D') , wave_rect2)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[2] else '#4D4D4D') , wave_rect3)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[3] else '#4D4D4D') , wave_rect4)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[4] else '#4D4D4D') , wave_rect5)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[5] else '#4D4D4D') , wave_rect6)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[6] else '#4D4D4D') , wave_rect7)
        pygame.draw.rect(Interface,('#FFA07A' if colorf[0] else '#4D4D4D') , filter_rect1)
        pygame.draw.rect(Interface,('#FFA07A' if colore[0] else '#4D4D4D') , effect_rect1)
        pygame.draw.rect(Interface,('#FFA07A' if colore[1] else '#4D4D4D') , effect_rect2)
        pygame.draw.rect(Interface,('#FFA07A' if colore[2] else '#4D4D4D') , effect_rect3)
        pygame.draw.rect(Interface,('#FFA07A' if colore[3] else '#4D4D4D') , effect_rect4)
        pygame.draw.rect(Interface,('#FFA07A' if colore[4] else '#4D4D4D') , effect_rect5)
        pygame.draw.rect(Interface,('#FFA07A' if colore[5] else '#4D4D4D') , effect_rect6)
        pygame.draw.rect(Interface,('#FFA07A' if coloren[0] else '#4D4D4D') , envelope_rect1)
        pygame.draw.rect(Interface,('#FFA07A' if coloren[1] else '#4D4D4D') , envelope_rect2)
        pygame.draw.rect(Interface,('#FFA07A' if coloren[2] else '#4D4D4D') , envelope_rect3)



        text1 = base_font.render('Note File Path:', True, '#4D4D4D')
        text2 = base_font.render('Beats File Path:', True, '#4D4D4D')

        wave_text1 = heading_font.render('Sine', True,'#FFF8DC')
        wave_text2 = heading_font.render('Square', True,'#FFF8DC')
        wave_text3 = heading_font.render('SawTooth', True,'#FFF8DC')
        wave_text4 = heading_font.render('Triangle', True,'#FFF8DC')
        wave_text5 = heading_font.render('Oboe', True,'#FFF8DC')
        wave_text6 = heading_font.render('Flute', True,'#FFF8DC')
        wave_text7 = heading_font.render('Bell', True,'#FFF8DC')
        filter_text1 = heading_font.render('Low-Pass', True,'#FFF8DC')
        
        effect_text1 = heading_font.render('White Noise', True,'#FFF8DC')
        effect_text2 = heading_font.render('Environmental Noise', True,'#FFF8DC')
        effect_text3 = heading_font.render('Time Stretch', True,'#FFF8DC')
        effect_text4 = heading_font.render('Pitch Scaling', True,'#FFF8DC')
        effect_text5 = heading_font.render('Inverse Polarity', True,'#FFF8DC')
        effect_text6 = heading_font.render('Random Gain', True,'#FFF8DC')

        envelope_text1 = heading_font.render('Trapezoidal', True,'#FFF8DC')
        envelope_text2 = heading_font.render('ADSR', True,'#FFF8DC')
        envelope_text3 = heading_font.render('LFO', True,'#FFF8DC')

        heading_text1 = base_font.render('Wavetype', True,'#4D4D4D')
        heading_text2 = base_font.render('Filters', True,'#4D4D4D')
        heading_text3 = base_font.render('Effects', True, '#4D4D4D')
        heading_text4 = base_font.render('Envelope', True,  '#4D4D4D')   

        text_surface1 = heading_font.render(user_text1, True, '#FFF8DC','#4D4D4D')
        text_surface2 = heading_font.render(user_text2, True, '#FFF8DC','#4D4D4D')


        Interface.blit(heading_text1, (heading_rect1.x, heading_rect1.y))
        Interface.blit(heading_text2, (heading_rect1.x, heading_rect1.y+130))
        Interface.blit(heading_text3, (heading_rect1.x, heading_rect1.y+260))
        Interface.blit(heading_text4, (heading_rect1.x, heading_rect1.y+430))

        Interface.blit(wave_text1, (wave_rect1.x+35, wave_rect1.y+10))
        Interface.blit(wave_text2, (wave_rect2.x+25, wave_rect2.y+10))
        Interface.blit(wave_text3, (wave_rect3.x+10, wave_rect3.y+10))
        Interface.blit(wave_text4, (wave_rect4.x+20, wave_rect4.y+10))
        Interface.blit(wave_text5, (wave_rect5.x+30, wave_rect5.y+10))
        Interface.blit(wave_text6, (wave_rect6.x+35, wave_rect6.y+10))
        Interface.blit(wave_text7, (wave_rect7.x+30, wave_rect7.y+10))

        Interface.blit(filter_text1, (filter_rect1.x+50, filter_rect1.y+10))
        Interface.blit(effect_text1, (effect_rect1.x+60, effect_rect1.y+10))
        Interface.blit(effect_text2, (effect_rect2.x+25, effect_rect2.y+10))
        Interface.blit(effect_text3, (effect_rect3.x+60, effect_rect3.y+10))
        Interface.blit(effect_text4, (effect_rect4.x+60, effect_rect4.y+10))
        Interface.blit(effect_text5, (effect_rect5.x+50, effect_rect5.y+10))
        Interface.blit(effect_text6, (effect_rect6.x+50, effect_rect6.y+10))

        Interface.blit(envelope_text1, (envelope_rect1.x+60, envelope_rect1.y+10))
        Interface.blit(envelope_text2, (envelope_rect2.x+100, envelope_rect2.y+10))
        Interface.blit(envelope_text3, (envelope_rect3.x+100, envelope_rect3.y+10))

        Interface.blit(text1, (text_rect.x+5, text_rect.y+5))
        Interface.blit(text2, (text_rect.x+5, text_rect.y+65))

        Interface.blit(text_surface1, (path1_input_rect.x+5, path1_input_rect.y+15)) 
        Interface.blit(text_surface2, (path2_input_rect.x+5, path2_input_rect.y+15))

        play_button_text = base_font.render('Play', True, '#FFA07A')
        Interface.blit(play_button_text, (play_button_rect.x+40, play_button_rect.y+15))  

        path1_input_rect.w = max(100, text_surface1.get_width()+10)
        path2_input_rect.w = max(100, text_surface2.get_width()+10)     
        pygame.display.flip()


def mode_2_window():
    pygame.init()
    pygame.display.set_caption('SimplySynth/ Mode 2')
    Interface = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()

    wave_path = None
    wavetype = None
    effects = None
    filters = None
    envelopes = None
    
    path_input_rect = pygame.Rect(330, 600, 240, 50)
    text_rect = pygame.Rect(30, 600, 300, 50)
    heading_rect1 = pygame.Rect(30, 50, 150, 40)
    play_button_rect = pygame.Rect(450, 730, 150, 60)


    wave_rect1 = pygame.Rect(30, 100, 120, 40)
    wave_rect2 = pygame.Rect(170, 100, 120, 40)
    wave_rect3 = pygame.Rect(310, 100, 120, 40)
    wave_rect4 = pygame.Rect(450, 100, 120, 40)
    wave_rect5 = pygame.Rect(590, 100, 120, 40)
    wave_rect6 = pygame.Rect(730, 100, 120, 40)
    wave_rect7 = pygame.Rect(870, 100, 100, 40)
    filter_rect1 = pygame.Rect(30, 230, 200, 40)
    effect_rect1 = pygame.Rect(30, 360, 250, 40)
    effect_rect2 = pygame.Rect(380, 360, 250, 40)
    effect_rect3 = pygame.Rect(720, 360, 250, 40)
    effect_rect4 = pygame.Rect(30, 420, 250, 40)
    effect_rect5 = pygame.Rect(380, 420, 250, 40)
    effect_rect6 = pygame.Rect(720, 420, 250, 40)
    envelope_rect1 = pygame.Rect(30, 520, 250, 40)
    envelope_rect2 = pygame.Rect(380, 520, 250, 40)
    envelope_rect3 = pygame.Rect(720, 520, 250, 40)
    

    base_font = pygame.font.SysFont('Futura', 48)
    heading_font = pygame.font.SysFont('Futura', 30)
    user_text = '<filename>.txt'

    active_1=False
    color_1='#4D4D4D'
    colorw = np.zeros(7)
    colore = np.zeros(6)
    colorf = np.zeros(1)
    coloren = np.zeros(3)
    
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if wave_rect1.collidepoint(event.pos):
                    wavetype=1
                    colorw=np.zeros(7)
                    colorw[0]=1
                if wave_rect2.collidepoint(event.pos):
                    wavetype=2
                    colorw=np.zeros(7)
                    colorw[1]=1
                if wave_rect3.collidepoint(event.pos):
                    wavetype=3
                    colorw=np.zeros(7)
                    colorw[2]=1
                if wave_rect4.collidepoint(event.pos):
                    wavetype=4
                    colorw=np.zeros(7)
                    colorw[3]=1
                if wave_rect5.collidepoint(event.pos):
                    wavetype=5
                    colorw=np.zeros(7)
                    colorw[4]=1
                if wave_rect6.collidepoint(event.pos):
                    wavetype=6
                    colorw=np.zeros(7)
                    colorw[5]=1
                if wave_rect7.collidepoint(event.pos):
                    wavetype=7
                    colorw=np.zeros(7)
                    colorw[6]=1
                if filter_rect1.collidepoint(event.pos):
                    filters=1
                    colorf=np.zeros(1)
                    colorf[0]=1
                if effect_rect1.collidepoint(event.pos):
                    effects=1
                    colore=np.zeros(6)
                    colore[0]=1
                if effect_rect2.collidepoint(event.pos):
                    effects=2
                    colore=np.zeros(6)
                    colore[1]=1
                if effect_rect3.collidepoint(event.pos):
                    effects=3
                    colore=np.zeros(6)
                    colore[2]=1
                if effect_rect4.collidepoint(event.pos):
                    effects=4
                    colore=np.zeros(6)
                    colore[3]=1
                if effect_rect5.collidepoint(event.pos):
                    effects=5
                    colore=np.zeros(6)
                    colore[4]=1
                if effect_rect6.collidepoint(event.pos):
                    effects=6
                    colore=np.zeros(6)
                    colore[5]=1
                if envelope_rect1.collidepoint(event.pos):
                    envelopes=1
                    coloren=np.zeros(3)
                    coloren[0]=1
                if envelope_rect2.collidepoint(event.pos):
                    envelopes=2
                    coloren=np.zeros(3)
                    coloren[1]=1
                if envelope_rect3.collidepoint(event.pos):
                    envelopes=3
                    coloren=np.zeros(3)
                    coloren[2]=1
                if play_button_rect.collidepoint(event.pos):
                    InterfaceHandler.play_midi(path = wave_path,wave_type=wavetype, effect=effects, filter_type=filters, envelope=envelopes)
                if path_input_rect.collidepoint(event.pos):
                    # Toggle the active_1 variable.
                    active_1 = not active_1
                    user_text = ''
                else:
                    active_1 = False
                
                # Change the current color of the input box.
                color_1 = '#FFA07A' if active_1 else '#4D4D4D'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    wave_path = user_text
                else:
                    user_text += event.unicode

        Interface.fill('#B2DFEE')
        pygame.draw.rect(Interface,'#4D4D4D' , play_button_rect)
        pygame.draw.rect(Interface,color_1 , path_input_rect)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[0] else '#4D4D4D') , wave_rect1)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[1] else '#4D4D4D') , wave_rect2)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[2] else '#4D4D4D') , wave_rect3)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[3] else '#4D4D4D') , wave_rect4)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[4] else '#4D4D4D') , wave_rect5)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[5] else '#4D4D4D') , wave_rect6)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[6] else '#4D4D4D') , wave_rect7)
        pygame.draw.rect(Interface,('#FFA07A' if colorf[0] else '#4D4D4D') , filter_rect1)
        pygame.draw.rect(Interface,('#FFA07A' if colore[0] else '#4D4D4D') , effect_rect1)
        pygame.draw.rect(Interface,('#FFA07A' if colore[1] else '#4D4D4D') , effect_rect2)
        pygame.draw.rect(Interface,('#FFA07A' if colore[2] else '#4D4D4D') , effect_rect3)
        pygame.draw.rect(Interface,('#FFA07A' if colore[3] else '#4D4D4D') , effect_rect4)
        pygame.draw.rect(Interface,('#FFA07A' if colore[4] else '#4D4D4D') , effect_rect5)
        pygame.draw.rect(Interface,('#FFA07A' if colore[5] else '#4D4D4D') , effect_rect6)
        pygame.draw.rect(Interface,('#FFA07A' if coloren[0] else '#4D4D4D') , envelope_rect1)
        pygame.draw.rect(Interface,('#FFA07A' if coloren[1] else '#4D4D4D') , envelope_rect2)
        pygame.draw.rect(Interface,('#FFA07A' if coloren[2] else '#4D4D4D') , envelope_rect3)

        wave_text1 = heading_font.render('Sine', True,'#FFF8DC')
        wave_text2 = heading_font.render('Square', True,'#FFF8DC')
        wave_text3 = heading_font.render('SawTooth', True,'#FFF8DC')
        wave_text4 = heading_font.render('Triangle', True,'#FFF8DC')
        wave_text5 = heading_font.render('Oboe', True,'#FFF8DC')
        wave_text6 = heading_font.render('Flute', True,'#FFF8DC')
        wave_text7 = heading_font.render('Bell', True,'#FFF8DC')
        filter_text1 = heading_font.render('Low-Pass', True,'#FFF8DC')
        effect_text1 = heading_font.render('White Noise', True,'#FFF8DC')
        effect_text2 = heading_font.render('Environmental Noise', True,'#FFF8DC')
        effect_text3 = heading_font.render('Tome Stretch', True,'#FFF8DC')
        effect_text4 = heading_font.render('Pitch Scaling', True,'#FFF8DC')
        effect_text5 = heading_font.render('Inverse Polarity', True,'#FFF8DC')
        effect_text6 = heading_font.render('Random Gain', True,'#FFF8DC')
        envelope_text1 = heading_font.render('Trapezoidal', True,'#FFF8DC')
        envelope_text2 = heading_font.render('ADSR', True,'#FFF8DC')
        envelope_text3 = heading_font.render('LFO', True,'#FFF8DC')

        text = base_font.render('Midi File Path:', True, '#4D4D4D')

        heading_text1 = base_font.render('Wavetype', True,'#4D4D4D')
        heading_text2 = base_font.render('Envelope', True,'#4D4D4D')
        heading_text3 = base_font.render('Filters', True, '#4D4D4D')
        heading_text4 = base_font.render('Effects', True,  '#4D4D4D')

        play_button_text = base_font.render('Play', True, '#FFA07A')
        text_surface = heading_font.render(user_text, True, '#FFF8DC')


        Interface.blit(heading_text1, (heading_rect1.x, heading_rect1.y))
        Interface.blit(heading_text2, (heading_rect1.x, heading_rect1.y+130))
        Interface.blit(heading_text3, (heading_rect1.x, heading_rect1.y+260))
        Interface.blit(heading_text4, (heading_rect1.x, heading_rect1.y+430))

        Interface.blit(wave_text1, (wave_rect1.x+35, wave_rect1.y+10))
        Interface.blit(wave_text2, (wave_rect2.x+25, wave_rect2.y+10))
        Interface.blit(wave_text3, (wave_rect3.x+10, wave_rect3.y+10))
        Interface.blit(wave_text4, (wave_rect4.x+20, wave_rect4.y+10))
        Interface.blit(wave_text5, (wave_rect5.x+30, wave_rect5.y+10))
        Interface.blit(wave_text6, (wave_rect6.x+35, wave_rect6.y+10))
        Interface.blit(wave_text7, (wave_rect7.x+30, wave_rect7.y+10))

        Interface.blit(filter_text1, (filter_rect1.x+50, filter_rect1.y+10))
        Interface.blit(effect_text1, (effect_rect1.x+60, effect_rect1.y+10))
        Interface.blit(effect_text2, (effect_rect2.x+25, effect_rect2.y+10))
        Interface.blit(effect_text3, (effect_rect3.x+60, effect_rect3.y+10))
        Interface.blit(effect_text4, (effect_rect4.x+60, effect_rect4.y+10))
        Interface.blit(effect_text5, (effect_rect5.x+50, effect_rect5.y+10))
        Interface.blit(effect_text6, (effect_rect6.x+50, effect_rect6.y+10))

        Interface.blit(envelope_text1, (envelope_rect1.x+60, envelope_rect1.y+10))
        Interface.blit(envelope_text2, (envelope_rect2.x+100, envelope_rect2.y+10))
        Interface.blit(envelope_text3, (envelope_rect3.x+100, envelope_rect3.y+10))

       

        Interface.blit(text, (text_rect.x+5, text_rect.y+5))
        Interface.blit(text_surface, (path_input_rect.x+5, path_input_rect.y+15)) 
        Interface.blit(play_button_text, (play_button_rect.x+40, play_button_rect.y+15))  

        path_input_rect.w = max(100, text_surface.get_width()+10)     
        pygame.display.flip()
        clock.tick(60)



def mode_3_window():
    pygame.init()
    pygame.display.set_caption('SimplySynth/ Mode 2')
    Interface = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()

    root_note=None
    tempo=None
    beats=None
    wavetype=None
    envelopes=None

    colorw = np.zeros(7)
    coloren = np.zeros(3)
    
    path1_input_rect = pygame.Rect(230, 400, 240, 50)
    path2_input_rect = pygame.Rect(230, 500, 240, 50)
    path3_input_rect = pygame.Rect(230, 600, 240, 50)

    text_rect = pygame.Rect(30, 400, 300, 50)
    heading_rect1 = pygame.Rect(30, 50, 150, 40)
    play_button_rect =  pygame.Rect(450, 730, 150, 60)

    wave_rect1 = pygame.Rect(30, 100, 120, 40)
    wave_rect2 = pygame.Rect(170, 100, 120, 40)
    wave_rect3 = pygame.Rect(310, 100, 120, 40)
    wave_rect4 = pygame.Rect(450, 100, 120, 40)
    wave_rect5 = pygame.Rect(590, 100, 120, 40)
    wave_rect6 = pygame.Rect(730, 100, 120, 40)
    wave_rect7 = pygame.Rect(870, 100, 100, 40)
    envelope_rect1 = pygame.Rect(30, 230, 250, 40)
    envelope_rect2 = pygame.Rect(380, 230, 250, 40)
    envelope_rect3 = pygame.Rect(720, 230, 250, 40)
    
    base_font = pygame.font.SysFont('Futura', 48)
    heading_font = pygame.font.SysFont('Futura', 30)

    user_text1 = '<filename>.txt'
    user_text2 = '<filename>.txt'
    user_text3 = '<filename>.txt'

    active_1=False
    active_2=False
    active_3=False

    color_1='#4D4D4D'
    color_2='#4D4D4D'
    color_3='#4D4D4D'

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if wave_rect1.collidepoint(event.pos):
                    wavetype=1
                    colorw=np.zeros(7)
                    colorw[0]=1
                if wave_rect2.collidepoint(event.pos):
                    wavetype=2
                    colorw=np.zeros(7)
                    colorw[1]=1
                if wave_rect3.collidepoint(event.pos):
                    wavetype=3
                    colorw=np.zeros(7)
                    colorw[2]=1
                if wave_rect4.collidepoint(event.pos):
                    wavetype=4
                    colorw=np.zeros(7)
                    colorw[3]=1
                if wave_rect5.collidepoint(event.pos):
                    wavetype=5
                    colorw=np.zeros(7)
                    colorw[4]=1
                if wave_rect6.collidepoint(event.pos):
                    wavetype=6
                    colorw=np.zeros(7)
                    colorw[5]=1
                if wave_rect7.collidepoint(event.pos):
                    wavetype=7
                    colorw=np.zeros(7)
                    colorw[6]=1
                if envelope_rect1.collidepoint(event.pos):
                    envelopes=1
                    coloren=np.zeros(3)
                    coloren[0]=1
                if envelope_rect2.collidepoint(event.pos):
                    envelopes=2
                    coloren=np.zeros(3)
                    coloren[1]=1
                if envelope_rect3.collidepoint(event.pos):
                    envelopes=3
                    coloren=np.zeros(3)
                    coloren[2]=1
                if play_button_rect.collidepoint(event.pos):
                    print(wavetype)
                    print(envelopes)
                    print(root_note)
                    print(tempo)
                    print(beats)

                    InterfaceHandler.play_aleatoric(root_note=root_note,bpm = int(tempo),beats=int(beats),wave_type=wavetype, envelope=envelopes)
                # If the user clicked on the input_box rect.
                if path1_input_rect.collidepoint(event.pos):
                    # Toggle the active_1 variable.
                    active_1 = not active_1
                    user_text1=''
                else:
                    active_1 = False

                if path2_input_rect.collidepoint(event.pos):
                    # Toggle the active_1 variable.
                    active_2 = not active_2
                    user_text2=''
                else:
                    active_2 = False

                if path3_input_rect.collidepoint(event.pos):
                    # Toggle the active_1 variable.
                    active_3 = not active_3
                    user_text3=''
                else:
                    active_3 = False

                # Change the current color of the input box.
                color_1 = '#FFA07A' if active_1 else '#4D4D4D'
                color_2 = '#FFA07A' if active_2 else '#4D4D4D'
                color_3 = '#FFA07A' if active_3 else '#4D4D4D'

            if event.type == pygame.KEYDOWN:
                if active_1:
                    if event.key == pygame.K_RETURN:
                        root_note =user_text1 
                    elif event.key == pygame.K_BACKSPACE:
                        user_text1 = user_text1[:-1]
                    else:
                        user_text1 += event.unicode

                if active_2:
                    if event.key == pygame.K_RETURN:
                        tempo = user_text2
                    elif event.key == pygame.K_BACKSPACE:
                        user_text2 = user_text2[:-1]
                    else:
                        user_text2 += event.unicode
                
                if active_3:
                    if event.key == pygame.K_RETURN:
                        beats = user_text3
                    elif event.key == pygame.K_BACKSPACE:
                        user_text3 = user_text3[:-1]
                    else:
                        user_text3 += event.unicode

        Interface.fill('#B2DFEE')
        pygame.draw.rect(Interface,'#4D4D4D' , play_button_rect)
        pygame.draw.rect(Interface, color_1 , path1_input_rect)
        pygame.draw.rect(Interface,color_2 , path2_input_rect)
        pygame.draw.rect(Interface,color_3 , path3_input_rect)

        pygame.draw.rect(Interface,('#FFA07A' if colorw[0] else '#4D4D4D') , wave_rect1)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[1] else '#4D4D4D') , wave_rect2)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[2] else '#4D4D4D') , wave_rect3)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[3] else '#4D4D4D') , wave_rect4)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[4] else '#4D4D4D') , wave_rect5)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[5] else '#4D4D4D') , wave_rect6)
        pygame.draw.rect(Interface,('#FFA07A' if colorw[6] else '#4D4D4D') , wave_rect7)
        pygame.draw.rect(Interface,('#FFA07A' if coloren[0] else '#4D4D4D') , envelope_rect1)
        pygame.draw.rect(Interface,('#FFA07A' if coloren[1] else '#4D4D4D') , envelope_rect2)
        pygame.draw.rect(Interface,('#FFA07A' if coloren[2] else '#4D4D4D') , envelope_rect3)

        wave_text1 = heading_font.render('Sine', True,'#FFF8DC')
        wave_text2 = heading_font.render('Square', True,'#FFF8DC')
        wave_text3 = heading_font.render('SawTooth', True,'#FFF8DC')
        wave_text4 = heading_font.render('Triangle', True,'#FFF8DC')
        wave_text5 = heading_font.render('Oboe', True,'#FFF8DC')
        wave_text6 = heading_font.render('Flute', True,'#FFF8DC')
        wave_text7 = heading_font.render('Bell', True,'#FFF8DC')
        envelope_text1 = heading_font.render('Trapezoidal', True,'#FFF8DC')
        envelope_text2 = heading_font.render('ADSR', True,'#FFF8DC')
        envelope_text3 = heading_font.render('LFO', True,'#FFF8DC')

        

        text1 = base_font.render('Root Note:', True, '#4D4D4D')
        text2 = base_font.render('Tempo:', True, '#4D4D4D')
        text3 = base_font.render('Beats:', True, '#4D4D4D')

        heading_text1 = base_font.render('Wavetype', True,'#4D4D4D')
        heading_text2 = base_font.render('Envelope', True,  '#4D4D4D')

        
        text_surface1 = heading_font.render(user_text1, True, '#FFF8DC')
        text_surface2 = heading_font.render(user_text2, True, '#FFF8DC')
        text_surface3 = heading_font.render(user_text3, True, '#FFF8DC')

        Interface.blit(heading_text1, (heading_rect1.x, heading_rect1.y))
        Interface.blit(heading_text2, (heading_rect1.x, heading_rect1.y+130))

        Interface.blit(wave_text1, (wave_rect1.x+35, wave_rect1.y+10))
        Interface.blit(wave_text2, (wave_rect2.x+25, wave_rect2.y+10))
        Interface.blit(wave_text3, (wave_rect3.x+10, wave_rect3.y+10))
        Interface.blit(wave_text4, (wave_rect4.x+20, wave_rect4.y+10))
        Interface.blit(wave_text5, (wave_rect5.x+30, wave_rect5.y+10))
        Interface.blit(wave_text6, (wave_rect6.x+35, wave_rect6.y+10))
        Interface.blit(wave_text7, (wave_rect7.x+30, wave_rect7.y+10))


        Interface.blit(envelope_text1, (envelope_rect1.x+60, envelope_rect1.y+10))
        Interface.blit(envelope_text2, (envelope_rect2.x+100, envelope_rect2.y+10))
        Interface.blit(envelope_text3, (envelope_rect3.x+100, envelope_rect3.y+10))


        Interface.blit(text1, (text_rect.x+5, text_rect.y+5))
        Interface.blit(text2, (text_rect.x+5, text_rect.y+100))
        Interface.blit(text3, (text_rect.x+5, text_rect.y+200))

        Interface.blit(text_surface1, (path1_input_rect.x+5, path1_input_rect.y+15)) 
        Interface.blit(text_surface2, (path2_input_rect.x+5, path2_input_rect.y+15))
        Interface.blit(text_surface3, (path3_input_rect.x+5, path3_input_rect.y+15))

        play_button_text = base_font.render('Play', True, '#FFA07A')
        Interface.blit(play_button_text, (play_button_rect.x+40, play_button_rect.y+15))  

        path1_input_rect.w = max(100, text_surface1.get_width()+10)
        path2_input_rect.w = max(100, text_surface2.get_width()+10) 
        path3_input_rect.w = max(100, text_surface3.get_width()+10)

        pygame.display.flip()
        clock.tick(60)