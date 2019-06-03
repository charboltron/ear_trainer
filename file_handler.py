#create list of file names to make wav files, append id number to sort
import wave as wave
import os
import shutil
import struct


#Define parameters to make .wav files
num_samples = 44100
nframes = num_samples                                    #nframes is just the number of samples
sampling_rate = 44100.0 
amplitude = 16000                                        #fixed amplitude
comptype="NONE"                                          #compression type
compname="not compressed" 
nchannels=1
sampwidth=2                                              #2 bytes so 16-bit.

def create_file_names(string, all_pitches):
    file_names = []
    i = 1
    for pitch in all_pitches:
        if i < 10:
            file_name = '00'+str(i)+string+pitch+'.wav'
        elif i < 100:
            file_name = '0'+str(i)+string+pitch+'.wav'
        else:
            file_name = str(i)+string+pitch+'.wav'
        file_names.append(file_name)
        i+=1

    file_pitch = dict(zip(file_names, all_pitches))
    return file_pitch

def write_wav_files(current_dir, target_dir, file_pitch, all_waves):
    for f, p in file_pitch.items():
        file = f
        amplitude = 16000
        wav_file = wave.open(file, 'w')
        #wav_file.setparams((1, 2, 44100.0, 44100, "NONE", "not compressed"))
        wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
        for sample in all_waves[p]:    
            wav_file.writeframes(struct.pack('h', int(sample*amplitude)))
        wav_file.close()
        move_files(current_dir, target_dir)

#move files from current directory to sin dir
def move_files(current_dir, target_dir):
    for file_name in os.listdir(current_dir):
        if file_name.endswith('.wav'):
            shutil.move(file_name, target_dir+file_name)
