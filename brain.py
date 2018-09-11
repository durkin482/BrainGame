# Had girlfriend at the time re-work the code so I could play the game with her as a writer. Please forgive comments

import main

area_object = main.Map()
 
area_object['brain'] = main.Area(
    (
        "Brain" # can change the contents of these quotes
    ),
    (
        '\nAs you enter the brain, you see bright, flashing bolts similar to lightning. '
        '\nThough there are thousands of natural pathways, there are few open spaces ' 	# can change the contents of these quotes
        '\nsafe enough to travel through. One area in particular seems to be shaped like '
        '\na heart! You should go there!\n'
    ),
    (
        'New location found - press enter to continue\n\n' # can change the contents of these quotes
    ),
    {
        "": "favorites" # the strings "favorites" controls what area the player is going to next - both changable as long as you change the 'brain' in (area_object['brain'] = main.Area on line 5)
    },
    (
    	[""] #correct answer(s) - this is used for the answer verification function in main.py
    )
)

area_object['favorites'] = main.Area(
    (
        "Favorites Center" # area name
    ),
    (
        '\nThe threshold from the main portion of the brain to the Favorites Center is '
        '\nglowing white. After entering, the area seems to change entirely as if you were ' 	# area description
        '\nentering the most focused scene in a movie. There are images of pizza,  '
        '\ninstruments, you, family, friends, and many other things, but more '
        '\nimportantly, there are lots of questions that need answers.\n'
    ),
    (
        '\nDo you have what it takes to find them? Y or N\n\n' # option string (what appears on the screen)
    ),
    {
        "y": "fav_question_1",
        "n": "brain" # area dictionary      
    },
    (
    	["y", "n"]
    )
)

area_object['fav_question_1'] = main.Q_and_A(
    (
        "Favorites Center - Question 1"
    ),
    (
        '\nThere are several instruments floating around your space. Out of '
        '\nall of them, what is my favorite to play?'
    ),
    (
        '\n A: Saxophone'
        '\n B: Drums'
        '\n C: Guitar'
        '\n D: Piano\n\n'
    ),
    {
        "a": 'fav_question_1',
        "b": 'fav_question_2',
        "c": 'fav_question_1',
        "d": 'fav_question_1'
    },
    (
    	["b"]
    )
)

area_object['fav_question_2'] = main.Q_and_A(
    (
        "Favorites Center - Question 2"
    ),
    (
        '\nThere seems to be people around. I must have lots '
        '\nof favorite people! Out of all of them, who would I '
        '\nrather spend the day with? '
    ),
    (
        '\n A: Friends'
        '\n B: Family'
        '\n C: Myself'
        '\n D: You'
        '\n E: You and friends\n\n'
    ),
    {
        "a": 'fav_question_2',
        "b": 'fav_question_2',
        "c": 'fav_question_2',
        "d": 'fav_question_3',
        "e": 'fav_question_3'
    },
    (
    	["d", "e"]
    )
)

area_object['fav_question_3'] = main.Q_and_A(
    (
        "Favorites Center - Question 3"
    ),
    (
        '\nMmmmmmm...food everywhere! Which one is my favorite?'
    ),
    (
        '\n A: Steak'
        '\n B: Burritos'
        '\n C: Pizza'
        '\n D: Mac & Cheese\n\n'
    ),
    {
        "a": 'fav_question_3',
        "b": 'fav_question_4',
        "c": 'fav_question_3',
        "d": 'fav_question_3'
    },
    (
    	["b"]
    )
)

area_object['fav_question_4'] = main.Q_and_A(
    (
        "Favorites Center - Question 4"
    ),
    (
        '\nMy mental image of you is floating before you.'
        '\nWhat is my favorite thing about you?'
    ),
    (
        '\n A: Your smile'
        '\n B: Your drive'
        '\n C: Your outlook on life'
        '\n D: Your hand-eye coordination'
        '\n E: Your love'
        '\n F: All of the above\n\n'
    ),
    {
        "a": 'fav_question_4',
        "b": 'fav_question_4',
        "c": 'fav_question_4',
        "d": 'fav_question_4',
        "e": 'fav_question_4',
        "f": 'fav_question_5'
    },
    (
    	["f"]
    ),
    guesses = 4
)

area_object['fav_question_5'] = main.Q_and_A(
    (
        "Favorites Center - Question 5"
    ),
    (
        '\nA beautiful painting appears. What is my favorite color?'
    ),
    (
        '\n A: Red'
        '\n B: Green'
        '\n C: Purple'
        '\n D: Blue\n\n'
    ),
    {
        "a": 'fav_question_5',
        "b": 'fav_question_5',
        "c": 'memories',
        "d": 'fav_question_5'
    },
    (
    	["c"]
    )
)

