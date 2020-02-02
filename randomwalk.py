# Asks for the dimensionality of the walks, the
# length of the random walk and the number of simulations
# desired. Output will be statistical data
# about the walks (TBD).

import numpy as np
import random as rand

# CONSTANTS

STEP_CAP = 1000
REPEAT_CAP = 1000

# CLASSES AND FUNCTIONS

class WalkResult:
    def __init__(self, walk, final_loc, came_home):
        self.walk = walk
        self.result = final_loc
        self.returned = came_home

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
    
def take_walk():
    loc = np.zeros(d) # this is the "current location"
    walk = np.zeros((steps,d)) # this is an array of the entire walk.
                            # each row is a step, starting at 0. there is a column for each dimension

    current_step = 0
    came_home = False

    while current_step < steps:
        take_step(loc, walk, current_step)
        current_step += 1

        if current_step > 1 and np.array_equal(loc,origin):
            came_home = True

    result = WalkResult(walk, loc, came_home)
    return result

# GET USER INPUT

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
        if steps > 0 and steps < STEP_CAP:
            break;
        else:
            print("Choose an integer between 1 and {}}.".format(STEP_CAP - 1))
    except ValueError:
        print("Choose an integer between 1 and {}.".format(STEP_CAP - 1))

while True:
    rep = input("Repeat __ times (1-{}): ".format(REPEAT_CAP - 1))
    try:
        rep = int(rep)
        if rep > 0 and rep < REPEAT_CAP:
            break;
        else:
            print("Choose an integer between 1 and {}}.".format(REPEAT_CAP - 1))
    except ValueError:
        print("Choose an integer between 1 and {}.".format(REPEAT_CAP - 1))

# SET UP VARIABLES

ival = 1/(2*d) # the interval for determining a random direction uning rand.random()
               # there are 2d possible directions, each one with 1/2d probability.

origin = np.zeros(d)

# RUN PROGRAM

return_count = 0

for i in range(rep):
    current_walk = take_walk()
    if current_walk.returned:
        return_count += 1

print("{} out of {} walks returned to the origin.".format(return_count, rep))