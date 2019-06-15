from playsound import playsound as ps
import os

chimes = os.getcwd()+'/chimes/'

def correct():

    ps(chimes+'correct.wav')

def incorrect():

    ps(chimes+'incorrect.wav')

def welcome():
    
    ps(chimes+'welcome.wav')
