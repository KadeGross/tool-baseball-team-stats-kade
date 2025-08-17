# Baseball Team Stats App

# File Imports
import constants
import copy
import random
import sys


# This function converts data to a more suitable format for the program
def clean_data(data):
    data_copy = copy.deepcopy(data)  # Copy data
    return [{'name': player['name'], 'guardians': player['guardians'].split(' and '),
             'experience': True if player['experience'] == 'YES' else False,
             'height': int(player['height'].split()[0])} for player in data_copy]  # List comprehension to store converted data


def sort_players_experience(data):  # Separates players by experience
    experienced_players = [player for player in data if player["experience"]]
    inexperienced_players = [player for player in data if not player["experience"]]
    random.shuffle(experienced_players)
    random.shuffle(inexperienced_players)
    return experienced_players, inexperienced_players


def balance_teams(teams, experienced, inexperienced):  # Distributes players evenly across teams
    teams.sort()  # Alphabetizes teams
    balanced_teams = []
    experienced_players_per_team = int(len(experienced) / len(teams))
    inexperienced_players_per_team = int(len(inexperienced) / len(teams))
    total_players_per_team = experienced_players_per_team + inexperienced_players_per_team
    for index, team in enumerate(teams, 1):
        balanced_team = {
            'team number': index,
            'team name': team,
            'experienced players': [],
            'inexperienced players': [],
            '# players': total_players_per_team,
            '# experienced': experienced_players_per_team,
            '# inexperienced': inexperienced_players_per_team,
        }

        for player in range(experienced_players_per_team):
            balanced_team['experienced players'].append(experienced.pop())

        for player in range(inexperienced_players_per_team):
            balanced_team['inexperienced players'].append(inexperienced.pop())

        all_team_players = balanced_team['experienced players'] + balanced_team['inexperienced players']
        player_heights = [all_team_players[index]['height'] for index, player in enumerate(all_team_players)]
        balanced_team['average height'] = round(sum(player_heights) / total_players_per_team, 1)  # Average height calculation rounded to 1 digit
        balanced_teams.append(balanced_team)
    return balanced_teams


def show_teams(teams):  # Main loop code
    while True:
        print("\n-----Team Selection-----\n")
        print("Teams:")
        for index, team in enumerate(teams):
            print(teams[index]['team number'], teams[index]['team name'])
        print("\nType 'Quit' to Exit")
        while True:
            choose_team = input("\nEnter team number to display stats: ")
            try:
                choice = int(choose_team)
                if type(choice) == int:
                    if choice in range(len(teams) + 1):
                        display_team(choice, teams)
                        input("\npress ENTER to continue...")
                        show_teams(teams)
                    else:
                        raise ValueError
            except ValueError:
                if choose_team.lower() == 'quit':
                    print('Program Exiting')
                    sys.exit(0)
                else:
                    print("Invalid input, try again.")
                    continue


def display_team(team_number, teams):  # Displays team based on user choice
    team_number -= 1  # Adjustment for indexing
    print("\n-----Team Stats-----\n")
    print("Team Name: " + teams[team_number]['team name'], '\n--------------------')
    print("Total Players: ", teams[team_number]['# players'])
    print("Total Experienced: ", teams[team_number]['# experienced'])
    print("Total Inexperienced: ", teams[team_number]['# inexperienced'])
    print("Average Height: ", teams[team_number]['average height'], "Inches\n")
    players = teams[team_number]['experienced players'] + teams[team_number]['inexperienced players']
    player_names = [players[index]['name'] for index, player in enumerate(players)]
    print("Team Players: \n ", ", ".join(player_names), '\n')
    guardians = []
    for index, player in enumerate(players):
        guardians += (players[index]['guardians'])
    print("Guardians: \n ", ", ".join(guardians), '\n')


def main():
    cleaned_data = clean_data(constants.PLAYERS)
    experienced_players, inexperienced_players = sort_players_experience(cleaned_data)
    teams = balance_teams(constants.TEAMS, experienced_players, inexperienced_players)
    show_teams(teams)


if __name__ == '__main__':
    main()