area_object['memories'] = main.Area(
    (
        "Memories Center" # can change the contents of these quotes
    ),
    (
        '\nYou\'ve made it this far! Don\'t stop now!\n'
    ),
    (
        'New location found - press enter to continue\n\n' # can change the contents of these quotes
    ),
    {
        "": "mem_question_1" # the strings "favorites" controls what area the player is going to next - both changable as long as you change the 'brain' in (area_object['brain'] = main.Area on line 5)
    },
    (
    	[""] #correct answer(s) - this is used for the answer verification function in main.py
    )
)

area_object['mem_question_1'] = main.Q_and_A(
    (
        "Memories Center - Question 1"
    ),
    (
        '\nA date is floating around. It seems to be my birthday. What is it?'
    ),
    (
        '\n A: 11/30/1993'
        '\n B: 11/30/1994'
        '\n C: 11/31/1993'
        '\n D: 11/31/1994\n\n'
    ),
    {
        "a": 'mem_question_2',
        "b": 'mem_question_1',
        "c": 'mem_question_1',
        "d": 'mem_question_1'
    },
    (
    	["a"]
    )
)

area_object['mem_question_2'] = main.Q_and_A(
    (
        "Memories Center - Question 2"
    ),
    (
        '\nA beautiful calico cat is soaring in the distance. She was my '
        '\nfirst cat. What was her name?'
    ),
    (
        '\n A: Rusty'
        '\n B: Musty'
        '\n C: Ditzy'
        '\n D: Dusty\n\n'
    ),
    {
        "a": 'mem_question_2',
        "b": 'mem_question_2',
        "c": 'mem_question_2',
        "d": 'mem_question_3'
    },
    (
    	["d"]
    )
)

area_object['mem_question_3'] = main.Q_and_A(
    (
        "Memories Center - Question 3"
    ),
    (
        '\nThis one is tricky! My father is floating around. What is '
        '\nhis name?'
    ),
    (
        '\n A: John'
        '\n B: Michael'
        '\n C: Frank'
        '\n D: Kevin\n\n'
    ),
    {
        "a": 'mem_question_3',
        "b": 'mem_question_4',
        "c": 'mem_question_3',
        "d": 'mem_question_3'
    },
    (
    	["b"]
    )
)

area_object['mem_question_4'] = main.Q_and_A(
    (
        "Memories Center - Question 4"
    ),
    (
        '\nYou can see some cars. What was the first car I ever purchased?'
    ),
    (
        '\n A: Honda Civic'
        '\n B: Saturn L200'
        '\n C: Saturn SL1'
        '\n D: Mazda Protege\n\n'
    ),
    {
        "a": 'mem_question_4',
        "b": 'mem_question_4',
        "c": 'mem_question_5',
        "d": 'mem_question_4'
    },
    (
    	["c"]
    )
)

area_object['mem_question_5'] = main.Q_and_A(
    (
        "Memories Center - Question 5"
    ),
    (
        '\nThe child-version of myself is somewhere around you holding '
        '\na guitar. How old was I when I picked up my first instrument?'
    ),
    (
        '\n A: 8'
        '\n B: 6'
        '\n C: 10'
        '\n D: 13\n\n'
    ),
    {
        "a": 'choice',
        "b": 'mem_question_5',
        "c": 'mem_question_5',
        "d": 'mem_question_5'
    },
    (
    	["a"]
    )
)

area_object['choice'] = main.Area(
    (
        "Option Center" # area name
    ),
    (
        '\nYou have a choice to make. Since you\'ve gotten this far without '
        '\nwithout losing, my brain would like to offer you a bonus area.'
    ),
    (
        '\nWhere would you like to go?' # option string (what appears on the screen)
        '\n A. Unexplored, totally awesome-sounding bonus area'
        '\n B. Boring ass next area\n\n'
    ),
    {
        "a": "bonus",
        "b": "thoughts" # area dictionary      
    },
    (
    	["a", "b"]
    )
)

area_object['bonus'] = main.Area(
    (
        "BONUS AREA MOTHERFUCKER!!!!!!!" # area name
    ),
    (
        '\n*Dance music playing*'
        '\nYeah bitches! You got to the bonus area!'
        '\nGet ready to answer some questions you may or may not know!'
        '\nYou better be sayin\' \"LET\'S FUCKIN\' GOOOOOOO!!!!'
    ),
    (
        '\nReady? Y or N\n\n'
    ),
    {
        "y": "bonus_question_1",
        "n": "choice" # area dictionary      
    },
    (
    	["y", "n"]
    )
)

