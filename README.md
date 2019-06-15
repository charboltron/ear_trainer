# ear_trainer
![GitHub Logo](/img/title.jpg)
Format: ![Alt Text](url)
Ear Trainer

Using the generator modules should not be necessary for playing the game. They are provided to anyone interested in how the .wav files were generated. To play the game, just run $python main.py from the command line and enjoy (or not).

For the ear trainer, I generated/created over 5,000 .wav files using four basic waveforms (sine, square, triangle, and saw). The different sound files are generated using the tone_generator and toolkit modules which generates basic pitch tones, interval tones, and chord tones. The interval and chord generators are their own respective modules and thus don't need to be accessed, either, except for the interested. The scale tones are simply the pitch tones but half as long (because slow scales are boring to listen to). Because the files are already saved in their respective waveform directories, it is unnecessary for the user to access or use these modules. However, they are included because the waveform generation is super interesting and I wanted to share it. Should you want to use the generators, run $python, import tone_generator as tg, and then run either tg.generate_tones() (a test function) or tg.save_tones (a file creation and save function). This could potentiall overwrite the files in the repository. These files will also not be faded at both ends and are therefore more annoying to listen to. I have curved the ends of the files in Logic Pro X to prevent this. It's also fun to look at the waveforms in a DAW, and I encourage you to do so. 

Each game has it's own trainer module which is essentially a CLI menu-based game. The trainer modules are interesting in that they access the dft module (for the interval and chord trainers), and the dft returns to the trainer modules the individual notes that make up a composite waveform. ---
