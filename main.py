# The propose of this application is to lear Python.
#
###Description###
#
# Create an application that will request input for user number and the number of dice rolling.
# generate an username and display the dice rolls and also display the winner of the game
#

import random


# function that will generate the dice values
def dice():
    number = random.randint(1, 6)
    return number


# function that will define the player name and the dice values
def playerData(n, rolls):
    tmp_name = "Player" + str(n)
    i = 0
    diceValues = []
    while i < rolls:
        diceValues.append(dice())
        i += 1
    return (tmp_name, diceValues)


# reading the users and dice roll counters
players = int(input("Enter the number of players: "), 10)
roll = int(input("How manny rolls for each player? : "), 10)

# generating the user names and dice roll values
j = 0
table = {}
while j < players:
    table.update(dict([playerData(j, roll)]))
    j += 1

print("This is the dice roll score: \n")
print(table)

winner = {}
# determining the total score  for each player
for key, value in table.items():
    suma = sum(value)
    winner[key] = suma

print("The final score for each player is: \n")
print(winner)

# determine the max value and display the winner
max_value = max(winner)
print("And the winner is..... : " + max_value)
