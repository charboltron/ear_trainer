heptatonic_names = ['Major', 'Natural Minor', 'Harmonic Minor', 'Melodic Minor', 'Dorian', 'Lydian', 'Phrygian', 
                    'Mixolydian', 'Locrian']

heptatonic_degrees = [[0, 2, 4, 5, 7, 9, 11, 12], [0, 2, 3, 5, 7, 8, 10, 12], [0, 2, 3, 5, 7, 8, 11, 12], 
                      [0, 2, 3, 5, 7, 8, 11, 12], [0, 2, 3, 5, 7, 9, 10, 12], [0, 1, 3, 5, 7, 8, 10, 12],
                      [0, 2, 4, 6, 7, 9, 11, 12], [0, 2, 4, 5, 7 ,9, 10, 12], [0, 1, 3, 5, 6, 8, 10, 12]]

scale_indices = [i for i in range(len(heptatonic_degrees))]
scale_degree_index = dict(zip(scale_indices, heptatonic_degrees))
scale_name_index   = dict(zip(scale_indices, heptatonic_names))
hept_dict = dict(zip(heptatonic_names, heptatonic_degrees))
