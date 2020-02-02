# Asks for the dimensionality of the walks, the
# length of the random walk and the number of simulations
# desired. Output will be statistical data
# about the walks (TBD).

import sys
import numpy as np
import random as rand

# CONSTANTS

STEP_CAP = 1000
REPEAT_CAP = 1000


# CLASSES AND FUNCTIONS

class WalkResult:
    def __init__(self, walk, final_loc, came_home):
        self.walk = walk # array with d columns and a row for each step
        self.result = final_loc # d dimension vector
        self.returned = came_home # bool

def take_step(loc, walk, step):
    x = rand.random()
    # x is btwn 0 and 1

    # subdivides [0,1] up into 2*d categories
    # depending on which interval x is in, one of our current loc dimensions
    # is incremented or decremented by 1
    # ival is 1/(2*d)
    for i in range(2*d):
        if i*ival <= x < (i+1)*ival:
            if i in range(d):
                loc[i] = loc[i] + 1
            else:
                loc[i-d] = loc[i-d] - 1
    # add current step to walk array
    walk[step] = loc
    
def take_walk():
    # takes a single walk, returns WalkResult
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


try:
    d = int(sys.argv[1])
    if d > 0 and d < 11:
        pass
    else:
        print("Dimension is an integer between 1 and 10.")
        sys.exit()
except IndexError:
    print("Usage: 'python randomwalk.py dimension steps repititions' (dim index)")
    sys.exit()
except ValueError:
    print("Usage: 'python randomwalk.py dimension steps repititions' (dim value)")
    sys.exit()

try:
    steps = int(sys.argv[2])
    if steps > 0 and steps < STEP_CAP:
        pass
    else:
        print("Steps are an integer between 1 and {}.".format(STEP_CAP - 1))
        sys.exit()
except IndexError:
    print("Usage: 'python randomwalk.py dimension steps repititions' (steps index)")
    sys.exit()
except ValueError:
    print("Usage: 'python randomwalk.py dimension steps repititions' (steps value)")
    sys.exit()

try:
    rep = int(sys.argv[3])
    if rep > 0 and rep < REPEAT_CAP:
        pass
    else:
        print("Choose an integer between 1 and {}}.".format(REPEAT_CAP - 1))
        sys.exit()
except IndexError:
    print("Usage: 'python randomwalk.py dimension steps repititions' (rep index)")
    sys.exit()
except ValueError:
    print("Usage: 'python randomwalk.py dimension steps repititions' (rep value)")
    sys.exit()

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