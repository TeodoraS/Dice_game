import random
import sys
from argparse import ArgumentParser
import argparse


all_rolls = []

def parse_opts():
    parser = argparse.ArgumentParser(description = '''
Dice-roll game, tracking frequency of rolls to accumulate 'n' points''')

    parser.add_argument('-g', '--games-number',
                        help = '''Insert the number of games to be played.
''',
                        metavar = 'games-number',
                        dest = 'game_nr',
                        type = int
                        )
    parser.add_argument('-a', '--accumulate-number',
                        help = '''Insert the number to be accumulated.
''',
                        metavar = 'accumulate-number',
                        dest = 'accum_nr',
                        type = int,
                        )
    return parser.parse_args()


def roll_dice(accumulate):
    rolls =[]
    while accumulate > 0:
        roll = random.randrange(1, 7, 1)
        accumulate = accumulate - roll
        rolls.append(roll)
    all_rolls.append(rolls)
    return all_rolls


def verify_dice(accumulate):
    for element in all_rolls:
        if sum(element) != accumulate:
            all_rolls.remove(element)
        else:
            pass

        
def sort_dice(accumulate):
    for i in range(1, (accumulate+1)):
        times = []
        for element in all_rolls:
            if len(element) == i:
                times.append(element)
        print "Roll the dice %d times = %s games" % (i, len(times))


def main():
    arg = parse_opts()
    if (arg.game_nr) and (arg.accum_nr) != None:
        while len(all_rolls) < (arg.game_nr):
            roll_dice(arg.accum_nr)
            verify_dice(arg.accum_nr)
        print all_rolls
        sort_dice(arg.accum_nr)
    else:
        print "No arguments, please see -help."
    
                
if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print e