area_object['bonus_question_1'] = main.Q_and_A(
    (
        "Bonus Area - Question 1"
    ),
    (
        '\nWhat is the name of my band?'
    ),
    (
        '\n A: If You\'re Ready'
        '\n B: If It\'s Cool'
        '\n C: If It\'s Cool With You'
        '\n D: If My Balls Touch Your Face\n\n'
    ),
    {
        "a": 'bonus_question_1',
        "b": 'bonus_question_2',
        "c": 'bonus_question_1',
        "d": 'bonus_question_1'
    },
    (
    	["b"]
    )
)

area_object['bonus_question_2'] = main.Q_and_A(
    (
        "Bonus Area - Question 2"
    ),
    (
        '\nHow many members are in my band?'
    ),
    (
        '\n A: 4'
        '\n B: 3'
        '\n C: 5'
        '\n D: 6\n\n'
    ),
    {
        "a": 'bonus_question_3',
        "b": 'bonus_question_2',
        "c": 'bonus_question_2',
        "d": 'bonus_question_2'
    },
    (
    	["a"]
    )
)

area_object['bonus_question_3'] = main.Q_and_A(
    (
        "Bonus Area - Question 3"
    ),
    (
        '\nWho plays guitar in the band?'
    ),
    (
        '\n A: Jeff'
        '\n B: Paul'
        '\n C: Jude'
        '\n D: Cody\n\n'
    ),
    {
        "a": 'bonus_question_3',
        "b": 'bonus_question_3',
        "c": 'bonus_question_3',
        "d": 'bonus_question_4'
    },
    (
    	["d"]
    )
)

area_object['bonus_question_4'] = main.Q_and_A(
    (
        "Bonus Area - Question 4"
    ),
    (
        '\nHow long have we been a band?'
    ),
    (
        '\n A: About a month'
        '\n B: About 3 months'
        '\n C: About 6 months'
        '\n D: About a year\n\n'
    ),
    {
        "a": 'bonus_question_4',
        "b": 'bonus_question_4',
        "c": 'bonus_question_5',
        "d": 'bonus_question_4'
    },
    (
    	["c"]
    )
)

area_object['bonus_question_5'] = main.Q_and_A(
    (
        "Bonus Area - Question 5"
    ),
    (
        '\nWho created the band?'
    ),
    (
        '\n A: Me'
        '\n B: Jude'
        '\n C: Jeff'
        '\n D: Cody\n\n'
    ),
    {
        "a": 'bonus_question_5',
        "b": 'thoughts',
        "c": 'bonus_question_5',
        "d": 'bonus_question_5'
    },
    (
    	["b"]
    )
)

area_object['thoughts'] = main.Area(
    (
        "Inner Thoughts" # area name
    ),
    (
        '\nYou\'ve come so far! I can\'t believe you haven\'t lost yet. '
    ),
    (
        '\nNew area found - press enter to continue\n\n'
    ),
    {
        "": "thoughts_question_1",  
    },
    (
    	[""]
    )
)

area_object['thoughts_question_1'] = main.Q_and_A(
    (
        "Inner Thoughts - Question 1"
    ),
    (
        '\nOn an average day, how often do you pop into my head?'
    ),
    (
        '\n A: Once every 30 seconds'
        '\n B: Once a day'
        '\n C: A few times a day'
        '\n D: A thousand times every second\n\n'
    ),
    {
        "a": 'thoughts_question_1',
        "b": 'thoughts_question_1',
        "c": 'thoughts_question_1',
        "d": 'thoughts_question_2'
    },
    (
    	["d"]
    )
)

area_object['thoughts_question_2'] = main.Q_and_A(
    (
        "Inner Thoughts - Question 2"
    ),
    (
        '\nWhat do I dream about the most?'
    ),
    (
        '\n A: Sex'
        '\n B: Guns'
        '\n C: Falling'
        '\n D: Work\n\n'
    ),
    {
        "a": 'thoughts_question_2',
        "b": 'thoughts_question_3',
        "c": 'thoughts_question_2',
        "d": 'thoughts_question_2'
    },
    (
    	["b"]
    )
)

area_object['thoughts_question_3'] = main.Q_and_A(
    (
        "Inner Thoughts - Question 2"
    ),
    (
        '\nWhat do I think about when doing little things like pooping, '
        '\nor driving?'
    ),
    (
        '\n A: You, sex, marriage'
        '\n B: Drums, code'
        '\n C: Life with you in 30 years'
        '\n D: All of the above\n\n'
    ),
    {
        "a": 'thoughts_question_3',
        "b": 'thoughts_question_3',
        "c": 'thoughts_question_3',
        "d": 'thoughts_question_4'
    },
    (
    	["d"]
    )
)

