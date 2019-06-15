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


current_dir = '/Users/charlesbolton/Desktop/510_Music/sound_project/ear_trainer'
'''
unit test to check if dft works for all piano frequencies.
'''
def test_dft_all_tones():
    all_waves = tk.get_all_waves_sin()
    pitch_freq = tk.get_pitch_freq()
    for pitch in all_waves.values():
        dft.dft(tk.num_samples, pitch, pitch_freq, 1)
#-------------------------------------------------------------------------------------

'''
unit test to see if dft can parse an interval
'''
def test_dft_interval_parse():
#make the tonic samples
    ref = reference_frequency
    frequency = ref * (2 ** (0/12))
    tonic = [np.sin(2 * np.pi * frequency * x/tk.sampling_rate) for x in range(tk.num_samples)]

#make the major third samples
    frequency = ref * (2 ** (4/12))
    third = [np.sin(2 * np.pi * frequency * x/tk.sampling_rate) for x in range(tk.num_samples)]
    maj_third = []
    for s in range(len(tonic)):
        maj_third.append((tonic[s]+third[s])/2)
    
    print("Testing the tonic:") 
    dft.dft(tk.num_samples, tonic, pitch_freq, 1)
    print("Testing the third:")
    dft.dft(tk.num_samples, third, pitch_freq, 1)
    print("Testing the composite major third:")
    dft.dft(tk.num_samples, maj_third, pitch_freq, 1)
#---------------------------------------------------------------------------------------
'''
Unit test for all intervals in the dft
'''

def test_dft_intervals():
    
    interval_names = []
    intervals = []
    sine_dir = current_dir+'sine_waves/'
    interval_dir = sine_dir+'intervals/'
    sine_tone_dir = sine_dir+'all_tones/'

    #make lists for intervals with file path and just interval names
    for file in os.listdir(interval_dir):
        if '.wav' in file:
            intervals.append((interval_dir+file))
            interval_names.append(str(file))
    intervals.sort()
    interval_names.sort()
    #print(interval_names)
    #gather all the sine tones for playback
    sines = [file for file in os.listdir(sine_tone_dir)]
    sines.sort()
    sine_tones = []
    for tone in range(0, len(sines)):
        sine_tone = sine_tone_dir+sines[tone]
        sine_tones.append(sine_tone)
    #print(sine_tones)
    count = 0
    max_sample = None
    min_sample = None
    for file in intervals:
       
        #print(file)
        wavfile = wave.open(file, 'rb')
        channels = wavfile.getnchannels()
        width = wavfile.getsampwidth()
        rate = wavfile.getframerate()
        frames = wavfile.getnframes()
        wave_bytes = wavfile.readframes(frames)
        frame_width = width * channels
        # Iterate over frames.
        samples = []
        for f in range(0, len(wave_bytes), frame_width):
            frame = wave_bytes[f : f + frame_width]
            # Iterate over channels.
            for c in range(0, len(frame), width):
                # Build a sample.
                sample_bytes = frame[c : c + width]
                #Eight-bit samples are unsigned
                sample = int.from_bytes(sample_bytes, byteorder='little',signed=(width>1))
                #print(sample)
                sample = float(sample)/16000 
                #divide by 16000 to get max and min to 1 and -1 for dft. Because you multiplied
                #by 16000 when you created the file (*tk.amplitude)
                samples.append(sample)
                if max_sample == None:
                    max_sample = sample
                if min_sample == None:
                    min_sample = sample
                if sample > max_sample:
                    max_sample = sample
                if sample < min_sample:
                    min_sample = sample
        print(max_sample)
        print(min_sample)    
        ps(intervals[count])
        print('DFT evaluating current file: {}'.format(interval_names[count]))
        count +=1
        composite_pitches = dft.dft(tk.num_samples, samples, pitch_freq, 1) 
        print(composite_pitches)
        for p in composite_pitches:    
            for i, s in enumerate(sine_tones): 
                if p in s:
                    ps(sine_tones[i])
                    print(sines[i])
                    time.sleep(1)
        print()
