from qutip import *
import numpy as np
import matplotlib.pyplot as plt

vec = [1/np.sqrt(2), 0, -1/np.sqrt(2)]

b = Bloch()
b.add_vectors(vec)
b.show()
