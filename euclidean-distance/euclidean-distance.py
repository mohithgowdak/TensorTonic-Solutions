import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x_array = np.asarray(x, dtype=float)
    y_array = np.asarray(y, dtype=float)

    # Calculate sum of squared differences
    sum_sq = np.sum(np.square(x_array - y_array))
    
    # Return the square root as a float
    return float(np.sqrt(sum_sq))