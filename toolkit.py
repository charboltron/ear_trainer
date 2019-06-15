import numpy as np
import os 

#The toolkit is provided for the various modules to have access to 
#common functions and resources such as directory names, variable 
#values and dictionaries.

#Define parameters to make .wav files
num_samples = 44100
nframes = num_samples                                    #nframes is just the number of samples
sampling_rate = 44100.0 
amplitude = 16000                                        #fixed amplitude
comptype="NONE"                                          #compression type
compname="not compressed" 
nchannels=1
sampwidth=2                                              #2 bytes so 16-bit.

#print formatting functions for debugging
def pf(thing):
    thingStr = str(thing)
    print(thingStr, f' = {thing}, type = {type(thing)}')

def pfo(string, thing):
    print(string, f' = {thing}, type = {type(thing)}, len = {len(thing)}')

current_dir = os.getcwd()+'/'

wave_dirs = ['sine_waves/','square_waves/','triangle_waves/','saw_waves/']
wave_types = ['_sine_', '_square_', '_triangle_', '_saw_']


#shared functions
def choose_wave_type():
   
   '''
   Returns two strings for chosen waveform type and the directory containing 
   the .wav files for the chosen type
   '''
      
   sels = ['1','2','3','4']
   while True:
       sel = input('Choose your wave type: sine (1) square (2)  triangle (3)  saw (4)')
       sel = sel.strip()
       if sel in sels:
           sel = int(sel)-1
           wave_type = wave_types[sel]
           type_dir = current_dir+wave_dirs[sel]
           return wave_type, type_dir
       else:
           print('Invalid input.')

def get_all_waves_sine():
   
    '''
    Generates all 88 sine frequencies in the range of an 88-key piano based on 
    equal temperament. Returns a dictionary {str:[]} of pitches (str) to a list of all 
    samples for that that pitch
    '''
    print('getting sines') 
    #Reference frequency begins at 440Hz. Other frequencies based on this tone
    reference_frequency = 440.0
    all_waves = {}
    all_pitches = get_pitches() 

    #compute all the semitones in all piano octaves from A0 to C8 (88 keys)
    for semitone in range(-48, 40): 
        pitch = all_pitches[semitone+48]
        frequency = reference_frequency * (2 ** (semitone/12))
        sine_wave = [np.sin(2 * np.pi * frequency * t/(sampling_rate)) for t in range(num_samples)]
        all_waves[pitch] = sine_wave

    return all_waves

def get_all_waves_square():
    
    reference_frequency = 440.0
    all_waves = {}
    all_pitches = get_pitches() 
    print('getting squares')
    #compute all the semitones in all piano octaves from A0 to C8 (88 keys)
    for semitone in range(-48, 40): 
        pitch = all_pitches[semitone+48]
        frequency = reference_frequency * (2 ** (semitone/12))
        odd_harmonics = []
        print(odd_harmonics)
        for n in range(1,30):
            #add up samples at time points by odd harmonics in range
            sine_harmonic = [np.sin(((2*n)-1)* 2*np.pi * frequency * t/(sampling_rate))/(2*n) for t in range(num_samples)]
            odd_harmonics.append(sine_harmonic)
            sine_harmonic = []  
        square_wave = [0 for i in range(num_samples)]
        print(len(odd_harmonics))
        norm_const = 0.0
        for harmonic in odd_harmonics:
            for i in range(num_samples):
                square_wave[i] += harmonic[i]
                if square_wave[i] > norm_const:
                    norm_const = square_wave[i]
        print(f'norm const = {norm_const}')
        square_wave = [i*(4/np.pi)for i in square_wave]   #normalize amplitude  
        #print(square_wave)
        print(pitch)
        all_waves[pitch] = square_wave

    return all_waves

