"""A collection of functions for doing my project."""

import random
import time  

def start_game(story, rules):
    
    """ 
    
    Introduction to the game, takes player's name via input and explains the story and rules to the player.

    Parameters:
    ----------
    
    story : str
        String explaining the game's story.
    
    rules : str
        String listing out the rules for the game.
        
    
    Return:
    ------
    
    None

    """
    
    player_name = input('Please enter your name. ') #Asks player to input their name and assigned to the variable player_name.
    
    if not player_name:  # Conditional that checks if the player inputted anything. 
        player_name = 'Player'  # If there is no input, the variable player_name becomes "Player".
    
    print("Welcome" + ' '+ player_name + '!') # Prints welcome statement.
        
    split_story(story)  # Calls the split_story function on the input story. 
    print("Directions: ")
    split_story(rules) # Calls the split_story function on the input rules.
    

    start_game_input = input('Type any letter to begin. ') #Asks player to type any letter to start the game.
    start_game = True  #Sets the variable start_game to True.

    while start_game: #Loop to check the variable start_game.
        if (start_game_input.isalnum()) == True: # Checks if the player typed a letter or number.
            start_game = False 
        else:
            start_game_input = input('Type any letter to begin.') # If player did not type a letter or a number, the input bar will be presented again.
            

def split_story(story):
    
    """ 

    Takes a string input with multiple sentences and splits into individual items.

    Parameter
    ----------
    
    level_story : str
        String explaining the game's story.
        
    
    Return:
    ------
    
    None

    """

    story = story.split('\n')   # Takes input and splits at the '\n' and assigns to the variable story.
    
    for item in story: # For loop to print each item from the variable story and waits two seconds between each item printed.
        print(item)
        time.sleep(2)

        
def new_level(level_story, dictionary, result):
    
    """ 

    Prints the level_story, gets a random item from the dictionary, determines if player input matches value of dictionary item, and prints result.

    Parameters:
    ----------
    
    level_story : str
        String explaining the story associated with the level
     
    dictionary : dict
        Dictionary for the function to select a random key from.
        
    result: str
        Prints the outcome of the user's answer.
        
    
    Return:
    ------
    
    player_status : bool
        Determines if the player's input matches the value from the dictionary.

    """
    
    player_status = True 
    
    split_story(level_story) # Calls the split_story function on the level_story input. 
    time.sleep(3) # Waits 3 seconds before continuing
    
    level_question = random.choice(list(dictionary)) # Randomly selects an item from dictionary input and prints the key. 
    print(level_question)

    player_answer = input() # Presents input bar for user to answer question. 
    
    
    if (player_answer.upper()).strip() == dictionary.get(level_question): # Conditional to check if the player's answer matches the value of the dictionary key.
        print (result)  
    
    elif (player_answer.upper()).strip() == 'END GAME': # Checks if player input is "END GAME".
        output = 'GAME OVER' 
        print(output) #Prints that the game is over.
        player_status = False # Sets the value of player_status to False.
    
    else:
        print('Incorrect!\nYou were unable to finish the quest and Voldemort got to the stone before you!\nGAME OVER.')
        # If answer does not match the dictionary value, statement will be printed.
        player_status = False # Sets the value of player_status to False
    
    return player_status # Returns player_status as a bool.

    
def num_copy (level_story, numbers, result):
   
    """ 
    
    Takes a string input of numbers and prints them one by one to create a memory task. 

    Parameters:
    ----------
    
    level_story : str
        String explaining the story associated with the level.
     
    numbers : str
        String of numbers for the function to use. 
    
    result : str
        Prints the outcome if the user's answer is correct.
        
    
    Return:
    ------
    
    player_status : bool
        Determines if the player's input matches the value from the dictionary.

    """
    
    split_story(level_story) # Calls the function split_story on level_story.
    time.sleep(3) # Waits 3 seconds before continuing.
    
    player_status = True 
    
    for num in numbers: #For loop to loop through each number in the numbers string.
        print(num, end ='\r') # Prints each number, and erases previous input.
        time.sleep(1) # Waits 1 second before printing the next number.
        
    player_input = input('Type the numbers that were shown.') #Asks for player to input their answer.
    
    if player_input == numbers: # Conditional to check if player_input matches the input string.
        print(result) # Prints the result if the answer is correct.  
    
    elif (player_input.upper()).strip() == 'END GAME': # Checks if player input is "END GAME".
        output = 'GAME OVER' 
        print(output) # Prints that the game is over.
        player_status = False # Sets the value of player_status to False.
        
    else:
        print('Incorrect!\nYou were unable to finish the quest and Voldemort got to the stone before you!\nGAME OVER.')
        player_status = False  # Sets the value of player_status to False if answer is incorrect.

    return player_status #Returns player_status as a bool.
    
    
