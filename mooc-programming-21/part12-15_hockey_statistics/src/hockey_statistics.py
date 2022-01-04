# In this exercise you will build an application for examining hockey league statistics from the NHL in a couple of different ways.

# The exercise template contains two JSON files: partial.json ja all.json. The first of these is mostly meant for testing. The latter contains a lot of data, as all the NHL player stats for the 2019-20 season are included in the file.

# The entry for a single player is in the following format:

# {
#     "name": "Patrik Laine",
#     "nationality": "FIN",
#     "assists": 35,
#     "goals": 28,
#     "penalties": 22,
#     "team": "WPG",
#     "games": 68
# }
# Both files contain a list of entries in the above format.

# If you need a refresher on handling JSON files, please take a look at part 7 of this course material.

# Search and list
# Please write an interactive application which first asks for the name of the file, and then offers the following functions:

# search by name for a single player's stats
# list all the abbreviations for team names in alphabetical order
# list all the abbreviations for countries in alphabetical order
# These functionalities grant you one exercise point. Your application should now work as follows:

# Sample output
# file name: partial.json
# read the data for 14 players

# commands:
# 0 quit
# 1 search for player
# 2 teams
# 3 countries
# 4 players in team
# 5 players from country
# 6 most points
# 7 most goals

# command: 1
# name: Travis Zajac

# Travis Zajac         NJD   9 + 16 =  25
# command: 2
# BUF
# CGY
# DAL
# NJD
# NYI
# OTT
# PIT
# WPG
# WSH

# command: 3
# CAN
# CHE
# CZE
# SWE
# USA

# command: 0

# NB: the printout format for a player must be exactly as follows:

# Sample output
# Leon Draisaitl       EDM  43 + 67 = 110
# Connor McDavid       EDM  34 + 63 =  97
# Travis Zajac         NJD   9 + 16 =  25
# Mike Green           EDM   3 +  8 =  11
# Markus Granlund      EDM   3 +  1 =   4
# 123456789012345678901234567890123456789
# The last line in the sample above is there to help you calculate the widths of the different fields in the output; you should not print the numbers line yourself in your final submission.

# The abbreviation for the team is printed from the 22nd character onwards. The + sign is the 30th character and the = sign is the 35th character. All the fields should be justified to the right edge. All whitespace is space characters.

# F-strings are probably the easiest way to achieve the required printout. The process is similar to this exercise from part 6.

# List players by points
# These two functionalities will grant you a second exercise point:

# list players in a specific team in the order of points scored, from highest to lowest. Points equals goals + assists
# list players from a specific country in the order of points scored, from highest to lowest
# Your application should now work as follows:

# Sample output
# file name: partial.json
# read the data for 14 players

# commands:
# 0 quit
# 1 search for player
# 2 teams
# 3 countries
# 4 players in team
# 5 players from country
# 6 most points
# 7 most goals

# command: 4
# team: OTT

# Drake Batherson      OTT   3 +  7 =  10
# Jonathan Davidsson   OTT   0 +  1 =   1
# command: 5
# country: CAN

# Jared McCann         PIT  14 + 21 =  35
# Travis Zajac         NJD   9 + 16 =  25
# Taylor Fedun         DAL   2 +  7 =   9
# Mark Jankowski       CGY   5 +  2 =   7
# Logan Shaw           WPG   3 +  2 =   5
# command: 0

# Most successful players
# These two functionalities will grant you a third exercise point:

# list of n players who've scored the most points
# if two players have the same score, whoever has scored the higher number of goals comes first
# list of n players who've scored the most goals
# if two players have the same number of goals, whoever has played the lower number of games comes first
# Your application should now work as follows:

# Sample output
# file name: partial.json
# read the data for 14 players

# commands:
# 0 quit
# 1 search for player
# 2 teams
# 3 countries
# 4 players in team
# 5 players from country
# 6 most points
# 7 most goals

# command: 6
# how many: 2

