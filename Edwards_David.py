import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
 
# In order to make the random numbers predictable, we will define fixed seeds for both Numpy and TensorFlow.
 
np.random.seed(101)
tf.set_random_seed(101)
 
# Now, let’s generate some random data for training the Linear Regression Model.
 
# Generating random linear data
# There will be 50 data points ranging from 0 to 50
x = np.linspace(0, 50, 50)
y = np.linspace(0, 50, 50)
 
# Adding noise to the random linear data
x += np.random.uniform(-4, 4, 50)
y += np.random.uniform(-4, 4, 50)
 
n = len(x) # Number of data points