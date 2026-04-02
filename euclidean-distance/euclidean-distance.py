import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x = np.array(x)
    y = np.array(y)
    
    return solverNumpy(x, y)

def solverLinalgNorm(x, y):
    return float(np.linalg.norm(x - y))

def solverNumpy(x, y):
    return float(np.sqrt(np.sum((x - y) ** 2)))