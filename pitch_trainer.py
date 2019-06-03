def run():
    
    import time
    import wave
    import os
    from playsound import playsound as ps
    import random
    import menus
    import toolkit as tk


    sines, sine_tones = tk.get_playback_set_pitches() 
    pitch_values = ['A_', 'As_Bb', 'B_', 'C_', 'Cs_Bb', 'D_', 'Ds_Eb', 'E_', 
                    'F_', 'Fs_Gb','G_', 'Gs_Ab' ]
    pitch_keys = ['a','s','b','c','v','d','r','e','f','t','g','x']
    print_pitches = ['A', 'A sharp B flat', 'B', 'C', 'C sharp D flat', 
                     'D', 'D sharp E flat', 'E', 'F', 'F sharp G flat', 'G', 'G Sharp A flat'] 

    pks = dict(zip(pitch_keys, pitch_values))
    print_pks = dict(zip(pitch_values, print_pitches))
   #print(pks)
    pitch_freq = tk.get_pitch_freq()
    pitches = pitch_freq.keys()
   #print(pitches)
    streak = 0
    first = True

    while True:  

        if first or sel.lower() != 'n':
            sel = input('Play tone (p) Quit (q):')
            sel = sel.lower()
        if sel.lower() == 'q':
            print("You entered 'q'. Quitting program. Thanks for playing!\n\n")
            exit(0)
        if sel.lower() == 'p' or 'n':
            first = False
            rand_pitch = random.choice(sine_tones)
            
            print("LISTEN CLOSELY...IMAGINE THE PITCH...")
            #print(f'random pitch: {rand_pitch!r}')
            for key in pks.values():
                if key in rand_pitch:
                    pitch = key
                    #print(f'pitch = {pitch}')
        ps(rand_pitch)
        menus.print_perfect_pitch_choices()
        print()
        menus.print_perfect_pitch_header()

        best = 0
        guessed = False
        while True:
            if sel.lower() == 'u':
                menus.print_perfect_pitch_header()
            sel = input('\nEnter a command or guess (\'?\' for commands):')
            if sel.lower() == 'q':
                print("You entered 'q'. Quitting program. Thanks for playing!\n\n")
                print(f'Your best streak: {best}') 
                exit(0)
            elif sel.lower() == 'p':
                ps(rand_pitch)
                continue
            elif sel.lower() == 'u':
                print('\nThe correct pitch was:')
                print(print_pks[pitch])
                print()
                continue
            elif sel.lower() == 'n':
                guessed = False
                break
            elif sel == '?':
                menus.print_perfect_pitch_choices()
                menus.print_perfect_pitch_header()
            if sel.lower() in pks.keys():
                print('\nYou guessed:')
                print(print_pks[pks[sel]])
                if pks[sel.lower()] == pitch:
                    print("Correct! \n\n(Type 'n', 'a', 'i', or \'?\')\n")
                    if guessed == False: 
                       streak += 1
                       if streak > best:
                           best = streak
                       guessed = True
                else:
                   guessed = True
                   streak = 0
                   print("That's not correct. Try again.")
            else:
                print('invalid input!')
                continue
        print(f'Streak: {streak}')