def status(player_status):
   
    """ 

    Takes input of player_status and runs while loop to break game if player_status is False. 

    Parameter
    ----------
    
    level_story : str
        String explaining the game's story
        
    
    Return:
    ------
    
    None

    """
    
    # Dictionary with questions as the key and the correct answer as the value.

    music_questions_answers = {'Eminem‘s 8 Mile is named after a road in which city?': 'DETROIT', 
                            'What year did Justin Bieber release the song "Baby"?': '2009',
                            'Who is considered the "King of Pop"?': 'MICHAEL JACKSON',
                            'Adam Levine is the lead singer of which pop group?': 'MAROON 5',
                            'Who was the very first American Idol winner?': 'KELLY CLARKSON'}

    # Dictionary with questions as the key and the correct answer as the value.
    
    popculture_questions_answers = {'How many kids does Angelina Jolie have?': '6',
                               'How many times did Ross Geller get divorced on Friends?': '3',
                               'Who did Forbes name the youngest “self-made billionaire ever” in 2019? (Full name)': 'KYLIE JENNER',
                               'Which tech entrepreneur named his son X Æ A-12? (Full name)': 'ELON MUSK',
                               "What nickname did Patrick Dempsey’s character often go by on Grey’s Anatomy?": 'MCDREAMY'}
    
    # Dictionary with questions as the key and the correct answer as the value.

    biology_questions_answers = {'If plants breathe in carbon dioxide, what do they breathe out?': 'OXYGEN', 
                            'A ____________is the necessity for the plant cell to have a fixed shape.': 'CELL WALL',
                            'Which plant has flowers but no proper leaves?': 'CACTUS',
                            'Photosynthesis is carried out in which part of the cell?': 'CHLOROPLAST',
                            'Which famous scientist introduced the idea of natural selection? (FULL NAME)': 'CHARLES DARWIN'} 


    logic_puzzle = {'I have keys, but no locks. I have a space, but no room. You can enter, but can’t go inside. What am I?\n (Type your answer as "A(n) _______")': 'A KEYBOARD'}

    #Story as a string for each level.
    
    level1_story = """
In order to access the entrance to the dungeon you need to open the corridor door first. 
You discover it's locked. 
Solve this puzzle to use the correct spell to unlock the door.\n""" 

    level2_story = """ 
Once you enter the door...
AHHHH!
You see the giant 3-headed dog, Fluffy, guarding the trap door to enter the dungeon.
But then you remember, Fluffy can be put to sleep with music.
In the room, you spot a harp that you can charm to play a harmony.
Answer this question to use the correct charm on the harp.\n """

    level3_story = """ 
You open the trap door and look inside and see nothing but darkness.
You jump in through the door and land on a mysterious plant. 
ITS DEVIL'S SNARE!
Its branches begin to coil around you, until you remember that devil's snare hates sunlight!
Answer the question to use the correct spell to free yourself from the plant.\n 
"""

    level4_story = """ 
As you walk through the dungeon, you encounter another locked door. 
There are hundreds of keys flying around you, but only one key can unlock the door. 
Solve this puzzle to get the right key to unlock the door.\n
"""

    level5_story = """
As you continue in the dungeon, you now encounter a giant puzzle with a barricade. 
You need to get past the barricade to get to the stone. 
Solve this riddle to get past the barricade.\n
"""

    level6_story = """
You are in the final room before getting to the room with the stone. 
The entrance to the room is blocked by a fire. 
There are several potions on the table in front of you, but only one will allow you through the fire. 
Answer this question to drink the correct potion and pass the fire.\n
"""
    
    while player_status == True: 
        
        player_status = num_copy(level1_story, '172930','Alohomora!\nThe spell worked and you were able to unlock the door.')
        # Sets player_status to the return value of the num_copy function. 
        
        if player_status == False: # Conditional to break the loop if player_status is False.
            break    
            
        player_status = new_level(level2_story, music_questions_answers, 'ZAPP!\nYour charm worked and Fluffy was put to sleep.')
         # Sets player_status to the return value of the new_level function.
            
        if player_status == False: # Conditional to break the loop if player_status is False.
            break
            
        player_status = new_level(level3_story, biology_questions_answers,"Lumos Solem!\nYour wand emitted a beam of sunlight and you were freed from the Devil's snare")  # Sets player_status to the return value of the new_level function.
        
        if player_status == False: # Conditional to break the loop if player_status is False.
            break
            
        player_status = num_copy(level4_story, '92830519', 'You used the correct key and the door unlocked!') 
        # Sets player_status to the return value of the num_copy function.
        
        if player_status == False :# Conditional to break the loop if player_status is False.
            break
            
        player_status = new_level(level5_story, logic_puzzle, 'Your answer was correct and the barricade disappeared!')
         # Sets player_status to the return value of the new_level function.
            
        if player_status == False : # Conditional to break the loop if player_status is False.
            break
            
        player_status = new_level(level6_story, popculture_questions_answers,'You drank the correct potion and were able to get to the stone!' )  # Sets player_status to the return value of the new_level function.
        
        if player_status == False : # Conditional to break the loop if player_status is False.
            break
        else: 
            print('Congrats!\nYou got to the stone before Voldemort!\nYou saved Hogwarts!') 
            break 
            #Prints statement if player successfully finishes all levels and breaks the while loop.
            
            
def quest(): 
    
    """
    Runs multiple functions in order to play game.

    Parameter
    ----------
    
    None
    
    
    Return:
    ------
    
    None 
    
    """
        
    game_rules = """
        To obtain the necessary spell or charm, you must answer the questions associated with each obstacle.
        If you answer any question incorrectly you will lose the game.
        For any question that requires a numerical answer, type only the number(s).
        If at any time you would like to stop the game, type "END GAME".
        Remember spelling counts!\n"""

    game_story = """
        Help! Lord Voldemort is back and he discovered where the Sorcerer's stone is hidden. 
        It is your job to aid Harry Potter and his friends to get the stone before Voldemort does!
        The stone is placed in a dungeon beneath the school.
        To get to the dungeon, you must pass the obstacles created by the professors of Hogwarts using spells 
        and charms.\n"""

    start_game(game_story, game_rules) # Calls the start_game function
    
    player_status = True # Sets player_status to True 
    
    status(player_status)  # Calls the status function with the input player_status
