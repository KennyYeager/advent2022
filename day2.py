#! python3

# Advent of Code 2022 - Day #2
# Challenge: Rock, Paper, Scissors!
# Author: Kenny Yeager

# cypher data given in prompt:
# A/X = rock, B/Y = paper, C/Z = scissors

# score caluated by shape value + outcome score
# shape values: rock = 1, paper = 2, scissors = 3
# outcome values: loss = 0, draw = 3, win = 6

# import text file containing the strategy guide
inputFile = open('inputdata/day2.txt', 'r')
fileLines = inputFile.readlines()

runningScore = 0
for thisRound in fileLines:
    opponentHand = thisRound.split(' ')[0].strip()
    myHand = thisRound.split(' ')[1].strip()
    #print('runningScore = ' + str(runningScore))
    #print(thisRound.strip() + ' -- ' + opponentHand + ' -- ' + myHand)
    if myHand == 'X':
        runningScore += 1
        if opponentHand == 'A':
            runningScore += 3
        elif opponentHand == 'B':
            continue
        else:
            runningScore += 6
    elif myHand == 'Y':
        runningScore += 2
        if opponentHand == 'A':
            runningScore += 6
        elif opponentHand == 'B':
            runningScore += 3
        else:
            continue
    else:
        runningScore += 3
        if opponentHand == 'A':
            continue
        elif opponentHand == 'B':
            runningScore += 6
        else:
            runningScore += 3

print('Following the strategy guide perfectly under a bad assumption of intent gives a total score of ' + str(runningScore) +'!')

# part two changes the assumption to the second column being intended outcome, not hand to play
# basically just recycling the main logic loop but changing values as appropriate
# the new outcome-based cypher is X = lose, Y = draw, Z = win
runningScore = 0
for thisRound in fileLines:
    opponentHand = thisRound.split(' ')[0].strip()
    intendedOutcome = thisRound.split(' ')[1].strip()
    if opponentHand == 'A':
        if intendedOutcome == 'X':
            runningScore += 3 + 0
        elif intendedOutcome == 'Y':
            runningScore += 1 + 3
        else:
            runningScore += 2 + 6
    elif opponentHand == 'B':
        if intendedOutcome == 'X':
            runningScore += 1 + 0
        elif intendedOutcome == 'Y':
            runningScore += 2 + 3
        else:
            runningScore += 3 + 6
    else:
        if intendedOutcome == 'X':
            runningScore += 2 + 0
        elif intendedOutcome == 'Y':
            runningScore += 3 + 3
        else:
            runningScore += 1 + 6

print('Following the strategy guide to purposely get intended win-loss-draw outcomes gives a total score of ' + str(runningScore) +'.')
print('Throwing matches is bad, though, mmk?')