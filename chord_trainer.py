#'chord_trainer.py'
def run():

    import chordkit as ck
    import time
    import wave
    import os
    from playsound import playsound as ps
    import random
    import menus
    import dft
    import toolkit as tk
    import chimes

    menus.print_chord_title()
    
    easy = intermediate = hard = False
    best = 0
    while True:
        mode = input('Choose difficulty: easy (1), intermediate (2), or hard (3)')
        mode = mode.strip()
        if mode == '1': 
            mode_menu = menus.print_chord_choices_easy
            mode_book = ck.easy_mode_book
            answers = [i for i in range(1, 7)]
            easy = True
            break
        elif mode == '2':
            mode_menu = menus.print_chord_choices_intermediate
            mode_book = ck.intermediate_mode_book
            answers = [i for i in range(1, 16)]
            intermediate = True
            break
        elif mode == '3':
            mode_menu = menus.print_chord_choices_hard
            mode_book = ck.hard_mode_book
            answers = [i for i in range(1, 47)]
            Hard = True
            break
        else: 
            print('Invalid input.')
            continue
   
    answer_key = {}
    #print(len(mode_book))
    for i, chord in enumerate(mode_book.items()):
        if i <= len(mode_book):
            pass
            #print(chord)
            #print(answers[i])
        else:
            break
    
    answer_key  = dict(zip(answers, mode_book.keys()))
    for ans in answer_key.items():
        pass
        #print(ans)

    #print(mode_book)
    #print(answer_key)
    pitch_print_dict = tk.get_pitch_print_dict()
    wave_tones, chords, chord_names = tk.get_playback_set_chords() 
    pitch_freq = tk.get_pitch_freq()
    streak = 0
    first = True
    while True:  

        #get user input, generate random chord 
        if first or sel.lower() != 'n':
            sel = input('Play chord (p)  Return to main menu (m!)   Quit (q):')
            sel = sel.lower()
        if sel.lower() == 'm!':
            return 'm!'
        if sel == 'q':
            chimes.correct()
            print("You entered 'q'. Quitting program. Thanks for playing!\n\n")
            exit(0)
        if sel == 'p' or sel.lower() == 'n':
            first = False
            if easy:
                chords = [chord for chord in chords if 'seven' not in chord]
                chords = [chord for chord in chords if 'inversion' not in chord]
            elif intermediate:
                chords = [chord for chord in chords if 'inversion' not in chord]
            rand_chord = random.choice(chords)
            print("LISTEN CLOSELY...IMAGINE THE CHORD...")
            #print(f'random chord: {rand_chord!r}') 
        
        #prepare wave file for dft
        wavfile = wave.open(rand_chord, 'rb')
        channels = wavfile.getnchannels()
        width = wavfile.getsampwidth()
        rate = wavfile.getframerate()
        frames = wavfile.getnframes()
        wave_bytes = wavfile.readframes(frames)
        frame_width = width * channels
        samples = []
        for f in range(0, len(wave_bytes), frame_width):
            frame = wave_bytes[f : f + frame_width]
            for c in range(0, len(frame), width):
                sample_bytes = frame[c : c + width]
                sample = int.from_bytes(sample_bytes, byteorder='little',signed=(width>1))
                sample = float(sample)/16000 
                samples.append(sample)
        #play chord
        ps(rand_chord)
        print("DFT considering chord...")
        mode_menu()
        print()
        menus.print_chord_header()
        composite_pitches, chord_intervals = dft.dft(tk.num_samples, samples, pitch_freq, 0, 'chord')
        #print(chord_intervals)
       
        sus = False
        correct_sus = []
        first_chord = True
        for chord_name_key, chord_vals in mode_book.items():
            if chord_vals == chord_intervals:
               if first_chord:
                  #print(chord_name_key)
                  answer_string = chord_name_key 
                  #print(mode_book[chord_name_key])
                  correct_sus.append(answer_string)
                  first_chord = False
               else:
                  correct_sus.append(chord_name_key)
                  sus = True
        
        l = len(composite_pitches)-1
        if 'First' in answer_string:
            correct_chord = composite_pitches[l]
        elif 'Second' in answer_string:
            correct_chord = composite_pitches[l-1]
        elif 'Third' in answer_string:
            correct_chord = composite_pitches[l-2] 
        else:
            correct_chord = composite_pitches[0]
        for pitch, print_pitch in pitch_print_dict.items():
            if pitch in correct_chord:
                correct_chord = print_pitch+' '+answer_string
        guessed = False
        while True:
            if sel == 'u':
                guessed = True
                menus.print_chord_header()
            sel = input('\nEnter a command or guess (type (?) for commands):')
            if sel == 'q':
                print("You entered 'q'. Quitting program. Thanks for playing!\n\n")
                chimes.correct()
                print(f'Your best streak: {best}') 
                exit(0)
            elif sel.lower() == 'p':
                ps(rand_chord)
                continue
            elif sel.lower() == 'i':
                for p in composite_pitches:    
                    for i, s in enumerate(wave_tones): 
                        if p in s:
                            ps(wave_tones[i])
                            time.sleep(1)
                continue
            elif sel.lower() == 'u':
                if sus and len(correct_sus) > 1:
                     
                    print('Inversions of augmented or suspended chords are the same intervals out of context!')
                    print('Correct chords: ')
                    for sus_chord in correct_sus:
                        print(sus_chord)
                    print()
                else:
                    print('\nThe correct chord was:')
                    print(correct_chord)
                    print('Pitches:')
                    pps = [p[:-1] for p in composite_pitches]
                    for p in pps:
                        print(pitch_print_dict[p])
                    print()
                continue  
            elif sel.lower() == 'm!':
                break
            elif sel.lower() == 'n':
                guessed = False
                break
            elif sel == '?':
                mode_menu()
                print()
                menus.print_chord_header()
            x = 0
            num = False
            for i in sel:
                x = ord(i)-48
                if x > 0 and x < 10:
                    num = True
            if num and  int(sel) < (len(answers)+1) and int(sel) > 0: #and sel != '0':
                guess = int(sel)
                print('\nYou guessed:')
                print(answer_key[guess])
                if sus and len(correct_sus) > 1:
                    correct = False
                    for ans in correct_sus:
                        if (answer_key[guess] == answer_string):
                           correct = True
                    if correct:       
                        chimes.correct()
                        print("Correct! \n\nnext (n) play (p) individual notes(i)\n")
                #print(mode_book[answer_string])
                elif (answer_key[guess] == answer_string):
                    chimes.correct()
                    print("Correct! \n\nnext (n) play (p) individual notes(i)\n")
                    if guessed == False: 
                        streak += 1
                        if streak > best:
                            best = streak
                        guessed = True
                else:
                    guessed = True
                    streak = 0
                    chimes.incorrect()
                    print("Try again.")
            else:
                print('invalid input!')
                continue    
        print(f'Streak: {streak}')
 
