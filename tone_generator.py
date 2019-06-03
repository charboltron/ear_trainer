#'tone generator'
#Copyright Charles Bolton, 2019

import os
import shutil
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
from playsound import playsound as ps
import time
import file_handler
from interval_generator import generate_intervals
import dft
import toolkit as tk

"""
This program generates the 88 sine tones typically found on in the range of frequencies 
on a piano. It does this by starting with a reference 440Hz and generating all the other 
sine tones based off of the mathematics of equal temperament.
"""

current_dir = '/Users/charlesbolton/Desktop/510_Music/sound_project/'

def generate_tones():
    
    #Reference frequency begins at 440Hz. Other frequencies based on this tone
    reference_frequency = 440.0
    pitch_freq = {} 
    pitches = ['A', 'As_Bb', 'B', 'C', 'Cs_Db', 'D', 'Ds_Eb', 'E', 'F', 'Fs_Gb', 'G', 'Gs_Ab']
    octave_count = 0
    tone_count = 0
    all_waves = {}
    all_pitches = []

    #compute all the semitones in all piano octaves from A0 to C8 (88 keys)
    for semitone in range(-48, 40): 
        #compute base value for frequency of each semitone from 440Hz reference 
        frequency = reference_frequency * (2 ** (semitone/12))
        #append semitone base frequency to dictionary of pitch/frequency pairs 
        pitch = pitches[semitone % 12]+'_'+str(octave_count) #append octave number
        all_pitches.append(pitch)
        pitch_freq[pitch] = frequency
        #Create a 1-second sine wave of 44.1kHz samples for each frequency
        sine_wave = [np.sin(2 * np.pi * frequency * x/(tk.sampling_rate)) for x in range(tk.num_samples)]
        all_waves[pitch] = sine_wave
        tone_count += 1
        #increment octave number
        if (tone_count -3) % 12 == 0:
            octave_count += 1
    #print(all_waves.keys())

    #for j, k in pitch_freq.items():
    #    print(j,k)

    all_waves_pitches = {}
    for i, pitch in enumerate(all_waves.keys()):
        all_waves_pitches[i] = pitch
    #print(all_waves_pitches)

def save_sine_tones():
    
    '''
    create sine tone files and write to a folder
    '''
    all_pitches = tk.get_pitches()
    all_waves = tk.get_all_waves_sin()
    sine_path = current_dir+'sine_waves/all_tones_test/'
    sine_dict = file_handler.create_file_names('_sine_', all_pitches)
    file_handler.write_wav_files(current_dir, sine_path, sine_dict, all_waves)
    file_handler.move_files(current_dir, sine_path)
#----------------------------------------------------------------------------------------

def generate_interval_tones(low,high):
    
    '''
    generates the intervals and stores them in
    the proper directory using interval_generator and file_handler
    '''

    if (high-low < 13) or (high > 74) or (low < 0):
        print("Range Error: You must enter a range of at least 12 to create intervals")
        print("Also, you must only enter numbers in the range of 0-87")
        exit(0)
    all_waves, all_waves_pitches = tk.get_all_waves_pitches()
    interval_subset = {}
    interval_index = []
    
    #print(all_waves_pitches[45])
    #low = 27
    #high = 76
    
    for i in range(low,high):
        p = all_waves_pitches[i]
        interval_subset[p] = all_waves[p]
        interval_index.append(p)

    #print(interval_subset.keys())
    #print(interval_index)
    #print(len(interval_index))
    #print(interval_subset['C_4'])
   
    generate_intervals(interval_subset, interval_index, high, high-low)
#-------------------------------------------------------------------------------------

