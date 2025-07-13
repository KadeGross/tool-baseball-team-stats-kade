# XTODO Add Dunder Main
# XTODO Import constants.py file
# XTODO Create data cleaning function
    # XTODO Copy list with copy.deepcopy(). (lookup how to use copy.deepcopy())
        # XTODO Import copy
    # XTODO Create cleaned_data list to store cleaned data
    # XTODO Loop through dictionaries in PLAYERS_copy
    # XTODO Create new dictionary for each player in for loop
    # XTODO Add dictionary values to new list of dictionaries
        # XTODO Add player name to new dictionary
        # XTODO Split guardians into list using .split(" and "). Add to new dictionary
        # XTODO Set 'experience' to True if 'YES' and False if 'NO'. Add to new dictionary
        # XTODO Set 'height' to integer. (.split() and take the index[0] value and convert to int). Add to dictionary
        # XTODO Extra Credit: Turn guardian stings into list of guardians using .split(" and "). Add to dictionary
        # XTODO Print to check if data has been properly cleaned
# TODO Create a balance_teams function
    # TODO
# TODO Create sort_players function
    # XTODO Create 2 lists of players, experienced and inexperienced
# TODO Create a while loop that runs the main code for the app. Run loop until user enters Quit.

import constants
import copy

def clean_data(data):
    cleaned_data = []
    for player in data:
        fixed = {}
        fixed['name'] = player['name']
        fixed['guardians'] = player['guardians'].split(' and ')
        fixed['experience'] = True if player['experience'] == 'YES' else False
        fixed['height'] = int(player['height'].split()[0])
        cleaned_data.append(fixed)
    return cleaned_data

def sort_players(data):
    experienced_players = []
    inexperienced_players = []
    for player in data:
        if player["experience"] == True:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    return experienced_players, inexperienced_players


# Create comprehension
# def balance_teams(experienced, inexperienced):


# def run_app():



def main():
    cleaned_data = clean_data(PLAYERS_copy)
    experienced_players, inexperienced_players = sort_players(cleaned_data)
    print(experienced_players)
    print(inexperienced_players)
    # balance_teams(experienced_players, inexperienced_players)
    # while True:


# Place calculations, function calls and logic blocks that need to run
# inside dunder main block at bottom of file.
# place all function calls in main() function so all functions run when dunder condition is met
# This prevents automatic execution when this app is imported into another script.
if  __name__ == '__main__':
    PLAYERS_copy = copy.deepcopy(constants.PLAYERS)
    main()