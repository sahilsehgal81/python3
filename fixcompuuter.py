#!/usr/bin/python

print("Help, My Computer doesn/'t work")
print("Ok!, let's go with the basic troubleshooting!")

choice = input("Is the Power of Compuer ON? (y/n)")
if choice == 'n':
	choice = input('Is Computer Plugged in? ')
	if choice == 'n':
		print('Please Plug the computer In')
	else:
		choice = input('Is the Switch On? ')
		if choice == 'n':
			print('Turn the Switch On!')
		else:
			choice = input('Is the Fuse OK? ')
			if choice == 'n':
				print('Check Fuse Please!')
			else:
				print('Retsart Computer!')
else:
	choice = input('Do you hear any beep or sound? ')
	if choice == 'n':
		print("If this still doesn't work, please seek Technical Help!")
	else:
		print('This must be RAM problem!\nTo fix this, open CPU, dittach RAM, Clean it and insert it back!\n\tThanks for contacting me!')
				
