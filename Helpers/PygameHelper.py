
import pygame
import pygame_gui


#def attributes():

def mode_1_window():
    pygame.init()
    pygame.display.set_caption('SimplySynth/ Mode 2')
    Interface = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()
    manager = pygame_gui.UIManager((1000, 800), 'Files/themes.json')
    
    path1_input_rect = pygame.Rect(450, 600, 240, 50)
    path2_input_rect = pygame.Rect(450, 650, 240, 50)

    text_rect = pygame.Rect(150, 600, 300, 50)
    heading_rect1 = pygame.Rect(150, 50, 150, 40)
    play_button_rect = pygame.Rect(475, 750, 100, 40)

    wave_rect1 = pygame.Rect(0, 100, 120, 40)
    wave_rect2 = pygame.Rect(140, 100, 120, 40)
    wave_rect3 = pygame.Rect(280, 100, 120, 40)
    wave_rect4 = pygame.Rect(420, 100, 120, 40)
    wave_rect5 = pygame.Rect(560, 100, 120, 40)
    wave_rect6 = pygame.Rect(700, 100, 120, 40)
    wave_rect7 = pygame.Rect(840, 100, 100, 40)

    filter_rect1 = pygame.Rect(0, 230, 200, 40)

    effect_rect1 = pygame.Rect(0, 360, 300, 40)
    effect_rect2 = pygame.Rect(350, 360, 300, 40)
    effect_rect3 = pygame.Rect(700, 360, 300, 40)
    effect_rect4 = pygame.Rect(0, 420, 300, 40)
    effect_rect5 = pygame.Rect(350, 420, 300, 40)
    effect_rect6 = pygame.Rect(700, 420, 300, 40)




    wavetype_1=pygame_gui.elements.UIButton(relative_rect=wave_rect1,
        text='Sine',
        manager=manager)
    wavetype_2=pygame_gui.elements.UIButton(relative_rect=wave_rect2,
        text='Square',
        manager=manager)
    wavetype_3=pygame_gui.elements.UIButton(relative_rect=wave_rect3,
        text='Sawtooth',
        manager=manager)
    wavetype_4=pygame_gui.elements.UIButton(relative_rect=wave_rect4,
        text='Triangle',
        manager=manager)
    wavetype_5=pygame_gui.elements.UIButton(relative_rect=wave_rect5,
        text='Oboe',
        manager=manager)
    wavetype_6=pygame_gui.elements.UIButton(relative_rect=wave_rect6,
        text='Flute',
        manager=manager)
    wavetype_7=pygame_gui.elements.UIButton(relative_rect=wave_rect7,
        text='Bell',
        manager=manager)
    filtertype_1=pygame_gui.elements.UIButton(relative_rect=filter_rect1,
        text='Low-Pass',
        manager=manager)
    effecttype_1=pygame_gui.elements.UIButton(relative_rect=effect_rect1,
        text='White Noise',
        manager=manager)
    effecttype_2=pygame_gui.elements.UIButton(relative_rect=effect_rect2,
        text='Environmental Noise',
        manager=manager)
    effecttype_3=pygame_gui.elements.UIButton(relative_rect=effect_rect3,
        text='Time Stretch',
        manager=manager)
    effecttype_4=pygame_gui.elements.UIButton(relative_rect=effect_rect4,
        text='Pitch Scaling',
        manager=manager)
    effecttype_5=pygame_gui.elements.UIButton(relative_rect=effect_rect5,
        text='Inverse Polarity',
        manager=manager)
    effecttype_6=pygame_gui.elements.UIButton(relative_rect=effect_rect6,
        text='Random Gain',
        manager=manager)
    

    base_font = pygame.font.Font(None, 48)
    heading_font = pygame.font.Font(None, 38)

    user_text1 = ''
    user_text2 = ''

    active_1=False
    active_2=False

    color_1='#3D59AB'
    color_2='#3D59AB'

    is_running = True
    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == wavetype_1:
                    print('1')
                elif event.ui_element == wavetype_2:
                    print('2')
                elif event.ui_element == wavetype_3:
                    print('3')
                elif event.ui_element == wavetype_4:
                    print('4')
                elif event.ui_element == wavetype_5:
                    print('5')   
                elif event.ui_element == wavetype_6:
                    print('6')
                elif event.ui_element == wavetype_7:
                    print('7') 
                elif event.ui_element == filtertype_1:
                    print('1')
                elif event.ui_element == effecttype_1:
                    print('1')
                elif event.ui_element == effecttype_2:
                    print('2')
                elif event.ui_element == effecttype_3:
                    print('3')
                elif event.ui_element == effecttype_4:
                    print('4')
                elif event.ui_element == effecttype_5:
                    print('5')
                elif event.ui_element == effecttype_6:
                    print('6')

            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if path1_input_rect.collidepoint(event.pos):
                    # Toggle the active_1 variable.
                    active_1 = not active_1
                else:
                    active_1 = False
                if path2_input_rect.collidepoint(event.pos):
                    # Toggle the active_1 variable.
                    active_2 = not active_2
                else:
                    active_2 = False
                # Change the current color of the input box.
                color_1 = '#6495ED' if active_1 else '#3D59AB'
                color_2 = '#6495ED' if active_2 else '#3D59AB'
            if event.type == pygame.KEYDOWN:
                if active_1:
                    if event.key == pygame.K_RETURN:
                        print(user_text1)
                        user_text1 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_text1 = user_text1[:-1]
                    else:
                        user_text1 += event.unicode
                if active_2:
                    if event.key == pygame.K_RETURN:
                        print(user_text2)
                        user_text2 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_text2 = user_text2[:-1]
                    else:
                        user_text2 += event.unicode
            manager.process_events(event)
        

        Interface.fill('#FFF8DC')
        pygame.draw.rect(Interface,'#3D59AB' , play_button_rect)
        pygame.draw.rect(Interface, color_1 , path1_input_rect)
        pygame.draw.rect(Interface,color_2 , path2_input_rect)
        pygame.draw.rect(Interface,color_1 , wave_rect1)
        pygame.draw.rect(Interface,color_1 , wave_rect2)
        pygame.draw.rect(Interface,color_1 , wave_rect3)
        pygame.draw.rect(Interface,color_1 , wave_rect4)
        pygame.draw.rect(Interface,color_1 , wave_rect5)
        pygame.draw.rect(Interface,color_1 , wave_rect6)
        pygame.draw.rect(Interface,color_1 , wave_rect7)
        pygame.draw.rect(Interface,color_1 , filter_rect1)

        pygame.draw.rect(Interface,color_1 , effect_rect1)
        pygame.draw.rect(Interface,color_1 , effect_rect2)
        pygame.draw.rect(Interface,color_1 , effect_rect3)
        pygame.draw.rect(Interface,color_1 , effect_rect4)
        pygame.draw.rect(Interface,color_1 , effect_rect5)
        pygame.draw.rect(Interface,color_1 , effect_rect6)



        text1 = base_font.render('Note File Path:', True, '#3D59AB')
        text2 = base_font.render('Tempo File Path:', True, '#3D59AB')

        wave_text1 = heading_font.render(wavetype_1.text, True,'#FFF8DC')
        wave_text2 = heading_font.render(wavetype_2.text, True,'#FFF8DC')
        wave_text3 = heading_font.render(wavetype_3.text, True,'#FFF8DC')
        wave_text4 = heading_font.render(wavetype_4.text, True,'#FFF8DC')
        wave_text5 = heading_font.render(wavetype_5.text, True,'#FFF8DC')
        wave_text6 = heading_font.render(wavetype_6.text, True,'#FFF8DC')
        wave_text7 = heading_font.render(wavetype_7.text, True,'#FFF8DC')
        filter_text1 = heading_font.render(filtertype_1.text, True,'#FFF8DC')
        effect_text1 = heading_font.render(effecttype_1.text, True,'#FFF8DC')
        effect_text2 = heading_font.render(effecttype_2.text, True,'#FFF8DC')
        effect_text3 = heading_font.render(effecttype_3.text, True,'#FFF8DC')
        effect_text4 = heading_font.render(effecttype_4.text, True,'#FFF8DC')
        effect_text5 = heading_font.render(effecttype_5.text, True,'#FFF8DC')
        effect_text6 = heading_font.render(effecttype_6.text, True,'#FFF8DC')

        heading_text1 = heading_font.render('Wavetype', True,'#3D59AB')
        heading_text2 = heading_font.render('Filters', True,'#3D59AB')
        heading_text3 = heading_font.render('Effects', True, '#3D59AB')
        heading_text4 = heading_font.render('Envelope', True,  '#3D59AB')

        
        text_surface1 = base_font.render(user_text1, True, '#FFF8DC','#3D59AB')
        text_surface2 = base_font.render(user_text2, True, '#FFF8DC','#3D59AB')

        Interface.blit(heading_text1, (heading_rect1.x, heading_rect1.y))
        Interface.blit(heading_text2, (heading_rect1.x, heading_rect1.y+130))
        Interface.blit(heading_text3, (heading_rect1.x, heading_rect1.y+260))
        Interface.blit(heading_text4, (heading_rect1.x, heading_rect1.y+440))

        Interface.blit(wave_text1, (wave_rect1.x+5, wave_rect1.y+5))
        Interface.blit(wave_text2, (wave_rect2.x+5, wave_rect2.y+5))
        Interface.blit(wave_text3, (wave_rect3.x+5, wave_rect3.y+5))
        Interface.blit(wave_text4, (wave_rect4.x+5, wave_rect4.y+5))
        Interface.blit(wave_text5, (wave_rect5.x+5, wave_rect5.y+5))
        Interface.blit(wave_text6, (wave_rect6.x+5, wave_rect6.y+5))
        Interface.blit(wave_text7, (wave_rect7.x+5, wave_rect7.y+5))
        Interface.blit(filter_text1, (filter_rect1.x+5, filter_rect1.y+5))
        Interface.blit(effect_text1, (effect_rect1.x+5, effect_rect1.y+5))
        Interface.blit(effect_text2, (effect_rect2.x+5, effect_rect2.y+5))
        Interface.blit(effect_text3, (effect_rect3.x+5, effect_rect3.y+5))
        Interface.blit(effect_text4, (effect_rect4.x+5, effect_rect4.y+5))
        Interface.blit(effect_text5, (effect_rect5.x+5, effect_rect5.y+5))
        Interface.blit(effect_text6, (effect_rect6.x+5, effect_rect6.y+5))


        Interface.blit(text1, (text_rect.x+5, text_rect.y+5))
        Interface.blit(text2, (text_rect.x+5, text_rect.y+50))
        Interface.blit(text_surface1, (path1_input_rect.x+5, path1_input_rect.y+5)) 
        Interface.blit(text_surface2, (path2_input_rect.x+5, path2_input_rect.y+5))

        play_button_text = heading_font.render('Play', True, '#FFF8DC', '#3D59AB')
        Interface.blit(play_button_text, (play_button_rect.x+25, play_button_rect.y+5))  

        path1_input_rect.w = max(100, text_surface1.get_width()+10)
        path2_input_rect.w = max(100, text_surface2.get_width()+10)     
        pygame.display.flip()

