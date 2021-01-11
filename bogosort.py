# Gimme bogosort babae!
import random

def lord_have_mercy(arr: list) -> list:
    while arr != sorted(arr):
        random.shuffle(arr)
    return arr