area_object['thoughts_question_4'] = main.Q_and_A(
    (
        "Inner Thoughts - Question 4"
    ),
    (
        '\nAm I pro-choice or pro-life?'
    ),
    (
        '\n A: Pro-choice'
        '\n B: Pro-life\n\n'
    ),
    {
        "a": 'thoughts_question_5',
        "b": 'thoughts_question_4'
    },
    (
    	["a"]
    )
)

area_object['thoughts_question_5'] = main.Q_and_A(
    (
        "Inner Thoughts - Question 5"
    ),
    (
        '\nHow would I rather show you I love you?'
    ),
    (
        '\n A: Just tell you'
        '\n B: Do nothing'
        '\n C: Take you out'
        '\n D: Make or do stupid things for you like this game\n\n'
    ),
    {
        "a": 'thoughts_question_5',
        "b": 'thoughts_question_5',
        "c": 'thoughts_question_5',
        "d": 'logic'
    },
    (
    	["d"]
    )
)

area_object['logic'] = main.Area(
    (
        "Logic Center" # area name
    ),
    (
        '\nFinal round! This one is all about how I\'d solve a particular problem. '
        '\nI suppose we\'ll find out here how well you know me, won\'t we? ;)'
    ),
    (
        '\nNew area found - press enter to continue\n\n'
    ),
    {
        "": "logic_question_1",  
    },
    (
    	[""]
    )
)

area_object['logic_question_1'] = main.Q_and_A(
    (
        "Logic Center - Question 1"
    ),
    (
        '\nI come home to you bawling because your cat just died. '
        '\nWhat do I do to try and make you feel better?'
    ),
    (
        '\n A: Tell you "You\'ll be ok"'
        '\n B: Make fun of the cat'
        '\n C: Have a funeral for the cat'
        '\n D: Hug you and nothing else\n\n'
    ),
    {
        "a": 'logic_question_1',
        "b": 'logic_question_1',
        "c": 'logic_question_2',
        "d": 'logic_question_1'
    },
    (
    	["c"]
    )
)

area_object['logic_question_2'] = main.Q_and_A(
    (
        "Logic Center - Question 2"
    ),
    (
        '\nI just witnessed a car accident while on my porch smoking. '
        '\nWhat decision do I make?'
    ),
    (
        '\n A: Stare at the cars'
        '\n B: Call the police, make sure everyone\'s okay'
        '\n C: Go back inside'
        '\n D: Yell "Slow down assholes!"\n\n'
    ),
    {
        "a": 'logic_question_2',
        "b": 'logic_question_3',
        "c": 'logic_question_2',
        "d": 'logic_question_2'
    },
    (
    	["b"]
    )
)

area_object['logic_question_3'] = main.Q_and_A(
    (
        "Logic Center - Question 3"
    ),
    (
        '\nYou and I get pulled over'
        '\nWhat do I do?'
    ),
    (
        '\n A: Pull over'
        '\n B: Run'
        '\n C: Start shooting'
        '\n D: Get naked\n\n'
    ),
    {
        "a": 'logic_question_4',
        "b": 'logic_question_3',
        "c": 'logic_question_3',
        "d": 'logic_question_3'
    },
    (
    	["a"]
    )
)

area_object['logic_question_4'] = main.Q_and_A(
    (
        "Logic Center - Question 4"
    ),
    (
        '\nWe\'re in Chicago and I realized I left my keys at home and '
        '\nmy car will not start. What do I do?'
    ),
    (
        '\n A: Call my mom for the spare'
        '\n B: Call Jeff for the spare'
        '\n C: Call a locksmith'
        '\n D: Hotwire it\n\n'
    ),
    {
        "a": 'logic_question_4',
        "b": 'logic_question_5',
        "c": 'logic_question_4',
        "d": 'logic_question_4'
    },
    (
    	["b"]
    )
)

area_object['logic_question_5'] = main.Q_and_A(
    (
        "Logic Center - Question 5"
    ),
    (
        '\nI receive a letter in the mail stating the power will be shut off '
        '\non a certain date. How do I handle the situation?'
    ),
    (
        '\n A: Pay NIPSCO lots of money'
        '\n B: Drive to a NIPSCO building'
        '\n C: Call NIPSCO'
        '\n D: Let the situation handle itself\n\n'
    ),
    {
        "a": 'logic_question_5',
        "b": 'logic_question_5',
        "c": 'win',
        "d": 'logic_question_5'
    },
    (
    	["c"]
    )
)

area_object['win'] = main.Area(
    (
        "Winner's Circle" # area name
    ),
    (
        '\nHoly shit babe! You fuckin\' won! How unexpected...;) '
        '\nYou shall be rewarded with kisses and hugs.'
    ),
    (
        '\nPress enter to close\n\n'
    ),
    {
        "": ""  
    },
    (
    	[""]
    ),
    win=True
)