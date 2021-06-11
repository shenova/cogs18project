"""Test for my functions.

"""

from functions import *
import unittest.mock

# used code from : https://stackoverflow.com/questions/18161330/using-unittest-mock-to-patch-input-in-python-3 to test functions with inputs. 

def test_start_game():

    test_game_story = 'this is a test game story' 
    test_game_rules = 'this is a test for the game rules.' 
    
    with unittest.mock.patch('builtins.input', return_value = 'bob'): # Automatically puts an input. 
        assert input() == 'bob' 
        assert start_game(test_game_story, test_game_rules) == None # Asserts that start_game has no return. 

        
def test_split_story():
    
    level_story = "There is a bird.\n It can fly.\n It has wings." # Test story for function. 
    
    assert callable (split_story) 
    assert split_story(level_story) == None  # Asserts that there is no return for the split_stroy function.

    
def test_new_level():
    
    test_level_story = "There is a bird. It can fly. It has wings."
    test_dict = {1: 'pizza', 2: 'wings', 3: 'pineapple'}
    test_result = "Your order is correct!"
    
    assert callable (new_level)
    
    with unittest.mock.patch('builtins.input', return_value = 'pizza'): # Automatically uses an input.
        assert type(new_level(test_level_story, test_dict, test_result )) == bool # Checks that the return is a bool.

        
def test_num_copy():

    assert callable (num_copy) # Asserts the function is callable.
    
    test_numstring = '27841'
    test_level_story_num = 'It is cold outside. The temperature is 49 degrees.'
    test_result_num = 'It is cloudy.'
    
    with unittest.mock.patch('builtins.input', return_value = '2917303'): # Automatically uses an input.
        assert type(num_copy(test_level_story_num, test_numstring, test_result_num)) == bool # Checks that the return is a bool.

        
def test_status():

    assert callable (status) # Asserts the function is callable.
    
    with unittest.mock.patch('builtins.input', return_value = 'bubbles'): # Automatically uses an input.
        assert status(player_status = True) == None
        assert status(player_status = False) == None

        
def test_all(): # Runs all of the above functions.
    test_start_game()
    test_split_story()
    test_new_level()
    test_num_copy()
    test_status()

