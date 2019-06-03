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

intervals = ['min_second', 'maj_second', 'min_third', 'maj_third', 'perf_fourth', 'tritone',
             'perf_fifth', 'min_sixth', 'maj_sixth', 'min_seventh', 'maj_seventh', 'octave']

ref = 440.0
interval_names = []

def generate_intervals(waves, index, t_last, interval_range):
     
    print(f'Last tonic: {t_last}') 
    print(f'Index: {index}')
    print(f'Index length: {len(index)}')
    interval_freq = {}
    current_octave = []
    t_count = 1
    
    for tonic, w in waves.items():
        t = waves[tonic]
        print('Tonic: {}'.format(tonic))
        print(t_count)
        for i in range(0, 12):
            #print('Tonic: {} plus {}'.format(tonic, intervals[i]))
            current_octave.append(waves[index[i+t_count]])
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
        t_count +=1
        if t_count == interval_range-12:
            print(f't count: {t_count}')
            interval_dict = file_handler.create_file_names('_sine_', interval_names)
            file_handler.write_wav_files(current_dir, interval_path, interval_dict, interval_freq) 
            return
