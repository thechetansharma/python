"""
    Assignment 4 - Team Chooser
    This program prints the teams and players names randomly from the teams.txt and players.txt file
"""

#Defining Imports"""
from random import choice

#Declaring Variables"""
teamA = []
teamB = []

#Fetching data from the Payers.txt file and storing in the variable"""
playersFile = open('players.txt', 'r')
players = playersFile.read().splitlines()

#Fetching data from the teams.txt file and storing in the variable"""
teamsFile = open('teams.txt', 'r')
teamNames = teamsFile.read().splitlines()

#Randomly assigning teams"""
firstTeam = choice(teamNames)
teamNames.remove(firstTeam)
secondTeam = choice(teamNames)

#Looping until there is no name left inside the players variable"""
while len(players) > 0:

    #Randomly getting the names from the players variable and adding in the Teams A """
    playerA= choice(players)
    teamA.append(playerA)
    
    #Removing those names from the players variable those already have chosen"""
    players.remove(playerA)

    #Breaking the loop, if there are an odd number of values in the players variable"""
    if players == []:
        break

    #Randomly getting the names from the players variable and adding in the Teams B """
    playerB= choice(players)
    teamB.append(playerB)

    #Removing those names from the players variable those already have chosen"""
    players.remove(playerB)

# Printing team names and there players
print("Here are your teams :")
print("Team 1 :",firstTeam,teamA)
print("Team 2 :", secondTeam,teamB)
