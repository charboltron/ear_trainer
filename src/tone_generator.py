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
from chord_generator import generate_chords
import dft
import toolkit as tk

"""
This program generates the 88 sine tones typically found on in the range of frequencies 
on a piano. It does this by starting with a reference 440Hz and generating all the other 
sine tones based off of the mathematics of equal temperament.
"""

current_dir = tk.current_dir

def generate_tones():
    
    '''
    Test function to see if samples are being created correctly 
    save_tones is used for generatoion and saving files
    '''
    wave_type, wave_dir = tk.choose_wave_type()
    max = 0.0
    if wave_type == '_sine_':
        all_waves = tk.get_all_waves_sine()  
    elif wave_type == '_square_':
        all_waves = tk. get_all_waves_square()
    elif wave_type == '_saw_':
        all_waves = tk. get_all_waves_saw()
    elif wave_type == '_triangle_':
        all_waves = tk. get_all_waves_triangle()
    #print(all_waves['A_4'])
    for w in all_waves['A_4']:
        if w > max:
             max = w
    print(all_waves.keys())
    print(f'max = {max}')

def save_tones():
    
    '''
    save tone files and write to a folder
    '''
    wave_type, type_dir = tk.choose_wave_type()
    all_pitches = tk.get_pitches()
    if wave_type == '_sine_':
        all_waves = tk.get_all_waves_sine()
    elif wave_type == '_square_':
        all_waves = tk.get_all_waves_square()
    elif wave_type == '_saw_':
        all_waves = tk.get_all_waves_saw()
    elif wave_type == '_triangle_': 
        all_waves = tk.get_all_waves_triangle()
    tone_path = type_dir+'all_tones/test/' #send to test dir first
    tone_dict = file_handler.create_file_names(wave_type, all_pitches)
    file_handler.write_wav_files(current_dir, tone_path, tone_dict, all_waves)
    #file_handler.move_files(current_dir, tone_path)
#----------------------------------------------------------------------------------------

def generate_interval_tones(low,high):
    
    '''
    generates the intervals and stores them in
    the proper directory using interval_generator and file_handler
    '''

    wave_type, type_dir = tk.choose_wave_type()

    print(type_dir)
    if (high-low < 13) or (high > 74) or (low < 0):
        print("Range Error: You must enter a range of at least 12 to create intervals")
        print("Also, you must only enter numbers in the range of 0-74")
        exit(0)
    all_waves, all_waves_pitches = tk.get_all_waves_pitches(wave_type)
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
   
    generate_intervals(interval_subset, interval_index, high, high-low, wave_type, type_dir)
#-------------------------------------------------------------------------------------

def generate_chord_tones(low,high):
    
    '''
    generates the chords and stores them in
    the proper directory using chord_generator and file_handler
    '''
   
    wave_type, type_dir  = tk.choose_wave_type()
    if (high-low < 22) or (high > 65 ) or (low < 0):
        print("Range Error: You must enter a range of at least 23 to create chords")
        print("Also, you must only enter numbers in the range of 0-74")
        exit(0)
    all_waves, all_waves_pitches = tk.get_all_waves_pitches(wave_type)
    chord_subset = {}
    chord_index = []
    
    for i in range(low,high+23):
        p = all_waves_pitches[i]
        chord_subset[p] = all_waves[p]
        chord_index.append(p)
    
    generate_chords(chord_subset, chord_index, high, high-low, wave_type, type_dir)

#---------------------------------------------------------------------------------------
