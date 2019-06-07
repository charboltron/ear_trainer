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

current_dir =   '/Users/charlesbolton/Desktop/510_Music/sound_project/ear_trainer/'
chord_path = current_dir+'sine_waves/chords/test/'

for chord in ck.chord_book.items():
    print(chord)

ref = 440.0
chord_names = []
chord_freq = {}
current_root_set = [] 

def generate_chords(waves, index, t_last, t_range, wave_type):
    
    print(f'Last tonic: {t_last}') 
    print(f'Index: {index}')
    print(f'Index length: {len(index)}')
    t_count = 0
    
    for tonic in waves.keys():
        print('Tonic: {}'.format(tonic))
        #print(t_count)
        for i in range(0, 21): #21 because inversions go that high above octave
            current_root_set.append(waves[index[i+t_count]])
            
        for chord, degree_list in chord_book.items(): 
            chord_degrees = []
            for degree in degree_list:
                #print(degree)
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
            '''
            playback test to determine if chord was generated correctly
            
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
        if t_count == t_range-21:
            print(f't count: {t_count}')
            chord_dict = file_handler.create_file_names(wave_type, chord_names)
            file_handler.write_wav_files(current_dir, chord_path, chord_dict, chord_freq) 
            return

