import numpy as np 

def check_consecutive(arr, target, count):
    # Check rows
    for row in arr:
        if np.any(np.convolve(row == target, np.ones(count, dtype=int), mode='valid') == count):
            return True

    # Check columns
    for col in arr.T:
        if np.any(np.convolve(col == target, np.ones(count, dtype=int), mode='valid') == count):
            return True

    # Check diagonals
    diagonals = [arr.diagonal(i) for i in range(-arr.shape[0] + 1, arr.shape[1])]
    diagonals.extend([np.fliplr(arr).diagonal(i) for i in range(-arr.shape[0] + 1, arr.shape[1])])

    for diag in diagonals:
        if np.any(np.convolve(diag == target, np.ones(count, dtype=int), mode='valid') == count):
            return True

    return False