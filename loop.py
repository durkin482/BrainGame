print "\nYou've mastered the use of Mermaid Man's utility belt and have shrunken "
print "down to the size of a single cell. Using this ability, you have been allowed "
print "to enter my brain and search for whatever you wish. Luckily for you, "
print "my brain has been compartmentalized into four areas that you will discover "
print "as you explore. Have fun, press enter to continue!\n"
raw_input()

import main
from brain import area_object

try_again = ""

while try_again.lower() != "n":
	player = main.Player(area_object, 'brain')
	
	while player.is_alive: 
	    player.run_turn()

	try_again = raw_input("\nTry again? Y or N\n\n")