def get_all_waves_saw():
    
    reference_frequency = 440.0
    all_waves = {}
    all_pitches = get_pitches() 
    print('getting saws')
    #compute all the semitones in all piano octaves from A0 to C8 (88 keys)
    for semitone in range(-48, 40): 
        pitch = all_pitches[semitone+48]
        frequency = reference_frequency * (2 ** (semitone/12))
        even_harmonics = []
        for n in range(1,30):
            #add up samples at time points by even harmonics in range
            sine_harmonic = [np.sin((n* 2*np.pi) * frequency * t/(sampling_rate))/(2*n) for t in range(num_samples)]
            even_harmonics.append(sine_harmonic)
            sine_harmonic = []  
        saw_wave = [0 for i in range(num_samples)]
        print(len(even_harmonics))
        norm_const = 0.0
        for harmonic in even_harmonics:
            for i in range(num_samples):
                saw_wave[i] += harmonic[i]
                if saw_wave[i] > norm_const:
                    norm_const = saw_wave[i]
        print(f'norm const = {norm_const}')
        #normalize amplitude 4/pi is overestimation, should be 3.489/pi but it works 
        saw_wave = [i*(4/np.pi)for i in saw_wave]   
        #print(saw_wave)
        #print(pitch)
        all_waves[pitch] = saw_wave
    
    return all_waves

def get_all_waves_triangle():
    
    reference_frequency = 440.0
    all_waves = {}
    all_pitches = get_pitches() 
    print('getting triangles')
    #compute all the semitones in all piano octaves from A0 to C8 (88 keys)
    for semitone in range(-48, 40): 
        pitch = all_pitches[semitone+48]
        frequency = reference_frequency * (2 ** (semitone/12))
        odd_harmonics = []
        for n in range(1,30):
            #add up samples at time points by odd harmonics in range
            sine_harmonic = [(np.sin(((2*n)-1) * 2*np.pi * frequency * t/(sampling_rate))/
                             (((2*n)-1)**2)) *((-1)**n)  for t in range(num_samples)]
            odd_harmonics.append(sine_harmonic)
            sine_harmonic = []  
        tri_wave = [0 for i in range(num_samples)]
        print(len(odd_harmonics))
        norm_const = 0.0
        for harmonic in odd_harmonics:
            for i in range(num_samples):
                tri_wave[i] += harmonic[i]
                if tri_wave[i] > norm_const:
                    norm_const = tri_wave[i]
        print(f'norm const = {norm_const}')
        tri_wave = [i/1.2254 for i in tri_wave]   #normalize amplitude 
        #print(tri_wave)
        #print(pitch)
        all_waves[pitch] = tri_wave
    
    return all_waves
    
def get_pitches():
   
    '''
    Returns a (str) list of the 88 pitches in file-save format for writing files.
    Each new octave appends the corresponding octave number to the str (eg. 'G_3').
    file_handler.create_file_names appends a serial number to each as well as a wave_type 
    '''

    pitches = ['A', 'As_Bb', 'B', 'C', 'Cs_Db', 'D', 'Ds_Eb', 'E', 'F', 'Fs_Gb', 'G', 'Gs_Ab']
    octave_count = 0
    tone_count = 0
    all_pitches = []
    octave_count = 0
    tone_count = 0

    for semitone in range(-48, 40): 
        pitch = pitches[semitone % 12]+'_'+str(octave_count) #append octave number
        all_pitches.append(pitch)
        tone_count += 1
        #increment octave number
        if (tone_count -3) % 12 == 0:
            octave_count += 1

    return all_pitches

def get_all_waves_pitches(wave_type):
    
    '''
    Returns two dictionaries, all_waves: {str:[]} a dict of pitch strings to sample lists, 
    and all_waves_pitches: {int:str} a dict of integer indices to the pitches (e.g. 
    {0: 'A_0', 1: 'As_Bb_0', 2: 'B_0'...}) 
    '''   
    if wave_type == '_sine_':
        all_waves = get_all_waves_sine()
    elif wave_type == '_square_':
        all_waves = get_all_waves_square()
    elif wave_type == '_triangle_':
        all_waves = get_all_waves_triangle()
    elif wave_type == '_saw_':
        all_waves = get_all_waves_saw()
    all_waves_pitches = {}
    for i, pitch in enumerate(all_waves.keys()):
        all_waves_pitches[i] = pitch
    
    return all_waves, all_waves_pitches

