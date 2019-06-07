from playsound import playsound as ps

chimes = '/Users/charlesbolton/Desktop/510_Music/sound_project/ear_trainer/chimes/'

def correct():

    ps(chimes+'correct.wav')

def incorrect():

    ps(chimes+'incorrect.wav')

def welcome():
    
    ps(chimes+'welcome.wav')
