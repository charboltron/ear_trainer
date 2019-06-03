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

current_dir =   '/Users/charlesbolton/Desktop/510_Music/sound_project/'
interval_path = current_dir+'sine_waves/intervals/test/'

triads = ['major', 'minor', 'augmented', 'diminished', 'suspended two', 'suspended four']
four_notes = ['dominant seven', 'major seven', 'minor seven', 'minor major seven', 
              'diminished seven', 'diminished major seven', 'half diminished seven',
              'augmented seven', 'augmented major seven']

triad_intervals = [[0, 4, 7],[0, 3, 7], [0, 4, 8], [0, 3, 6], [0, 2, 7], [0, 5, 7]]
four_intervals  = [[0, 4, 7, 10], [0, 4, 7, 11], [0, 3, 7, 10], [0, 3, 7, 11], [0, 3, 6, 9],
                   [0, 3, 6, 11], [0, 3, 6, 10], [0, 4, 8, 10], [0, 4, 8, 11]]

triad_book = dict(zip(triads, triad_intervals))
four_book = dict(zip(four_notes, four_intervals))

print(triad_book, four_book)

ref = 440.0
interval_names = []

exit(0)

def generate_chords(waves, index, c_last, c_range):
     
    print(f'Last tonic: {t_last}') 
    print(f'Index: {index}')
    print(f'Index length: {len(index)}')
    interval_freq = {}
    current_octave = []
    c_count = 1
    
    for tonic, w in waves.items():
        t = waves[tonic]
        print('Tonic: {}'.format(tonic))
        print(c_count)
        for i in range(0, 12):
            #print('Tonic: {} plus {}'.format(tonic, intervals[i]))
            current_octave.append(waves[index[i+c_count]])
            interval = current_octave[i]
            tonic_plus_interval = []
            
            #the normalization constant allows us to combine multiple waves
            #while maintaining peak amplitude of 1 for the composite wave
            norm_const = 0.0

            for sample in range(0, tk.num_samples):
                add_sample = t[sample]+interval[sample]
                if add_sample > norm_const:
                    norm_const = add_sample
                tonic_plus_interval.append(add_sample)
            #print('NC: {}'.format(norm_const))
            for sample in range(0, tk.num_samples):
                tonic_plus_interval[sample] = tonic_plus_interval[sample]/norm_const
                interval_freq[tonic+intervals[i]] = tonic_plus_interval
                
            interval_names.append(tonic+intervals[i])
           
            '''
            playback test to determine if interval was generated correctly
            '''
            #wav_file = wave.open(file, 'w')
            #wav_file.setparams((tk.nchannels, tk.sampwidth, int(tk.sampling_rate), tk.nframes, tk.comptype, tk.compname))
            #for sample in tonic_plus_interval:    
            #    wav_file.writeframes(struct.pack('h', int(sample*tk.amplitude)))
            #sound = current_dir+file 
            #print(str(file))
            #ps(sound)
            #wav_file.close() 
            
        current_octave = []
        c_count +=1
        if c_count == interval_range-12:
            print(f'c count: {c_count}')
            interval_dict = file_handler.create_file_names('_sine_', interval_names)
            file_handler.write_wav_files(current_dir, interval_path, interval_dict, interval_freq) 
            return

