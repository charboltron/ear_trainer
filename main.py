import menus
import pitch_trainer
import interval_trainer
import chord_trainer
import scale_trainer
import chimes

chimes.welcome()
menus.title()
menus.print_play_menu()
while True:
  sel = input()
  sel = sel.strip()
  if sel == '1': 
      r = pitch_trainer.run()
  if sel == '2':
      r = interval_trainer.run()
  if sel == '3':
      r = chord_trainer.run()
  if sel == '4':
      r = scale_trainer.run()
  if sel == 'q':
      chimes.correct()
      print("You entered 'q'. Quitting program. Thanks for playing!\n\n")
      exit(0)
  if r == 'm!':
      menus.print_play_menu()
      continue
  else:
      print('invalid input!')
      continue  
