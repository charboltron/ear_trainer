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

def get_playback_set_intervals():
    
    current_dir = '/Users/charlesbolton/Desktop/510_Music/sound_project/'
    sine_dir = current_dir+'sine_waves/'
    interval_dir = sine_dir+'intervals/'
    sine_tone_dir = sine_dir+'all_tones/'
    
    interval_names = []
    intervals = []
    for file in os.listdir(interval_dir):
        if '.wav' in file:
            intervals.append((interval_dir+file))
            interval_names.append(str(file))
    intervals.sort()
    interval_names.sort()

    #prepare all sine files for playback
    sines = [file for file in os.listdir(sine_tone_dir) if '.wav' in file]
    sines.sort()
    sine_tones = []
    for tone in range(0, len(sines)):
      sine_tone = sine_tone_dir+sines[tone]
      sine_tones.append(sine_tone)

    return sines, sine_tones, intervals, interval_names

def get_playback_set_pitches():
    
    current_dir = '/Users/charlesbolton/Desktop/510_Music/sound_project/'
    sine_dir = current_dir+'sine_waves/'
    sine_tone_dir = sine_dir+'all_tones/'
      
    sines = [file for file in os.listdir(sine_tone_dir) if '.wav' in file]
    sines.sort()
    sine_tones = []
    for tone in range(0, len(sines)):
      sine_tone = sine_tone_dir+sines[tone]
      sine_tones.append(str(sine_tone))

    return sines, sine_tones

      

