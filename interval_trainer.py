#'interval_trainer.py'
def run():

    '''
    Runs the menu-based game format for the interval 
    trainer
    '''
    import time
    import wave
    import os
    from playsound import playsound as ps
    import random
    import menus
    import dft
    import toolkit as tk
    import chimes


    interval_choice_dict = {}
    icd = interval_choice_dict
    interval_choices = ['Minor Second', 'Major Second', 'Minor Third', 'Major Third',
                        'Perfect Fourth', 'Tritone', 'Perfect Fifth', 'Minor Sixth',
                        'Major Sixth', 'Minor Seventh', 'Major Seventh', 'Octave']

    x = [i for i in range(1, 13)]
    icd = dict(zip(x, interval_choices))

    answer_key = {}
    answers = ['@', '2', '#','3', '4', '$','5', '^', '6', '&', '7', '8']
    answer_key  = dict(zip(answers, interval_choices))

   #print(icd)
   #print(answer_key)

    wave_tones, intervals, interval_names = tk.get_playback_set_intervals() 
    pitch_freq = tk.get_pitch_freq()
    streak = 0
    first = True
    while True:  

        if first or sel.lower() != 'n':
            sel = input('Play interval (p)  Return to main menu (m!)   Quit (q):')
            sel = sel.lower()
        if sel.lower() == 'm!':
            return 'm!'
        if sel == 'q':
            chimes.correct()
            print("You entered 'q'. Quitting program. Thanks for playing!\n\n")
            exit(0)
        if sel == 'p' or 'n':
            first = False
            rand_interval = random.choice(intervals)
            print("LISTEN CLOSELY...IMAGINE THE INTERVAL...")
            #print(f'random interval: {rand_interval!r}') 
        wavfile = wave.open(rand_interval, 'rb')
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
        ps(rand_interval)
        print("DFT considering interval...")
        menus.print_interval_choices()
        menus.print_interval_header()
        composite_pitches, interv = dft.dft(tk.num_samples, samples, pitch_freq, 0, 'interval')
        #print(interv)
        #print(icd[interv])
        
        best = 0
        guessed = False
        while True:
            if sel == 'u':
                menus.print_interval_header()
            sel = input('\nEnter a command or guess (type (?) for commands):')
            if sel == 'q':
                print("You entered 'q'. Quitting program. Thanks for playing!\n\n")
                print(f'Your best streak: {best}') 
                exit(0)
            elif sel.lower() == 'p':
                ps(rand_interval)
                continue
            elif sel.lower() == 'm!':
                break
            elif sel.lower() == 'i':
                for p in composite_pitches:    
                    for i, s in enumerate(wave_tones): 
                        if p in s:
                            ps(wave_tones[i])
                            time.sleep(1)
            elif sel.lower() == 'u':
                guessed = True
                print('\nThe correct interval was:')
                print(icd[interv])
                print()
            elif sel.lower() == 'n':
                guessed = False
                break
            elif sel == '?':
                menus.print_interval_choices()
                menus.print_interval_header()
            elif sel in answers:
                print('\nYou guessed:')
                print(answer_key[sel])
                if (icd[interv] == answer_key[sel]):
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
 
