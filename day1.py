#! python3

# Advent of Code 2022 - Day #1
# Challenge: Counting calories in elven inventories
# Author: Kenny Yeager

from operator import itemgetter

#create array (elves) of dictionaries {sum, items [caloric value of a foodstuff]}
elves = []

#import text file containing calorie inventories
inputFile = open('inputdata/day1.txt', 'r')
fileLines = inputFile.readlines()

#parse text file, moving to next elf on every line break
elfIterator = 1
currentElf = {}
currentSum = 0
currentInventory = []
for thisLine in fileLines:
    if thisLine.strip() == '':
        currentElf = {'id':elfIterator, 'sum':currentSum, 'inventory':currentInventory}
        elves.append(currentElf)
        currentElf = {}
        currentSum = 0
        currentInventory = []
        elfIterator = elfIterator + 1
        continue
    currentSum = currentSum + int(thisLine)
    currentInventory.append(int(thisLine))

#cycle through array, sorting by sums
#make it easy by using sorted and itemgetter--thanks SO for syntax helps!
orderedElves = sorted(elves, key=itemgetter('sum'), reverse=True)

#print the number of the elf with the highest sum
print('The elf carrying the most calories in their inventory is')
print('elf #' + str(orderedElves[0]['id']) + ' with ' + str(orderedElves[0]['sum']) + ' calories.\n')

#part two: sum of the three most load-bearing elves' inventories
combinedCalories = orderedElves[0]['sum'] + orderedElves[1]['sum'] + orderedElves[2]['sum']
print('The three elves with the most calories in their inventories are')
print('elves #' + str(orderedElves[0]['id']) + ', #' + str(orderedElves[1]['id']) + ', and #' + str(orderedElves[2]['id']) + '.')
print('Their combined inventory contains ' + str(combinedCalories) + ' total calories!')