# Package: statix
# Module:  descriptive
# About:   A module for computing descriptive statistics.
# Author:  Matthew D. Kearns
# Contact: mattdkearns@gmail.com

from math import ceil

def mean(data, trim=0, weights=None):
    """Calculate and return the mean value of the data.

    data: a python list-like object
    trim: [0, 1]; default=0
    weights: a python list-like object; default=None
    """

    average = 0

    if 0 < trim <= 1:                             # trim data
        trim_amt = ceil(trim*len(data))
        data = sorted(data)
        for i in range(trim_amt):
            data.pop(0)
            data.pop()
            if weights:
                weights.pop(0)
                weights.pop()

    if weights:                                  # if weighted, compute weighted average
        for i in range(len(data)):
            average += data[i] * weights[i]
    else:                                        # otherwise, compute normal average
        for val in data:
            average += val

    return average / len(data)

