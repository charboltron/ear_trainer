import menus
import pitch_trainer
import interval_trainer

menus.title()
menus.print_play_menu()
while True:
  sel = input()
  if sel == '1': 
      pitch_trainer.run()
  if sel == '2':
      interval_trainer.run()
  if sel == '3':
      pass
  if sel == '4':
      pass
  if sel == 'q':
      print("You entered 'q'. Quitting program. Thanks for playing!\n\n")
      exit(0)
  else:
      print('invalid input!')
      continue  
