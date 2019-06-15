# 'chord_generator.py'
from   playsound import playsound as ps
import os
import shutil
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
import dft
import time
import file_handler
import toolkit as tk 
import copy
import chordkit as ck

current_dir = tk.current_dir

#for chord in ck.hard_mode_book.items():
#    print(chord)

ref = 440.0
chord_names = []
chord_freq = {}

def generate_chords(waves, index, t_last, t_range, wave_type, type_dir):
    
    '''
    Generates chord files. Called from tone_generator, it takes 
    a dictionary waves, a range of keys for makingchords, a value indicating the last 
    tonic considered, an index of the chords considered, and a wave type
    '''
    chord_path = type_dir+'/chords/test/'
    print(f'Last tonic: {t_last}') 
    print(f'Index: {index}')
    print(f'Index length: {len(index)}')
    t_count = 0
    
    for tonic in waves.keys():
        current_root_set = [] 
        print('Tonic: {}'.format(tonic))
        print(f't_count = {t_count}')
        for i in range(0, 21): #21 because inversions go that high above octave
            print(f'index = {index[i+t_count]}')
            current_root_set.append(waves[index[i+t_count]]) 
        for chord, degree_list in ck.chord_generator_book.items(): 
            chord_degrees = []
            #print(f'degree_list = {degree_list}')
            for degree in degree_list:
                #print(f'degree = {degree}')
                chord_degrees.append(current_root_set[degree])
            #print(chord_degrees)
                #the normalization constant allows us to combine multiple waves
                #while maintaining peak amplitude of 1 for the composite wave
            norm_const = 0.0
            chord_samples = []
            for sample in range(0, tk.num_samples):
                add_sample = 0.0
                for degree_sample in range(len(chord_degrees)):
                     add_sample += chord_degrees[degree_sample][sample]
                if add_sample > norm_const:
                    norm_const = add_sample
                chord_samples.append(add_sample)
            #print('NC: {}'.format(norm_const))
            for sample in range(0, tk.num_samples):
                chord_samples[sample] = chord_samples[sample]/norm_const
            chord_name = tonic+'_'+chord
            chord_freq[chord_name] = chord_samples
            chord_names.append(chord_name)
            print(chord_name) 
            
            #playback test to determine if chord was generated correctly
            ''' 
            file = chord_name+'.wav'
            wav_file = wave.open(file, 'w')
            wav_file.setparams((tk.nchannels, tk.sampwidth, int(tk.sampling_rate), tk.nframes, tk.comptype, tk.compname))
            for sample in chord_samples:    
                wav_file.writeframes(struct.pack('h', int(sample*tk.amplitude)))
            sound = current_dir+file 
            print(str(file))
            ps(sound)
            wav_file.close() 
            '''

        current_octave = []
        t_count +=1
        print(t_count)
        if t_count == t_range:
            print(f't count finished: {t_count}')
            chord_dict = file_handler.create_file_names(wave_type, chord_names)
            file_handler.write_wav_files(current_dir, chord_path, chord_dict, chord_freq) 
            return