def mode_2_window():
    pygame.init()
    pygame.display.set_caption('SimplySynth/ Mode 2')
    Interface = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()
    
    path_input_rect = pygame.Rect(400, 650, 240, 50)
    text_rect = pygame.Rect(150, 650, 240, 50)
    heading_rect1 = pygame.Rect(150, 50, 150, 40)
    play_button_rect = pygame.Rect(475, 750, 100, 40)

    base_font = pygame.font.Font(None, 48)
    heading_font = pygame.font.Font(None, 38)
    user_text = ''
    
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    path = user_text
                    print(path)
                else:
                    user_text += event.unicode

        Interface.fill('#FFF8DC')
        pygame.draw.rect(Interface,'#3D59AB' , play_button_rect)
        pygame.draw.rect(Interface,'#3D59AB' , path_input_rect)
        text = base_font.render('Midi File Path:', True, '#3D59AB')

        heading_text1 = heading_font.render('Wavetype', True,'#3D59AB')
        heading_text2 = heading_font.render('Envelope', True,'#3D59AB')
        heading_text3 = heading_font.render('Filters', True, '#3D59AB')
        heading_text4 = heading_font.render('Effects', True,  '#3D59AB')

        play_button_text = heading_font.render('Play', True, '#FFF8DC', '#3D59AB')
        text_surface = base_font.render(user_text, True, '#FFF8DC','#3D59AB')

        Interface.blit(heading_text1, (heading_rect1.x, heading_rect1.y))
        Interface.blit(heading_text2, (heading_rect1.x, heading_rect1.y+150))
        Interface.blit(heading_text3, (heading_rect1.x, heading_rect1.y+300))
        Interface.blit(heading_text4, (heading_rect1.x, heading_rect1.y+450))

        Interface.blit(text, (text_rect.x+5, text_rect.y+5))
        Interface.blit(text_surface, (path_input_rect.x+5, path_input_rect.y+5)) 
        Interface.blit(play_button_text, (play_button_rect.x+25, play_button_rect.y+5))  

        path_input_rect.w = max(100, text_surface.get_width()+10)     
        pygame.display.flip()
        clock.tick(60)

