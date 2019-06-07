import numpy as np
import os 

#Define parameters to make .wav files
num_samples = 44100
nframes = num_samples                                    #nframes is just the number of samples
sampling_rate = 44100.0 
amplitude = 16000                                        #fixed amplitude
comptype="NONE"                                          #compression type
compname="not compressed" 
nchannels=1
sampwidth=2                                              #2 bytes so 16-bit.


def pf(thing):
    thingStr = str(thing)
    print(thingStr, f' = {thing}, type = {type(thing)}')

def pfo(string, thing):
    print(string, f' = {thing}, type = {type(thing)}, len = {len(thing)}')

current_dir = '/Users/charlesbolton/Desktop/510_Music/sound_project/ear_trainer/'
wave_dirs = ['sine_waves/','square_waves/','triangle_waves/','saw_waves/']
wave_types = ['_sine_', '_square_', '_triangle_', '_saw_']

def choose_wave_type():

   sels = ['1','2','3','4']
   while True:
       sel = input('Choose your wave type: sine (1) square (2)  triangle (3)  saw (3)')
       sel = sel.strip()
       if sel in sels:
           sel = int(sel)-1
           wave_type = wave_types[sel]
           type_dir = current_dir+wave_dirs[sel]
           return wave_type, type_dir
       else:
           print('Invalid input.')

def get_all_waves_sin():
    
    #Reference frequency begins at 440Hz. Other frequencies based on this tone
    reference_frequency = 440.0
    all_waves = {}
    all_pitches = get_pitches() 

    #compute all the semitones in all piano octaves from A0 to C8 (88 keys)
    for semitone in range(-48, 40): 
        pitch = all_pitches[semitone+48]
        frequency = reference_frequency * (2 ** (semitone/12))
        sine_wave = [np.sin(2 * np.pi * frequency * x/(sampling_rate)) for x in range(num_samples)]
        all_waves[pitch] = sine_wave

    return all_waves

def get_pitches():
    
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

def get_all_waves_pitches():
   
    all_waves = get_all_waves_sin()
    all_waves_pitches = {}
    for i, pitch in enumerate(all_waves.keys()):
        all_waves_pitches[i] = pitch
    
    return all_waves, all_waves_pitches

def get_pitch_freq():
   
    #returns a dict of pitch names and corresponding frequencies
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

    pitch_values =  ['A_', 'As_Bb_', 'B_', 'C_', 'Cs_Bb_', 'D_', 'Ds_Eb_', 'E_', 
                     'F_', 'Fs_Gb_','G_', 'Gs_Ab_' ]
    print_pitches = ['A', 'A sharp B flat', 'B', 'C', 'C sharp D flat', 
                     'D', 'D sharp E flat', 'E', 'F', 'F sharp G flat', 'G', 'G Sharp A flat'] 
    print_pks = dict(zip(pitch_values, print_pitches))
    return print_pks  
