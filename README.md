# dice_game

## Description
Assuming `n=20`, how many rolls of a fair die does one need to accumulate at exactly `20` points? 

Of course one needs at least `4` rolls (as in `6 + 6 + 6 + 2` or `6 + 5 + 4 + 5`) and at most `20` rolls 
(getting `20` times `1`'s in a row). 
However these situations are rather unlikely! 
Hence, we ask ourselves: what is the most likely number of times that one has to roll a die to get exactly 20 points? 

To answer this question, the program asks the user to simulate a number of games (e.g., `1000` games) and keeps frequency 
of the number of times that was needed to play one game. A game is defined as the number of times it is needed to get 
20 points. 
The program then prints how many games the dice was rolled `4` times, `5` times, `6` times, `7` times …. up to `20` times. 

##Usage

* user dialog

Run program with no arguments and follow dialog.

* cli args

`python.exe dice-roll.py <no-of-games> <no-to-accumulate>`
