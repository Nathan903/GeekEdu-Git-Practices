import sys
import random

chars = r'\|/'

def draw(rows, columns):
    for r in rows:
        print(''.join(random.choice(chars) for _ in range(columns)))
draw(10, 20)
