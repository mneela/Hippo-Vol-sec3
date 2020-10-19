"""
Contains various functions for computing statistics over 3D volumes
"""
import numpy as np

def Dice3d(a, b):
    """
    This will compute the Dice Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks -
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Dice3D. If you completed exercises in the lessons
    # you should already have it.
    # <YOUR CODE HERE>
    # dice score is two 
    # intersection of two volumes (a & b) / 
    #  2*(a intesection b)/ sum(a+b)
    
    a_t = np.where(a>0,1,0)
    b_t = np.where(b>0,1,0)
    
    inter = np.sum(a_t*b_t)
    total_vol = np.sum(a_t) + np.sum(b_t)
    
    return (2.*float(inter) / float(total_vol))

def Jaccard3d(a, b):
    """
    This will compute the Jaccard Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Jaccard similarity coefficient. Please do not use 
    # the Dice3D function from above to do the computation ;)
    # <YOUR CODE GOES HERE>
    a_t = np.where(a>0,1,0)
    b_t = np.where(b>0,1,0)
    inter = np.sum(a_t*b_t)

    a_plus_b = np.sum(a_t) + np.sum(b_t)
    union = a_plus_b - inter
    
    return float(inter)/float(union)