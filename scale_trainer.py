#'scale_trainer.py' 
def run():
    
    import scalekit as sk
    import time
    import wave
    import os
    from playsound import playsound as ps
    import random
    import menus
    import toolkit as tk
    import chimes
    #scale_roots are the files
    waves, wave_tones, scale_roots, scale_root_names = tk.get_playback_set_scales()  
    pks = tk.get_pitch_freq()
    pitch_freq = tk.get_pitch_freq()
    pitches = pitch_freq.keys()
    streak = 0
    first = True
      
    #for i in scale_root_names:
    #    print(i)
    #currently there are only heptatonic scales
    scale_choice =[i for i in range(len(sk.hept_dict))]
    descend = False  
    both = False
    best = 0
    play_style = ['[',']','=']
    first_commands = ['n', 'm!', 'p', 'q']
    while True:  
        
        if first:
            while True:
                sel = input('Play scale (p)  Return to main menu (m!)   Quit (q):')
                if sel not in first_commands:
                    continue
                else:
                    sel = sel.lower()
                    break
        sel = sel.strip()
        if sel.lower() == 'm!':
            return 'm!'
        if sel.lower() == 'q':
            print("You entered 'q'. Quitting program. Thanks for playing!\n\n")
            chimes.correct()
            exit(0)
        if sel.lower() == 'p' or sel.lower() == 'n':
            first = False
            rand_pitch = random.choice(scale_roots)
            while True:
                root = scale_roots.index(rand_pitch) 
                if root > len(scale_root_names) -13: 
                    rand_pitch = random.choice(scale_roots)
                else:
                    break
            #print(f'root = {root}')
            
            rand_scale = random.choice(scale_choice)
            rand_scale_degrees = sk.scale_degree_index[rand_scale]
            rand_scale_degrees_rev = rand_scale_degrees
            #print(f'random pitch: {rand_pitch!r}')
            #print(f'random number = {rand_scale}')
            #print(rand_scale_degrees)
            
            print("LISTEN CLOSELY...IMAGINE THE SCALE...")
            for i, key in enumerate(pks.keys()):
                if key in rand_pitch:
                    pitch = key 
                     
            while True: 
                sel = input('Play ascending ([)  or descending (]) or both (=) ? ')
                if sel.lower() == '[' or ']' or '=':
                    if sel == ']':
                        descend = True
                        both = False
                    elif sel == '[':
                        descend = False
                        both = False
                    elif sel == '=':
                        both = True
                        descend = False
                    break
                else:
                    print('oops...')
        if both:
            for i in rand_scale_degrees:
                #print(scale_root_names[root+i])
                #print(root+i)
                ps(scale_roots[root+i])
            for cnt, i in enumerate(reversed(rand_scale_degrees)):
                if rand_scale == 3 and cnt == 1:
                    ps(scale_roots[root+i-1])
                else:
                    #print(root+i)
                    ps(scale_roots[root+i])
                #print(scale_root_names[root+i])
        
        elif descend:
            for cnt, i in enumerate(reversed(rand_scale_degrees)):
                if rand_scale == 3 and cnt == 1:
                    ps(scale_roots[root+i-1])
                else:
                    #print(root+i)
                    ps(scale_roots[root+i])
                #print(scale_root_names[root+i])
        
        else:  
            for i in rand_scale_degrees:
                #print(scale_root_names[root+i])
                ps(scale_roots[root+i])
        
        menus.print_scale_choices()
        print()
        menus.print_scale_header()

        guessed = False
        while True:
            if sel.lower() == 'u':
                menus.print_scale_header()
            sel = input('\nEnter a command or guess. Type (?) for choices:')
            if sel.lower() == 'q':
                print("You entered 'q'. Quitting program. Thanks for playing!\n\n")
                chimes.correct()
                print(f'Your best streak: {best}') 
                print('And remember, "I don\'t particularly like modes a lot. ;)"')
                exit(0)
            elif sel.lower() == 'p':
                sel = '' 
                break
            elif sel.lower() == 'm!':
                break
            elif sel.lower() == 'u':
                guessed = True
                print('\nThe correct scale was:')
                if rand_scale == 3:
                    print('Melodic Minor')
                elif rand_scale == 2:
                    print('Harmonic Minor')
                else:
                    ans = [v for k,v in sk.scale_name_index.items() if 
                           sk.scale_degree_index[k] == rand_scale_degrees]
                    #print(ans)
                    if len(ans) == 1:
                        print(ans[0])
                print()
                continue
            elif sel.lower() == 'n' or sel in play_style:
                if sel == '[':
                    descend = both = False
                elif sel == ']':
                    descend = True
                    both = False
                elif sel == '=':
                    both = True
                    descend = False
                elif sel.lower == 'n':
                    guessed = False
                break
            elif sel == '?':
                menus.print_scale_choices()
                menus.print_scale_header()
            x = 0
            num = False
            for i in sel:
                x = ord(i)-48
                if x > 0 and x < 10:
                    num = True
            if num and int(sel) < len(sk.scale_degree_index) and int(sel) > 0:
                guess = int(sel)-1
                print('\nYou guessed:')
                print(sk.scale_name_index[guess])
                if sk.scale_degree_index[guess] == rand_scale_degrees:
                    chimes.correct()
                    print("Correct! \n\nnext (n) play again (p) ascend ( [ ) descend ( ] ) both ( = ) or menu (?)  \n")
                    if rand_scale == 3: 
                        print('This was actually a Melodic Minor! Did you catch it?')
                    if guessed == False: 
                       streak += 1
                       if streak > best:
                           best = streak
                       guessed = True
                else:
                   guessed = True
                   streak = 0
                   chimes.incorrect()
                   print("That's not correct. Try again.")
            else:
                print('invalid input!')
                continue
        print(f'Streak: {streak}')

