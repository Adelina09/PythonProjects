#!/usr/bin/env python3.8

import random

words= ['camera', 'set', 'machine', 'glass']
guess=[]
word_to_guess=random.choice(words)
lengthword=len(secretword)
alphabet='a, b, c, d, e,f, g, h, i, j, k, l, m, n, o, p, q, r, s, t , u, v, w, x, y, z'
letter_storage=[]

while True:
    gamechoice= input('start game? (yes/no')
    if gamechoice=='yes':
        break
    else gamechoice=='no':
        sys.exit('sorry to see you go')
