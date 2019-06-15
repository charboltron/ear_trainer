#create list of file names to make wav files, append id number to sort
import wave as wave
import os
import shutil
import struct
import toolkit as tk

def create_file_names(wave_type, all_pitches):

    '''
    Creates file names by appending serial numbers to files and 
    '''
    file_names = []
    i = 1
    for pitch in all_pitches:
        if i < 10:
            file_name = '00'+str(i)+wave_type+pitch+'.wav'
        elif i < 100:
            file_name = '0'+str(i)+wave_type+pitch+'.wav'
        else:
            file_name = str(i)+wave_type+pitch+'.wav'
        file_names.append(file_name)
        i+=1

    file_pitch = dict(zip(file_names, all_pitches))
    return file_pitch

def write_wav_files(current_dir, target_dir, file_pitch, all_waves):
    for f, p in file_pitch.items():
        file = f
        wav_file = wave.open(file, 'w')
        wav_file.setparams((tk.nchannels, tk.sampwidth, int(tk.sampling_rate), tk.nframes, tk.comptype, tk.compname))
        for sample in all_waves[p]:   
            wav_file.writeframes(struct.pack('h', int(sample*tk.amplitude)))
        wav_file.close()
        move_files(current_dir, target_dir)

#move files from current directory to sin dir
def move_files(current_dir, target_dir):
    for file_name in os.listdir(current_dir):
        if file_name.endswith('.wav'):
            shutil.move(file_name, target_dir+file_name)