def get_pitch_freq():
   
    '''
    Returns a dict of pitch names and corresponding frequencies (e.g. {'A_0': 27.5, 
    'As_Bb_0': 29.13523509488062, 'B_0': 30.86770632850775, 'C_1':...}) 
    '''
    reference_frequency = 440.0
    pitch_freq = {} 
    pitches = ['A', 'As_Bb', 'B', 'C', 'Cs_Db', 'D', 'Ds_Eb', 'E', 'F', 'Fs_Gb', 'G', 'Gs_Ab']
    octave_count = 0
    tone_count = 0
   
    for semitone in range(-48, 40): 
        
        frequency = reference_frequency * (2 ** (semitone/12))
        pitch = pitches[semitone % 12]+'_'+str(octave_count) #append octave number
        pitch_freq[pitch] = frequency
        tone_count += 1
        #increment octave number
        if (tone_count -3) % 12 == 0:
            octave_count += 1

    return  pitch_freq  

def get_playback_set_pitches():
    
    '''
    Returns a list of tone files for the pitch_trainer to play back based 
    on selected wave type
    '''
    wave_type, type_dir = choose_wave_type()
    type_dir = type_dir+'all_tones/'
    waves = [file for file in os.listdir(type_dir) if '.wav' in file]
    waves.sort()
    wave_tones = []
    for tone in range(0, len(waves)):
      wave_tone = type_dir+waves[tone]
      wave_tones.append(str(wave_tone))

    return wave_tones

def get_playback_set_intervals():
    
    '''
    Returns a list of interval tone files for the interval_trainer to play back
    based on selected wave type
    '''
    wave_type, type_dir = choose_wave_type()
    interval_dir = type_dir+'intervals/'
    interval_names = []
    intervals = []
    for file in os.listdir(interval_dir):
        if '.wav' in file:
            intervals.append((interval_dir+file))
            interval_names.append(str(file))
    intervals.sort()
    interval_names.sort()

    #prepare all wave files for playback, dft
    waves = [file for file in os.listdir(type_dir+'all_tones/') if '.wav' in file]
    waves.sort()
    wave_tones = []
    for tone in range(0, len(waves)):
      wave_tone = type_dir+'all_tones/'+waves[tone]
      wave_tones.append(wave_tone)

    return wave_tones, intervals, interval_names

def get_playback_set_chords():
    
    '''
    Returns a list of chord tone files for the chord_trainer to play back
    based on selected wave type
    '''
    wave_type, type_dir = choose_wave_type()
    chord_dir = type_dir+'chords/'
    chord_names = []
    chords = []
    for file in os.listdir(chord_dir):
        if '.wav' in file:
            chords.append((chord_dir+file))
            chord_names.append(str(file))
    chords.sort()
    chord_names.sort()

    #prepare all wave files for playback, dft
    waves = [file for file in os.listdir(type_dir+'all_tones/') if '.wav' in file]
    waves.sort()
    wave_tones = []
    for tone in range(0, len(waves)):
      wave_tone = type_dir+'all_tones/'+waves[tone]
      wave_tones.append(wave_tone)

    return wave_tones, chords, chord_names


def get_playback_set_scales():
    
    '''
    Returns a list of scale tone files for the scale_trainer to play back
    based on selected wave type
    '''
    wave_type, type_dir = choose_wave_type()
    scale_dir = type_dir+'scales/'
    scale_roots = []
    scale_root_names = []
    for file in os.listdir(scale_dir):
        if '.wav' in file:
            scale_roots.append((scale_dir+file))
            scale_root_names.append(str(file))
    scale_roots.sort()
    scale_root_names.sort()

    #prepare all wave files for playback, dft
    waves = [file for file in os.listdir(type_dir+'all_tones/') if '.wav' in file]
    waves.sort()
    wave_tones = []
    for tone in range(0, len(waves)):
      wave_tone = type_dir+'all_tones/'+waves[tone]
      wave_tones.append(wave_tone)

    return waves, wave_tones, scale_roots, scale_root_names
   
def get_pitch_print_dict():

    '''
    Returns a dictionary of pitch strings formatted for file saving to pitch
    strings formatted for printing to the screen
    '''
    pitch_values =  ['A_', 'As_Bb_', 'B_', 'C_', 'Cs_Db_', 'D_', 'Ds_Eb_', 'E_', 
                     'F_', 'Fs_Gb_','G_', 'Gs_Ab_' ]
    print_pitches = ['A', 'A sharp B flat', 'B', 'C', 'C sharp D flat', 
                     'D', 'D sharp E flat', 'E', 'F', 'F sharp G flat', 'G', 'G Sharp A flat'] 
    print_pks = dict(zip(pitch_values, print_pitches))
    return print_pks  
