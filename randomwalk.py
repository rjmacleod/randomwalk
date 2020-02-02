# Asks for the dimensionality of the walks, the
# length of the random walk and the number of simulations
# desired. Output will be statistical data
# about the walks (TBD).

import numpy as np
import random as rand

STEP_CAP = 100000

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
    d = input("Dimension (1-10): ")
    try:
        d = int(d)
        if d > 0 and d < 11:
            break;
        else:
            print("Choose an integer between 1 and 10.")
    except ValueError:
        print("Choose an integer between 1 and 10.")

while True:
    steps = input("Steps (1-{}): ".format(STEP_CAP - 1))
    try:
        steps = int(steps)
        if d > 0 and d < STEP_CAP:
            break;
        else:
            print("Choose an integer between 1 and {}}.".format(STEP_CAP - 1))
    except ValueError:
        print("Choose an integer between 1 and {}.".format(STEP_CAP - 1))


ival = 1/(2*d) # the interval for determining a random direction uning rand.random()
               # there are 2d possible directions, each one with 1/2d probability.

origin = np.zeros(d)

loc = np.zeros(d) # this is the "current location"
walk = np.zeros((steps,d)) # this is an array of the entire walk.
                           # each row is a step, starting at 0. there is a column for each dimension

current_step = 0

print("Starting walk...")
while current_step < steps:
    take_step(loc, walk, current_step)
    current_step += 1

    if current_step > 1 and np.array_equal(loc,origin):
        print("Came home!")

print("Final location: ")
print(loc)



        