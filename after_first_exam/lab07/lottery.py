import math
import sys
import random

max_nr = sys.argv[1]
draw_size = sys.argv[2]
number_of_players = sys.argv[3]

winning_combination = list()
for item in range(0,int(draw_size)):
    winning_combination.append(random.randint(1, int(max_nr)))   

fd = open('output.txt', "a+")
fd.write(f'{str(winning_combination)} \n')

for player in range(0, int(number_of_players)):
    numbers = []
    for item in range(0,int(draw_size)):
        numbers.append(random.randint(1, int(max_nr)))
    distinct = set(numbers) & set(winning_combination)
    fd.write(f'{str(list(distinct))} \n')
