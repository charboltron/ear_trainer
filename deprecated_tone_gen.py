
    #To be implemented: take wavetype as argument
    #Reference frequency begins at 440Hz. Other frequencies based on this tone
    reference_frequency = 440.0
    pitch_freq = {} 
    pitches = ['A', 'As_Bb', 'B', 'C', 'Cs_Db', 'D', 'Ds_Eb', 'E', 'F', 'Fs_Gb', 'G', 'Gs_Ab']
    octave_count = 0
    tone_count = 0
    all_waves = {}
    all_pitches = []

    #compute all the semitones in all piano octaves from A0 to C8 (88 keys)
    for semitone in range(-48, 40): 
        #compute base value for frequency of each semitone from 440Hz reference 
        frequency = reference_frequency * (2 ** (semitone/12))
        #append semitone base frequency to dictionary of pitch/frequency pairs 
        pitch = pitches[semitone % 12]+'_'+str(octave_count) #append octave number
        all_pitches.append(pitch)
        pitch_freq[pitch] = frequency
        #Create a 1-second sine wave of 44.1kHz samples for each frequency
        sine_wave = [np.sin(2 * np.pi * frequency * x/(tk.sampling_rate)) for x in range(tk.num_samples)]
        all_waves[pitch] = sine_wave
        tone_count += 1
        #increment octave number
        if (tone_count -3) % 12 == 0:
            octave_count += 1
    #print(all_waves.keys())

    #for j, k in pitch_freq.items():
    #    print(j,k)

    all_waves_pitches = {}
    for i, pitch in enumerate(all_waves.keys()):
        all_waves_pitches[i] = pitch
    #print(all_waves_pitches)
