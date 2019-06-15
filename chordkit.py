import copy
import toolkit as tk

#Kit for chord dictionary generation

triads = ['major', 'minor', 'augmented', 'diminished', 'suspended_two', 'suspended_four']
four_notes = ['dominant_seven', 'major_seven', 'minor_seven', 'minor_major_seven', 
              'diminished_seven', 'diminished_major_seven', 'half_diminished_seven',
              'augmented_seven', 'augmented_major_seven']
inversions = ['major_1st_inversion', 'major_2nd_inversion', 'minor_1st_inversion', 'minor_2nd_inversion',
              'augmented_1st_inversion', 'augmented_2nd_inversion', 'suspended_two_1st_inversion', 
              'suspended_two_2nd_inversion', 'suspended_four_1st_inversion', 'suspended_four_2nd_inversion', 
              'dominant_seven_1st_inversion', 'dominant_seven_2nd_inversion', 'dominant_seven_3rd_inversion', 
              'major_seven_1st_inversion', 'major_seven_2nd_inversion', 'major_seven_3rd_inversion', 
              'minor_seven_1st_inversion', 'minor_seven_2nd_inversion', 'minor_seven_3rd_inversion',
              'minor_major_seven_1st_inversion','minor_major_seven_2nd_inversion', 'minor_major_seven_3rd_inversion',
              'diminished_major_seven_1st_inversion','diminished_major_seven_2nd_inversion', 'diminished_major_seven_3rd_inversion',
              'half_diminished_seven_1st_inversion', 'half_diminished_seven_2nd_inversion', 'half_diminished_seven_3rd_inversion',
              'augmented_seven_1st_inversion', 'augmented_seven_2nd_inversion', 'augmented_seven_3rd_inversion',
              'augmented_major_seven_1st_inversion', 'augmented_major_seven_2nd_inversion', 'augmented_major_seven_3rd_inversion']

chord_file_appends = [chord for chord in triads]
for chord in four_notes:
    chord_file_appends.append(chord)
for chord in inversions:
    chord_file_appends.append(chord)

answers = []
for chord in triads:
    answers.append(chord)
for chord in four_notes:
    answers.append(chord)
for chord in inversions:
    answers.append(chord)
for i, name in enumerate(answers):
    if '1st' in name:
        name = name.replace('1st', 'First')
    elif '2nd' in name:
        name = name.replace('2nd', 'Second')
    elif '3rd' in name:
        name = name.replace('3rd', 'Third')
    name = name.replace('_', ' ')
    name = name.title()
    answers[i] = name


triad_degrees =         [[0, 4, 7], [0, 3, 7], [0, 4, 8], [0, 3, 6], [0, 2, 7], [0, 5, 7]]
four_degrees  =         [[0, 4, 7, 10], [0, 4, 7, 11], [0, 3, 7, 10], [0, 3, 7, 11], [0, 3, 6, 9],
                        [0, 3, 6, 11], [0, 3, 6, 10], [0, 4, 8, 10], [0, 4, 8, 11]]
inversion_degrees =     [[4, 7, 12],[7, 12, 16], [3, 7, 12], [7, 12, 15],[4, 8, 12],[8, 12, 16],
                        [2, 7, 12],[7, 12, 14], [5, 7, 12], [7, 12, 17],   [4, 7, 10, 12], [7, 10, 12, 16], [10, 12, 16, 19], 
                        [4, 7, 11, 12], [7, 11, 12, 16], [11, 12, 16, 19], [3, 7, 10, 12], [7, 10, 12, 15], [10, 12, 15, 19], 
                        [3, 7, 11, 12], [7, 11, 12, 15], [11, 12, 15, 19], [3, 6, 11, 12], [6, 11, 12, 15], [11, 12, 15, 18],
                        [3, 6, 10, 12], [6, 10, 12, 15], [10, 12, 15, 18], [4, 8, 10, 12], [8, 10, 12, 16], [10, 12, 16, 20],
                        [4, 8, 11, 12], [8, 11, 12, 16], [11, 12, 16, 20]]


inversion_mappings = []
for inversion in inversion_degrees:
    norm_const = inversion[0]
    inversion_mapping = [(i-norm_const) for i in inversion]
    #print(inversion_mapping)
    inversion_mappings.append(inversion_mapping)

inversion_map = dict(zip(inversions, inversion_mappings))
#print(inversion_map)

all_chords_degrees = [chord for chord in triad_degrees]
for chord in four_degrees:
    all_chords_degrees.append(chord)
for chord in inversion_mappings:
    all_chords_degrees.append(chord)

chord_generator_book = dict(zip(chord_file_appends, all_chords_degrees))
#chord_generator_book = dict(zip(chord_file_appends, all_chords_degrees))
#pfo('all', all_chords_degrees)


triad_answers = answers[0:6]
four_answers = answers[6:15]
inversion_answers = answers[15:46]

triad_book = dict(zip(triad_answers, triad_degrees))
four_book = dict(zip(four_answers, four_degrees))
inversion_book = dict(zip(inversion_answers, inversion_mappings))
#tk.pfo('three', triad_book)
#tk.pfo('four', four_book)
#tk.pfo('inv', inversion_book)

easy_mode_book = triad_book.copy()
intermediate_mode_book = easy_mode_book.copy()
intermediate_mode_book.update(four_book)
hard_mode_book = intermediate_mode_book.copy()
hard_mode_book.update(inversion_book)
#pfo('chord book', chord_book)