# Jakub Vrana          WSH  25 + 27 =  52
# Jared McCann         PIT  14 + 21 =  35
# command: 6
# how many: 5

# Jakub Vrana          WSH  25 + 27 =  52
# Jared McCann         PIT  14 + 21 =  35
# John Klingberg       DAL   6 + 26 =  32
# Travis Zajac         NJD   9 + 16 =  25
# Conor Sheary         BUF  10 + 13 =  23
# command: 7
# how many: 6

# Jakub Vrana          WSH  25 + 27 =  52
# Jared McCann         PIT  14 + 21 =  35
# Conor Sheary         BUF  10 + 13 =  23
# Travis Zajac         NJD   9 + 16 =  25
# John Klingberg       DAL   6 + 26 =  32
# Mark Jankowski       CGY   5 +  2 =   7
# command: 0

import json

class Player:
    def __init__(self, name:str, nationality:str, assists:int, goals:int, penalties:int, team:str, games:str):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        return f'{self.name:21}{self.team:3}{self.goals:4} + {self.assists:2} = {(self.goals+self.assists):3}'

class HockeyApplication:    
    def __init__(self):
        self.players = []
    
    def help(self):
        print('commands:')
        print('0 quit')
        print('1 search for player')
        print('2 teams')
        print('3 countries')
        print('4 players in team')
        print('5 players from country')
        print('6 most points')
        print('7 most goals')
    
    def read_file(self, file_name: str):
        with open(file_name) as file:
            data = file.read()
        return json.loads(data)

    def add_players(self, all_players: list):
        for player in all_players:
            p = Player(player['name'], player['nationality'], player['assists'], player['goals'], player['penalties'], player['team'], player['games'])
            self.players.append(p)

    def search_player(self):
        name = input('name: ')
        for player in self.players:
            if player.name == name:
                print(player)
    
    def list_teams(self):
        teams = map(lambda player: player.team, self.players)
        teams = set(list(teams))
        for team in sorted(teams):
            print(team)

    def list_countries(self):
        countries = map(lambda player: player.nationality, self.players)
        countries = set(list(countries))
        for country in sorted(countries):
            print(country)

    def __points_scored(self, player: Player):
        return [(player.goals + player.assists), player.goals]

    def list_players_in_team(self):
        team = input('team: ')
        team_players = filter(lambda player: player.team == team, self.players)
        team_players = sorted(team_players, key=self.__points_scored, reverse=True)
        for player in team_players:
            print(player)

    def list_players_in_country(self):
        country = input('country: ')
        country_players = filter(lambda player: player.nationality == country, self.players)
        country_players = sorted(country_players, key=self.__points_scored, reverse=True)
        for player in country_players:
            print(player)

    def list_players_most_points(self):
        max_num_of_players = int(input('how many: '))
        points_players = sorted(self.players, key=self.__points_scored, reverse=True)
        count = 1
        for player in points_players:
            if count <= max_num_of_players:
                print(player)
                count += 1

    def __goals_scored(self, player: Player):
        return [player.goals, (player.games)*-1]

    def list_players_most_goals(self):
        max_num_of_players = int(input('how many: '))
        points_players = sorted(self.players, key=self.__goals_scored, reverse=True)
        count = 1
        for player in points_players:
            if count <= max_num_of_players:
                print(player)
                count += 1

    def execute(self):
        if True:
            file_name = input('file name: ')
        else:
            file_name = 'partial.json'
        all_players = self.read_file(file_name)
        print(f'read the data of {len(all_players)} players')
        self.add_players(all_players)
        self.help()
        while True:
            print()
            command = input('command: ')
            if command == '0':
                break
            elif command == '1':
                self.search_player()
            if command == '2':
                self.list_teams()
            elif command == '3':
                self.list_countries()
            if command == '4':
                self.list_players_in_team()
            elif command == '5':
                self.list_players_in_country()
            if command == '6':
                self.list_players_most_points()
            elif command == '7':
                self.list_players_most_goals()

app = HockeyApplication()
app.execute()