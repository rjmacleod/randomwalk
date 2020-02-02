# Asks for the dimensionality of the walks, the
# length of the random walk and the number of simulations
# desired. Output will be statistical data
# about the walks (TBD).

import numpy as np
import random as rand

def take_step(loc, walk, step):
    x = rand.random()
    # x is btwn 0 and 1
    for i in range(2*d):
        if i*ival <= x < (i+1)*ival:
            if i in range(d):
                loc[i] = loc[i] + 1
            else:
                loc[i-d] = loc[i-d] - 1
    walk[step] = loc
    

while True:
    d = input("Dimension: ")

    try:
        d = int(d)
        if d > 0 and d < 11:
            break;
        else:
            print("Choose an integer between 1 and 10.")
    except ValueError:
        print("Choose an integer between 1 and 10.")


steps = 10
ival = 1/(2*d) # the interval for determining a random direction uning rand.random()
               # there are 2d possible directions, each one with 1/2d probability.
loc = np.zeros(d)
print(loc)
walk = np.zeros((steps,d))
current_step = 0

while current_step < steps:
    take_step(loc, walk, current_step)
    print(loc)
    current_step += 1

print("Final location: ")
print(loc)



        