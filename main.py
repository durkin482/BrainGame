class Area(): # area objects are defined in brain.py

	def __init__(self, area_name, description, question_string, answers_dict, correct_answer, guesses=3, win=False):
		self.area_name = area_name
		self.description = description
		self.question_string = question_string
		self.answers_dict = answers_dict
		self.correct_answer = correct_answer
		self.guesses = guesses
		self.win = win


class Q_and_A(): # Q_and_A objects defined in brain.py

	def __init__(self, area_name, description, question_string, answers_dict, correct_answer, guesses=3):
		self.area_name = area_name
		self.description = description
		self.question_string = question_string
		self.answers_dict = answers_dict
		self.correct_answer = correct_answer
		self.guesses = guesses
		

class Map: # created for easy area changes - used in loop.py and brain.py (like area_object['favorites'] would take you to favorites)

	def __init__(self, locations={}):
		self.locations = locations

	def __getitem__(self, location):
		return self.locations[location]
    
	def __setitem__(self, location, location_object):
		self.locations[location] = location_object


class Player: 

	def __init__(self, game_map, starting_area, is_alive=True):
		self.game_map = game_map
		self.current_area = self.game_map[starting_area]
		self.is_alive = is_alive
		self.visited_areas = []

	def run_turn(self):
		print "\nYou've entered the %s" % (self.current_area.area_name)
		if self.current_area in self.visited_areas:
			print "\nYou've been here already..."
		else:
			print self.current_area.description
			self.visited_areas.append(self.current_area)
		if self.is_alive:
			self.run_next_action()

	def get_next_area(self, player_input):
		while True:
			try: # this checks the dictionary defined in brain.py to see if the player input matches the key of the dictionary.
				return self.current_area.answers_dict[player_input.lower()] 
			except KeyError:
				print "\nThat was not a valid choice."

	def verify_answer(self, player_input):
		if player_input in self.current_area.correct_answer:
			print "\nGood choice!"
			return
		else:
			print "\nBad choice! Wrong Answer!"
			self.wrong_answer()

	def win(self):
		if self.current_area.win:
			raw_input()
			quit()
			
			
	def wrong_answer(self):
		self.current_area.guesses -= 1
		if self.current_area.guesses == 1:
			print "\nOnly one guess remaining! Don't fuck it up!"
			return self.run_next_action()
		if self.current_area.guesses == 0:
			print "\nYou fucked it up. Start over!"
			self.run_next_action()
		else:
			print "\nGuesses remaining until auto-quit: %d" % (self.current_area.guesses)
			return self.run_next_action()


   
	def run_next_action(self):
		while True:
			if self.current_area.guesses > 0:
				player_input = raw_input(self.current_area.question_string)
				self.verify_answer(player_input)
				next_area = self.get_next_area(player_input) 
				self.current_area = self.game_map[next_area]
				self.run_turn()
			else:
				quit()
			