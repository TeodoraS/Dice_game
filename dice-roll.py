import random
import sys

#It can be used with or without arguments. If used with arguments, first write the number of games you want to play, 
#and second the number to be accumulated.

all_rolls = []
if len(sys.argv) > 1:
    game_nr = int(sys.argv[1]) 
else:
    game_nr = int(raw_input("Insert the number of games:\t"))

if len(sys.argv) > 1:
    accum_nr = int(sys.argv[2])
else:
    accum_nr = int(raw_input("Insert the number to accumulate:\t"))

def roll_dice(accum_nr):
    rolls =[]
    while accum_nr > 0:
        roll = random.randrange(1, 7, 1)
        accum_nr = accum_nr - roll
        rolls.append(roll)
    all_rolls.append(rolls)

def verify_dice():
    for element in all_rolls:
        if sum(element) != accum_nr:
            all_rolls.remove(element)
        else:
            pass
        
def sort_dice(accum_nr):
    for i in range(1, (accum_nr+1)):
        times = []
        for element in all_rolls:
            if len(element) == i:
                times.append(element)
        print "Roll the dice %d times = %s games" % (i, len(times))

while len(all_rolls) < game_nr :
    roll_dice(accum_nr)
    verify_dice()
print all_rolls
sort_dice(accum_nr)

            

    