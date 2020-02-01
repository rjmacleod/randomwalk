# Asks for the dimensionality of the walks, the
# length of the random walk and the number of simulations
# desired. Output will be statistical data
# about the walks (TBD).

import numpy as np

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

print(d)
