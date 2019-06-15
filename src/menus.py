
'''
All the menus for each of the sub-games in the tone trainer
'''

def title():

   print("\nCopyright ©  Charles Bolton, 2019\n") 
   print("+---------------------------------------+")
   print("|                                       |")
   print("|  WELCOME  TO  THE   TONE  TRAINER!    |")
   print("|                                       |")
   print("+---------------------------------------+")

def print_play_menu():
    
   print('Choose your challenge!')
   print()
   print('To train pitch:.......: (1)')
   print('To train intervals....: (2)')
   print('To train chords.......: (3)')
   print('To train scales.......: (4)')
   print('To quit...............: (q)')

def print_perfect_pitch_header():
      
   print('Play pitch again.......: (p)')
   print('Give up:...............: (u)')
   print('Next pitch:............: (n)')
   print('Menu:..................: (m!)')
   print('Guess the pitch by typing corresponding key: ')

def print_perfect_pitch_choices():

   print("Enter the key following the pitch to guess...")
   print()
   print('A......................: (a)')
   print('A#/Bb..................: (s)')
   print('B......................: (b)')
   print('C......................: (c)')
   print('C#/Db..................: (v)')
   print('D......................: (d)')
   print('D#/Eb..................: (r)')
   print('E......................: (e)')
   print('F......................: (f)')
   print('F#/Gb..................: (t)')
   print('G......................: (g)')
   print('G#/Ab..................: (x)')
   
def print_interval_choices():
   
   print("Enter the key following the interval to guess...")
   print()
   print("Minor 2nd   :.............................(@)")
   print("Major 2nd   :.............................(2)")
   print("Minor 3rd   :.............................(#)")
   print("Major 3rd   :.............................(3)")
   print("Perfect 4th :.............................(4)")
   print("Tritone     :.............................($)")
   print("Perfect 5th :.............................(5)")
   print("Minor 6th   :.............................(^)")
   print("Major 6th   :.............................(6)")
   print("Minor 7th   :.............................(&)")
   print("Major 7th   :.............................(7)")
   print("Octave      :.............................(8)")

def print_interval_header():

    print('Play composite again:  (p)')
    print('Play individual notes: (i)')
    print('Give up:               (u)')
    print('Next interval:         (n)')
    print('Menu:                  (m!)')
    print('Guess the interval by typing corresponding key: ')

def print_chord_header():

    print('Play composite again:           (p)')
    print('Play individual notes:          (i)')
    print('Give up:                        (u)')
    print('Next chord:                     (n)')
    print('Menu:                           (m!)')
    print('Guess the chord by typing corresponding key: ')

def print_chord_title():

   print('In the chord trainer there are three modes:', 
         '\nEasy mode: basic triads (Major, Minor, Augmented, Diminished, Suspended)',
         '\nIntermediate mode: triads and sevenths',
         '\nHard mode: triads, sevenths, and inversions\n')

def print_chord_choices_easy():
   
   print('Enter the key following the chord to guess...',
        '\nMajor         :............(1)',
        '\nMinor         :............(2)',
        '\nAugmented     :............(3)',
        '\nDiminished    :............(4)',
        '\nSuspend Two   :............(5)',
        '\nSuspended Four:............(6)')
         
def print_chord_choices_intermediate():

   print('Enter the key following the chord to guess...',
        '\nMajor                  :...(1)',
        '\nMinor                  :...(2)',
        '\nAugmented              :...(3)',
        '\nDiminished             :...(4)',
        '\nSuspend Two            :...(5)',
        '\nSuspended Four         :...(6)',
        '\nDominant seven         :...(7)',
        '\nMajor Seven            :...(8)',
        '\nMinor Seven            :...(9)',
        '\nMinor Major Seven      :...(10)', 
        '\nDiminished Seven       :...(11)',
        '\nDiminished Major Seven :...(12)',
        '\nHalf Diminished Seven  :...(13)',
        '\nAugmented Seven        :...(14)',
        '\nAugmented Major Seven  :...(15)')

def print_chord_choices_hard():

   print('Enter the key following the chord to guess...'
        '\nMajor                  (1)     Augmented 1st Inversion          (20)     Diminished Major Seven 1st Inversion (38)',
        '\nMinor                  (2)     Augmented 2nd Inversion          (21)     Diminished Major Seven 2nd Inversion (39)',
        '\nAugmented              (3)     Suspended Two 1st Inversion      (22)     Diminished Major Seven 3rd Inversion (40)',
        '\nDiminished             (4)     Suspended Two 2nd Inversion      (23)     Augmented Seven 1st Inversion        (41)',
        '\nSuspend Two            (5)     Suspended Four 1st Inversion     (24)     Augmented Seven 2nd Inversion        (42)',
        '\nSuspended Four         (6)     Suspended Four 2nd Inversion     (25)     Augmented Seven 3rd Inversion        (43)',
        '\nDominant seven         (7)     Dominant Seven 1st Inversion     (26)     Augmented Major Seven 1st Inversion  (44)',
        '\nMajor Seven            (8)     Dominant Seven 2nd Inversion     (27)     Augmented Major Seven 2nd Inversion  (45)',
        '\nMinor Seven            (9)     Dominant Seven 3rd Inversion     (28)     Augmented Major Seven 3rd Inversion  (46)',
        '\nMinor Major Seven      (10)    Major Seven 1st Inversion        (29)',
        '\nDiminished Seven       (11)    Major Seven 2nd Inversion        (30)',
        '\nDiminished Major Seven (12)    Major Seven 3rd Inversion        (31)',
        '\nHalf Diminished Seven  (13)    Minor Seven 1st Inversion        (32)',
        '\nAugmented Seven        (14)    Minor Seven 2nd Inversion        (33)',
        '\nAugmented Major Seven  (15)    Minor Seven 3rd Inversion        (34)',
        '\nMajor 1st Inversion    (16)    Minor Major Seven 1st Inversion  (35)',
        '\nMajor 2nd Inversion    (17)    Minor Major Seven 2nd Inversion  (36)',
        '\nMinor 1st Inversion    (18)    Minor Major Seven 3rd Inversion  (37)',
        '\nMinor 2nd Inversion    (19)')

def print_scale_header():
    
    print('Play again:              (p)')
    print('Play ascending scale:    ([)')
    print('Play descending scale:   (])')
    print('Play both:               (=)')
    print('Give up:                 (u)')
    print('Next scale:              (n)')
    print('Menu:                    (m!)')

def print_scale_choices():

   print('Enter the key following the scale to guess...'
        '\nMajor (Ionian)             (1)',
        '\nNatural  Minor (Aeolian)   (2)', 
        '\nHarmonic Minor             (3)',
        '\nMelodic  Minor             (4)',
        '\nDorian                     (5)',
        '\nLydian                     (6)',
        '\nPhrygian                   (7)',
        '\nMixolydian                 (8)',
        '\nLocrian                    (9)'
        )