def mode_3_window():
    pygame.init()
    pygame.display.set_caption('SimplySynth/ Mode 2')
    Interface = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()
    
    path1_input_rect = pygame.Rect(450, 400, 240, 50)
    path2_input_rect = pygame.Rect(450, 500, 240, 50)
    path3_input_rect = pygame.Rect(450, 600, 240, 50)

    text_rect = pygame.Rect(150, 400, 300, 50)
    heading_rect1 = pygame.Rect(150, 50, 150, 40)
    play_button_rect = pygame.Rect(475, 750, 100, 40)

    base_font = pygame.font.Font(None, 48)
    heading_font = pygame.font.Font(None, 38)

    user_text1 = ''
    user_text2 = ''
    user_text3 = ''

    active_1=False
    active_2=False
    active_3=False

    color_1='#3D59AB'
    color_2='#3D59AB'
    color_3='#3D59AB'

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if path1_input_rect.collidepoint(event.pos):
                    # Toggle the active_1 variable.
                    active_1 = not active_1
                else:
                    active_1 = False

                if path2_input_rect.collidepoint(event.pos):
                    # Toggle the active_1 variable.
                    active_2 = not active_2
                else:
                    active_2 = False

                if path3_input_rect.collidepoint(event.pos):
                    # Toggle the active_1 variable.
                    active_3 = not active_3
                else:
                    active_3 = False

                # Change the current color of the input box.
                color_1 = '#6495ED' if active_1 else '#3D59AB'
                color_2 = '#6495ED' if active_2 else '#3D59AB'
                color_3 = '#6495ED' if active_3 else '#3D59AB'

            if event.type == pygame.KEYDOWN:
                if active_1:
                    if event.key == pygame.K_RETURN:
                        print(user_text1)
                        user_text1 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_text1 = user_text1[:-1]
                    else:
                        user_text1 += event.unicode

                if active_2:
                    if event.key == pygame.K_RETURN:
                        print(user_text2)
                        user_text2 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_text2 = user_text2[:-1]
                    else:
                        user_text2 += event.unicode
                
                if active_3:
                    if event.key == pygame.K_RETURN:
                        print(user_text3)
                        user_text3 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_text3 = user_text3[:-1]
                    else:
                        user_text3 += event.unicode

        Interface.fill('#FFF8DC')
        pygame.draw.rect(Interface,'#3D59AB' , play_button_rect)
        pygame.draw.rect(Interface, color_1 , path1_input_rect)
        pygame.draw.rect(Interface,color_2 , path2_input_rect)
        pygame.draw.rect(Interface,color_3 , path3_input_rect)

        text1 = base_font.render('Root Note:', True, '#3D59AB')
        text2 = base_font.render('Tempo:', True, '#3D59AB')
        text3 = base_font.render('Beats:', True, '#3D59AB')

        heading_text1 = heading_font.render('Wavetype', True,'#3D59AB')
        heading_text2 = heading_font.render('Envelope', True,  '#3D59AB')

        
        text_surface1 = base_font.render(user_text1, True, '#FFF8DC','#3D59AB')
        text_surface2 = base_font.render(user_text2, True, '#FFF8DC','#3D59AB')
        text_surface3 = base_font.render(user_text3, True, '#FFF8DC','#3D59AB')

        Interface.blit(heading_text1, (heading_rect1.x, heading_rect1.y))
        Interface.blit(heading_text2, (heading_rect1.x, heading_rect1.y+150))

        Interface.blit(text1, (text_rect.x+5, text_rect.y+5))
        Interface.blit(text2, (text_rect.x+5, text_rect.y+100))
        Interface.blit(text3, (text_rect.x+5, text_rect.y+200))

        Interface.blit(text_surface1, (path1_input_rect.x+5, path1_input_rect.y+5)) 
        Interface.blit(text_surface2, (path2_input_rect.x+5, path2_input_rect.y+5))
        Interface.blit(text_surface3, (path3_input_rect.x+5, path3_input_rect.y+5))

        play_button_text = heading_font.render('Play', True, '#FFF8DC', '#3D59AB')
        Interface.blit(play_button_text, (play_button_rect.x+25, play_button_rect.y+5))  

        path1_input_rect.w = max(100, text_surface1.get_width()+10)
        path2_input_rect.w = max(100, text_surface2.get_width()+10) 
        path3_input_rect.w = max(100, text_surface3.get_width()+10)

        pygame.display.flip()
        clock.tick(60)