# Gimme bogosort babae!
import random

def lord_have_mercy(arr: list) -> list:
    while arr != sorted(arr):
        random.shuffle(arr)
    return arr

print(lord_have_mercy([random.randint(1, 100) for i in range(10)]))