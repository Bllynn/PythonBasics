from random import random


def flip_coin():
    print("How many coin flips do you want to do?")
    count = int(input())
    tosses = 0
    heads = 0
    tails = 0
    while tosses < count:
        if random() > 0.5:
            heads += 1
            tosses += 1   
        else:
            tails += 1
            tosses += 1
    print(f"Out of {count} coin flips, {heads}, or {(heads/tosses)*100}% were heads and {tails}, or {(tails/tosses)*100}% were tails")
flip_coin();