import os
import shutil

current_dir = '/Users/charlesbolton/Desktop/510_Music/sound_project/ear_trainer/sine_waves/chords/'

for file_name in os.listdir(current_dir):
    if 'augemented_seven_3rd' in file_name:
        file_name_replace = file_name.replace('augemented_seven_3rd', 'augmented_seven_3rd')
        shutil.move(file_name, current_dir+file_name_replace)
