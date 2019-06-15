import os
import shutil

current_dir = '/Users/charlesbolton/Desktop/510_Music/sound_project/ear_trainer/square_waves/chords/'

ls = ['_a_', '_b_', '_c_', '_d_', '_e_', '_f_', '_g_']
ls = ['_cs_db_', 'fs_gb', 'as_bb', 'gs_ab', 'ds_eb']
ls = ['ab']
for f in os.listdir(current_dir):
    for l in ls:
        if l in f:
            fr = f.replace(l, 'Ab')
            shutil.move(f, current_dir+fr)
