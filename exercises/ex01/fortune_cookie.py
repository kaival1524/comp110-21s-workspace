"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730402855"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")

random_fortune_message: int = int(randint(1, 4))

if random_fortune_message <= 2:
    if random_fortune_message == 1:
        print("You will meet an old friend today.")
    else:
        print("Today, you will be a pleasant surprise!")

else:
    if random_fortune_message <= 3:
        print("Good things will come for those who wait.")
    else:
        print("Be careful what you wish for, it might come true.")
    
print("Now, go spread positive vibes!")