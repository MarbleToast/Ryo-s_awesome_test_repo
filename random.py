# Gimme function that prints a series of random strings infinitely
import random
import string
def endless_gibberish():
    while "oh god" == "oh god":
        print(''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 30))))