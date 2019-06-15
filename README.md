#Ear Trainer
![Title Picture](/img/title.jpg)

### About
Created by Charles Bolton in May/June 2019, this project is a music and digital signal processing exploration into waveform generation, composition, and decomposition. It was inspired by my longing to understand how the Discrete Fourier Transform works. I began by generating simple sinusoids to determine if my DFT could pick out the correct frequenicies. The idea to turn the DFT into the backbone for an Ear Trainer game came naturally from the idea to parse two sine waves added together. Musically, these waves comprise an interval that an aspiring musician might want to be able to recognize.   

For the ear trainer, I generated over 5,000 .wav files using four basic waveforms (sine, square, triangle, and saw). The different sound files are generated using the tone_generator and toolkit modules which generate basic pitch tones, interval tones, and chord tones. The interval and chord generators are their own respective modules and thus don't need to be accessed, either, except for the interested. Because the files are already saved in their respective waveform directories, it is unnecessary for the user to access or use these modules. Should you really want to use the generators, run 

$python, import tone_generator as tg

and then run either 

tg.generate_tones() (a test function) 

or 

tg.save_tones (a file creation and save function). 

Note that this could potentially overwrite the files in the repository or cause duplicates. These files will also not be faded at both ends and are therefore more annoying to listen to in the context of the game. I have curved the ends of the files in Logic Pro X to prevent this. It's also fun to look at the waveforms in a DAW, and I encourage anyone to do so. 

Each game has its own trainer module which is essentially a CLI menu-based game. The trainer modules are interesting in that they access the dft module (for the interval and chord trainers), and the dft returns to the trainer modules the individual notes that make up a composite waveform. This is why there is a slight delay after each new tone is played. This could be avoided but would do away with the whole contrivance of using the DFT to learn about domain transformation, which is the reason for this project. 

### Running

Using the generator modules should not be necessary for playing the game. They are provided to anyone interested in how the .wav files were generated. To play the game, just go to the src folder and run:

python main.py 

from the command line and enjoy (or not).


### Python Modules 

* playsound
* numpy 
* wave (native)
