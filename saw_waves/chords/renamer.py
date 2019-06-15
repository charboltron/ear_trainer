import os
import shutil

current_dir = '/Users/charlesbolton/Desktop/510_Music/sound_project/ear_trainer/saw_waves/chords/'

for file_name in os.listdir(current_dir):
    if '.wav' in file_name:
        file_name_replace = file_name.replace(' ', '_')
        shutil.move(file_name, current_dir+file_name_replace)
