import scipy.ndimage	
import numpy as np
import matplotlib.pyplot as plt

"""
In Conway's game of Life (Conway), we watch how a system of cellular
automata (CA) evolve over time.
"""

kernel = np.array([[1,1,1],
                      [1,0,1],
                      [1,1,1]])

# we use convolution (from digital image processing) to
# compute functions based on an image's pixels
neighbors = scipy.ndimage.filters.convolve(array, kernel)

def step(a, w, m):
    """
    Step forward in time for some array a with weights w and mode m.
    """
    con = scipy.ndimage.filters.convolve(a, w, m)
