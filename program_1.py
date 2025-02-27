# Eliya Statema
# 2/27/25
# Random Dice

import random

def ranDice():
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    return die_1 + die_2

rolls_sum = 0
for loop in range(100):
    rolls_sum += ranDice()
    
average = rolls_sum / 100
print(f"The average of two dice rolled 100 times is {average:.2f}.")