import numpy as np
inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
weights = [0.2, 0.8, -0.5, -0.2, -0.8, 0.5, 0.1, -0.1, 0.3, 0.6]
bias = 9.0
output = np.dot(weights, inputs) + bias
print(output)