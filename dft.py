import numpy as np
import toolkit as tk

#'samples' is a list of 44100 sample values 
def dft(num_samples, samples, pitch_freq, test): 
    bins = {}
    return_pitches = []
    summation = 0.+ 1j*0.
    for pitch, frequency in pitch_freq.items():
        #assign k to piano-valued pitches
        k = pitch_freq[pitch]
        for sample in range(0, int(num_samples/2)):
            e_exp = ((-2*np.pi*(k)*sample))/num_samples
            c = float(np.cos(e_exp))
            s = float(np.sin(e_exp))
            summation += float(samples[sample])*(c+1j*s)
        summation = summation*2
        summation = summation/num_samples
        magnitude = abs(summation)
        #print(magnitude)
        if magnitude > .1: 
            if test:
                print('Frequency detected in the sine wave: {}'.format(k))
            for pitch, freq in pitch_freq.items():
                if int(k) == int(freq):
                    if test:
                        print('This corresponds to pitch: {}.'.format(pitch))
                    return_pitches.append(pitch)
        bins[k]=(magnitude)
    interv = compute_interval(return_pitches, pitch_freq)    
    #print(bins)
    return return_pitches, interv


def compute_interval(return_pitches, pitch_freq):
   tonic = None
   interval = None
   for i, key in enumerate(pitch_freq.keys()):
       if key in return_pitches:
           if tonic == None:
             tonic = key
             low = i 
           elif interval == None:
             interval = key
             high = i
   #print(tonic, interval)
   #print(high, low, high-low)
   interv = high-low
   return interv


'''      
ft = []
average_point = 0. + 1*j*0.
for n, meas in zip(range(1, num_samples, samples)):
            
            #how far we have travelled across the 'length' of our sample
            #this is the n/N part of the equation
            
            fractional_distance = float(n)/num_samples
            average_point += meas*np.exp(-1j*2*np.pi*frequency \
            *fractional_distance)

        average_point = average_point /num_samples
        ft.append(average_point)
    print(ft)
'''


